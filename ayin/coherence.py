"""
Coherence monitor — diagnostic instrumentation embedded in the propagation loop.

This module READS the web's state. It never WRITES to it. Every measurement here
is a passive observation of the tension field, the same way a strain gauge on a
bridge reads stress without altering the structure.

Four measurement responsibilities:

1. RECOVERY TIME TRACKING (acute mode)
   After a perturbation injects energy, measure how many steps the web takes
   to relax back within ε of a new steady-state energy level. A perturbation
   is detected as an energy spike above a noise floor. Recovery = the energy
   envelope has settled. Trending recovery times reveal coherence decay:
   if each successive perturbation takes longer to absorb, the web's capacity
   to redistribute is degrading.

2. DAMPING RATIO MEASUREMENT
   The analytical prediction for each eigenmode is ζ = β / (2√(α·λ)).
   We measure the empirical damping ratio from the energy decay envelope
   using the log-decrement method on successive energy peaks. Divergence
   between analytical and empirical ζ indicates the linear model is breaking
   down (e.g., under sustained superimposed perturbations where nonlinear
   effects accumulate).

3. INCOHERENCE DETECTION
   The most critical measurement. In normal diffusion, a tension change at
   node i propagates to neighbors through strands — neighbors respond with
   correlated (delayed, attenuated) changes. Incoherence = a node's tension
   is changing but the expected diffusion signature at its neighbors is absent
   or contradictory.

   Approach: sliding-window Pearson correlation between each node's tension
   changes (ΔT_i) and the coupling-weighted average of its neighbors' changes.

   The incoherence score is continuous, not binary. It is a per-node measure
   of how much of the node's recent behavior is unexplained by the web's
   known topology.

4. CHRONIC INCOHERENCE TRACKING (chronic mode)
   The acute recovery tracker detects sharp energy spikes (accident, stadium).
   But gradual coherence degradation — where incoherence scores drift upward
   over many observations without ever spiking — evades the spike detector.

   Chronic mode tracks the TRAJECTORY of incoherence scores over time:
     - Slope: OLS linear regression on each node's incoherence score history
       over a sliding window. Persistently positive slope = the web's local
       correlation structure is decaying, even if no single observation is
       alarming.
     - Elevated mean: the current sliding window mean compared to a baseline
       mean from the first M observations. If the current mean has drifted
       above baseline by a configurable margin, the node's incoherence is
       chronically elevated.

   These are continuous statistical measurements of the tension field's
   temporal correlation structure. They are read-only diagnostics — they
   do not steer behavior or trigger actions.

Physical basis for the correlation measure:
   The Laplacian restoring force a_i = -α(D_ii T_i - Σ W_ij T_j) drives
   tension GRADIENTS toward zero. When T_i is above its neighbors, the
   force pushes T_i DOWN and neighbors UP. Consequently, ΔT_i and the
   weighted average ΔT_neighbors are ANTI-CORRELATED (r ≈ -1) during
   normal coherent redistribution. This anti-correlation is the fundamental
   signature of Laplacian diffusion.

   Incoherence manifests as a BREAKDOWN of this anti-correlation:
     - r ≈ 0: the node is changing but neighbors show no corresponding
       response, or vice versa. The web's topology doesn't explain the motion.
     - r > 0: node AND neighbors are being pushed in the SAME direction
       simultaneously. This cannot happen from internal diffusion alone —
       it requires independent external forces acting on multiple nodes.
       This is exactly the signature of an unmapped external cause (e.g.,
       a stadium event pushing both T1 and T2 from outside the web).

   We map correlation to incoherence score as (1 + r) / 2:
     r = -1 → score = 0.0 (perfect anti-correlation = coherent diffusion)
     r =  0 → score = 0.5 (uncorrelated = moderate incoherence)
     r = +1 → score = 1.0 (positive correlation = strong incoherence)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final
from collections import deque

import numpy as np
from numpy.typing import NDArray


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CoherenceConfig:
    """
    Configurable parameters for coherence monitoring.

    These control the MEASUREMENT apparatus, not the physics.
    Changing them changes what we observe, not how the web behaves.
    """

    # --- Recovery time tracking ---
    # Energy spike detection: a perturbation is detected when the energy
    # at the current step exceeds the recent baseline by this factor.
    # Not a hard threshold — it defines the sensitivity of the detector.
    energy_spike_factor: float = 2.0

    # Number of recent energy samples to average for the baseline.
    # Must be long enough to smooth out noise but short enough to
    # track the actual baseline as it shifts with total tension.
    energy_baseline_window: int = 20

    # Recovery tolerance ε: the web is considered settled when energy
    # drops below (1 + ε) * post-perturbation baseline. Small ε is strict.
    recovery_epsilon: float = 0.05

    # Maximum number of recovery times to store for trend analysis.
    recovery_history_length: int = 50

    # --- Damping ratio measurement ---
    # Minimum number of energy peaks needed to estimate damping ratio.
    # Log-decrement needs at least 2 successive peaks.
    min_peaks_for_damping: int = 2

    # Maximum number of energy samples to keep for peak detection.
    energy_history_length: int = 200

    # --- Incoherence detection ---
    # Sliding window size for correlation computation.
    # Must be long enough for statistical significance but short enough
    # to detect recent incoherence events (not wash them out in history).
    correlation_window: int = 30

    # Minimum samples in the window before producing a score.
    # Below this, the correlation estimate is too noisy to be meaningful.
    min_correlation_samples: int = 10

    # --- Chronic incoherence tracking ---
    # Rolling window of incoherence score observations for slope estimation.
    # Longer window = more stable slope estimate, but slower to detect onset.
    # At 5 steps/interval, 50 observations = 10 intervals of history.
    chronic_window: int = 50

    # Number of initial observations used to establish baseline mean.
    # The baseline captures the web's "healthy" incoherence profile before
    # any degradation accumulates. Should cover several intervals of
    # normal operation so noise averages out.
    chronic_baseline_observations: int = 25

    # Minimum observations before computing chronic diagnostics.
    # Below this, slope and mean estimates are statistically meaningless.
    chronic_min_observations: int = 10

    # Elevation margin: the current sliding window mean must exceed the
    # baseline mean by at least this amount to be flagged as elevated.
    # This is a continuous measurement threshold for the "elevated" flag,
    # not a behavioral trigger. Expressed in incoherence score units [0, 1].
    chronic_elevation_margin: float = 0.05


# ---------------------------------------------------------------------------
# Measurement snapshots
# ---------------------------------------------------------------------------

@dataclass
class RecoveryMeasurement:
    """A single recovery episode: perturbation detected at step S, settled at step E."""
    perturbation_step: int
    recovery_step: int
    peak_energy: float
    settled_energy: float

    @property
    def recovery_steps(self) -> int:
        return self.recovery_step - self.perturbation_step


@dataclass
class ChronicNodeScore:
    """
    Chronic incoherence measurement for a single node.

    These are time-series statistics on the node's incoherence score trajectory.
    All fields are continuous measurements — none steer behavior.

    Physical interpretation:
      - slope > 0: the local correlation structure at this node is decaying
        over time. The web's topology is becoming less able to explain the
        node's tension changes through mapped strands.
      - elevated mean: the node's recent incoherence is chronically above
        its early-observation baseline, indicating a sustained shift in the
        diffusion pattern — not just a transient spike.
    """
    # OLS slope of incoherence scores over the sliding window.
    # Units: incoherence-score-per-observation. Positive = worsening.
    # NaN if fewer than chronic_min_observations have been collected.
    slope: float

    # Mean incoherence score over the current sliding window.
    mean: float

    # Mean incoherence score over the baseline period (first M observations).
    # NaN if the baseline period hasn't completed yet.
    baseline_mean: float

    # Whether current mean exceeds baseline mean by more than the
    # configured elevation margin. False if baseline is not yet established.
    elevated: bool

    # Whether the slope is persistently positive (slope > 0 and we have
    # enough data for the estimate to be meaningful). This is a convenience
    # reading, equivalent to checking slope > 0 and not isnan(slope).
    trending: bool


@dataclass
class CoherenceSnapshot:
    """
    Complete coherence diagnostic at a single point in time.
    This is what gets broadcast to the visualization layer.
    """
    step: int

    # Per-node incoherence scores in [0, 1]. Higher = more unexplained tension.
    incoherence_scores: NDArray[np.float64]

    # Most recent empirical damping ratio (from energy decay envelope).
    # NaN if not enough data to estimate yet.
    empirical_damping_ratio: float

    # Analytical damping ratio for the dominant eigenmode (for comparison).
    analytical_damping_ratio: float

    # Latest recovery time in steps (NaN if no recovery episode completed yet).
    last_recovery_time: float

    # Linear trend slope of recovery times over the history window.
    # Positive slope = coherence is decaying (each recovery takes longer).
    # NaN if fewer than 2 recovery episodes recorded.
    recovery_trend_slope: float

    # Current total energy (for context).
    total_energy: float

    # Per-node chronic incoherence diagnostics. Keyed by node index.
    # Empty dict if chronic tracking hasn't accumulated enough observations yet.
    chronic_scores: dict[int, ChronicNodeScore] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Chronic incoherence tracker
# ---------------------------------------------------------------------------

class _ChronicTracker:
    """
    Tracks the trajectory of per-node incoherence scores over time.

    This is a statistical instrument, not a controller. It maintains a
    rolling history of incoherence scores for each node and computes:
      1. OLS slope over the sliding window (is incoherence trending upward?)
      2. Current window mean vs baseline mean (has incoherence shifted?)

    WHY this exists: the acute recovery tracker detects energy spikes —
    sharp perturbations that double the energy baseline. Gradual coherence
    decay (e.g., 1% capacity loss per interval) never produces such spikes.
    But the incoherence SCORES do drift upward, because the accumulating
    external forcing increasingly violates the Laplacian diffusion pattern.
    This tracker measures that drift.
    """

    def __init__(self, num_nodes: int, config: CoherenceConfig) -> None:
        self._num_nodes: Final[int] = num_nodes
        self._config: Final[CoherenceConfig] = config

        # Per-node rolling history of incoherence scores.
        # Each deque stores the last chronic_window scores for one node.
        self._score_history: list[deque[float]] = [
            deque(maxlen=config.chronic_window) for _ in range(num_nodes)
        ]

        # Baseline accumulator: we collect the first M observations to
        # establish a per-node baseline mean. Once M observations are
        # collected, the baseline is frozen.
        self._baseline_accum: list[list[float]] = [[] for _ in range(num_nodes)]
        self._baseline_means: list[float | None] = [None] * num_nodes
        self._baseline_frozen: bool = False

        # Total observation count (how many times record() has been called).
        self._observation_count: int = 0

    def record(self, incoherence_scores: NDArray[np.float64]) -> None:
        """
        Record one observation of incoherence scores (one per node).

        Called once per observe() step, using the scores already computed
        by the existing incoherence detector. No additional web state reads.
        """
        self._observation_count += 1

        for i in range(self._num_nodes):
            score = float(incoherence_scores[i])
            self._score_history[i].append(score)

            # Accumulate baseline until we have enough observations.
            if not self._baseline_frozen:
                self._baseline_accum[i].append(score)

        # Freeze baseline once we have enough observations.
        if (
            not self._baseline_frozen
            and self._observation_count >= self._config.chronic_baseline_observations
        ):
            for i in range(self._num_nodes):
                self._baseline_means[i] = float(np.mean(self._baseline_accum[i]))
            self._baseline_frozen = True
            # Free the accumulator memory — baseline is frozen.
            self._baseline_accum = [[] for _ in range(self._num_nodes)]

    def compute_chronic_scores(self) -> dict[int, ChronicNodeScore]:
        """
        Compute chronic diagnostics for all nodes from their score histories.

        Returns an empty dict if fewer than chronic_min_observations have
        been recorded — the statistics would be meaningless.

        The OLS slope measures: is the incoherence score at this node
        trending upward over the sliding window? In a healthy web under
        stationary forcing, the slope should fluctuate around zero. A
        persistently positive slope means the web's local correlation
        structure is degrading — the topology explains less and less of
        the node's tension changes over time.

        The elevated mean compares the current window's average incoherence
        to the early-observation baseline. A shift indicates chronic
        departure from the web's initial coherence profile.
        """
        min_obs = self._config.chronic_min_observations
        if self._observation_count < min_obs:
            return {}

        result: dict[int, ChronicNodeScore] = {}

        for i in range(self._num_nodes):
            history = self._score_history[i]
            n = len(history)

            if n < min_obs:
                continue

            scores_array = np.array(history, dtype=np.float64)

            # --- OLS slope: dy/dx where x = observation index ---
            # slope = cov(x, y) / var(x)
            x = np.arange(n, dtype=np.float64)
            x_mean = np.mean(x)
            y_mean = float(np.mean(scores_array))
            numerator = float(np.sum((x - x_mean) * (scores_array - y_mean)))
            denominator = float(np.sum((x - x_mean) ** 2))

            if denominator < 1e-15:
                slope = 0.0
            else:
                slope = numerator / denominator

            # --- Baseline comparison ---
            baseline_mean = (
                self._baseline_means[i]
                if self._baseline_means[i] is not None
                else float("nan")
            )

            current_mean = y_mean

            # Elevated: current mean exceeds baseline by the configured margin.
            if self._baseline_means[i] is not None:
                elevated = current_mean > baseline_mean + self._config.chronic_elevation_margin
            else:
                elevated = False

            # Trending: slope is meaningfully positive (not just noise).
            # We report slope > 0 as trending. The caller decides significance.
            trending = slope > 0.0

            result[i] = ChronicNodeScore(
                slope=slope,
                mean=current_mean,
                baseline_mean=baseline_mean,
                elevated=elevated,
                trending=trending,
            )

        return result


# ---------------------------------------------------------------------------
# The monitor
# ---------------------------------------------------------------------------

class CoherenceMonitor:
    """
    Passive diagnostic instrument embedded in the propagation loop.

    Usage:
        monitor = CoherenceMonitor(num_nodes, coupling_matrix, params)
        # Inside the propagation loop:
        monitor.observe(tension, velocity, energy, step)
        # Query diagnostics:
        snapshot = monitor.snapshot()

    This class maintains rolling buffers of observed state and computes
    diagnostics on demand. It never modifies the tension, velocity, or
    any web state.
    """

    def __init__(
        self,
        num_nodes: int,
        coupling_matrix: NDArray[np.float64],
        analytical_damping_ratio: float,
        config: CoherenceConfig | None = None,
    ) -> None:
        self._num_nodes: Final[int] = num_nodes
        self._coupling_matrix: NDArray[np.float64] = coupling_matrix.copy()
        self._analytical_damping_ratio: float = analytical_damping_ratio
        self._config: Final[CoherenceConfig] = config or CoherenceConfig()

        # --- Precompute neighbor weights for incoherence detection ---
        # For each node i, the expected diffusion response at neighbor j
        # is proportional to the coupling strength W_ij. We normalize per
        # node so the weighted neighbor average is a proper weighted mean.
        row_sums = np.sum(coupling_matrix, axis=1)
        # Avoid division by zero for isolated nodes (shouldn't happen in a
        # well-formed web, but be defensive in measurement code).
        row_sums_safe = np.where(row_sums > 0, row_sums, 1.0)
        self._neighbor_weights: NDArray[np.float64] = coupling_matrix / row_sums_safe[:, np.newaxis]

        # --- Rolling buffers ---
        window = self._config.correlation_window
        history = self._config.energy_history_length

        # Tension change history per node: each entry is ΔT at that step.
        # Shape of stored arrays: (correlation_window, num_nodes)
        self._tension_deltas: deque[NDArray[np.float64]] = deque(maxlen=window)

        # Total energy history for recovery tracking.
        self._energy_history: deque[float] = deque(maxlen=history)

        # Kinetic energy history for damping ratio measurement.
        # KE = 0.5 * ||V||² oscillates in the underdamped regime —
        # it peaks twice per oscillation cycle (at each velocity extremum).
        # The envelope of these peaks decays exponentially, and the
        # log-decrement between successive peaks gives the damping ratio.
        self._kinetic_energy_history: deque[float] = deque(maxlen=history)

        # Previous tension vector (to compute ΔT at each step).
        self._prev_tension: NDArray[np.float64] | None = None

        # --- Recovery tracking state machine ---
        # We track whether we are currently in a "recovering" state
        # (energy was spiked and hasn't settled yet).
        self._in_recovery: bool = False
        self._perturbation_step: int = 0
        self._perturbation_peak_energy: float = 0.0
        self._pre_perturbation_energy: float = 0.0

        # Completed recovery episodes.
        max_recoveries = self._config.recovery_history_length
        self._recovery_history: deque[RecoveryMeasurement] = deque(maxlen=max_recoveries)

        # Energy baseline buffer (for spike detection).
        baseline_window = self._config.energy_baseline_window
        self._energy_baseline_buffer: deque[float] = deque(maxlen=baseline_window)

        # Current step counter (set by observe()).
        self._current_step: int = 0
        self._current_energy: float = 0.0

        # --- Chronic incoherence tracker ---
        # Tracks incoherence score trajectories over time to detect
        # gradual coherence decay that the spike-based recovery tracker misses.
        self._chronic_tracker: _ChronicTracker = _ChronicTracker(
            num_nodes=num_nodes, config=self._config,
        )

    # --- Core observation entry point ---

    def observe(
        self,
        tension: NDArray[np.float64],
        velocity: NDArray[np.float64],
        energy: float,
        step: int,
    ) -> None:
        """
        Feed the current web state into the monitor.

        Called once per propagation step. Purely passive: reads the state
        vectors, updates rolling buffers, tracks recovery episodes.
        Does NOT modify tension, velocity, or any web state.

        Args:
            tension:  Current tension vector T(t), shape (num_nodes,).
            velocity: Current velocity vector V(t), shape (num_nodes,).
            energy:   Total mechanical energy at this step.
            step:     Integer step counter from the web.
        """
        self._current_step = step
        self._current_energy = energy

        # --- Tension delta computation ---
        # ΔT_i(t) = T_i(t) - T_i(t-1). This is the raw signal for
        # incoherence detection. First call has no previous state.
        if self._prev_tension is not None:
            delta: NDArray[np.float64] = tension - self._prev_tension
            self._tension_deltas.append(delta.copy())
        self._prev_tension = tension.copy()

        # --- Energy tracking ---
        self._energy_history.append(energy)
        kinetic_energy: float = 0.5 * float(np.dot(velocity, velocity))
        self._kinetic_energy_history.append(kinetic_energy)
        self._track_recovery(energy, step)

        # --- Chronic incoherence tracking ---
        # Compute incoherence scores at this step and feed them to the
        # chronic tracker. We cache the result so snapshot() doesn't
        # recompute. The chronic tracker needs scores at EVERY observation,
        # not just when snapshot() is called, to maintain an accurate
        # temporal record of the incoherence trajectory.
        self._cached_incoherence: NDArray[np.float64] = self._compute_incoherence_scores()
        self._chronic_tracker.record(self._cached_incoherence)

    # --- Recovery time tracking ---

    def _track_recovery(self, energy: float, step: int) -> None:
        """
        Detect perturbation onset (energy spike) and track relaxation.

        State machine with two states:
          IDLE:      watching for an energy spike above the baseline.
          RECOVERING: waiting for energy to settle within ε of a new baseline.

        The "new baseline" is the pre-perturbation energy level. We don't
        try to predict the new equilibrium energy — we wait for the energy
        to drop below (1 + ε) * pre_perturbation_energy, which indicates
        the injected kinetic energy has been dissipated.
        """
        cfg = self._config

        if not self._in_recovery:
            # --- IDLE: look for a spike ---
            self._energy_baseline_buffer.append(energy)

            if len(self._energy_baseline_buffer) >= cfg.energy_baseline_window:
                baseline = float(np.mean(self._energy_baseline_buffer))

                # Spike detection: current energy significantly above baseline.
                # The factor is a sensitivity dial, not a hard decision boundary.
                if baseline > 0 and energy > baseline * cfg.energy_spike_factor:
                    self._in_recovery = True
                    self._perturbation_step = step
                    self._perturbation_peak_energy = energy
                    self._pre_perturbation_energy = baseline
        else:
            # --- RECOVERING: track peak and watch for settlement ---
            # Update the peak energy if we see a higher value
            # (the perturbation might still be injecting energy).
            if energy > self._perturbation_peak_energy:
                self._perturbation_peak_energy = energy

            # Settlement condition: energy has dropped back within ε of
            # the pre-perturbation baseline. This means the kinetic energy
            # from the perturbation has been dissipated by damping.
            target = self._pre_perturbation_energy * (1.0 + cfg.recovery_epsilon)

            if energy <= target:
                # Recovery complete. Record the episode.
                measurement = RecoveryMeasurement(
                    perturbation_step=self._perturbation_step,
                    recovery_step=step,
                    peak_energy=self._perturbation_peak_energy,
                    settled_energy=energy,
                )
                self._recovery_history.append(measurement)
                self._in_recovery = False

                # Reset the baseline buffer so we start fresh for the
                # next perturbation detection.
                self._energy_baseline_buffer.clear()

    # --- Damping ratio measurement ---

    def _measure_empirical_damping(self) -> float:
        """
        Extract empirical damping ratio from the kinetic energy decay envelope.

        Method: log-decrement of successive kinetic energy peaks.

        In the underdamped regime, kinetic energy KE = 0.5*||V||² oscillates
        as the web rings. KE peaks occur at half-period intervals (velocity
        reaches maximum magnitude at both the positive and negative swings).

        The KE peak envelope decays as:
            KE_peak(t) ~ A₀² exp(-2ζωₙt)

        Between successive KE peaks separated by T_d/2 (half the damped period):
            δ = ln(KE_k / KE_{k+1}) = 2ζωₙ · T_d/2 = ζωₙT_d = 2πζ/√(1-ζ²)

        This is exactly the standard amplitude log-decrement formula because
        the factor-of-2 from squaring (KE ~ v²) cancels with the half-period
        spacing. Therefore:
            ζ = δ / √(4π² + δ²)

        Returns NaN if insufficient data for estimation.
        """
        if len(self._kinetic_energy_history) < self._config.min_peaks_for_damping + 2:
            return float("nan")

        # Find local maxima in the kinetic energy history.
        # KE oscillates, so peaks are well-defined in the underdamped regime.
        ke_values = list(self._kinetic_energy_history)
        peaks: list[float] = []
        for k in range(1, len(ke_values) - 1):
            if ke_values[k] > ke_values[k - 1] and ke_values[k] > ke_values[k + 1]:
                peaks.append(ke_values[k])

        if len(peaks) < self._config.min_peaks_for_damping:
            return float("nan")

        # Compute log-decrements between successive KE peaks.
        log_decrements: list[float] = []
        for i in range(len(peaks) - 1):
            if peaks[i] > 1e-15 and peaks[i + 1] > 1e-15:
                delta = np.log(peaks[i] / peaks[i + 1])
                if delta > 0:
                    log_decrements.append(delta)

        if not log_decrements:
            return float("nan")

        # Average log-decrement, convert to damping ratio.
        # ζ = δ / √(4π² + δ²)  (exact formula, not small-ζ approximation)
        mean_delta = float(np.mean(log_decrements))
        zeta = mean_delta / np.sqrt(4.0 * np.pi**2 + mean_delta**2)
        return float(zeta)

    # --- Incoherence detection ---

    def _compute_incoherence_scores(self) -> NDArray[np.float64]:
        """
        Compute per-node incoherence score from the sliding window of tension deltas.

        For each node i, we compute the Pearson correlation between:
          - ΔT_i(t): the node's own tension change series
          - ΔT_neighbors_i(t): the coupling-weighted average of its neighbors'
            tension change series

        Under normal Laplacian diffusion, the restoring force drives the
        perturbed node's tension DOWN while pushing neighbor tensions UP.
        This means ΔT_i and ΔT_neighbors are ANTI-CORRELATED (r ≈ -1)
        during coherent redistribution. This is a direct consequence of
        the Laplacian: a(i) = -α * (D_ii * T_i - Σ W_ij * T_j).

        Incoherence score = (1 + correlation) / 2, mapped to [0, 1]:
          - correlation = -1  → score = 0.0 (perfect anti-correlation = coherent diffusion)
          - correlation =  0  → score = 0.5 (uncorrelated — moderate incoherence)
          - correlation = +1  → score = 1.0 (positive correlation — both moving same way,
                                              driven by independent external forces)

        The known test case (unmapped stadium shock) produces positive correlation:
        T1 and T2 both receive external pushes that aren't mediated by the web,
        so they move together instead of in the anti-correlated diffusion pattern.
        This detector finds that pattern WITHOUT being told to look for it.

        Returns zeros if insufficient data in the window.
        """
        scores = np.zeros(self._num_nodes, dtype=np.float64)

        if len(self._tension_deltas) < self._config.min_correlation_samples:
            return scores

        # Stack the tension delta history into a (window_len, num_nodes) matrix.
        delta_matrix: NDArray[np.float64] = np.array(self._tension_deltas, dtype=np.float64)
        window_len = delta_matrix.shape[0]

        for i in range(self._num_nodes):
            # Node i's own tension change series.
            node_deltas: NDArray[np.float64] = delta_matrix[:, i]

            # Coupling-weighted average of neighbors' tension changes.
            # self._neighbor_weights[i, :] has the normalized weights.
            # For node i, W_ii = 0 (no self-loop), so this is purely neighbors.
            neighbor_avg: NDArray[np.float64] = delta_matrix @ self._neighbor_weights[i, :]

            # Pearson correlation between node_deltas and neighbor_avg.
            # Handle degenerate cases: if either series is constant (zero variance),
            # the correlation is undefined.
            node_std = np.std(node_deltas)
            neighbor_std = np.std(neighbor_avg)

            if node_std < 1e-15 and neighbor_std < 1e-15:
                # Both series are flat — the web is at rest, no incoherence signal.
                scores[i] = 0.0
            elif node_std < 1e-15 or neighbor_std < 1e-15:
                # One series is active, the other is dead — moderate incoherence.
                # The node is either changing without neighbor response, or
                # neighbors are changing without this node responding.
                scores[i] = 0.5
            else:
                # Standard Pearson correlation.
                node_centered = node_deltas - np.mean(node_deltas)
                neighbor_centered = neighbor_avg - np.mean(neighbor_avg)
                correlation = float(
                    np.dot(node_centered, neighbor_centered)
                    / (node_std * neighbor_std * window_len)
                )
                # Clamp to [-1, 1] for numerical safety.
                correlation = max(-1.0, min(1.0, correlation))
                # Map to incoherence score: (1 + r) / 2.
                # Anti-correlated (coherent diffusion) → low score.
                # Positively correlated (external forcing) → high score.
                scores[i] = (1.0 + correlation) / 2.0

        return scores

    # --- Recovery trend ---

    def _compute_recovery_trend(self) -> float:
        """
        Linear regression slope of recovery times over the history window.

        Positive slope means each successive perturbation takes more steps
        to recover — coherence is decaying. This trend is a leading indicator:
        it signals degradation before any single recovery time is alarming.

        Uses ordinary least squares on the recovery_steps sequence.
        Returns NaN if fewer than 2 recovery episodes are recorded.
        """
        if len(self._recovery_history) < 2:
            return float("nan")

        recovery_times = np.array(
            [m.recovery_steps for m in self._recovery_history],
            dtype=np.float64,
        )
        n = len(recovery_times)
        x = np.arange(n, dtype=np.float64)

        # OLS slope: cov(x, y) / var(x)
        x_mean = np.mean(x)
        y_mean = np.mean(recovery_times)
        numerator = float(np.sum((x - x_mean) * (recovery_times - y_mean)))
        denominator = float(np.sum((x - x_mean) ** 2))

        if denominator < 1e-15:
            return 0.0

        return numerator / denominator

    # --- Public diagnostic interface ---

    def snapshot(self) -> CoherenceSnapshot:
        """
        Produce a complete coherence diagnostic at the current moment.

        This is the primary output of the monitor. Call it after observe()
        to get the latest measurements. It is a pure read — no side effects.
        """
        # Use cached incoherence scores from the latest observe() call
        # to avoid recomputing. Falls back to fresh computation if
        # snapshot() is called before any observe() (e.g., at init).
        if hasattr(self, '_cached_incoherence'):
            incoherence = self._cached_incoherence
        else:
            incoherence = self._compute_incoherence_scores()

        empirical_zeta = self._measure_empirical_damping()
        trend = self._compute_recovery_trend()
        chronic = self._chronic_tracker.compute_chronic_scores()

        last_recovery = float("nan")
        if self._recovery_history:
            last_recovery = float(self._recovery_history[-1].recovery_steps)

        return CoherenceSnapshot(
            step=self._current_step,
            incoherence_scores=incoherence,
            empirical_damping_ratio=empirical_zeta,
            analytical_damping_ratio=self._analytical_damping_ratio,
            last_recovery_time=last_recovery,
            recovery_trend_slope=trend,
            total_energy=self._current_energy,
            chronic_scores=chronic,
        )

    @property
    def recovery_history(self) -> list[RecoveryMeasurement]:
        """Read-only access to completed recovery episodes."""
        return list(self._recovery_history)

    @property
    def is_recovering(self) -> bool:
        """Whether the web is currently in a recovery episode."""
        return self._in_recovery

    @property
    def incoherence_scores(self) -> NDArray[np.float64]:
        """Latest incoherence scores without building a full snapshot."""
        if hasattr(self, '_cached_incoherence'):
            return self._cached_incoherence.copy()
        return self._compute_incoherence_scores()
