"""
Phase 2 validation: probationary strand integration protocol.

This script validates that attaching a fourth node (Stadium/Event Venue)
to the three-node triangle web via a probationary strand produces
measurable improvement in coherence at the target node.

The test:
  1. Run the stadium scenario on a 3-node web WITHOUT the fourth node.
     Record baseline incoherence scores at Node 2 (Approaching Traffic).

  2. Run the SAME scenario on a NEW 3-node web WITH a fourth node
     attached via a probationary strand to Node 2. During surge intervals,
     feed the fourth node with the actual stadium demand signal.

  3. Compare:
     - Incoherence scores: did they drop at Node 2?
     - Bidirectional flow: did tension propagate both ways?
     - Energy convergence: did the Lyapunov function still decrease?

  4. Gradually ramp the strand weight (0.01 -> 0.05 -> 0.1 -> 0.25)
     during the run to simulate probationary load bearing.

Physics rationale:
  When the stadium surge hits Node 2 from outside the 3-node model,
  the coherence monitor sees unexplained tension (high incoherence).
  With a fourth node carrying the actual stadium signal and coupled
  to Node 2, the tension at Node 2 is now EXPLAINED by the strand —
  the Laplacian diffusion pattern between Node 3 and Node 2 accounts
  for the tension change. The anti-correlation signature should
  return, lowering the incoherence score.

  The new strand also enables equilibrium-seeking dynamics: excess
  tension at Node 2 can flow BACK to Node 3 through the strand,
  which is bidirectional propagation. This is the physical test of
  whether the strand is a genuine coupling or just a sensor.
"""

from __future__ import annotations

import sys
import os
from datetime import datetime, timezone

import numpy as np

# Ensure the project root is on sys.path
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from ayin.web import create_triangle_web, ProbationTracker
from ayin.simulator import (
    BaselineConfig,
    generate_baseline,
    UnmappedShockConfig,
    generate_unmapped_shock,
    volume_to_tension_delta,
    BASELINE_MIDDAY,
    NODE_SENSITIVITY,
)
from ayin.nodes import NODE_LABELS


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

WEB_STRAND_STRENGTH    = 1.0
WEB_PROPAGATION_RATE   = 1.0
WEB_DAMPING_COEFF      = 0.3
WEB_DT                 = 0.05

SEED                   = 314
START_HOUR             = 20.5
NUM_INTERVALS          = 36
STEPS_PER_INTERVAL     = 5

# Probationary strand weight ramp schedule.
# Format: (interval_threshold, new_weight)
# At the start of each interval >= threshold, set the strand weight.
WEIGHT_RAMP = [
    (0,  0.01),   # initial: near-zero, strand exists but carries almost no load
    (12, 0.05),   # after surge onset: begin loading
    (14, 0.10),   # mid-surge: moderate coupling
    (16, 0.25),   # late surge: significant coupling
]

LOGBOOK_PATH = os.path.join(ROOT, "ayin", "docs", "logbook.md")


# ---------------------------------------------------------------------------
# Step 1: Generate scenario data
# ---------------------------------------------------------------------------

def generate_scenario():
    """Generate the stadium scenario tension deltas and raw surge signal."""
    rng_perturbed = np.random.default_rng(SEED)
    cfg = BaselineConfig(start_hour=START_HOUR, num_intervals=NUM_INTERVALS)
    baseline_volumes = generate_baseline(cfg, rng_perturbed)

    unmapped_cfg = UnmappedShockConfig()
    perturbed_volumes = generate_unmapped_shock(baseline_volumes, unmapped_cfg, rng_perturbed)

    # Clean baseline for delta computation
    rng_clean = np.random.default_rng(SEED)
    clean_baseline = generate_baseline(cfg, rng_clean)

    # Tension deltas for the 3-node web
    tension_deltas = volume_to_tension_delta(perturbed_volumes, clean_baseline)

    # Extract the raw stadium surge signal for Node 2.
    # This is the fractional deviation at Node 2 — the part that is
    # unmapped in the 3-node web. We'll feed this to the external node.
    stadium_signal = tension_deltas[:, 2].copy()  # Node 2 tension deltas

    return tension_deltas, stadium_signal, unmapped_cfg


# ---------------------------------------------------------------------------
# Step 2: Baseline run (no fourth node)
# ---------------------------------------------------------------------------

def run_baseline(tension_deltas: np.ndarray) -> list[float]:
    """
    Run the stadium scenario on the standard 3-node web.
    Returns per-step incoherence scores at Node 2.
    """
    web = create_triangle_web(
        strand_strength=WEB_STRAND_STRENGTH,
        propagation_rate=WEB_PROPAGATION_RATE,
        damping_coefficient=WEB_DAMPING_COEFF,
        dt=WEB_DT,
    )

    node2_incoherence: list[float] = []

    for interval_idx in range(NUM_INTERVALS):
        delta = tension_deltas[interval_idx]
        web.perturb_vector(delta)

        for _ in range(STEPS_PER_INTERVAL):
            web.step()
            snap = web.coherence()
            node2_incoherence.append(float(snap.incoherence_scores[2]))

    return node2_incoherence


# ---------------------------------------------------------------------------
# Step 3: Probationary run (with fourth node)
# ---------------------------------------------------------------------------

def run_probationary(
    tension_deltas: np.ndarray,
    stadium_signal: np.ndarray,
    unmapped_cfg: UnmappedShockConfig,
) -> tuple[list[float], 'ProbationTracker', list[float], list[float]]:
    """
    Run the stadium scenario with a fourth node attached to Node 2.

    During surge intervals, feed the fourth node with the actual
    stadium demand signal. The probationary strand connects the
    fourth node to Node 2 with a gradually increasing weight.

    Returns:
        node2_incoherence: per-step incoherence at Node 2 (4-node web)
        tracker: ProbationTracker with accumulated measurements
        energy_history: total energy at each step
        weight_log: strand weight at each step
    """
    web = create_triangle_web(
        strand_strength=WEB_STRAND_STRENGTH,
        propagation_rate=WEB_PROPAGATION_RATE,
        damping_coefficient=WEB_DAMPING_COEFF,
        dt=WEB_DT,
    )

    # Attach the probationary strand: "Stadium/Event Venue" -> Node 2
    external_node = web.attach_probationary_strand(
        source_label="Stadium/Event Venue",
        target_node=2,
        initial_weight=0.01,
    )
    print(f"  Attached external node {external_node} ('{NODE_LABELS[external_node]}')")
    print(f"  Coupling matrix shape: {web.coupling_matrix.shape}")
    print(f"  Eigenvalues: {web.eigenvalues.round(4)}")
    print(f"  Damping ratios per mode: {web.damping_ratio_per_mode().round(4)}")
    print()

    # Initialize the probation tracker
    tracker = ProbationTracker(source_node=external_node, target_node=2)

    node2_incoherence: list[float] = []
    energy_history: list[float] = []
    weight_log: list[float] = []
    current_weight = 0.01

    for interval_idx in range(NUM_INTERVALS):
        # --- Weight ramp: adjust strand weight at interval boundaries ---
        for threshold, new_weight in WEIGHT_RAMP:
            if interval_idx == threshold and new_weight != current_weight:
                web.set_strand_weight(external_node, 2, new_weight)
                current_weight = new_weight
                print(f"  Interval {interval_idx}: strand weight -> {current_weight}")

        # --- Inject the 3-node perturbation ---
        # The tension deltas are (3,) vectors for the original 3 nodes.
        # We need to expand to (4,) for the 4-node web.
        delta_3 = tension_deltas[interval_idx]
        delta_4 = np.zeros(web.num_nodes, dtype=np.float64)
        delta_4[:3] = delta_3

        # --- Feed the external node with the stadium signal ---
        # During surge intervals, the external node receives the actual
        # stadium demand as a perturbation. This is the signal that was
        # previously unmapped — now it enters the web through a strand.
        if (unmapped_cfg.surge_onset_interval
                <= interval_idx
                < unmapped_cfg.surge_onset_interval + unmapped_cfg.surge_duration_intervals):
            # The stadium signal at this interval is the tension delta
            # that was applied to Node 2 due to the surge. We feed the
            # SAME magnitude to the external node — the strand then
            # carries it to Node 2 via diffusion, explaining the tension.
            delta_4[external_node] = stadium_signal[interval_idx]

        web.perturb_vector(delta_4)

        # --- Propagation steps ---
        for _ in range(STEPS_PER_INTERVAL):
            web.step()

            # Observe for probation tracking
            tracker.observe(web)

            # Record measurements
            snap = web.coherence()
            # Incoherence score for original Node 2 in the expanded web
            node2_incoherence.append(float(snap.incoherence_scores[2]))
            energy_history.append(web.total_energy())
            weight_log.append(current_weight)

    # --- Settle phase: let the web dissipate without perturbation ---
    # Run additional steps with no external forcing so the Lyapunov
    # function (total energy) can demonstrate monotonic decrease.
    settle_target = 1e-4
    max_settle = 2000
    settle_steps = 0
    while web.total_energy() > settle_target and settle_steps < max_settle:
        web.step()
        tracker.observe(web)
        energy_history.append(web.total_energy())
        weight_log.append(current_weight)
        settle_steps += 1

    print(f"  Settle phase: {settle_steps} steps (final energy: {web.total_energy():.4e})")

    return node2_incoherence, tracker, energy_history, weight_log


# ---------------------------------------------------------------------------
# Step 4: Compare and report
# ---------------------------------------------------------------------------

def compare_and_report(
    baseline_incoherence: list[float],
    probation_incoherence: list[float],
    tracker: ProbationTracker,
    energy_history: list[float],
    weight_log: list[float],
    unmapped_cfg: UnmappedShockConfig,
) -> str:
    """
    Compare baseline vs probationary run and build a report.
    Returns the report as a string.
    """
    result = tracker.result(baseline_incoherence)

    lines: list[str] = []
    lines.append("=" * 70)
    lines.append("STRAND VALIDATION RESULTS")
    lines.append("=" * 70)
    lines.append("")

    # --- Criterion 1: Bidirectional propagation ---
    flux = result.flux_accumulator
    lines.append("CRITERION 1: Bidirectional Propagation")
    lines.append("-" * 40)
    lines.append(f"  Flux source->target (Node {result.source_node} -> Node {result.target_node}): "
                 f"{flux.flux_i_to_j:.6f}")
    lines.append(f"  Flux target->source (Node {result.target_node} -> Node {result.source_node}): "
                 f"{flux.flux_j_to_i:.6f}")
    lines.append(f"  Total flux:            {flux.total_flux:.6f}")
    lines.append(f"  Directionality ratio:  {flux.directionality_ratio:.4f} "
                 f"(0.5=balanced, 1.0=one-way)")
    lines.append(f"  RESULT: {'PASS - bidirectional' if result.passed_bidirectional else 'FAIL - unidirectional (sensor, not strand)'}")
    lines.append("")

    # --- Criterion 2: Coherence improvement ---
    lines.append("CRITERION 2: Coherence Improvement at Target Node")
    lines.append("-" * 40)

    # Overall means
    lines.append(f"  Mean incoherence (baseline, no strand):  {result.mean_baseline_incoherence:.4f}")
    lines.append(f"  Mean incoherence (with strand):          {result.mean_target_incoherence:.4f}")
    lines.append(f"  Improvement (positive = better):         {result.incoherence_improvement:.4f}")
    lines.append(f"  RESULT: {'PASS - coherence improved' if result.passed_coherence else 'FAIL - coherence did not improve'}")
    lines.append("")

    # Breakdown by phase: pre-surge, during surge, post-surge
    surge_start_step = unmapped_cfg.surge_onset_interval * STEPS_PER_INTERVAL
    surge_end_step = (unmapped_cfg.surge_onset_interval + unmapped_cfg.surge_duration_intervals) * STEPS_PER_INTERVAL

    phases = [
        ("Pre-surge", 0, surge_start_step),
        ("During surge", surge_start_step, surge_end_step),
        ("Post-surge", surge_end_step, NUM_INTERVALS * STEPS_PER_INTERVAL),
    ]

    lines.append("  Per-phase breakdown:")
    for phase_name, start, end in phases:
        n = min(end, len(baseline_incoherence)) - start
        if n <= 0:
            continue
        bl_slice = baseline_incoherence[start:end]
        pr_slice = probation_incoherence[start:end]
        bl_mean = float(np.mean(bl_slice))
        pr_mean = float(np.mean(pr_slice))
        improvement = bl_mean - pr_mean
        lines.append(f"    {phase_name:15s}: baseline={bl_mean:.4f}, "
                     f"with_strand={pr_mean:.4f}, improvement={improvement:+.4f}")
    lines.append("")

    # --- Criterion 3: Energy convergence (Lyapunov) ---
    lines.append("CRITERION 3: Energy Convergence (Lyapunov Stability)")
    lines.append("-" * 40)
    if energy_history:
        peak_energy = max(energy_history)
        final_energy = energy_history[-1]
        lines.append(f"  Peak energy:   {peak_energy:.4e}")
        lines.append(f"  Final energy:  {final_energy:.4e}")
        lines.append(f"  Dissipated:    {peak_energy - final_energy:.4e}")
        lines.append(f"  RESULT: {'PASS - energy converged' if result.energy_converged else 'FAIL - energy did not converge'}")
    lines.append("")

    # --- Weight ramp log ---
    lines.append("STRAND WEIGHT RAMP")
    lines.append("-" * 40)
    prev_w = None
    for step_idx, w in enumerate(weight_log):
        if w != prev_w:
            interval = step_idx // STEPS_PER_INTERVAL
            lines.append(f"  Step {step_idx:4d} (interval {interval:2d}): weight = {w}")
            prev_w = w
    lines.append("")

    # --- Overall verdict ---
    lines.append("=" * 70)
    all_passed = (
        result.passed_bidirectional
        and result.passed_coherence
        and result.energy_converged
    )
    lines.append(f"OVERALL: {'PASS - strand earned its place' if all_passed else 'FAIL - strand did not pass probation'}")
    lines.append("=" * 70)

    return "\n".join(lines)


def build_logbook_entry(
    baseline_incoherence: list[float],
    probation_incoherence: list[float],
    tracker: ProbationTracker,
    energy_history: list[float],
    weight_log: list[float],
    unmapped_cfg: UnmappedShockConfig,
    timestamp: str,
) -> str:
    """Build the logbook markdown entry for this validation run."""
    result = tracker.result(baseline_incoherence)
    flux = result.flux_accumulator

    surge_start_step = unmapped_cfg.surge_onset_interval * STEPS_PER_INTERVAL
    surge_end_step = (unmapped_cfg.surge_onset_interval + unmapped_cfg.surge_duration_intervals) * STEPS_PER_INTERVAL

    lines: list[str] = []
    lines.append(f"## Strand Integration Validation (Phase 2) -- {timestamp}")
    lines.append("")
    lines.append("**Scenario:** Stadium/Event Venue probationary strand attached to Node 2 (Approaching Traffic)  ")
    lines.append(f"**Run timestamp:** {timestamp}  ")
    lines.append(f"**Script:** run_strand_validation.py  ")
    lines.append("")

    # Parameters
    lines.append("### Parameters")
    lines.append("")
    lines.append("| Parameter | Value |")
    lines.append("|-----------|-------|")
    lines.append(f"| strand_strength (triangle) | {WEB_STRAND_STRENGTH} |")
    lines.append(f"| propagation_rate | {WEB_PROPAGATION_RATE} |")
    lines.append(f"| damping_coefficient | {WEB_DAMPING_COEFF} |")
    lines.append(f"| dt | {WEB_DT} |")
    lines.append(f"| seed | {SEED} |")
    lines.append(f"| num_intervals | {NUM_INTERVALS} |")
    lines.append(f"| steps_per_interval | {STEPS_PER_INTERVAL} |")
    lines.append(f"| initial_strand_weight | 0.01 |")
    lines.append(f"| weight_ramp | 0.01 -> 0.05 -> 0.10 -> 0.25 |")
    lines.append("")

    # Criterion 1
    lines.append("### Criterion 1: Bidirectional Propagation")
    lines.append("")
    lines.append("| Measure | Value |")
    lines.append("|---------|-------|")
    lines.append(f"| Flux source->target | {flux.flux_i_to_j:.6f} |")
    lines.append(f"| Flux target->source | {flux.flux_j_to_i:.6f} |")
    lines.append(f"| Total flux | {flux.total_flux:.6f} |")
    lines.append(f"| Directionality ratio | {flux.directionality_ratio:.4f} |")
    lines.append(f"| Result | {'PASS' if result.passed_bidirectional else 'FAIL'} |")
    lines.append("")

    # Criterion 2
    lines.append("### Criterion 2: Coherence Improvement")
    lines.append("")
    lines.append("| Measure | Value |")
    lines.append("|---------|-------|")
    lines.append(f"| Mean incoherence (baseline) | {result.mean_baseline_incoherence:.4f} |")
    lines.append(f"| Mean incoherence (with strand) | {result.mean_target_incoherence:.4f} |")
    lines.append(f"| Improvement | {result.incoherence_improvement:+.4f} |")
    lines.append(f"| Result | {'PASS' if result.passed_coherence else 'FAIL'} |")
    lines.append("")

    # Per-phase
    phases = [
        ("Pre-surge", 0, surge_start_step),
        ("During surge", surge_start_step, surge_end_step),
        ("Post-surge", surge_end_step, NUM_INTERVALS * STEPS_PER_INTERVAL),
    ]
    lines.append("Per-phase breakdown:")
    lines.append("")
    lines.append("| Phase | Baseline | With Strand | Improvement |")
    lines.append("|-------|----------|-------------|-------------|")
    for phase_name, start, end in phases:
        n = min(end, len(baseline_incoherence)) - start
        if n <= 0:
            continue
        bl_mean = float(np.mean(baseline_incoherence[start:end]))
        pr_mean = float(np.mean(probation_incoherence[start:end]))
        improvement = bl_mean - pr_mean
        lines.append(f"| {phase_name} | {bl_mean:.4f} | {pr_mean:.4f} | {improvement:+.4f} |")
    lines.append("")

    # Criterion 3
    lines.append("### Criterion 3: Energy Convergence")
    lines.append("")
    if energy_history:
        peak_e = max(energy_history)
        final_e = energy_history[-1]
        lines.append("| Measure | Value |")
        lines.append("|---------|-------|")
        lines.append(f"| Peak energy | {peak_e:.4e} |")
        lines.append(f"| Final energy | {final_e:.4e} |")
        lines.append(f"| Dissipated | {peak_e - final_e:.4e} |")
        lines.append(f"| Result | {'PASS' if result.energy_converged else 'FAIL'} |")
    lines.append("")

    # Overall
    all_passed = (
        result.passed_bidirectional
        and result.passed_coherence
        and result.energy_converged
    )
    lines.append(f"### Overall Result: {'PASS' if all_passed else 'FAIL'}")
    lines.append("")
    if all_passed:
        lines.append("The probationary strand earned its place. The stadium demand signal,")
        lines.append("when fed through the fourth node and coupled to Node 2, reduced")
        lines.append("incoherence at the target node. Tension flowed bidirectionally along")
        lines.append("the strand, confirming it is a genuine coupling, not a sensor.")
        lines.append("The Lyapunov function (total energy) still converged, confirming")
        lines.append("the expanded web maintains stability.")
    else:
        lines.append("The probationary strand did not pass all criteria.")
        if not result.passed_bidirectional:
            lines.append(f"  - Bidirectional flow FAILED (directionality={flux.directionality_ratio:.4f})")
        if not result.passed_coherence:
            lines.append(f"  - Coherence improvement FAILED (delta={result.incoherence_improvement:+.4f})")
        if not result.energy_converged:
            lines.append("  - Energy convergence FAILED")
    lines.append("")
    lines.append("---")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 70)
    print("PHASE 2: STRAND INTEGRATION VALIDATION")
    print("=" * 70)
    print()
    print(f"Web params: strand={WEB_STRAND_STRENGTH}, alpha={WEB_PROPAGATION_RATE}, "
          f"beta={WEB_DAMPING_COEFF}, dt={WEB_DT}")
    print(f"Scenario:   seed={SEED}, start_hour={START_HOUR}, "
          f"num_intervals={NUM_INTERVALS}, steps_per_interval={STEPS_PER_INTERVAL}")
    print()

    # Step 1: Generate scenario
    print("Step 1: Generating scenario data...")
    tension_deltas, stadium_signal, unmapped_cfg = generate_scenario()
    print(f"  Tension deltas shape: {tension_deltas.shape}")
    print(f"  Stadium signal range: [{stadium_signal.min():.4f}, {stadium_signal.max():.4f}]")
    print()

    # Step 2: Baseline run
    print("Step 2: Running baseline (3-node web, no external strand)...")
    baseline_incoherence = run_baseline(tension_deltas)
    print(f"  Collected {len(baseline_incoherence)} incoherence observations")
    print(f"  Mean incoherence at Node 2: {np.mean(baseline_incoherence):.4f}")
    print()

    # Step 3: Probationary run
    print("Step 3: Running probationary (4-node web, external strand to Node 2)...")
    (
        probation_incoherence,
        tracker,
        energy_history,
        weight_log,
    ) = run_probationary(tension_deltas, stadium_signal, unmapped_cfg)
    print(f"  Collected {len(probation_incoherence)} incoherence observations")
    print(f"  Mean incoherence at Node 2: {np.mean(probation_incoherence):.4f}")
    print()

    # Step 4: Compare and report
    print("Step 4: Comparing results...")
    print()

    report = compare_and_report(
        baseline_incoherence,
        probation_incoherence,
        tracker,
        energy_history,
        weight_log,
        unmapped_cfg,
    )
    print(report)
    print()

    # Step 5: Write logbook entry
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = build_logbook_entry(
        baseline_incoherence,
        probation_incoherence,
        tracker,
        energy_history,
        weight_log,
        unmapped_cfg,
        timestamp,
    )

    with open(LOGBOOK_PATH, "a", encoding="utf-8") as f:
        f.write("\n" + entry + "\n")

    print(f"Logbook entry appended to: {LOGBOOK_PATH}")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
