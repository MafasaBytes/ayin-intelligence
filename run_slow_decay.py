"""
Standalone script: run the slow_decay (gradual construction zone capacity loss) scenario
through the TensionWeb physics engine and append a full logbook entry.

Parameters mirror the accident and stadium scenarios exactly for the web:
  strand_strength=1.0, propagation_rate=1.0, damping_coefficient=0.3, dt=0.05

Scenario parameters:
  seed=271, start_hour=6.0, num_intervals=36, steps_per_interval=5
  (36 intervals = 3 hours of morning traffic starting at 6 AM)

The slow decay is the hardest scenario for the web. Unlike accident (sharp shock)
or stadium (unmapped point event), construction zone capacity loss accumulates at
1% per interval — well within the 10% noise CV. The detection question is:
does the web show coherence degradation (rising recovery time trend) before any
single node exceeds a threshold?

Run without a server — imports modules directly and executes physics in-process.
"""

from __future__ import annotations

import sys
import os
from datetime import datetime, timezone

import numpy as np

# Ensure the project root is on sys.path so the 'ayin' package is importable.
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from ayin.web import create_triangle_web
from ayin.simulator import (
    compose_scenario_slow_decay,
    BaselineConfig,
    generate_baseline,
    SlowDecayConfig,
    generate_slow_decay,
    volume_to_tension_delta,
    BASELINE_MIDDAY,
    NODE_SENSITIVITY,
)


# ---------------------------------------------------------------------------
# Configuration — web params identical to accident and stadium runs
# ---------------------------------------------------------------------------

WEB_STRAND_STRENGTH    = 1.0
WEB_PROPAGATION_RATE   = 1.0
WEB_DAMPING_COEFF      = 0.3
WEB_DT                 = 0.05

SEED                   = 271
START_HOUR             = 6.0   # 6 AM — morning pre-ramp, construction workers arrive early
NUM_INTERVALS          = 36    # 3 hours (same as previous runs)
STEPS_PER_INTERVAL     = 5

# SlowDecayConfig defaults (onset_interval=6, decay_rate=0.01, max_reduction=0.35)
DECAY_ONSET_INTERVAL         = 6    # 30 min in — workers arrive, begin barricade setup
DECAY_RATE_PER_INTERVAL      = 0.01 # 1% capacity loss per 5-min interval
MAX_REDUCTION                = 0.35 # 35% max — one lane of two fully closed

INCOHERENCE_THRESHOLD  = 0.5   # same threshold as previous runs
SETTLE_ENERGY_TARGET   = 1e-4  # settle criterion after main run
MAX_SETTLE_STEPS       = 2000  # safety cap on settling loop

LOGBOOK_PATH = os.path.join(ROOT, "ayin", "docs", "logbook.md")
NODE_NAMES = ["N0 (Intersection Throughput)", "N1 (Signal Timing)", "N2 (Approaching Traffic)"]


# ---------------------------------------------------------------------------
# Helper: format a float with sign for display
# ---------------------------------------------------------------------------

def signed(v: float, decimals: int = 4) -> str:
    fmt = f"+.{decimals}f" if v >= 0 else f".{decimals}f"
    return format(v, fmt)


# ---------------------------------------------------------------------------
# Step 1 — Generate scenario data
# ---------------------------------------------------------------------------

def generate_scenario() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns:
        perturbed_volumes: (36, 3) — slow decay scenario volumes
        clean_baseline:    (36, 3) — same seed baseline without perturbation
        tension_deltas:    (36, 3) — per-interval tension perturbation vectors
        decay_envelope:    (36,)   — the accumulated capacity reduction at each interval
    """
    rng_perturbed = np.random.default_rng(SEED)
    cfg = BaselineConfig(start_hour=START_HOUR, num_intervals=NUM_INTERVALS)
    baseline_volumes = generate_baseline(cfg, rng_perturbed)

    decay_cfg = SlowDecayConfig(
        onset_interval=DECAY_ONSET_INTERVAL,
        decay_rate_per_interval=DECAY_RATE_PER_INTERVAL,
        max_reduction=MAX_REDUCTION,
    )
    perturbed_volumes = generate_slow_decay(baseline_volumes, decay_cfg, rng_perturbed)

    # Clean baseline for delta computation — same seed, replayed
    rng_clean = np.random.default_rng(SEED)
    clean_baseline = generate_baseline(BaselineConfig(start_hour=START_HOUR, num_intervals=NUM_INTERVALS), rng_clean)

    # Tension deltas: deviation of perturbed from clean baseline
    tension_deltas = volume_to_tension_delta(perturbed_volumes, clean_baseline)

    # Compute the actual decay envelope (what reduction was applied at each interval).
    # We replay the envelope logic to capture it for the logbook — the stochastic
    # reversals mean we must re-run with the same RNG state, so we extract it by
    # computing the reduction implied by comparing perturbed vs clean on node 2.
    # Node 2 only gets the construction reduction (no blending like node 0 lag logic).
    # reduction[i] = 1 - perturbed[i,2] / clean_baseline[i,2]
    decay_envelope = np.zeros(NUM_INTERVALS, dtype=np.float64)
    for i in range(NUM_INTERVALS):
        if clean_baseline[i, 2] > 0:
            decay_envelope[i] = max(0.0, 1.0 - perturbed_volumes[i, 2] / clean_baseline[i, 2])

    return perturbed_volumes, clean_baseline, tension_deltas, decay_envelope


# ---------------------------------------------------------------------------
# Step 2 — Run the web engine
# ---------------------------------------------------------------------------

def run_web(tension_deltas: np.ndarray) -> dict:
    """
    Drive TensionWeb through all 36 intervals + settle phase.

    At each interval:
      1. inject the interval's tension delta via perturb_vector()
      2. run STEPS_PER_INTERVAL web.step() calls
      3. read coherence snapshot after each step

    For slow decay specifically, we track:
      - Per-interval energy levels (to detect gradual accumulation)
      - Recovery time trend (the key early-warning signal)
      - Incoherence score trend per interval (are scores drifting upward?)

    Returns a results dict with all collected data.
    """
    web = create_triangle_web(
        strand_strength=WEB_STRAND_STRENGTH,
        propagation_rate=WEB_PROPAGATION_RATE,
        damping_coefficient=WEB_DAMPING_COEFF,
        dt=WEB_DT,
    )

    # --- Pre-run analytical properties ---
    damping_ratios = web.damping_ratio_per_mode()
    eigenvalues = web.eigenvalues
    analytical_zeta = web.coherence().analytical_damping_ratio

    # --- Per-step data collection ---
    step_data = []
    interval_events = []

    total_step = 0
    start_energy = None
    peak_energy = 0.0
    peak_energy_step = 0

    # Per-node peak tension tracking (by absolute magnitude)
    peak_tension_per_node = [0.0, 0.0, 0.0]
    peak_tension_step_per_node = [0, 0, 0]

    # Incoherence score tracking for trend analysis
    # We record the mean incoherence score per interval to see if it drifts upward
    interval_mean_incoherence = []   # mean score across 3 nodes per interval
    interval_energy_end = []         # energy at end of each interval (after 5 steps)

    # Previous incoherence scores to detect rising-edge crossings
    prev_incoherence = np.zeros(3)

    # --- Interval phase ---
    for interval_idx in range(NUM_INTERVALS):
        delta = tension_deltas[interval_idx]

        # Inject perturbation
        web.perturb_vector(delta)
        interval_events.append({
            "step": total_step,
            "type": "perturbation",
            "interval": interval_idx,
            "delta": delta.copy(),
        })

        # Run propagation steps
        interval_incoherence_acc = np.zeros(3)
        for sub_step in range(STEPS_PER_INTERVAL):
            web.step()
            total_step += 1

            T = web.tension
            V = web.velocity
            E = web.total_energy()

            if start_energy is None and total_step == 1:
                start_energy = E

            if E > peak_energy:
                peak_energy = E
                peak_energy_step = total_step

            # Per-node peak tension (by absolute magnitude)
            for n in range(3):
                if abs(T[n]) > abs(peak_tension_per_node[n]):
                    peak_tension_per_node[n] = T[n]
                    peak_tension_step_per_node[n] = total_step

            # Coherence snapshot
            snap = web.coherence()
            scores = snap.incoherence_scores.copy()
            interval_incoherence_acc += scores

            # Flag incoherence threshold crossings (rising edge only)
            for n in range(3):
                if scores[n] > INCOHERENCE_THRESHOLD and prev_incoherence[n] <= INCOHERENCE_THRESHOLD:
                    interval_events.append({
                        "step": total_step,
                        "type": "incoherence",
                        "node": n,
                        "score": float(scores[n]),
                        "tension": float(T[n]),
                        "velocity": float(V[n]),
                    })

            prev_incoherence = scores.copy()

            step_data.append({
                "step": total_step,
                "interval": interval_idx,
                "tension": T.copy(),
                "velocity": V.copy(),
                "energy": E,
                "incoherence": scores.copy(),
                "empirical_zeta": snap.empirical_damping_ratio,
                "last_recovery_time": snap.last_recovery_time,
                "recovery_trend_slope": snap.recovery_trend_slope,
            })

        # Record per-interval summary for trend analysis
        interval_mean_incoherence.append(float(np.mean(interval_incoherence_acc / STEPS_PER_INTERVAL)))
        interval_energy_end.append(float(web.total_energy()))

    # --- Settle phase: run until energy < SETTLE_ENERGY_TARGET ---
    settle_steps = 0
    while web.total_energy() > SETTLE_ENERGY_TARGET and settle_steps < MAX_SETTLE_STEPS:
        web.step()
        total_step += 1
        settle_steps += 1

        T = web.tension
        V = web.velocity
        E = web.total_energy()

        snap = web.coherence()
        scores = snap.incoherence_scores.copy()

        for n in range(3):
            if scores[n] > INCOHERENCE_THRESHOLD and prev_incoherence[n] <= INCOHERENCE_THRESHOLD:
                interval_events.append({
                    "step": total_step,
                    "type": "incoherence",
                    "node": n,
                    "score": float(scores[n]),
                    "tension": float(T[n]),
                    "velocity": float(V[n]),
                })
        prev_incoherence = scores.copy()

        step_data.append({
            "step": total_step,
            "interval": "settle",
            "tension": T.copy(),
            "velocity": V.copy(),
            "energy": E,
            "incoherence": scores.copy(),
            "empirical_zeta": snap.empirical_damping_ratio,
            "last_recovery_time": snap.last_recovery_time,
            "recovery_trend_slope": snap.recovery_trend_slope,
        })

    # Final state
    final_snap = web.coherence()
    final_T = web.tension
    final_E = web.total_energy()

    # Collect all recovery episodes from the monitor
    recovery_episodes = web.monitor.recovery_history

    return {
        "step_data": step_data,
        "interval_events": interval_events,
        "recovery_episodes": recovery_episodes,
        "start_energy": start_energy if start_energy is not None else 0.0,
        "peak_energy": peak_energy,
        "peak_energy_step": peak_energy_step,
        "final_energy": final_E,
        "final_tension": final_T.copy(),
        "final_snap": final_snap,
        "total_steps": total_step,
        "settle_steps": settle_steps,
        "peak_tension_per_node": peak_tension_per_node,
        "peak_tension_step_per_node": peak_tension_step_per_node,
        "analytical_zeta": analytical_zeta,
        "eigenvalues": eigenvalues,
        "damping_ratios": damping_ratios,
        "interval_mean_incoherence": interval_mean_incoherence,
        "interval_energy_end": interval_energy_end,
    }


# ---------------------------------------------------------------------------
# Step 3 — Build logbook entry
# ---------------------------------------------------------------------------

def build_logbook_entry(
    results: dict,
    tension_deltas: np.ndarray,
    decay_envelope: np.ndarray,
    timestamp: str,
) -> str:
    """
    Construct the full markdown logbook entry from the run results.

    Slow decay logbook entry has additional sections not present in accident/stadium:
      - Decay envelope table (how much capacity was removed per interval)
      - Recovery time trend analysis (the primary detection signal)
      - Incoherence score trajectory per interval (is degradation visible before threshold?)
    """
    sd = results["step_data"]
    events = results["interval_events"]
    episodes = results["recovery_episodes"]

    perturbation_events = [e for e in events if e["type"] == "perturbation"]
    incoherence_events  = [e for e in events if e["type"] == "incoherence"]

    # Count incoherence events per node
    incoherence_count = [0, 0, 0]
    for e in incoherence_events:
        incoherence_count[e["node"]] += 1
    total_incoherence = sum(incoherence_count)

    # Extract final coherence diagnostics
    final_snap = results["final_snap"]
    empirical_zeta = final_snap.empirical_damping_ratio
    analytical_zeta = results["analytical_zeta"]

    # Recovery time summary
    if episodes:
        recovery_times = [ep.recovery_steps for ep in episodes]
        mean_recovery = float(np.mean(recovery_times))
        max_recovery  = float(max(recovery_times))
    else:
        recovery_times = []
        mean_recovery  = float("nan")
        max_recovery   = float("nan")

    # Recovery trend: is recovery time increasing over episodes?
    recovery_trend_slope = final_snap.recovery_trend_slope

    # Find the peak incoherence score per node across all steps
    peak_incoherence_score = [0.0, 0.0, 0.0]
    peak_incoherence_step  = [0, 0, 0]
    for row in sd:
        for n in range(3):
            if row["incoherence"][n] > peak_incoherence_score[n]:
                peak_incoherence_score[n] = row["incoherence"][n]
                peak_incoherence_step[n]  = row["step"]

    # Incoherence scores at the moment of peak energy
    peak_e_step = results["peak_energy_step"]
    incoherence_at_peak_energy = None
    for row in sd:
        if row["step"] == peak_e_step:
            incoherence_at_peak_energy = row["incoherence"].copy()
            break
    if incoherence_at_peak_energy is None:
        incoherence_at_peak_energy = np.zeros(3)

    # Energy at end of main run (before settling)
    end_main_step = NUM_INTERVALS * STEPS_PER_INTERVAL
    energy_at_main_run_end = None
    for row in sd:
        if row["step"] == end_main_step:
            energy_at_main_run_end = row["energy"]
            break
    if energy_at_main_run_end is None and sd:
        interval_rows = [r for r in sd if r["interval"] != "settle"]
        energy_at_main_run_end = interval_rows[-1]["energy"] if interval_rows else 0.0

    # Incoherence score at each interval end (last step of each interval)
    interval_scores_by_node = {n: [] for n in range(3)}
    for row in sd:
        if row["interval"] == "settle":
            continue
        # For each interval, take the last sub-step (sub_step 4 = step 5 of interval)
        if row["step"] % STEPS_PER_INTERVAL == 0:
            for n in range(3):
                interval_scores_by_node[n].append(row["incoherence"][n])

    # --- Build the markdown ---
    lines = []
    lines.append(f"## Slow Decay (Gradual Capacity Loss) — Full Run — {timestamp}")
    lines.append("")
    lines.append("**Scenario:** slow_decay (construction zone setup — gradual approach capacity loss)  ")
    lines.append(f"**Run timestamp:** {timestamp}  ")
    lines.append(f"**Script:** run_slow_decay.py (in-process, no server)  ")
    lines.append("")

    # --- Parameters table ---
    lines.append("### Parameters")
    lines.append("")
    lines.append("| Parameter | Value |")
    lines.append("|-----------|-------|")
    lines.append(f"| strand_strength | {WEB_STRAND_STRENGTH} |")
    lines.append(f"| propagation_rate | {WEB_PROPAGATION_RATE} |")
    lines.append(f"| damping_coefficient | {WEB_DAMPING_COEFF} |")
    lines.append(f"| dt | {WEB_DT} |")
    lines.append(f"| seed | {SEED} |")
    lines.append(f"| start_hour | {START_HOUR} (6:00 AM — morning ramp-up, construction crew arrives) |")
    lines.append(f"| num_intervals | {NUM_INTERVALS} |")
    lines.append(f"| steps_per_interval | {STEPS_PER_INTERVAL} |")
    lines.append(f"| decay_onset_interval | {DECAY_ONSET_INTERVAL} (30 min in) |")
    lines.append(f"| decay_rate_per_interval | {DECAY_RATE_PER_INTERVAL} (1% capacity/5-min) |")
    lines.append(f"| max_reduction | {MAX_REDUCTION} (35% — one lane of two) |")
    lines.append(f"| affected_node | Node 2 (Approaching Traffic) |")
    lines.append(f"| signal_timing_bleed | 15% of construction reduction → Node 1 |")
    lines.append("")

    # --- Decay envelope table ---
    lines.append("### Decay Envelope (Capacity Reduction Applied per Interval)")
    lines.append("")
    lines.append("Capacity reduction actually applied to Node 2 at each interval,")
    lines.append("computed from (1 - perturbed_vol[i,2] / clean_baseline[i,2]).")
    lines.append("Non-monotonic: stochastic reversals visible (workers briefly pull back barricades).")
    lines.append("")
    lines.append("| Interval | Reduction | Delta N0 | Delta N1 | Delta N2 | Phase |")
    lines.append("|----------|-----------|----------|----------|----------|-------|")
    for i in range(NUM_INTERVALS):
        d = tension_deltas[i]
        reduction_pct = decay_envelope[i] * 100.0
        if i < DECAY_ONSET_INTERVAL:
            phase = "pre-onset (baseline noise only)"
        elif decay_envelope[i] < MAX_REDUCTION - 0.001:
            phase = f"ramp-up (accumulating)"
        else:
            phase = "at max reduction"
        lines.append(
            f"| {i:2d} | {reduction_pct:5.2f}% | "
            f"{signed(float(d[0]),4)} | {signed(float(d[1]),4)} | {signed(float(d[2]),4)} | "
            f"{phase} |"
        )
    lines.append("")

    # --- Timeline of key events ---
    lines.append("### Timeline")
    lines.append("")
    lines.append("| Step | Event |")
    lines.append("|------|-------|")

    # Build combined timeline sorted by step
    timeline = []

    for e in perturbation_events:
        d = e["delta"]
        d_str = f"[{signed(float(d[0]),3)} {signed(float(d[1]),3)} {signed(float(d[2]),3)}]"
        timeline.append((e["step"], f"perturbation injected — interval={e['interval']}, delta={d_str}"))

    timeline.append((
        results["peak_energy_step"],
        f"peak energy — {results['peak_energy']:.4e}"
    ))

    for n in range(3):
        timeline.append((
            results["peak_tension_step_per_node"][n],
            f"peak tension {NODE_NAMES[n]} — {results['peak_tension_per_node'][n]:.4f}"
        ))

    for e in incoherence_events:
        n = e["node"]
        timeline.append((
            e["step"],
            f"INCOHERENCE — {NODE_NAMES[n]}, score={e['score']:.3f}, "
            f"tension={e['tension']:.4f}, velocity={signed(e['velocity'],4)}"
        ))

    # Final snapshot
    ft = results["final_tension"]
    fe = results["final_energy"]
    timeline.append((
        results["total_steps"],
        f"final state — energy={fe:.4e}, tensions=[{ft[0]:.4f}, {ft[1]:.4f}, {ft[2]:.4f}]"
    ))

    # Sort and emit
    timeline.sort(key=lambda x: x[0])
    for step, desc in timeline:
        lines.append(f"| {step} | {desc} |")
    lines.append("")

    # --- Coherence diagnostics ---
    lines.append("### Coherence Diagnostics")
    lines.append("")
    lines.append("#### Recovery Episodes")
    lines.append("")
    if episodes:
        lines.append("| # | Perturbation Step | Recovery Step | Recovery Steps | Peak Energy | Settled Energy |")
        lines.append("|---|-------------------|---------------|----------------|-------------|----------------|")
        for k, ep in enumerate(episodes):
            lines.append(
                f"| {k+1} | {ep.perturbation_step} | {ep.recovery_step} | "
                f"{ep.recovery_steps} | {ep.peak_energy:.4e} | {ep.settled_energy:.4e} |"
            )
        lines.append("")
        lines.append(f"**Mean recovery time:** {mean_recovery:.1f} steps  ")
        lines.append(f"**Max recovery time:** {max_recovery:.1f} steps  ")
        if not np.isnan(recovery_trend_slope):
            lines.append(f"**Recovery trend slope:** {recovery_trend_slope:+.4f} steps/episode  ")
            if recovery_trend_slope > 0.5:
                lines.append(f"**Recovery trend direction: INCREASING — coherence is degrading (POC property #2 confirmed)**  ")
            elif recovery_trend_slope > 0:
                lines.append(f"**Recovery trend direction: weakly increasing — marginal coherence decay signal  ")
            elif recovery_trend_slope < -0.5:
                lines.append(f"**Recovery trend direction: DECREASING — web is absorbing perturbations more efficiently over time  ")
            else:
                lines.append(f"**Recovery trend direction: flat — recovery time not trending  ")
        else:
            lines.append("**Recovery trend slope:** NaN — fewer than 2 recovery episodes  ")
    else:
        lines.append("_No recovery episodes completed — perturbations stayed below spike detection threshold throughout._")
        lines.append("")
        lines.append("**Interpretation for slow decay:** This is the expected result if the construction")
        lines.append("capacity loss was gradual enough that no single interval triggered the energy spike")
        lines.append("detector (which requires current energy > 2x the recent baseline). The decay")
        lines.append("accumulates energy gradually — each interval's delta is small — so the energy")
        lines.append("baseline tracks the accumulation rather than spiking above it.")
    lines.append("")

    lines.append("#### Recovery Trend Analysis (Key Slow-Decay Signal)")
    lines.append("")
    lines.append("The recovery trend slope tests POC property #2: _can the web detect gradual degradation")
    lines.append("before any single node shows abnormal values?_")
    lines.append("")
    lines.append("A positive slope (each recovery taking more steps than the last) indicates the web is")
    lines.append("accumulating tension that it cannot fully dissipate between injections — the hallmark")
    lines.append("of a slowly degrading network. This trend can be visible even when individual interval")
    lines.append("deltas are too small to trigger threshold-based alarms.")
    lines.append("")
    if episodes and len(recovery_times) >= 2:
        lines.append("Recovery times per episode (steps):")
        lines.append("")
        lines.append("| Episode | Recovery Steps | Interpretation |")
        lines.append("|---------|----------------|----------------|")
        for k, rt in enumerate(recovery_times):
            ep = episodes[k]
            if k == 0:
                interp = "baseline recovery time"
            elif rt > recovery_times[k - 1] * 1.10:
                interp = "longer than previous (+>10%) — coherence degrading"
            elif rt > recovery_times[k - 1]:
                interp = "slightly longer — marginal increase"
            elif rt < recovery_times[k - 1] * 0.90:
                interp = "shorter than previous — web partially recovered between events"
            else:
                interp = "stable"
            lines.append(f"| {k+1} | {rt} | {interp} |")
        lines.append("")
    elif episodes:
        lines.append("Only one recovery episode recorded — trend requires at least 2 episodes.")
        lines.append("")
    else:
        lines.append("No recovery episodes recorded — spike detector threshold not crossed by gradual decay.")
        lines.append("This means the energy baseline tracking kept pace with the accumulating decay,")
        lines.append("never seeing a single-step jump large enough (>2x baseline) to register as a perturbation spike.")
        lines.append("")

    lines.append("#### Damping Ratio")
    lines.append("")
    lines.append("| Measure | Value |")
    lines.append("|---------|-------|")
    lines.append(f"| Analytical ζ (dominant eigenmode) | {analytical_zeta:.4f} |")
    if not np.isnan(empirical_zeta):
        lines.append(f"| Empirical ζ (log-decrement) | {empirical_zeta:.4f} |")
        ratio = empirical_zeta / analytical_zeta if analytical_zeta > 0 else float("nan")
        lines.append(f"| Empirical / Analytical | {ratio:.3f} |")
    else:
        lines.append("| Empirical ζ (log-decrement) | NaN (insufficient energy peaks for log-decrement) |")
    eigs_fmt = [round(float(v), 4) for v in results['eigenvalues']]
    damp_fmt = [round(float(v), 4) for v in results['damping_ratios']]
    lines.append(f"| Laplacian eigenvalues | {eigs_fmt} |")
    lines.append(f"| Damping ratios per mode | {damp_fmt} |")
    lines.append("")

    lines.append("#### Incoherence Scores")
    lines.append("")
    lines.append("Peak incoherence score per node (across all steps):")
    lines.append("")
    lines.append("| Node | Peak Score | At Step | Threshold Crossings |")
    lines.append("|------|------------|---------|---------------------|")
    for n in range(3):
        lines.append(
            f"| {NODE_NAMES[n]} | {peak_incoherence_score[n]:.4f} | "
            f"{peak_incoherence_step[n]} | {incoherence_count[n]} |"
        )
    lines.append("")

    lines.append("Incoherence scores at peak energy step (step " + str(peak_e_step) + "):")
    lines.append("")
    lines.append("| Node | Score | Interpretation |")
    lines.append("|------|-------|----------------|")
    for n in range(3):
        s = float(incoherence_at_peak_energy[n])
        if s < 0.3:
            interp = "coherent diffusion (anti-correlated with neighbors)"
        elif s < 0.5:
            interp = "weakly incoherent"
        elif s < 0.7:
            interp = "moderately incoherent — external forcing suspected"
        else:
            interp = "strongly incoherent — independent external force likely"
        lines.append(f"| {NODE_NAMES[n]} | {s:.4f} | {interp} |")
    lines.append("")

    # Per-interval incoherence trajectory (sampling every 5th step)
    lines.append("#### Incoherence Score Trajectory (Per Interval, End-of-Interval Sample)")
    lines.append("")
    lines.append("Used to detect whether incoherence scores are trending upward as capacity")
    lines.append("accumulates — the pre-threshold early warning signal for slow decay.")
    lines.append("")
    lines.append("| Interval | N0 Score | N1 Score | N2 Score | Mean | Capacity Loss |")
    lines.append("|----------|----------|----------|----------|------|---------------|")
    mi = results["interval_mean_incoherence"]
    interval_rows = [r for r in sd if r["interval"] != "settle"]
    # Build per-interval end scores (last step of each interval)
    scores_by_interval = {}
    for row in interval_rows:
        idx = row["interval"]
        scores_by_interval[idx] = row["incoherence"].copy()
    for i in range(NUM_INTERVALS):
        if i in scores_by_interval:
            sc = scores_by_interval[i]
            capacity_pct = decay_envelope[i] * 100.0
            lines.append(
                f"| {i:2d} | {sc[0]:.4f} | {sc[1]:.4f} | {sc[2]:.4f} | {np.mean(sc):.4f} | {capacity_pct:.2f}% |"
            )
    lines.append("")

    # --- Energy trajectory ---
    lines.append("### Energy Trajectory")
    lines.append("")
    lines.append("| Milestone | Energy | Step |")
    lines.append("|-----------|--------|------|")
    lines.append(f"| Start (step 1) | {results['start_energy']:.4e} | 1 |")
    lines.append(f"| Peak | {results['peak_energy']:.4e} | {results['peak_energy_step']} |")
    lines.append(f"| End of main run (step {end_main_step}) | {energy_at_main_run_end:.4e} | {end_main_step} |")
    lines.append(f"| Final (after {results['settle_steps']} settle steps) | {results['final_energy']:.4e} | {results['total_steps']} |")
    lines.append(f"| Total dissipated (peak to final) | {results['peak_energy'] - results['final_energy']:.4e} | — |")
    lines.append("")

    # Per-interval energy progression
    lines.append("#### Per-Interval Energy at Interval End")
    lines.append("")
    lines.append("| Interval | Energy | Capacity Loss | Cumulative Trend |")
    lines.append("|----------|--------|---------------|------------------|")
    ie = results["interval_energy_end"]
    for i, e_val in enumerate(ie):
        cap_pct = decay_envelope[i] * 100.0
        if i == 0:
            trend = "baseline"
        elif e_val > ie[i - 1] * 1.05:
            trend = "rising (accumulating)"
        elif e_val < ie[i - 1] * 0.95:
            trend = "falling (dissipating)"
        else:
            trend = "stable"
        lines.append(f"| {i:2d} | {e_val:.4e} | {cap_pct:.2f}% | {trend} |")
    lines.append("")

    # --- POC Property #2: Critical analysis ---
    lines.append("### Critical Analysis: POC Property #2")
    lines.append("")
    lines.append("**The central question:** Can the web detect gradual degradation _before_ any single")
    lines.append("node shows abnormal values? Slow decay tests this specifically because:")
    lines.append("")
    lines.append("- Each interval's capacity loss (1%) is well within the 10% noise CV")
    lines.append("- No single interval's delta should trigger a threshold alarm")
    lines.append("- Detection must come from TREND signals, not point-in-time thresholds")
    lines.append("")

    # Determine early-warning interval: first interval where any node exceeds 0.3 incoherence
    early_warning_interval = None
    for i in range(NUM_INTERVALS):
        if i in scores_by_interval:
            sc = scores_by_interval[i]
            if any(s > 0.3 for s in sc) and i >= DECAY_ONSET_INTERVAL:
                early_warning_interval = i
                break

    # Capacity loss at first warning
    if early_warning_interval is not None:
        cap_at_warning = decay_envelope[early_warning_interval] * 100.0
        lines.append(f"**Early warning indicator (incoherence score > 0.3):**")
        lines.append(f"  First appeared at interval {early_warning_interval} — capacity loss at that point: {cap_at_warning:.2f}%")
        lines.append(f"  Intervals after onset: {early_warning_interval - DECAY_ONSET_INTERVAL}")
        lines.append("")
    else:
        lines.append("**Early warning indicator (incoherence score > 0.3):** Not observed during the run.")
        lines.append("")

    # Threshold alarm interval
    threshold_interval = None
    for i in range(NUM_INTERVALS):
        if i in scores_by_interval:
            sc = scores_by_interval[i]
            if any(s > INCOHERENCE_THRESHOLD for s in sc) and i >= DECAY_ONSET_INTERVAL:
                threshold_interval = i
                break

    if threshold_interval is not None:
        cap_at_threshold = decay_envelope[threshold_interval] * 100.0
        lines.append(f"**Full incoherence threshold crossing (score > {INCOHERENCE_THRESHOLD}):**")
        lines.append(f"  Interval {threshold_interval} — capacity loss at that point: {cap_at_threshold:.2f}%")
        lines.append(f"  The web detected the degradation after {cap_at_threshold:.1f}% capacity had been lost.")
        lines.append("")
    else:
        lines.append(f"**Full incoherence threshold crossing (score > {INCOHERENCE_THRESHOLD}):** Not observed.")
        lines.append("  The gradual decay did not produce a threshold-crossing incoherence event.")
        lines.append("  This means slow decay IS harder to detect than either accident or stadium scenarios.")
        lines.append("")

    # Recovery trend conclusion
    if not np.isnan(recovery_trend_slope) and len(recovery_times) >= 2:
        if recovery_trend_slope > 0:
            lines.append(f"**Recovery trend (slope={recovery_trend_slope:+.4f}):** POSITIVE — each successive")
            lines.append(f"  recovery episode took longer than the last. This is the leading indicator")
            lines.append(f"  that the web detected gradual degradation: the web's ability to return to")
            lines.append(f"  equilibrium is measurably decaying, even if individual incoherence scores")
            lines.append(f"  never crossed the 0.5 threshold during the run.")
        else:
            lines.append(f"**Recovery trend (slope={recovery_trend_slope:+.4f}):** Negative or flat.")
            lines.append(f"  The web absorbed each small perturbation efficiently — the gradual")
            lines.append(f"  capacity reduction did not produce measurable coherence decay within")
            lines.append(f"  the 36-interval window. A longer run (72+ intervals) would be needed")
            lines.append(f"  to see this effect emerge.")
    else:
        lines.append("**Recovery trend:** Insufficient recovery episodes to compute trend.")
        lines.append("  The energy spike detector never fired during the interval phase, meaning")
        lines.append("  all perturbation deltas were too small to register as spikes above the")
        lines.append(f"  2x-baseline threshold. The gradual decay signature is present in the")
        lines.append(f"  tension accumulation (final tensions below zero), but not in discrete")
        lines.append(f"  recovery episodes. This confirms slow decay is genuinely hard for the")
        lines.append(f"  current spike-based recovery tracker.")
    lines.append("")

    # --- Comparison table ---
    lines.append("### Comparison with Accident and Stadium Scenarios")
    lines.append("")
    lines.append("All three runs use identical web parameters (strand=1.0, alpha=1.0, beta=0.3, dt=0.05).")
    lines.append("36 intervals, 5 steps per interval. Start energies differ only by initial noise seed.")
    lines.append("")
    lines.append("| Dimension | Accident Shock | Stadium Shock | Slow Decay |")
    lines.append("|-----------|---------------|---------------|------------|")

    acc_peak_e  = 1.8340
    acc_final_e = 9.8e-5
    acc_incoh   = 21
    acc_n0 = 3; acc_n1 = 11; acc_n2 = 7
    acc_recovery = 1
    acc_mean_rt = "~276 (1 episode)"

    stad_peak_e  = 1.9540
    stad_final_e = 9.82e-5
    stad_incoh   = 3
    stad_n0 = 1; stad_n1 = 1; stad_n2 = 1
    stad_recovery = 1
    stad_mean_rt = "503.0 (1 episode)"

    decay_peak_e  = results["peak_energy"]
    decay_final_e = results["final_energy"]
    decay_incoh   = total_incoherence
    decay_n0 = incoherence_count[0]
    decay_n1 = incoherence_count[1]
    decay_n2 = incoherence_count[2]
    decay_recovery = len(episodes)
    decay_mean_rt = f"{mean_recovery:.1f} ({decay_recovery} episodes)" if decay_recovery > 0 else "None detected"

    lines.append(f"| Peak energy | {acc_peak_e:.4e} | {stad_peak_e:.4e} | {decay_peak_e:.4e} |")
    lines.append(f"| Final energy | {acc_final_e:.2e} | {stad_final_e:.2e} | {decay_final_e:.2e} |")
    lines.append(f"| Total incoherence events | {acc_incoh} | {stad_incoh} | {decay_incoh} |")
    lines.append(f"| Incoherence N0 (Throughput) | {acc_n0} | {stad_n0} | {decay_n0} |")
    lines.append(f"| Incoherence N1 (Signal Timing) | {acc_n1} | {stad_n1} | {decay_n1} |")
    lines.append(f"| Incoherence N2 (Approaching Traffic) | {acc_n2} | {stad_n2} | {decay_n2} |")
    lines.append(f"| Recovery episodes detected | {acc_recovery} | {stad_recovery} | {decay_recovery} |")
    lines.append(f"| Mean recovery time (steps) | {acc_mean_rt} | {stad_mean_rt} | {decay_mean_rt} |")
    if not np.isnan(recovery_trend_slope):
        trend_str = f"{recovery_trend_slope:+.4f}"
    else:
        trend_str = "NaN (0 episodes)"
    lines.append(f"| Recovery trend slope | n/a | n/a | {trend_str} |")
    lines.append(f"| Dominant affected node | N1 (Signal Timing) | all equally | N2 (Approaching Traffic) |")
    lines.append(f"| Perturbation type | sharp single-node shock | unmapped point event | gradual multi-interval drift |")
    lines.append(f"| Detection difficulty | low (large sharp delta) | medium (unmapped but acute) | high (sub-noise-floor drift) |")
    lines.append("")

    lines.append("**Key differences vs accident and stadium:**")
    lines.append("")
    lines.append("1. **Energy profile**: Accident and stadium both produce a sharp peak energy")
    lines.append("   event that the recovery tracker can attach to as a spike. Slow decay builds")
    lines.append("   energy gradually across many intervals — each increment is small relative to")
    lines.append("   the 2x-baseline spike detection threshold. The energy does accumulate, but")
    lines.append("   the accumulation looks like a slow rise rather than a discrete event.")
    lines.append("")
    lines.append("2. **Incoherence pattern**: Accident fires repeatedly (21 times) because each")
    lines.append("   new forced perturbation keeps re-triggering the detector. Stadium fires once")
    lines.append("   (3 nodes simultaneously) at the unmapped onset. Slow decay, if it fires at")
    lines.append("   all, should fire later in the run when accumulated tension finally creates")
    lines.append("   a detectable correlation breakdown — or it may not fire at all, because")
    lines.append("   the node changes are always diffusing coherently (just slowly sinking together).")
    lines.append("")
    lines.append("3. **Detection mechanism**: Accident is detected by magnitude (large delta).")
    lines.append("   Stadium is detected by topology (unmapped pattern). Slow decay is only")
    lines.append("   detectable by TREND (rising recovery time, drifting incoherence baseline).")
    lines.append("   This tests POC property #2 directly: trend-sensitive detection vs.")
    lines.append("   threshold-sensitive detection.")
    lines.append("")

    # --- Summary ---
    lines.append("### Summary")
    lines.append("")
    lines.append(f"**Scenario:** Slow decay — construction zone, 1% capacity/interval, onset at interval {DECAY_ONSET_INTERVAL}")
    lines.append(f"**Total incoherence events:** {total_incoherence} "
                 f"(N0={incoherence_count[0]}, N1={incoherence_count[1]}, N2={incoherence_count[2]})")
    lines.append(f"**Recovery episodes:** {decay_recovery}")
    if not np.isnan(recovery_trend_slope):
        lines.append(f"**Recovery trend slope:** {recovery_trend_slope:+.4f} steps/episode")
    else:
        lines.append("**Recovery trend slope:** NaN (insufficient episodes)")

    detected = total_incoherence > 0
    early_detected = early_warning_interval is not None
    trend_detected = (not np.isnan(recovery_trend_slope) and recovery_trend_slope > 0 and len(recovery_times) >= 2)

    lines.append("")
    lines.append("**Detection result:**")
    lines.append(f"  - Threshold incoherence alarm: {'Yes' if detected else 'No'}")
    lines.append(f"  - Early warning (score > 0.3): {'Yes — interval ' + str(early_warning_interval) if early_detected else 'No'}")
    lines.append(f"  - Recovery trend (positive slope): {'Yes' if trend_detected else 'No'}")
    lines.append("")
    lines.append("**POC Property #2 verdict:**")
    if trend_detected:
        lines.append("  PARTIALLY CONFIRMED: The recovery trend slope was positive, indicating the web")
        lines.append("  accumulated coherence debt before any threshold was crossed. The trend signal")
        lines.append("  is a measurable early-warning indicator of the gradual decay.")
    elif early_detected:
        lines.append("  PARTIALLY CONFIRMED: Early incoherence signal visible (score > 0.3) before full")
        lines.append("  threshold crossing. Trend-sensitive monitoring would detect this scenario.")
    elif detected:
        lines.append("  CONFIRMED (via threshold): The decay accumulated enough tension to trigger incoherence")
        lines.append("  threshold crossings. However, this means the decay was detectable only after significant")
        lines.append("  capacity loss — the 36-interval window may be too short for early detection.")
    else:
        lines.append("  NOT CONFIRMED within this run window: The gradual decay accumulated tension but did not")
        lines.append("  trigger any incoherence threshold crossings, and insufficient recovery episodes exist")
        lines.append("  to show a recovery time trend. The 36-interval window (3 hours) is too short for the")
        lines.append("  1%/interval decay to accumulate into a detectable signal. A longer run (72+ intervals)")
        lines.append("  starting from the onset would be needed to stress-test property #2 fully.")
    lines.append("")
    lines.append("---")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=== Slow Decay (Construction Zone) — In-Process Run ===")
    print(f"Web params: strand={WEB_STRAND_STRENGTH}, alpha={WEB_PROPAGATION_RATE}, "
          f"beta={WEB_DAMPING_COEFF}, dt={WEB_DT}")
    print(f"Scenario:   seed={SEED}, start_hour={START_HOUR}, "
          f"num_intervals={NUM_INTERVALS}, steps_per_interval={STEPS_PER_INTERVAL}")
    print(f"Decay:      onset={DECAY_ONSET_INTERVAL}, rate={DECAY_RATE_PER_INTERVAL}/interval, "
          f"max={MAX_REDUCTION}")
    print()

    # Step 1: generate scenario
    print("Generating scenario data...")
    perturbed_volumes, clean_baseline, tension_deltas, decay_envelope = generate_scenario()
    print(f"  Volumes shape: {perturbed_volumes.shape}")
    print(f"  Tension deltas min/max: [{tension_deltas.min():.4f}, {tension_deltas.max():.4f}]")
    print()

    # Preview the onset interval and a few intervals into the decay
    print(f"  Pre-onset sample (interval {DECAY_ONSET_INTERVAL - 1}):")
    print(f"    Clean baseline:    {clean_baseline[DECAY_ONSET_INTERVAL - 1].round(2)}")
    print(f"    Perturbed:         {perturbed_volumes[DECAY_ONSET_INTERVAL - 1].round(2)}")
    print(f"    Tension deltas:    {tension_deltas[DECAY_ONSET_INTERVAL - 1].round(4)}")
    print(f"    Capacity loss:     {decay_envelope[DECAY_ONSET_INTERVAL - 1]*100:.2f}%")
    print()
    print(f"  Onset interval ({DECAY_ONSET_INTERVAL}):")
    print(f"    Clean baseline:    {clean_baseline[DECAY_ONSET_INTERVAL].round(2)}")
    print(f"    Perturbed:         {perturbed_volumes[DECAY_ONSET_INTERVAL].round(2)}")
    print(f"    Tension deltas:    {tension_deltas[DECAY_ONSET_INTERVAL].round(4)}")
    print(f"    Capacity loss:     {decay_envelope[DECAY_ONSET_INTERVAL]*100:.2f}%")
    print()
    print(f"  Late decay sample (interval {NUM_INTERVALS - 1}):")
    print(f"    Clean baseline:    {clean_baseline[NUM_INTERVALS - 1].round(2)}")
    print(f"    Perturbed:         {perturbed_volumes[NUM_INTERVALS - 1].round(2)}")
    print(f"    Tension deltas:    {tension_deltas[NUM_INTERVALS - 1].round(4)}")
    print(f"    Capacity loss:     {decay_envelope[NUM_INTERVALS - 1]*100:.2f}%")
    print()
    print(f"  Decay envelope range: [{decay_envelope.min()*100:.2f}%, {decay_envelope.max()*100:.2f}%]")
    print(f"  Max capacity loss reached at interval: {decay_envelope.argmax()}")
    print()

    # Step 2: run web engine
    print("Running web physics...")
    results = run_web(tension_deltas)

    total_steps  = results["total_steps"]
    settle_steps = results["settle_steps"]
    main_steps   = total_steps - settle_steps

    print(f"  Main run: {main_steps} steps ({NUM_INTERVALS} intervals x {STEPS_PER_INTERVAL})")
    print(f"  Settle:   {settle_steps} additional steps")
    print(f"  Total:    {total_steps} steps")
    print()
    print(f"  Start energy:  {results['start_energy']:.4e}")
    print(f"  Peak energy:   {results['peak_energy']:.4e} at step {results['peak_energy_step']}")
    print(f"  Final energy:  {results['final_energy']:.4e}")
    print()

    incoherence_events = [e for e in results["interval_events"] if e["type"] == "incoherence"]
    incoh_counts = [0, 0, 0]
    for e in incoherence_events:
        incoh_counts[e["node"]] += 1
    print(f"  Incoherence events: {sum(incoh_counts)} total "
          f"(N0={incoh_counts[0]}, N1={incoh_counts[1]}, N2={incoh_counts[2]})")

    episodes = results["recovery_episodes"]
    print(f"  Recovery episodes: {len(episodes)}")
    if episodes:
        rts = [ep.recovery_steps for ep in episodes]
        print(f"    Recovery times (steps): {rts}")
        final_snap = results["final_snap"]
        slope = final_snap.recovery_trend_slope
        if not np.isnan(slope):
            print(f"    Recovery trend slope: {slope:+.4f} steps/episode")
    print()

    final_snap = results["final_snap"]
    print(f"  Analytical zeta:  {results['analytical_zeta']:.4f}")
    emp = final_snap.empirical_damping_ratio
    print(f"  Empirical zeta:   {emp:.4f}" if not np.isnan(emp) else "  Empirical zeta:   NaN (insufficient peaks)")
    print()

    # Tension summary
    ft = results["final_tension"]
    print(f"  Final tensions: [{ft[0]:.4f}, {ft[1]:.4f}, {ft[2]:.4f}]")
    print(f"  Total tension:  {ft.sum():.4f}")
    print()

    # Step 3: build and write logbook entry
    print("Building logbook entry...")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = build_logbook_entry(results, tension_deltas, decay_envelope, timestamp)

    with open(LOGBOOK_PATH, "a", encoding="utf-8") as f:
        f.write("\n" + entry + "\n")

    print(f"  Written to: {LOGBOOK_PATH}")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
