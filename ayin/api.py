"""
FastAPI application — ingestion, websocket broadcast, static serving.

Single-process architecture. All state lives in memory.

On startup:
  - Creates a 3-node triangle TensionWeb
  - Generates an accident_shock perturbation series via the simulator
  - Runs a background task that steps through the series at ~10 Hz,
    calling web.step() and broadcasting full state after each step

Websocket broadcast cadence: 10 Hz (100ms between frames).
That is fast enough to watch shockwave propagation across strands,
slow enough for the engineer to track causality without visual noise.

Control messages (client -> server, over the same websocket):
  {"cmd": "restart"}                   — reset scenario to beginning
  {"cmd": "pause"}                     — halt simulation loop
  {"cmd": "resume"}                    — resume from pause
  {"cmd": "step"}                      — advance exactly one tick while paused
  {"cmd": "speed", "value": X}         — set speed multiplier (0.25, 0.5, 1, 2, 4)
  {"cmd": "log"}                       — write current run data to ayin/docs/logbook.md
  {"cmd": "scenario", "value": NAME}   — switch active scenario and restart
                                         NAME: "accident_shock" | "stadium_shock"
"""

from __future__ import annotations

import asyncio
import datetime
import json
import time
from pathlib import Path
from typing import Any

import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from ayin.nodes import NODE_LABELS
from ayin.simulator import (
    AccidentShockConfig,
    BaselineConfig,
    UnmappedShockConfig,
    generate_accident_shock,
    generate_baseline,
    generate_unmapped_shock,
    volume_to_tension_delta,
    baseline_volume,
)
from ayin.web import TensionWeb, create_triangle_web


# ---------------------------------------------------------------------------
# Shared web state — the single source of truth for all connected clients
# ---------------------------------------------------------------------------

# The physical web. Lives for the lifetime of the process.
web: TensionWeb = create_triangle_web(
    strand_strength=1.0,
    propagation_rate=1.0,
    damping_coefficient=0.3,   # underdamped (ζ≈0.087) — visible oscillations
    dt=0.05,
)

# Connected websocket clients. Modified under asyncio event loop (no threads).
_clients: set[WebSocket] = set()

# Perturbation schedule: list of (step_index, perturbation_vector) tuples,
# sorted by step_index ascending. The background task pops from the front
# as simulation time advances.
_perturbation_schedule: list[tuple[int, np.ndarray]] = []

# Simulation tick counter — used by the visualization as a liveness indicator.
_tick: int = 0

# ---------------------------------------------------------------------------
# Playback control state
# ---------------------------------------------------------------------------

# When paused, the simulation loop idles without advancing physics.
_paused: bool = False

# Speed multiplier. Base cadence is 100ms / tick. At 2x we run twice as many
# ticks per wall-clock interval. Supported: 0.25, 0.5, 1.0, 2.0, 4.0.
_speed: float = 1.0

# When True, advance exactly one tick on the next loop iteration even if paused.
_step_requested: bool = False

# Flag to signal the loop to restart the scenario.
_restart_requested: bool = False

# Active scenario name. Changing this (via websocket cmd) triggers a restart.
# Valid values: "accident_shock" | "stadium_shock"
_active_scenario: str = "accident_shock"

# Flag to signal the loop to switch scenarios (rebuilds schedule + markers, then restarts).
_scenario_switch_requested: str | None = None

# Known perturbation events: list of dicts {tick, sim_step, label} recorded
# as each perturbation fires. Sent in state so the chart can draw markers.
# Cleared on scenario restart.
_perturbation_events: list[dict[str, Any]] = []

# Tick at which the scenario started (for relative timing in events).
_scenario_start_tick: int = 0


# ---------------------------------------------------------------------------
# Run logger — in-memory accumulator for post-run logbook entries
# ---------------------------------------------------------------------------

# Logbook path — always append, never overwrite.
_LOGBOOK_PATH = Path(__file__).parent / "docs" / "logbook.md"

# Snapshot interval: record a state snapshot every N ticks (not every tick).
# At 10Hz and ~180 total ticks per scenario, every 2 ticks gives ~90 snapshots — enough
# resolution to see energy trajectory and recovery dynamics clearly.
_LOG_SNAPSHOT_EVERY_N_TICKS = 2

class RunLogger:
    """
    Accumulates key events and periodic snapshots during a scenario run.

    Records:
      - Run start wall-clock time and tick
      - Perturbation injection events (tick, sim_step, delta vector)
      - Peak tension per node (value + tick when it occurred)
      - Incoherence events (node index, tick, tension, velocity)
      - Periodic state snapshots (every N ticks): tick, sim_step, energy,
        total_tension, per-node tensions
      - Energy at run start and each snapshot (trajectory)

    write_entry() formats these into a markdown section and appends to the
    logbook file. It does not clear accumulated data — that happens on
    scenario restart via reset().
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.run_start_wall: str = datetime.datetime.now().isoformat(timespec="seconds")
        self.run_start_tick: int = 0
        self.run_start_sim_step: int = 0

        # Perturbation events: list of dicts
        # {tick, sim_step, wall_offset_s, delta: [float, float, float]}
        self.perturbation_events: list[dict[str, Any]] = []

        # Peak tension per node: {node_index: {"value": float, "tick": int}}
        self.peak_tension: dict[int, dict[str, Any]] = {}

        # Incoherence events: {tick, node_index, tension, velocity}
        self.incoherence_events: list[dict[str, Any]] = []

        # Periodic snapshots for energy trajectory and recovery analysis.
        # Each: {tick, sim_step, energy, total_tension, tensions: [f,f,f]}
        self.snapshots: list[dict[str, Any]] = []

        # Wall time of run start (monotonic, for offset calculation)
        self._wall_start: float = time.monotonic()

        # Track when energy first peaked (for energy dissipation calc)
        self._peak_energy: float = 0.0
        self._peak_energy_tick: int = 0

    def record_snapshot(
        self,
        tick: int,
        sim_step: int,
        energy: float,
        total_tension: float,
        node_tensions: list[float],
        node_velocities: list[float],
    ) -> None:
        """Call every N ticks from the simulation loop."""
        self.snapshots.append({
            "tick": tick,
            "sim_step": sim_step,
            "energy": round(energy, 6),
            "total_tension": round(total_tension, 4),
            "tensions": [round(t, 4) for t in node_tensions],
        })

        # Track peak energy
        if energy > self._peak_energy:
            self._peak_energy = energy
            self._peak_energy_tick = tick

        # Track peak tension per node
        for i, t in enumerate(node_tensions):
            abs_t = abs(t)
            if i not in self.peak_tension or abs_t > abs(self.peak_tension[i]["value"]):
                self.peak_tension[i] = {"value": round(t, 4), "tick": tick}

        # Check incoherence: high velocity + significant tension
        for i, (t, v) in enumerate(zip(node_tensions, node_velocities)):
            if abs(v) > 0.5 and abs(t) > 0.8:
                # Only record if not already logged in the last 5 ticks for this node
                recent = [
                    e for e in self.incoherence_events
                    if e["node_index"] == i and tick - e["tick"] < 5
                ]
                if not recent:
                    self.incoherence_events.append({
                        "tick": tick,
                        "node_index": i,
                        "tension": round(t, 4),
                        "velocity": round(v, 4),
                    })

    def record_perturbation(
        self,
        tick: int,
        sim_step: int,
        delta: "np.ndarray",
    ) -> None:
        wall_offset = round(time.monotonic() - self._wall_start, 2)
        self.perturbation_events.append({
            "tick": tick,
            "sim_step": sim_step,
            "wall_offset_s": wall_offset,
            "delta": [round(float(d), 4) for d in delta],
        })

    def write_entry(
        self,
        scenario_name: str,
        web_config: dict[str, Any],
        shock_config: dict[str, Any],
        current_tick: int,
        current_sim_step: int,
        current_energy: float,
    ) -> str:
        """
        Format and append a markdown entry to the logbook.
        Returns the formatted entry text.
        """
        now = datetime.datetime.now().isoformat(timespec="seconds")
        run_duration_ticks = current_tick - self.run_start_tick

        lines: list[str] = []

        # --- Run header ---
        lines.append(f"## Run — {now}")
        lines.append(f"")
        lines.append(f"**Scenario:** {scenario_name}  ")
        lines.append(f"**Run started:** {self.run_start_wall}  ")
        lines.append(f"**Log written:** {now}  ")
        lines.append(f"**Duration:** {run_duration_ticks} ticks ({run_duration_ticks * 0.1:.1f}s wall at 1x speed)  ")
        lines.append(f"**Ticks at log time:** {current_tick} (sim_step {current_sim_step})")
        lines.append(f"")

        # --- Parameter summary ---
        lines.append(f"### Parameters")
        lines.append(f"")
        lines.append(f"| Parameter | Value |")
        lines.append(f"|-----------|-------|")
        lines.append(f"| strand_strength | {web_config.get('strand_strength', 1.0)} |")
        lines.append(f"| propagation_rate | {web_config.get('propagation_rate', 1.0)} |")
        lines.append(f"| damping_coefficient | {web_config.get('damping_coefficient', 0.3)} |")
        lines.append(f"| dt | {web_config.get('dt', 0.05)} |")
        lines.append(f"| num_intervals | {shock_config.get('num_intervals', 36)} |")
        lines.append(f"| steps_per_interval | {shock_config.get('steps_per_interval', 5)} |")
        lines.append(f"| onset_interval | {shock_config.get('onset_interval', 6)} |")
        lines.append(f"| onset_duration_intervals | {shock_config.get('onset_duration_intervals', 2)} |")
        lines.append(f"| peak_duration_intervals | {shock_config.get('peak_duration_intervals', 14)} |")
        lines.append(f"| recovery_duration_intervals | {shock_config.get('recovery_duration_intervals', 6)} |")
        lines.append(f"| peak_reduction_fraction | {shock_config.get('peak_reduction_fraction', 0.50)} |")
        lines.append(f"")

        # --- Timeline of key events ---
        lines.append(f"### Timeline")
        lines.append(f"")

        # Merge perturbation events and incoherence events into a single timeline
        timeline: list[tuple[int, str]] = []

        # Energy start
        if self.snapshots:
            first_snap = self.snapshots[0]
            timeline.append((
                first_snap["tick"],
                f"run start — energy={first_snap['energy']:.4e}, "
                f"tensions={first_snap['tensions']}"
            ))

        # Perturbation events (sample every 5th to keep log concise — full list is huge)
        perturb_sample = self.perturbation_events
        if len(perturb_sample) > 20:
            # Show first 3, phase boundary approx (every 5th), last 3
            perturb_sample = (
                self.perturbation_events[:3]
                + self.perturbation_events[3:-3:5]
                + self.perturbation_events[-3:]
            )
        for ev in perturb_sample:
            delta_str = " ".join(f"{d:+.3f}" for d in ev["delta"])
            timeline.append((
                ev["tick"],
                f"perturbation injected — sim_step={ev['sim_step']}, "
                f"delta=[{delta_str}], t+{ev['wall_offset_s']}s"
            ))

        # Peak tension events
        for node_idx, pk in sorted(self.peak_tension.items()):
            label = NODE_LABELS.get(node_idx, f"Node-{node_idx}")
            timeline.append((
                pk["tick"],
                f"peak tension N{node_idx} ({label}) — {pk['value']:+.4f}"
            ))

        # Peak energy
        if self._peak_energy > 0:
            timeline.append((
                self._peak_energy_tick,
                f"peak energy — {self._peak_energy:.4e}"
            ))

        # Incoherence events
        for ev in self.incoherence_events:
            label = NODE_LABELS.get(ev["node_index"], f"Node-{ev['node_index']}")
            timeline.append((
                ev["tick"],
                f"INCOHERENCE — N{ev['node_index']} ({label}), "
                f"tension={ev['tension']:+.4f}, velocity={ev['velocity']:+.4f}"
            ))

        # Final snapshot
        if self.snapshots:
            last_snap = self.snapshots[-1]
            timeline.append((
                last_snap["tick"],
                f"snapshot — energy={last_snap['energy']:.4e}, "
                f"total_tension={last_snap['total_tension']:.4f}, "
                f"tensions={last_snap['tensions']}"
            ))

        # Sort by tick
        timeline.sort(key=lambda x: x[0])

        if timeline:
            lines.append(f"| Tick | Event |")
            lines.append(f"|------|-------|")
            for tick_val, description in timeline:
                lines.append(f"| {tick_val} | {description} |")
        else:
            lines.append(f"_(no events recorded yet)_")
        lines.append(f"")

        # --- Summary statistics ---
        lines.append(f"### Summary Statistics")
        lines.append(f"")

        # Energy trajectory
        if self.snapshots:
            e_start = self.snapshots[0]["energy"]
            e_final = self.snapshots[-1]["energy"]
            e_peak = self._peak_energy
            e_dissipated = max(0.0, e_peak - e_final)
            lines.append(f"**Energy trajectory:**")
            lines.append(f"- Start: {e_start:.4e}")
            lines.append(f"- Peak: {e_peak:.4e} at tick {self._peak_energy_tick}")
            lines.append(f"- Final: {e_final:.4e}")
            lines.append(f"- Total dissipated (peak -> final): {e_dissipated:.4e}")
            lines.append(f"")

        # Peak tension per node
        lines.append(f"**Peak tension per node:**")
        for node_idx in sorted(self.peak_tension.keys()):
            pk = self.peak_tension[node_idx]
            label = NODE_LABELS.get(node_idx, f"Node-{node_idx}")
            lines.append(f"- N{node_idx} ({label}): {pk['value']:+.4f} at tick {pk['tick']}")
        lines.append(f"")

        # Perturbation count
        lines.append(
            f"**Perturbations injected:** {len(self.perturbation_events)} "
            f"(across {current_sim_step} sim steps)"
        )
        lines.append(f"")

        # Incoherence count
        if self.incoherence_events:
            node_incoherence_counts: dict[int, int] = {}
            for ev in self.incoherence_events:
                ni = ev["node_index"]
                node_incoherence_counts[ni] = node_incoherence_counts.get(ni, 0) + 1
            ic_parts = ", ".join(
                f"N{ni}={cnt}"
                for ni, cnt in sorted(node_incoherence_counts.items())
            )
            lines.append(f"**Incoherence events:** {len(self.incoherence_events)} total ({ic_parts})")
        else:
            lines.append(f"**Incoherence events:** none detected")
        lines.append(f"")

        # Recovery: ticks from peak energy to energy dropping below 1% of peak
        recovery_ticks = self._estimate_recovery_ticks()
        if recovery_ticks is not None:
            lines.append(
                f"**Recovery (energy to 1% of peak):** "
                f"~{recovery_ticks} ticks ({recovery_ticks * 0.1:.1f}s at 1x speed)"
            )
        else:
            lines.append(f"**Recovery:** not yet complete at log time")
        lines.append(f"")

        # --- Qualitative assessment ---
        lines.append(f"### Qualitative Assessment")
        lines.append(f"")
        lines.append(f"_(Fill in manually after observation.)_")
        lines.append(f"")
        lines.append(f"- Wave propagation character:")
        lines.append(f"- Damping behavior observed:")
        lines.append(f"- Node most affected:")
        lines.append(f"- Recovery quality:")
        lines.append(f"- Notes:")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

        entry = "\n".join(lines)

        # Append to logbook
        _LOGBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)
        with _LOGBOOK_PATH.open("a", encoding="utf-8") as f:
            f.write(entry)

        return entry

    def _estimate_recovery_ticks(self) -> int | None:
        """
        Estimate ticks from peak energy to energy falling below 1% of peak.
        Returns None if recovery hasn't completed yet in the recorded snapshots.
        """
        if not self.snapshots or self._peak_energy <= 0:
            return None
        threshold = self._peak_energy * 0.01
        past_peak = False
        peak_tick = self._peak_energy_tick
        for snap in self.snapshots:
            if snap["tick"] >= peak_tick:
                past_peak = True
            if past_peak and snap["energy"] <= threshold:
                return snap["tick"] - peak_tick
        return None


# Single process-lifetime logger instance. Reset on scenario restart.
_run_logger = RunLogger()


# ---------------------------------------------------------------------------
# Scenario preparation
# ---------------------------------------------------------------------------

# Shared time-compression constants — same for both scenarios.
_SIM_STEPS_PER_INTERVAL = 5
_NUM_INTERVALS = 36

# Web construction parameters — identical for both scenarios so results are comparable.
_WEB_CONFIG: dict[str, Any] = {
    "strand_strength": 1.0,
    "propagation_rate": 1.0,
    "damping_coefficient": 0.3,
    "dt": 0.05,
}

# accident_shock config (fixed parameters)
_ACCIDENT_CONFIG = AccidentShockConfig(
    onset_interval=6,
    onset_duration_intervals=2,
    peak_duration_intervals=14,
    recovery_duration_intervals=6,
    peak_reduction_fraction=0.50,
)

# stadium_shock (unmapped shock) config — uses simulator defaults
_STADIUM_CONFIG = UnmappedShockConfig(
    surge_fraction=0.65,
    surge_duration_intervals=6,
    surge_onset_interval=10,
)


def _build_accident_schedule() -> list[tuple[int, np.ndarray]]:
    """
    Generate the accident_shock perturbation schedule.

    36 intervals, 5 sim steps each -> 180 total sim steps.
    Each sim step = one web.step() call = 100ms wall time at 1x speed.
    Full scenario arc = 18s at 1x. Short enough to loop repeatedly.
    """
    rng = np.random.default_rng(seed=42)
    config = BaselineConfig(start_hour=7.0, num_intervals=_NUM_INTERVALS, apply_lag=False)
    baseline_vols = generate_baseline(config, rng)
    perturbed_vols, _envelope = generate_accident_shock(baseline_vols, _ACCIDENT_CONFIG, rng)

    rng2 = np.random.default_rng(seed=42)
    clean_config = BaselineConfig(start_hour=7.0, num_intervals=_NUM_INTERVALS, apply_lag=False, noise_cv=0.0)
    clean_vols = generate_baseline(clean_config, rng2)

    schedule: list[tuple[int, np.ndarray]] = []
    for i in range(_NUM_INTERVALS):
        delta = volume_to_tension_delta(perturbed_vols[i], clean_vols[i])
        schedule.append((i * _SIM_STEPS_PER_INTERVAL, delta))
    return schedule


def _build_accident_markers() -> list[dict[str, Any]]:
    """
    Phase boundary markers for the accident_shock scenario.
    Phases: baseline -> onset -> peak -> recovery -> tail
    """
    cfg = _ACCIDENT_CONFIG
    onset_start  = cfg.onset_interval
    onset_end    = onset_start + cfg.onset_duration_intervals
    peak_end     = onset_end   + cfg.peak_duration_intervals
    recovery_end = peak_end    + cfg.recovery_duration_intervals

    phase_map = {
        onset_start:  ("onset",    "accident onset"),
        onset_end:    ("peak",     "peak congestion"),
        peak_end:     ("recovery", "recovery start"),
        recovery_end: ("tail",     "near-normal"),
    }
    markers = []
    for i, (phase, label) in phase_map.items():
        markers.append({
            "sim_step": i * _SIM_STEPS_PER_INTERVAL,
            "interval": i,
            "label": label,
            "phase": phase,
        })
    return markers


def _build_stadium_schedule() -> list[tuple[int, np.ndarray]]:
    """
    Generate the stadium_shock (unmapped) perturbation schedule.

    Same time compression as accident_shock: 36 intervals, 5 steps each.
    Start hour 20.5 (8:30 PM) — game ends after evening peak.
    Seed 314 — same as compose_scenario_unmapped for reproducibility.
    """
    rng = np.random.default_rng(seed=314)
    config = BaselineConfig(start_hour=20.5, num_intervals=_NUM_INTERVALS, apply_lag=False)
    baseline_vols = generate_baseline(config, rng)
    perturbed_vols = generate_unmapped_shock(baseline_vols, _STADIUM_CONFIG, rng)

    rng2 = np.random.default_rng(seed=314)
    clean_config = BaselineConfig(start_hour=20.5, num_intervals=_NUM_INTERVALS, apply_lag=False, noise_cv=0.0)
    clean_vols = generate_baseline(clean_config, rng2)

    schedule: list[tuple[int, np.ndarray]] = []
    for i in range(_NUM_INTERVALS):
        delta = volume_to_tension_delta(perturbed_vols[i], clean_vols[i])
        schedule.append((i * _SIM_STEPS_PER_INTERVAL, delta))
    return schedule


def _build_stadium_markers() -> list[dict[str, Any]]:
    """
    Phase boundary markers for the stadium_shock scenario.
    Phases: baseline -> surge -> drain -> tail

    surge_onset_interval=10: game ends, crowd exits.
    surge ends at interval 10+6=16: main wave passes.
    tail from 16 onward: stragglers, parking lot drains.
    """
    cfg = _STADIUM_CONFIG
    surge_start = cfg.surge_onset_interval
    surge_end   = surge_start + cfg.surge_duration_intervals

    phase_map = {
        surge_start: ("surge",    "stadium surge"),
        surge_end:   ("drain",    "crowd draining"),
        surge_end + 4: ("tail",   "near-normal"),
    }
    markers = []
    for i, (phase, label) in phase_map.items():
        if i >= _NUM_INTERVALS:
            continue
        markers.append({
            "sim_step": i * _SIM_STEPS_PER_INTERVAL,
            "interval": i,
            "label": label,
            "phase": phase,
        })
    return markers


def _build_schedule_for(scenario: str) -> list[tuple[int, np.ndarray]]:
    if scenario == "stadium_shock":
        return _build_stadium_schedule()
    return _build_accident_schedule()


def _build_markers_for(scenario: str) -> list[dict[str, Any]]:
    if scenario == "stadium_shock":
        return _build_stadium_markers()
    return _build_accident_markers()


def _build_shock_log_config(scenario: str) -> dict[str, Any]:
    """Summarize scenario-specific parameters for the logbook entry."""
    if scenario == "stadium_shock":
        cfg = _STADIUM_CONFIG
        return {
            "num_intervals": _NUM_INTERVALS,
            "steps_per_interval": _SIM_STEPS_PER_INTERVAL,
            "surge_onset_interval": cfg.surge_onset_interval,
            "surge_duration_intervals": cfg.surge_duration_intervals,
            "surge_fraction": cfg.surge_fraction,
            "affected_node": cfg.affected_node,
            "timing_incoherence_fraction": cfg.timing_incoherence_fraction,
        }
    else:
        cfg = _ACCIDENT_CONFIG
        return {
            "num_intervals": _NUM_INTERVALS,
            "steps_per_interval": _SIM_STEPS_PER_INTERVAL,
            "onset_interval": cfg.onset_interval,
            "onset_duration_intervals": cfg.onset_duration_intervals,
            "peak_duration_intervals": cfg.peak_duration_intervals,
            "recovery_duration_intervals": cfg.recovery_duration_intervals,
            "peak_reduction_fraction": cfg.peak_reduction_fraction,
        }


# Build initial schedule and markers at module load time.
_perturbation_schedule = _build_schedule_for(_active_scenario)
_scenario_markers = _build_markers_for(_active_scenario)
_schedule_cursor: int = 0

# Shock config dict for the logbook — rebuilt when scenario switches.
_SHOCK_LOG_CONFIG: dict[str, Any] = _build_shock_log_config(_active_scenario)


# ---------------------------------------------------------------------------
# State serialization — what gets broadcast to clients
# ---------------------------------------------------------------------------

def _build_state_snapshot() -> dict[str, Any]:
    """
    Serialize the current web state to a flat JSON-safe dict.

    Schema:
      tick              — monotonic step counter (liveness indicator)
      sim_time          — simulation time in web physics units
      energy            — total mechanical energy (kinetic + potential)
      total_tension     — sum of all node tensions
      paused            — whether playback is currently paused
      speed             — current speed multiplier
      scenario_progress — fraction of schedule consumed [0.0, 1.0]
      active_scenario   — name of the currently active scenario
      total_sim_steps   — total sim steps in the active scenario schedule
      nodes             — list of {index, label, tension, velocity, net_flux}
      strands           — list of {i, j, coupling, tension_gradient, tension_i, tension_j}
      scenario_markers  — fixed list of phase-boundary events for chart annotation
                          each: {sim_step, interval, label, phase}
    """
    nodes_raw = web.observe()
    tension_vec = web.tension
    coupling = web.coupling_matrix

    nodes_payload = [
        {
            "index": n.index,
            "label": n.label,
            "tension": round(n.tension, 4),
            "velocity": round(n.velocity, 4),
            "net_flux": round(n.net_flux, 4),
        }
        for n in nodes_raw
    ]

    # Strands: upper triangle of the coupling matrix (3 strands for a triangle)
    strands_payload = []
    n = web.num_nodes
    for i in range(n):
        for j in range(i + 1, n):
            w = float(coupling[i, j])
            if w > 0:
                gradient = abs(float(tension_vec[i]) - float(tension_vec[j])) * w
                strands_payload.append({
                    "i": i,
                    "j": j,
                    "coupling": round(w, 4),
                    "tension_gradient": round(gradient, 4),
                    "tension_i": round(float(tension_vec[i]), 4),
                    "tension_j": round(float(tension_vec[j]), 4),
                })

    return {
        "tick": _tick,
        "sim_time": round(web.time, 4),
        "sim_step": web.step_count,
        "energy": round(web.total_energy(), 6),
        "total_tension": round(web.total_tension(), 4),
        "paused": _paused,
        "speed": _speed,
        "scenario_progress": round(_schedule_cursor / len(_perturbation_schedule), 4),
        "active_scenario": _active_scenario,
        "total_sim_steps": _NUM_INTERVALS * _SIM_STEPS_PER_INTERVAL,
        "nodes": nodes_payload,
        "strands": strands_payload,
        "scenario_markers": _scenario_markers,
    }


# ---------------------------------------------------------------------------
# Background simulation loop
# ---------------------------------------------------------------------------

async def _simulation_loop() -> None:
    """
    Drive the web physics forward at ~10 Hz, injecting perturbations
    from the pre-built schedule and broadcasting state to all clients.

    Loop structure:
      1. Handle scenario switch, restart, or step request
      2. If paused and no step request, broadcast current state and idle
      3. Apply any scheduled perturbations for the current step
      4. Advance the web by one physics step (repeated per speed multiplier)
      5. Serialize and broadcast state to all connected clients
      6. Sleep to maintain target cadence
      7. When schedule exhausts, reset web and restart scenario
    """
    global _tick, _schedule_cursor, web
    global _paused, _speed, _step_requested, _restart_requested
    global _perturbation_events, _scenario_start_tick, _run_logger
    global _active_scenario, _scenario_switch_requested
    global _perturbation_schedule, _scenario_markers, _SHOCK_LOG_CONFIG

    BASE_INTERVAL = 0.10  # seconds — 10 Hz base cadence

    while True:
        loop_start = asyncio.get_event_loop().time()

        # --- Handle scenario switch (rebuilds schedule + markers, then restarts) ---
        if _scenario_switch_requested is not None:
            new_scenario = _scenario_switch_requested
            _scenario_switch_requested = None
            if new_scenario in ("accident_shock", "stadium_shock"):
                _active_scenario = new_scenario
                _perturbation_schedule = _build_schedule_for(_active_scenario)
                _scenario_markers = _build_markers_for(_active_scenario)
                _SHOCK_LOG_CONFIG = _build_shock_log_config(_active_scenario)
            _restart_requested = True  # fall through to restart logic below

        # --- Handle restart ---
        if _restart_requested:
            _restart_requested = False
            web = create_triangle_web(**_WEB_CONFIG)
            _schedule_cursor = 0
            _perturbation_events = []
            _scenario_start_tick = _tick
            _run_logger.reset()
            _run_logger.run_start_tick = _tick
            _run_logger.run_start_sim_step = 0

        # --- If paused and no step request, just broadcast and idle ---
        if _paused and not _step_requested:
            if _clients:
                snapshot = _build_state_snapshot()
                payload = json.dumps(snapshot)
                dead: set[WebSocket] = set()
                for ws in _clients:
                    try:
                        await ws.send_text(payload)
                    except Exception:
                        dead.add(ws)
                _clients.difference_update(dead)
            elapsed = asyncio.get_event_loop().time() - loop_start
            await asyncio.sleep(max(0.0, BASE_INTERVAL - elapsed))
            continue

        # --- Consume step request flag ---
        if _step_requested:
            _step_requested = False

        # --- Determine how many physics ticks to run this interval ---
        # Speed multiplier > 1 means more ticks per wall-clock interval.
        # Speed < 1 means we only tick every Nth interval (handled by not always stepping).
        # Simplest model: run floor(speed) ticks always, plus an extra one probabilistically
        # for fractional parts. This keeps the cadence smooth.
        if _speed >= 1.0:
            ticks_this_interval = int(_speed)
        else:
            # Sub-1x speed: run one tick every (1/speed) intervals on average.
            # We track fractional accumulator to avoid drift.
            if not hasattr(_simulation_loop, '_speed_acc'):
                _simulation_loop._speed_acc = 0.0
            _simulation_loop._speed_acc += _speed
            if _simulation_loop._speed_acc >= 1.0:
                ticks_this_interval = 1
                _simulation_loop._speed_acc -= 1.0
            else:
                ticks_this_interval = 0
        if hasattr(_simulation_loop, '_speed_acc') and _speed >= 1.0:
            _simulation_loop._speed_acc = 0.0

        # At sub-1x speed, ticks_this_interval may be 0 — skip physics entirely.
        n_ticks = ticks_this_interval if ticks_this_interval > 0 else 0

        for _ in range(n_ticks):
            # Apply perturbations scheduled for this step
            while (
                _schedule_cursor < len(_perturbation_schedule)
                and _perturbation_schedule[_schedule_cursor][0] <= web.step_count
            ):
                _scheduled_step, delta = _perturbation_schedule[_schedule_cursor]
                web.perturb_vector(delta)
                _run_logger.record_perturbation(_tick, web.step_count, delta)
                _schedule_cursor += 1

            # Advance physics
            web.step()
            _tick += 1

            # Periodic snapshot for the logbook (every N ticks)
            if _tick % _LOG_SNAPSHOT_EVERY_N_TICKS == 0:
                t_vec = web.tension
                v_vec = web.velocity
                _run_logger.record_snapshot(
                    tick=_tick,
                    sim_step=web.step_count,
                    energy=web.total_energy(),
                    total_tension=web.total_tension(),
                    node_tensions=[float(t_vec[i]) for i in range(web.num_nodes)],
                    node_velocities=[float(v_vec[i]) for i in range(web.num_nodes)],
                )

        # --- Broadcast to all connected clients ---
        if _clients:
            snapshot = _build_state_snapshot()
            payload = json.dumps(snapshot)
            dead: set[WebSocket] = set()
            for ws in _clients:
                try:
                    await ws.send_text(payload)
                except Exception:
                    dead.add(ws)
            _clients.difference_update(dead)

        # --- Reset scenario when schedule is exhausted and web is quiet ---
        # Auto-log the completed run BEFORE resetting, so the full scenario
        # data is always captured in the logbook.
        if _schedule_cursor >= len(_perturbation_schedule):
            energy = web.total_energy()
            if energy < 1e-4 or web.step_count > 10_000:
                # Capture final snapshot before reset
                t_vec = web.tension
                v_vec = web.velocity
                _run_logger.record_snapshot(
                    tick=_tick,
                    sim_step=web.step_count,
                    energy=energy,
                    total_tension=web.total_tension(),
                    node_tensions=[float(t_vec[i]) for i in range(web.num_nodes)],
                    node_velocities=[float(v_vec[i]) for i in range(web.num_nodes)],
                )
                # Auto-log the completed run
                try:
                    _run_logger.write_entry(
                        scenario_name=_active_scenario,
                        web_config=_WEB_CONFIG,
                        shock_config=_SHOCK_LOG_CONFIG,
                        current_tick=_tick,
                        current_sim_step=web.step_count,
                        current_energy=energy,
                    )
                except Exception:
                    pass  # Don't let logging errors crash the loop
                # Now reset
                web = create_triangle_web(**_WEB_CONFIG)
                _schedule_cursor = 0
                _perturbation_events = []
                _scenario_start_tick = _tick
                _run_logger.reset()
                _run_logger.run_start_tick = _tick
                _run_logger.run_start_sim_step = 0

        # --- Maintain cadence (adjusted for speed) ---
        # At speed > 1 we still broadcast at ~10 Hz (humans can't track faster).
        # The extra ticks per interval is how we accelerate, not the broadcast rate.
        elapsed = asyncio.get_event_loop().time() - loop_start
        if _speed < 1.0:
            # Slow mode: stretch the interval
            sleep_time = max(0.0, (BASE_INTERVAL / _speed) - elapsed)
        else:
            sleep_time = max(0.0, BASE_INTERVAL - elapsed)
        await asyncio.sleep(sleep_time)


# ---------------------------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------------------------

app = FastAPI(title="Ayin Intelligence — Tension Web", version="0.1.0")

# Serve static files (visualize.html lives here)
_static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(_static_dir)), name="static")


@app.on_event("startup")
async def _startup() -> None:
    """Start the simulation loop as a background task on server startup."""
    _run_logger.run_start_tick = _tick
    _run_logger.run_start_sim_step = 0
    asyncio.create_task(_simulation_loop())


@app.get("/")
async def root() -> FileResponse:
    """Serve the visualization HTML at the root route."""
    return FileResponse(str(_static_dir / "visualize.html"))


# ---------------------------------------------------------------------------
# WebSocket endpoint — streams full web state at 10 Hz, receives control messages
# ---------------------------------------------------------------------------

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket connection for real-time state streaming and playback control.

    Server -> client: JSON state snapshots at ~10 Hz (from simulation loop).

    Client -> server: control messages (JSON):
      {"cmd": "restart"}            — reset scenario
      {"cmd": "pause"}              — pause simulation
      {"cmd": "resume"}             — resume simulation
      {"cmd": "step"}               — advance one tick while paused
      {"cmd": "speed", "value": X}  — set speed (0.25, 0.5, 1, 2, 4)

    On connect: immediately send one snapshot so the client renders
    something before the next broadcast tick.
    """
    global _paused, _speed, _step_requested, _restart_requested, _scenario_switch_requested

    await websocket.accept()
    _clients.add(websocket)

    VALID_SPEEDS = {0.25, 0.5, 1.0, 2.0, 4.0}

    try:
        # Send initial snapshot immediately so the client isn't blank
        snapshot = _build_state_snapshot()
        await websocket.send_text(json.dumps(snapshot))

        # Listen for control messages
        while True:
            raw = await websocket.receive_text()
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                await websocket.send_text(json.dumps({"error": "invalid JSON"}))
                continue

            cmd = msg.get("cmd")
            if cmd == "restart":
                _restart_requested = True
                _paused = False
            elif cmd == "pause":
                _paused = True
            elif cmd == "resume":
                _paused = False
            elif cmd == "step":
                _step_requested = True
            elif cmd == "speed":
                val = msg.get("value")
                if val in VALID_SPEEDS:
                    _speed = float(val)
                else:
                    await websocket.send_text(json.dumps({
                        "error": f"invalid speed {val!r}, valid: {sorted(VALID_SPEEDS)}"
                    }))
            elif cmd == "scenario":
                val = msg.get("value")
                if val in ("accident_shock", "stadium_shock"):
                    _scenario_switch_requested = val
                    _paused = False
                    await websocket.send_text(json.dumps({
                        "scenario_switching": True,
                        "scenario": val,
                    }))
                else:
                    await websocket.send_text(json.dumps({
                        "error": (
                            f"invalid scenario {val!r}, "
                            "valid: 'accident_shock' | 'stadium_shock'"
                        )
                    }))
            elif cmd == "log":
                try:
                    entry = _run_logger.write_entry(
                        scenario_name=_active_scenario,
                        web_config=_WEB_CONFIG,
                        shock_config=_SHOCK_LOG_CONFIG,
                        current_tick=_tick,
                        current_sim_step=web.step_count,
                        current_energy=web.total_energy(),
                    )
                    await websocket.send_text(json.dumps({
                        "logged": True,
                        "path": str(_LOGBOOK_PATH),
                        "entry_lines": entry.count("\n"),
                    }))
                except Exception as exc:
                    await websocket.send_text(json.dumps({
                        "error": f"log failed: {exc}"
                    }))
            else:
                await websocket.send_text(json.dumps({"error": f"unknown cmd {cmd!r}"}))

    except WebSocketDisconnect:
        pass
    except Exception:
        pass
    finally:
        _clients.discard(websocket)


# ---------------------------------------------------------------------------
# Ingestion endpoints — POST per node
# ---------------------------------------------------------------------------

def _validate_tension_payload(body: dict[str, Any]) -> float:
    """
    Validate an ingestion payload. Expects {"tension": <float>}.
    Returns the validated tension value.
    Raises ValueError with a clear message on invalid input.
    """
    if "tension" not in body:
        raise ValueError("Payload must contain 'tension' key")
    val = body["tension"]
    if not isinstance(val, (int, float)):
        raise ValueError(f"'tension' must be a number, got {type(val).__name__}")
    val = float(val)
    if not np.isfinite(val):
        raise ValueError(f"'tension' must be finite, got {val}")
    if abs(val) > 100.0:
        raise ValueError(
            f"'tension' magnitude {val:.2f} exceeds limit 100.0 — "
            "check volume-to-tension scaling"
        )
    return val


from fastapi import Request
from fastapi.responses import JSONResponse


@app.post("/ingest/node/{node_index}")
async def ingest_node(node_index: int, request: Request) -> JSONResponse:
    """
    Inject a perturbation at a specific node.

    Request body: {"tension": <float>}
      tension — perturbation magnitude to add at this node.
                Positive = excess load. Negative = underload.
                Typical range: [-2.0, 2.0] for realistic traffic deviations.

    Returns the updated node tension after injection.
    """
    if node_index not in range(web.num_nodes):
        return JSONResponse(
            status_code=422,
            content={
                "error": f"node_index {node_index} out of range [0, {web.num_nodes})",
                "valid_nodes": list(range(web.num_nodes)),
            },
        )

    try:
        body = await request.json()
    except Exception:
        return JSONResponse(
            status_code=422,
            content={"error": "Request body must be valid JSON"},
        )

    try:
        tension_delta = _validate_tension_payload(body)
    except ValueError as exc:
        return JSONResponse(status_code=422, content={"error": str(exc)})

    web.perturb(node_index, tension_delta)

    return JSONResponse(
        content={
            "ok": True,
            "node_index": node_index,
            "node_label": NODE_LABELS.get(node_index, f"Node-{node_index}"),
            "tension_after": round(float(web.tension[node_index]), 4),
        }
    )


@app.post("/ingest/web")
async def ingest_web(request: Request) -> JSONResponse:
    """
    Inject perturbations at all nodes simultaneously.

    Request body: {"tensions": [<float>, <float>, <float>]}
      tensions — list of perturbation magnitudes, one per node.
                 Length must equal the number of nodes (3).

    Useful for correlated external events that affect multiple nodes at once.
    """
    try:
        body = await request.json()
    except Exception:
        return JSONResponse(
            status_code=422,
            content={"error": "Request body must be valid JSON"},
        )

    if "tensions" not in body:
        return JSONResponse(
            status_code=422,
            content={"error": "Payload must contain 'tensions' key (list of floats)"},
        )

    tensions_raw = body["tensions"]
    if not isinstance(tensions_raw, list) or len(tensions_raw) != web.num_nodes:
        return JSONResponse(
            status_code=422,
            content={
                "error": f"'tensions' must be a list of {web.num_nodes} floats",
                "got_length": len(tensions_raw) if isinstance(tensions_raw, list) else None,
            },
        )

    validated: list[float] = []
    for i, v in enumerate(tensions_raw):
        try:
            validated.append(_validate_tension_payload({"tension": v}))
        except ValueError as exc:
            return JSONResponse(
                status_code=422,
                content={"error": f"Node {i}: {exc}"},
            )

    delta = np.array(validated, dtype=np.float64)
    web.perturb_vector(delta)

    return JSONResponse(
        content={
            "ok": True,
            "tensions_after": [round(float(t), 4) for t in web.tension],
        }
    )


@app.get("/state")
async def get_state() -> JSONResponse:
    """Return the current web state snapshot as JSON (same schema as websocket)."""
    return JSONResponse(content=_build_state_snapshot())


@app.post("/log")
async def trigger_log() -> JSONResponse:
    """
    Write the current run's accumulated data to ayin/docs/logbook.md.

    This is the REST equivalent of the websocket {cmd: "log"} message.
    Returns a summary of what was written.
    """
    try:
        entry = _run_logger.write_entry(
            scenario_name=_active_scenario,
            web_config=_WEB_CONFIG,
            shock_config=_SHOCK_LOG_CONFIG,
            current_tick=_tick,
            current_sim_step=web.step_count,
            current_energy=web.total_energy(),
        )
        return JSONResponse(content={
            "logged": True,
            "path": str(_LOGBOOK_PATH),
            "entry_lines": entry.count("\n"),
            "snapshots_recorded": len(_run_logger.snapshots),
            "perturbations_recorded": len(_run_logger.perturbation_events),
            "incoherence_events": len(_run_logger.incoherence_events),
        })
    except Exception as exc:
        return JSONResponse(status_code=500, content={"error": str(exc)})
