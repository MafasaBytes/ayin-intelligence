"""
Full end-to-end pipeline validation: simulator → web engine → coherence monitor → strand agent.

This script runs the stadium (unmapped shock) scenario and feeds EVERY coherence snapshot
to the strand agent for autonomous investigation. Logs all Claude API calls, responses,
and parsed proposals to understand whether the scout correctly identifies the unmapped force.

Expected outcome: Agent should propose something like "stadium event" or "upstream demand surge"
connected to Node 2 (Approaching Traffic), with positive tension direction.
"""

from __future__ import annotations

import sys
import os
import logging
from datetime import datetime, timezone

import numpy as np

# Ensure the project root is on sys.path
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from ayin.web import create_triangle_web
from ayin.coherence import CoherenceSnapshot
from ayin.strand_agent import StrandAgent, StrandAgentConfig
from ayin.simulator import (
    generate_baseline,
    generate_unmapped_shock,
    volume_to_tension_delta,
    BaselineConfig,
    UnmappedShockConfig,
)
from ayin.nodes import NODE_LABELS

# Configure logging for auditability
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

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

LOGBOOK_PATH = os.path.join(ROOT, "ayin", "docs", "logbook.md")


# ---------------------------------------------------------------------------
# Step 1: Generate scenario data
# ---------------------------------------------------------------------------

def generate_scenario() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns:
        perturbed_volumes: (36, 3) — stadium scenario volumes
        clean_baseline:    (36, 3) — same seed baseline without perturbation
        tension_deltas:    (36, 3) — per-interval tension perturbation vectors
    """
    print("Generating scenario data...")
    rng_perturbed = np.random.default_rng(SEED)
    cfg = BaselineConfig(start_hour=START_HOUR, num_intervals=NUM_INTERVALS)
    baseline_volumes = generate_baseline(cfg, rng_perturbed)

    unmapped_cfg = UnmappedShockConfig()
    perturbed_volumes = generate_unmapped_shock(baseline_volumes, unmapped_cfg, rng_perturbed)

    # Clean baseline for delta computation
    rng_clean = np.random.default_rng(SEED)
    clean_baseline = generate_baseline(cfg, rng_clean)

    # Tension deltas
    tension_deltas = volume_to_tension_delta(perturbed_volumes, clean_baseline)

    print(f"  Volumes shape: {perturbed_volumes.shape}")
    print(f"  Tension deltas min/max: [{tension_deltas.min():.4f}, {tension_deltas.max():.4f}]")

    # Preview the surge onset interval
    surge_interval = 10
    print(f"\n  Surge onset interval ({surge_interval}):")
    print(f"    Perturbed volumes: {perturbed_volumes[surge_interval]}")
    print(f"    Clean baseline:    {clean_baseline[surge_interval]}")
    print(f"    Tension deltas:    {tension_deltas[surge_interval]}")
    print()

    return perturbed_volumes, clean_baseline, tension_deltas


# ---------------------------------------------------------------------------
# Step 2: Run the full pipeline with strand agent
# ---------------------------------------------------------------------------

def run_full_pipeline(tension_deltas: np.ndarray) -> dict:
    """
    Drive TensionWeb through all 36 intervals while feeding coherence snapshots
    to the StrandAgent for continuous evaluation.

    Returns results dict with all collected data and proposals.
    """
    print("Initializing web and strand agent...")
    web = create_triangle_web(
        strand_strength=WEB_STRAND_STRENGTH,
        propagation_rate=WEB_PROPAGATION_RATE,
        damping_coefficient=WEB_DAMPING_COEFF,
        dt=WEB_DT,
    )

    # Initialize the strand agent with default config
    agent_config = StrandAgentConfig()
    agent = StrandAgent(agent_config)

    print(f"Web: 3-node triangle, ζ_analytical={web.coherence().analytical_damping_ratio:.4f}")
    print(f"Agent: min_nodes={agent_config.min_nodes_for_acute_signature}, "
          f"threshold={agent_config.incoherence_threshold}\n")

    # Data collection
    step_data = []
    all_proposals = []
    snapshot_count = 0
    triggered_count = 0

    total_step = 0
    start_energy = None
    peak_energy = 0.0
    peak_energy_step = 0

    # Per-node peak tension tracking
    peak_tension_per_node = [0.0, 0.0, 0.0]
    peak_tension_step_per_node = [0, 0, 0]

    print("Running 36 intervals × 5 steps per interval = 180 steps in main phase...\n")

    # --- Interval phase ---
    for interval_idx in range(NUM_INTERVALS):
        delta = tension_deltas[interval_idx]

        # Inject perturbation
        web.perturb_vector(delta)

        if interval_idx == 10:
            print(f">>> Surge onset at interval {interval_idx}:")
            print(f"    Injected delta: {delta}")
            print()

        # Run propagation steps
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

            # Per-node peak tension
            for n in range(3):
                if abs(T[n]) > abs(peak_tension_per_node[n]):
                    peak_tension_per_node[n] = T[n]
                    peak_tension_step_per_node[n] = total_step

            # Get coherence snapshot
            snapshot = web.coherence()
            snapshot_count += 1

            # Feed to agent
            proposals = agent.evaluate(snapshot)

            if proposals:
                triggered_count += 1
                print(f">>> AGENT TRIGGERED at step {total_step} (interval {interval_idx}, substep {sub_step+1})")
                print(f"    Incoherence scores: {snapshot.incoherence_scores}")
                print(f"    Proposals generated: {len(proposals)}\n")

                for prop in proposals:
                    all_proposals.append(prop)
                    print(f"    Proposal ID: {prop.proposal_id}")
                    print(f"      Source: {prop.hypothesized_source}")
                    print(f"      Target: Node {prop.target_node} ({NODE_LABELS.get(prop.target_node, '?')})")
                    print(f"      Direction: {prop.expected_tension_direction:+d}")
                    print(f"      Confidence: {prop.confidence:.2f}")
                    print(f"      Rationale: {prop.rationale}")
                    print(f"      Claude response:\n{prop.claude_response}\n")

            step_data.append({
                "step": total_step,
                "interval": interval_idx,
                "tension": T.copy(),
                "velocity": V.copy(),
                "energy": E,
                "incoherence": snapshot.incoherence_scores.copy(),
                "proposals_triggered": len(proposals),
            })

    # Final state
    final_snap = web.coherence()
    final_T = web.tension
    final_E = web.total_energy()

    recovery_episodes = web.monitor.recovery_history

    print(f"\n{'='*70}")
    print(f"PIPELINE SUMMARY")
    print(f"{'='*70}\n")

    print(f"Main run complete:")
    print(f"  Total steps: {total_step}")
    print(f"  Start energy: {start_energy:.4e}")
    print(f"  Peak energy: {peak_energy:.4e} at step {peak_energy_step}")
    print(f"  Final energy: {final_E:.4e}")
    print(f"  Energy dissipated (peak to final): {peak_energy - final_E:.4e}\n")

    print(f"Coherence monitoring:")
    print(f"  Snapshots evaluated: {snapshot_count}")
    print(f"  Agent triggers: {triggered_count}")
    print(f"  Total proposals: {len(all_proposals)}\n")

    print(f"Recovery episodes: {len(recovery_episodes)}")
    if recovery_episodes:
        recovery_times = [ep.recovery_steps for ep in recovery_episodes]
        print(f"  Recovery times (steps): {recovery_times}\n")

    print(f"Peak incoherence scores per node (across all steps):")
    for n in range(3):
        scores = [d["incoherence"][n] for d in step_data]
        max_score = max(scores)
        max_step = next(d["step"] for d in step_data if d["incoherence"][n] == max_score)
        print(f"  Node {n} ({NODE_LABELS.get(n, '?')}): {max_score:.4f} at step {max_step}")

    return {
        "step_data": step_data,
        "all_proposals": all_proposals,
        "snapshot_count": snapshot_count,
        "triggered_count": triggered_count,
        "agent_stats": agent.statistics(),
        "start_energy": start_energy if start_energy is not None else 0.0,
        "peak_energy": peak_energy,
        "peak_energy_step": peak_energy_step,
        "final_energy": final_E,
        "final_tension": final_T.copy(),
        "total_steps": total_step,
        "recovery_episodes": recovery_episodes,
        "peak_tension_per_node": peak_tension_per_node,
        "peak_tension_step_per_node": peak_tension_step_per_node,
    }


# ---------------------------------------------------------------------------
# Step 3: Append summary to logbook
# ---------------------------------------------------------------------------

def append_logbook_summary(results: dict) -> None:
    """Append a summary of this full pipeline run to the logbook."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    lines.append(f"\n## Full Pipeline Validation (Stadium Shock) — {timestamp}")
    lines.append("")
    lines.append("**Test:** End-to-end validation of simulator → web → coherence → strand agent")
    lines.append("")

    lines.append("### Pipeline Statistics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total steps | {results['total_steps']} |")
    lines.append(f"| Snapshots evaluated | {results['snapshot_count']} |")
    lines.append(f"| Agent triggers | {results['triggered_count']} |")
    lines.append(f"| Proposals generated | {len(results['all_proposals'])} |")
    lines.append(f"| Peak energy | {results['peak_energy']:.4e} at step {results['peak_energy_step']} |")
    lines.append(f"| Final energy | {results['final_energy']:.4e} |")
    lines.append("")

    if results['all_proposals']:
        lines.append("### Proposals Generated by Agent")
        lines.append("")
        for i, prop in enumerate(results['all_proposals'], 1):
            lines.append(f"#### Proposal {i}: {prop.proposal_id}")
            lines.append("")
            lines.append(f"- **Source:** {prop.hypothesized_source}")
            lines.append(f"- **Target Node:** {prop.target_node} ({NODE_LABELS.get(prop.target_node, '?')})")
            lines.append(f"- **Direction:** {prop.expected_tension_direction:+d}")
            lines.append(f"- **Confidence:** {prop.confidence:.3f}")
            lines.append(f"- **Rationale:** {prop.rationale}")
            lines.append(f"- **Status:** {prop.status.value}")
            lines.append(f"- **Affected nodes:** {prop.affected_nodes}")
            lines.append("")
    else:
        lines.append("### Proposals Generated by Agent")
        lines.append("")
        lines.append("**None.** Agent did not detect acute incoherence signature.")
        lines.append("")

    lines.append("### Agent Statistics")
    lines.append("")
    stats = results['agent_stats']
    lines.append(f"- **Total proposals:** {stats['total_proposals']}")
    lines.append(f"- **Average confidence:** {stats['avg_confidence']:.3f}")
    lines.append(f"- **By status:**")
    for status, count in stats['by_status'].items():
        lines.append(f"  - {status}: {count}")
    lines.append("")

    lines.append("### Test Conclusion")
    lines.append("")
    if results['all_proposals']:
        # Analyze proposals
        has_stadium_like = any(
            "stadium" in p.hypothesized_source.lower() or
            "event" in p.hypothesized_source.lower() or
            "surge" in p.hypothesized_source.lower()
            for p in results['all_proposals']
        )
        has_node2 = any(p.target_node == 2 for p in results['all_proposals'])
        has_positive = any(p.expected_tension_direction > 0 for p in results['all_proposals'])

        result_text = "✓ PASS" if (has_stadium_like and has_node2) else "~ PARTIAL"
        lines.append(f"**Result: {result_text}**")
        lines.append("")
        lines.append("Evidence:")
        if has_stadium_like:
            lines.append("  ✓ Agent hypothesized external event/surge (not internal diffusion)")
        else:
            lines.append("  ✗ Agent did not recognize event/surge pattern")
        if has_node2:
            lines.append("  ✓ Agent connected proposal to Node 2 (Approaching Traffic) — correct")
        else:
            lines.append("  ✗ Agent did not identify Node 2 as affected")
        if has_positive:
            lines.append("  ✓ Agent predicted positive tension direction (demand surge) — correct")
        else:
            lines.append("  ✗ Agent did not identify positive direction")
    else:
        lines.append("**Result: FAIL**")
        lines.append("")
        lines.append("Agent did not trigger investigation despite unmapped shock scenario.")

    lines.append("")

    # Write to logbook
    content = "\n".join(lines)
    with open(LOGBOOK_PATH, "a", encoding="utf-8") as f:
        f.write(content)

    print(f"\nLogbook appended to: {LOGBOOK_PATH}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 70)
    print("FULL PIPELINE VALIDATION: STADIUM (UNMAPPED SHOCK) SCENARIO")
    print("=" * 70)
    print()

    print(f"Web parameters: strand={WEB_STRAND_STRENGTH}, alpha={WEB_PROPAGATION_RATE}, "
          f"beta={WEB_DAMPING_COEFF}, dt={WEB_DT}")
    print(f"Scenario: seed={SEED}, start_hour={START_HOUR}, "
          f"num_intervals={NUM_INTERVALS}, steps_per_interval={STEPS_PER_INTERVAL}")
    print()

    try:
        # Step 1: Generate scenario
        perturbed_volumes, clean_baseline, tension_deltas = generate_scenario()

        # Step 2: Run full pipeline
        results = run_full_pipeline(tension_deltas)

        # Step 3: Append summary to logbook
        append_logbook_summary(results)

        print("\n" + "=" * 70)
        print("SUCCESS: Full pipeline executed end-to-end")
        print("=" * 70)

    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        print(f"\nERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
