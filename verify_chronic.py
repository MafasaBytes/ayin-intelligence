"""
Verification script: run the slow_decay scenario and confirm that chronic mode
detects the incoherence drift that acute mode misses.

This mirrors run_slow_decay.py's structure but focuses on chronic diagnostics.
"""
from __future__ import annotations

import sys
import os

import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from ayin.web import create_triangle_web
from ayin.simulator import (
    BaselineConfig,
    generate_baseline,
    SlowDecayConfig,
    generate_slow_decay,
    volume_to_tension_delta,
)

# ---------------------------------------------------------------------------
# Configuration — identical to run_slow_decay.py
# ---------------------------------------------------------------------------

WEB_STRAND_STRENGTH    = 1.0
WEB_PROPAGATION_RATE   = 1.0
WEB_DAMPING_COEFF      = 0.3
WEB_DT                 = 0.05

SEED                   = 271
START_HOUR             = 6.0
NUM_INTERVALS          = 36
STEPS_PER_INTERVAL     = 5

DECAY_ONSET_INTERVAL   = 6
DECAY_RATE_PER_INTERVAL= 0.01
MAX_REDUCTION          = 0.35

NODE_NAMES = ["N0 (Throughput)", "N1 (Signal)", "N2 (Approach)"]


def main() -> None:
    # --- Generate scenario ---
    rng_perturbed = np.random.default_rng(SEED)
    cfg = BaselineConfig(start_hour=START_HOUR, num_intervals=NUM_INTERVALS)
    baseline_volumes = generate_baseline(cfg, rng_perturbed)

    decay_cfg = SlowDecayConfig(
        onset_interval=DECAY_ONSET_INTERVAL,
        decay_rate_per_interval=DECAY_RATE_PER_INTERVAL,
        max_reduction=MAX_REDUCTION,
    )
    perturbed_volumes = generate_slow_decay(baseline_volumes, decay_cfg, rng_perturbed)

    rng_clean = np.random.default_rng(SEED)
    clean_baseline = generate_baseline(
        BaselineConfig(start_hour=START_HOUR, num_intervals=NUM_INTERVALS), rng_clean
    )
    tension_deltas = volume_to_tension_delta(perturbed_volumes, clean_baseline)

    # --- Create web ---
    web = create_triangle_web(
        strand_strength=WEB_STRAND_STRENGTH,
        propagation_rate=WEB_PROPAGATION_RATE,
        damping_coefficient=WEB_DAMPING_COEFF,
        dt=WEB_DT,
    )

    # --- Run with diagnostics ---
    print("=" * 80)
    print("CHRONIC MODE VERIFICATION — Slow Decay Scenario")
    print("=" * 80)
    print(f"Web: alpha={WEB_PROPAGATION_RATE}, beta={WEB_DAMPING_COEFF}, dt={WEB_DT}")
    print(f"Scenario: seed={SEED}, {NUM_INTERVALS} intervals, decay onset at interval {DECAY_ONSET_INTERVAL}")
    print(f"Decay: {DECAY_RATE_PER_INTERVAL*100:.0f}% per interval, max {MAX_REDUCTION*100:.0f}%")
    print()

    total_step = 0
    recovery_episodes_detected = 0

    # Print header
    print(f"{'Int':>3} {'Step':>4} | {'N0 incoh':>8} {'N1 incoh':>8} {'N2 incoh':>8} | "
          f"{'N0 slope':>9} {'N1 slope':>9} {'N2 slope':>9} | "
          f"{'N0 mean':>7} {'N1 mean':>7} {'N2 mean':>7} | "
          f"{'N0 elev':>7} {'N1 elev':>7} {'N2 elev':>7} | "
          f"{'Recovery':>8}")
    print("-" * 155)

    for interval_idx in range(NUM_INTERVALS):
        delta = tension_deltas[interval_idx]
        web.perturb_vector(delta)

        for sub_step in range(STEPS_PER_INTERVAL):
            web.step()
            total_step += 1

        # Snapshot at end of each interval
        snap = web.coherence()
        scores = snap.incoherence_scores
        chronic = snap.chronic_scores

        # Recovery status
        recovery_episodes_detected = len(web.monitor.recovery_history)
        in_recovery = web.monitor.is_recovering

        # Format chronic data
        if chronic:
            slopes = [chronic[i].slope for i in range(3)]
            means = [chronic[i].mean for i in range(3)]
            elevs = [chronic[i].elevated for i in range(3)]
        else:
            slopes = [float("nan")] * 3
            means = [float("nan")] * 3
            elevs = [False] * 3

        recovery_str = f"{recovery_episodes_detected} ep" if recovery_episodes_detected else "none"
        if in_recovery:
            recovery_str += " [R]"

        print(
            f"{interval_idx:3d} {total_step:4d} | "
            f"{scores[0]:8.4f} {scores[1]:8.4f} {scores[2]:8.4f} | "
            f"{slopes[0]:9.6f} {slopes[1]:9.6f} {slopes[2]:9.6f} | "
            f"{means[0]:7.4f} {means[1]:7.4f} {means[2]:7.4f} | "
            f"{'YES' if elevs[0] else 'no':>7} {'YES' if elevs[1] else 'no':>7} {'YES' if elevs[2] else 'no':>7} | "
            f"{recovery_str:>8}"
        )

    # --- Summary ---
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()

    # Acute mode results
    episodes = web.monitor.recovery_history
    print(f"ACUTE MODE (spike-based recovery tracking):")
    print(f"  Recovery episodes detected: {len(episodes)}")
    if episodes:
        for i, ep in enumerate(episodes):
            print(f"    Episode {i+1}: perturbation at step {ep.perturbation_step}, "
                  f"recovered at step {ep.recovery_step} ({ep.recovery_steps} steps)")
    else:
        print("  ** No recovery episodes — gradual decay never triggered the 2x energy spike threshold **")
    print()

    # Chronic mode results
    final_snap = web.coherence()
    chronic = final_snap.chronic_scores
    print(f"CHRONIC MODE (incoherence trajectory tracking):")
    if chronic:
        for i in range(3):
            cs = chronic[i]
            print(f"  {NODE_NAMES[i]}:")
            print(f"    slope     = {cs.slope:+.6f} {'(TRENDING UP)' if cs.trending else '(stable/declining)'}")
            print(f"    mean      = {cs.mean:.4f}")
            print(f"    baseline  = {cs.baseline_mean:.4f}")
            print(f"    elevated  = {'YES — mean exceeds baseline' if cs.elevated else 'no'}")
            print(f"    trending  = {'YES — positive slope' if cs.trending else 'no'}")
            print()
    else:
        print("  Insufficient observations for chronic diagnostics.")
    print()

    # Detection comparison
    any_acute = len(episodes) > 0
    any_chronic_elevated = chronic and any(chronic[i].elevated for i in range(3))
    any_chronic_trending = chronic and any(chronic[i].trending for i in range(3))

    print("DETECTION COMPARISON:")
    print(f"  Acute mode detected degradation:  {'YES' if any_acute else 'NO'}")
    print(f"  Chronic mode — elevated nodes:    {'YES' if any_chronic_elevated else 'NO'}")
    print(f"  Chronic mode — trending nodes:    {'YES' if any_chronic_trending else 'NO'}")
    print()

    if not any_acute and (any_chronic_elevated or any_chronic_trending):
        print("  >>> CHRONIC MODE DETECTED THE DRIFT THAT ACUTE MODE MISSED <<<")
    elif any_acute:
        print("  Both modes detected the issue.")
    else:
        print("  Neither mode detected the issue — check parameters.")


if __name__ == "__main__":
    main()
