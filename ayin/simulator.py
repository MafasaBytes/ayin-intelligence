"""
Synthetic traffic data generator and perturbation injector.

Architecture: three-node triangle traffic intersection.
  Node 0 — Intersection Throughput (vehicles/cycle, queue depth, clearance rate)
  Node 1 — Signal Timing (phase allocation, green time distribution)
  Node 2 — Approaching Traffic (vehicle density on each approach, upstream measurement)

Design philosophy:
  Traffic volumes are the observed physical quantities. The web does not ingest
  raw volumes — it ingests DEVIATIONS from baseline expressed as tension deltas.
  A volume 20% above baseline is a perturbation of +0.20 (fractional deviation)
  times a sensitivity scaling factor. The web then propagates that perturbation
  across strands as a damped wave.

  This means the simulator has two distinct jobs:
    1. Generate plausible traffic volumes (the domain reality).
    2. Translate those volumes into tension perturbations (the web interface).

  These two jobs are completely separated. Generation functions return numpy
  arrays. Push functions call TensionWeb.perturb_vector(). Never mix them.

Inter-node causality in the traffic domain:
  Approaching Traffic (node 2) is upstream: vehicles arrive from outside
  the modeled intersection. What happens there determines what arrives at
  Intersection Throughput (node 0), with a lag equal to the travel time
  from the upstream detector to the stop bar (~1-3 five-minute intervals).
  Signal Timing (node 1) responds to queue pressure from both directions —
  it is downstream of Throughput feedback and upstream of green time grants.
  The correct causal chain for this intersection: 2 -> 0 -> 1.

Volume-to-tension mapping:
  Fractional deviation from baseline: δ = (volume - baseline) / baseline.
  This normalizes across nodes with different absolute volume ranges.
  Tension perturbation magnitude: Δt = δ * sensitivity.
  Sensitivity is tuned so a 50% volume shock produces a tension delta of ~0.5,
  which in the default underdamped web (ζ≈0.144) creates oscillations that
  persist for several propagation cycles — detectable but not explosive.

Noise calibration target: CV = 5-15% for 5-minute aggregations.
  Real traffic counters on urban arterials show CV≈8-12% at 5-min resolution.
  We target CV≈0.10 (10%) as the center of the realistic range.
  Formula: σ = CV * baseline_volume. At 1000 veh/hr, σ ≈ 100 veh/hr.

References:
  - HCM 7th Edition, Chapter 16 (arterial flow, volume-capacity ratios)
  - Gazis (1974) traffic flow fundamentals — volume-to-density relationships
  - WSN diffusion reference: Olfati-Saber & Murray (2004)
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Final

import numpy as np
from numpy.typing import NDArray
from numpy.random import Generator

from ayin.nodes import INTERSECTION_THROUGHPUT, SIGNAL_TIMING, APPROACHING_TRAFFIC
from ayin.web import TensionWeb, create_triangle_web


# ---------------------------------------------------------------------------
# Domain constants
# ---------------------------------------------------------------------------

# Typical midday baseline volumes (veh/hr/lane) per node.
# Urban arterial with moderate signal control.
#   Throughput: measured at the stop bar — slightly below approach volume
#               because signal cycles have lost time (4-6 sec per phase).
#   Signal timing: dimensionless load index (green fraction * saturation flow).
#                  We represent it as an equivalent volume in the same scale
#                  so the CV and deviation math stays consistent. Value here
#                  is a proxy: 1200 ~ 0.80 g/C * 1500 sat_flow.
#   Approaching traffic: upstream detector volume — higher than throughput
#                        because not all vehicles clear in a single cycle.
BASELINE_MIDDAY: Final[NDArray[np.float64]] = np.array([
    1000.0,   # Node 0: Intersection Throughput (veh/hr)
    1200.0,   # Node 1: Signal Timing (proxy volume, see note above)
    1150.0,   # Node 2: Approaching Traffic (veh/hr)
], dtype=np.float64)

# Sensitivity: fractional deviation → tension perturbation magnitude.
# Tuned so a complete capacity drop (δ = -1.0) generates tension = -1.0.
# The web's underdamped response will amplify this briefly before dissipating.
# Per-node sensitivity differs because:
#   - Throughput (0) is the most directly observable and most sensitive signal.
#   - Signal Timing (1) changes slowly (controller cycle is 60-120 sec); dampen it.
#   - Approaching Traffic (2) has high variance; lower sensitivity prevents
#     noise from overwhelming the web with false perturbations.
NODE_SENSITIVITY: Final[NDArray[np.float64]] = np.array([
    1.0,   # Node 0: full sensitivity
    0.6,   # Node 1: signal controllers are sluggish — attenuate noise coupling
    0.8,   # Node 2: upstream detectors have more measurement noise
], dtype=np.float64)

# Noise coefficient of variation: σ = CV * baseline.
# Target: CV ≈ 0.10. This is the natural scatter in 5-min volume counts
# on a moderately busy urban arterial without unusual events.
NOISE_CV: Final[float] = 0.10

# Five-minute interval = standard traffic engineering aggregation window.
INTERVAL_SECONDS: Final[int] = 300


# ---------------------------------------------------------------------------
# Time-of-day baseline profile
# ---------------------------------------------------------------------------

def time_of_day_factor(hour: float) -> NDArray[np.float64]:
    """
    Return a per-node multiplicative factor [0, 1] representing the
    fraction of peak-hour volume occurring at the given hour of day.

    Shape is calibrated from field-measured diurnal profiles on urban arterials.
    Key properties enforced:
      - Morning peak: 7-9 AM (sharp ramp-up, rounded top, asymmetric: rises faster
        than it falls — commuters arrive in a tighter cluster than they disperse).
      - Evening peak: 4-7 PM (broader, higher, asymmetric: rises slowly
        through the afternoon and drops more steeply after 6 PM).
      - Overnight trough: 1-5 AM (~8-15% of peak — maintenance vehicles,
        shift workers, overnight delivery).
      - Midday shoulder: 11 AM-2 PM (~55-70% of peak).

    Per-node differences in the shape:
      Node 2 (Approaching Traffic) leads the other nodes by ~15 minutes
      because the upstream detector sees the demand before it reaches the
      intersection. We model this as a 0.25-hour phase advance.

    Returns a (3,) array of factors in [0.08, 1.0].

    Args:
        hour: Hour of day in [0, 24). Fractional hours supported (e.g., 7.5 = 7:30 AM).
    """
    # Modular arithmetic to handle hour=23.9 -> hour=0.1 wrapping
    h = hour % 24.0

    # Approaching traffic leads by 15 minutes — it's the upstream signal.
    # When 15 min of lead is applied near midnight, wrap correctly.
    h_approach = (h - 0.25) % 24.0

    def _profile(t: float) -> float:
        """
        Piecewise profile shaped from HCM diurnal volume curves.

        The profile is NOT a smooth sinusoid — real traffic has:
          - An abrupt morning ramp (people leave home in a narrower window
            than they return).
          - A sustained but variable PM peak (staggered departure times,
            school pickup, shopping trips that broaden the peak).
          - A flat overnight trough (roughly constant low demand, not zero).
        """
        if 1.0 <= t < 5.0:
            # Overnight trough — essentially constant at minimum.
            return 0.10

        elif 5.0 <= t < 7.0:
            # Pre-morning ramp: parking lot emptiers, early shift workers.
            # Rises from 10% to 40% in 2 hours — gentle slope.
            frac = (t - 5.0) / 2.0
            return 0.10 + 0.30 * frac

        elif 7.0 <= t < 8.0:
            # Morning peak ramp-up: steepest segment of the day.
            # 40% -> 100% in one hour. Asymmetric: commuters cluster tightly.
            frac = (t - 7.0) / 1.0
            # Convex upward: slow start then rapid climb as everyone leaves
            # between 7:15 and 7:50 AM.
            return 0.40 + 0.60 * (frac ** 0.7)

        elif 8.0 <= t < 9.0:
            # Peak plateau with slight decay — rush still high, spreading out.
            frac = (t - 8.0) / 1.0
            return 1.00 - 0.15 * frac

        elif 9.0 <= t < 11.0:
            # Post-morning falloff: commuters gone, errand traffic lower.
            frac = (t - 9.0) / 2.0
            return 0.85 - 0.20 * frac

        elif 11.0 <= t < 14.0:
            # Midday shoulder: lunch trips add a modest bump but it's flatter.
            frac = (t - 11.0) / 3.0
            # Gentle concave-up curve: dips slightly then recovers.
            return 0.65 + 0.08 * np.sin(np.pi * frac)

        elif 14.0 <= t < 16.0:
            # Afternoon build-up: school dismissal (2:30-3:30) and early
            # flexible-schedule workers drive a gradual rise.
            frac = (t - 14.0) / 2.0
            return 0.65 + 0.25 * (frac ** 1.3)

        elif 16.0 <= t < 18.0:
            # PM peak ramp: broader than AM because departure times are
            # more staggered (flex schedules, school pickups done earlier).
            frac = (t - 16.0) / 2.0
            return 0.90 + 0.10 * (frac ** 0.5)

        elif 18.0 <= t < 19.0:
            # PM peak top and onset of rapid drop.
            frac = (t - 18.0) / 1.0
            return 1.00 - 0.20 * frac

        elif 19.0 <= t < 22.0:
            # Evening decay: dinner out, entertainment venues close.
            frac = (t - 19.0) / 3.0
            return 0.80 - 0.50 * (frac ** 1.2)

        elif 22.0 <= t < 24.0 or 0.0 <= t < 1.0:
            # Late evening transition to overnight.
            t_norm = t if t >= 22.0 else t + 24.0
            frac = (t_norm - 22.0) / 3.0
            return max(0.10, 0.30 - 0.20 * frac)

        else:
            return 0.10

    # Throughput (0) and Signal Timing (1) share the same profile —
    # signal timing is driven by intersection demand.
    # Approaching Traffic (2) uses the phase-advanced profile.
    f_main = _profile(h)
    f_approach = _profile(h_approach)

    return np.array([f_main, f_main, f_approach], dtype=np.float64)


def baseline_volume(hour: float) -> NDArray[np.float64]:
    """
    Expected (noiseless) traffic volume at the given hour.

    Returns a (3,) array of volumes in veh/hr (or proxy units for Node 1).
    These are the means around which noise will be layered — not the actual
    readings. The gap between this and the noisy output is what makes
    the simulation realistic.

    Volume range verification (HCM arterial classes):
      Overnight low:   BASELINE_MIDDAY * 0.10 ≈ [100, 120, 115] veh/hr — plausible
      Morning peak:    BASELINE_MIDDAY * 1.00 ≈ [1000, 1200, 1150] veh/hr — plausible
      Applies to a 4-lane arterial (2 thru lanes each direction): ~500/lane
    """
    factors = time_of_day_factor(hour)
    return BASELINE_MIDDAY * factors


# ---------------------------------------------------------------------------
# Noise model
# ---------------------------------------------------------------------------

def apply_traffic_noise(
    volumes: NDArray[np.float64],
    rng: Generator,
    cv: float = NOISE_CV,
) -> NDArray[np.float64]:
    """
    Add realistic measurement and stochastic demand noise to traffic volumes.

    Traffic noise has two distinct sources:
      1. Stochastic demand: arrival headways are Poisson-distributed, so
         5-minute counts are Poisson-like. For large volumes the Poisson
         approximates to Gaussian with σ = sqrt(mean). However, demand
         is bursty (platoon effects), so measured CV is higher than pure
         Poisson would predict. We calibrate to CV≈0.10.
      2. Measurement error: loop detectors and radar have systematic
         and random errors (~2-5% RMS). Included in the total CV budget.

    We do NOT use pure Gaussian — that can produce negative volumes.
    Instead we use a log-normal model with matching μ and σ, which
    correctly prevents negative output and has slightly heavier right
    tails (consistent with platoon clustering effects).

    Log-normal parameters from CV:
      σ_ln = sqrt(ln(1 + CV²))
      μ_ln = ln(μ) - 0.5 * σ_ln²
    """
    sigma_ln = np.sqrt(np.log(1.0 + cv ** 2))
    mu_ln = np.log(volumes) - 0.5 * sigma_ln ** 2
    noisy = rng.lognormal(mean=mu_ln, sigma=sigma_ln)
    return noisy.astype(np.float64)


# ---------------------------------------------------------------------------
# Volume-to-tension translation
# ---------------------------------------------------------------------------

def volume_to_tension_delta(
    observed_volumes: NDArray[np.float64],
    baseline_volumes: NDArray[np.float64],
) -> NDArray[np.float64]:
    """
    Translate observed traffic volumes into tension perturbation magnitudes.

    The web does not think in vehicles per hour. It thinks in tension — a
    dimensionless measure of how far each node is displaced from its
    expected operating point. We normalize by baseline so a 20% excess
    anywhere in the network registers as the same magnitude regardless of
    whether that node normally carries 500 or 2000 veh/hr.

    Fractional deviation: δ_i = (observed_i - baseline_i) / baseline_i
    Tension delta:        Δt_i = δ_i * sensitivity_i

    A positive Δt means the node is operating above capacity — excess
    demand is building up. A negative Δt means underload — vehicles are
    moving freely but the node is underutilized.

    The web then propagates these deltas via the Laplacian diffusion —
    excess tension bleeds to neighbors, which is exactly how intersection
    queues and signal adjustments ripple through a real network.
    """
    fractional_deviation = (observed_volumes - baseline_volumes) / baseline_volumes
    tension_delta = fractional_deviation * NODE_SENSITIVITY
    return tension_delta


# ---------------------------------------------------------------------------
# Inter-node correlation: upstream propagation with lag
# ---------------------------------------------------------------------------

def apply_upstream_lag(
    volume_history: list[NDArray[np.float64]],
    lag_intervals: int = 2,
) -> NDArray[np.float64] | None:
    """
    Model the causal lag between upstream detector (Node 2) and the
    intersection stop bar (Node 0).

    In the real system, vehicles observed upstream will reach the intersection
    approximately lag_intervals * 5 minutes later. During that travel time,
    some will turn off, some will join from cross streets. We model the
    attenuation of the propagated signal here in the generation layer —
    the web's Laplacian propagation handles redistribution once tension
    is injected, but the CAUSAL DELAY between nodes is a traffic phenomenon
    that belongs in the simulator, not the physics.

    Causal chain: Approaching Traffic (2) -> Intersection Throughput (0)
    with lag = travel time / aggregation period.

    Travel time calibration:
      At 35 mph (56 km/hr) link speed, detector is 1/4 mile upstream:
      travel_time ≈ 0.25 / 35 * 60 ≈ 0.43 min. Aggressive.
      Typical urban arterial with stops: 1/2 mile at 15 mph effective speed:
      travel_time ≈ 2 min ≈ 0.4 intervals. Round to lag_intervals=1 or 2.

    Args:
        volume_history: list of volume arrays in time order (newest last).
        lag_intervals:  number of 5-min intervals for upstream-to-stop-bar lag.

    Returns:
        Volume array with Node 0 replaced by a lagged + attenuated version of
        Node 2, or None if history is too short to compute the lag.
    """
    if len(volume_history) <= lag_intervals:
        return None

    lagged = volume_history[-(lag_intervals + 1)].copy()
    current = volume_history[-1].copy()

    # Attenuation: not all upstream vehicles reach this intersection —
    # turning movements, parking, mid-block pedestrian crossings remove ~15%.
    # This is the "turn-and-park" attenuation factor from HCM arrival rate models.
    attenuation = 0.85

    # Node 0 throughput is partially predicted by lagged Node 2 approach volume.
    # We blend: 60% lagged upstream, 40% current local demand.
    # This reflects that some demand originates locally (right turns from
    # side streets) and is not visible at the upstream detector.
    current[INTERSECTION_THROUGHPUT] = (
        0.60 * lagged[APPROACHING_TRAFFIC] * attenuation
        + 0.40 * current[INTERSECTION_THROUGHPUT]
    )

    return current


# ---------------------------------------------------------------------------
# Baseline traffic generation (no perturbation)
# ---------------------------------------------------------------------------

@dataclass
class BaselineConfig:
    """
    Configuration for baseline traffic generation.

    Parameters chosen to hit the CV=5-15% plausibility target while
    maintaining realistic volume ranges for urban arterials.
    """
    # Starting hour of day for the simulation (0-24)
    start_hour: float = 7.0
    # Duration in intervals (1 interval = 5 minutes)
    num_intervals: int = 288  # 24 hours at 5-minute resolution
    # Noise coefficient of variation
    noise_cv: float = NOISE_CV
    # Apply upstream-to-downstream lag in generation (realistic)
    apply_lag: bool = True
    # Lag in 5-minute intervals (Approaching -> Throughput)
    lag_intervals: int = 2


def generate_baseline(
    config: BaselineConfig,
    rng: Generator,
) -> NDArray[np.float64]:
    """
    Generate a baseline traffic volume time series with no perturbations.

    Returns an array of shape (num_intervals, 3) where columns are
    [Throughput, Signal_Timing, Approaching_Traffic].

    The overnight trough values (~100-120 veh/hr) stay well above zero
    because real arterials have freight, emergency vehicles, and shift
    workers at all hours. If the simulator ever produces zero volumes,
    something is wrong with the profile calibration.

    Volume plausibility check:
      Peak hour: ~[1000, 1200, 1150] veh/hr → ~500/lane on a 2-lane section.
      At g/C=0.55 and saturation flow=1800 pc/hr/ln, capacity=990 pc/hr/ln.
      v/c ≈ 0.50 — level of service C. Appropriate for a moderately loaded
      urban arterial at peak hour. (HCM 7th, Exhibit 16-3)
    """
    volumes = np.zeros((config.num_intervals, 3), dtype=np.float64)
    history: list[NDArray[np.float64]] = []

    for i in range(config.num_intervals):
        hour = (config.start_hour + i * 5.0 / 60.0) % 24.0
        clean = baseline_volume(hour)
        noisy = apply_traffic_noise(clean, rng, config.noise_cv)

        history.append(noisy.copy())

        if config.apply_lag:
            lagged = apply_upstream_lag(history, config.lag_intervals)
            if lagged is not None:
                noisy = lagged

        volumes[i] = noisy

    return volumes


# ---------------------------------------------------------------------------
# Perturbation scenario 1: Single-node shock (upstream accident)
# ---------------------------------------------------------------------------

@dataclass
class AccidentShockConfig:
    """
    Parameters for a single-node capacity reduction event (accident, breakdown,
    debris in roadway) on the approach leg.

    Defaults calibrated from INRIX incident duration data:
      - Minor incident (fender-bender, no injury): 20-40 min median clearance
      - Moderate incident (injury, 1 lane blocked): 45-90 min
      - Major incident (multi-vehicle, full closure): 60-180 min
    We default to a moderate blocking incident.

    Realistic onset is NOT a step function. First-responders arrive 3-5 min
    after the crash, rubbernecking builds over 2-4 min, then the lane is
    blocked. Recovery is gradual too: tow trucks take 10-20 min to clear.

    The affected node is Node 2 (Approaching Traffic) — the accident is on
    the approach, so the upstream detector sees reduced volume immediately.
    Throughput (Node 0) feels the impact after the lag delay.
    """
    # Which node to shock (default: approaching traffic leg)
    affected_node: int = APPROACHING_TRAFFIC
    # Capacity reduction at peak impact: 0.45 = 45% capacity loss.
    # Rationale: one of two approach lanes blocked in peak direction.
    # HCM: capacity reduction ≈ 1 - (lanes_remaining / total_lanes) * adjustment.
    # 1 lane blocked of 2 → ~50% reduction with rubbernecking → 45%.
    peak_reduction_fraction: float = 0.45
    # When the shock begins (interval index from scenario start)
    onset_interval: int = 12  # 1 hour into the simulation
    # Ramp-up duration in intervals (2-5 min in intervals: 1 interval = 5 min)
    onset_duration_intervals: int = 2  # 10 minutes to full impact
    # Duration at full impact (intervals)
    peak_duration_intervals: int = 16  # 80 minutes at full impact
    # Recovery duration (intervals) — gradual, not step-function
    recovery_duration_intervals: int = 6  # 30 minutes to clear


def _shock_envelope(
    num_intervals: int,
    onset_interval: int,
    onset_duration: int,
    peak_duration: int,
    recovery_duration: int,
) -> NDArray[np.float64]:
    """
    Compute the temporal shape of a perturbation event.

    Returns a (num_intervals,) array in [0, 1] where 1.0 = full impact.

    Shape:
      - Before onset: 0.0
      - Onset ramp: sigmoid-like rise from 0 to 1 (not linear — rubbernecking
        builds nonlinearly as the incident becomes visible to approaching drivers)
      - Peak plateau: 1.0 (or near it, with small fluctuations)
      - Recovery ramp: concave-down fall (initial lane-opening clears quickly,
        residual congestion drains slowly)
      - After recovery: 0.0

    The sigmoid onset is important: a step function onset is unrealistic and
    would inject an implausibly sharp perturbation spike into the web.
    """
    envelope = np.zeros(num_intervals, dtype=np.float64)

    for i in range(num_intervals):
        t = i - onset_interval

        if t < 0:
            envelope[i] = 0.0

        elif t < onset_duration:
            # Sigmoid-shaped ramp: slow at first (incident just happened,
            # not yet affecting flow), then rapid as rubbernecking spreads.
            frac = t / onset_duration
            # Logistic function centered at 0.5 of the ramp:
            # f(x) = 1 / (1 + exp(-k*(x - 0.5))) normalized to [0,1]
            k = 6.0  # steepness; k=6 gives ~0.07 at x=0, ~0.93 at x=1
            sigmoid = 1.0 / (1.0 + np.exp(-k * (frac - 0.5)))
            envelope[i] = (sigmoid - 1.0 / (1.0 + np.exp(k * 0.5))) / (
                1.0 / (1.0 + np.exp(-k * 0.5)) - 1.0 / (1.0 + np.exp(k * 0.5))
            )

        elif t < onset_duration + peak_duration:
            # Full impact plateau. Small fluctuations because incident
            # clearance is rarely perfectly stable — tow trucks maneuver,
            # officers redirect traffic. We add no noise here (the baseline
            # noise model already layers randomness on top of the envelope).
            envelope[i] = 1.0

        elif t < onset_duration + peak_duration + recovery_duration:
            # Recovery: concave-down (fast initial clearance, slow tail).
            # After lane opens, first vehicles surge through (quick relief),
            # but queue discharge takes time proportional to queue length.
            frac = (t - onset_duration - peak_duration) / recovery_duration
            # Power-law decay: fast start, slow finish (exponent < 1 = concave)
            envelope[i] = 1.0 - frac ** 0.6

        else:
            envelope[i] = 0.0

    return envelope


def generate_accident_shock(
    baseline_volumes: NDArray[np.float64],
    config: AccidentShockConfig,
    rng: Generator,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Inject a single-node accident shock into a baseline volume time series.

    The shock reduces capacity on the affected node. This creates a volume
    drop on the approach. After the lag, Throughput (Node 0) drops too
    because vehicles can't reach the intersection.

    Secondary effect: when approach volume drops due to the accident, the
    signal controller (Node 1) cannot adapt instantly — it keeps serving
    a now-absent demand for several cycles before timing reoptimizes.
    This creates a brief SIGNAL TIMING anomaly (underutilized green time)
    that is a leading indicator of the upstream disturbance.

    Args:
        baseline_volumes: (num_intervals, 3) array from generate_baseline().
        config: AccidentShockConfig with event parameters.
        rng: Seeded random generator.

    Returns:
        perturbed_volumes: (num_intervals, 3) with accident effects applied.
        envelope: (num_intervals,) the temporal impact envelope [0, 1].
    """
    num_intervals = baseline_volumes.shape[0]
    perturbed = baseline_volumes.copy()

    envelope = _shock_envelope(
        num_intervals,
        config.onset_interval,
        config.onset_duration_intervals,
        config.peak_duration_intervals,
        config.recovery_duration_intervals,
    )

    for i in range(num_intervals):
        impact = envelope[i]
        if impact <= 0:
            continue

        # Volume reduction on the directly affected node.
        # Real capacity drop: blocked lane reduces maximum flow through that
        # section by approximately peak_reduction_fraction.
        capacity_factor = 1.0 - impact * config.peak_reduction_fraction
        perturbed[i, config.affected_node] *= capacity_factor

        # Downstream lag effect: if the upstream approach is congested,
        # throughput at the stop bar drops after lag_intervals have passed.
        # (The lag was baked in during baseline generation — here we reduce
        # throughput directly when the upstream signal has already been lagged.)
        lag = 2  # 5-minute intervals
        if i >= lag and config.affected_node == APPROACHING_TRAFFIC:
            # Throughput drops with attenuation: not all impact propagates downstream.
            # Cross-street demand partially compensates (drivers divert to parallel routes).
            downstream_factor = 1.0 - impact * config.peak_reduction_fraction * 0.70
            perturbed[i, INTERSECTION_THROUGHPUT] = (
                baseline_volumes[i, INTERSECTION_THROUGHPUT] * downstream_factor
            )

        # Signal timing anomaly: controller cannot immediately reoptimize.
        # For the first recovery_duration intervals after onset, signal wastes
        # green time on the congested approach. This shows as below-expected
        # throughput efficiency — we reduce the signal timing proxy.
        # The anomaly is smaller than the approach reduction (controller does
        # adapt, just slowly: ~30% of the approach impact bleeds into timing).
        if config.affected_node == APPROACHING_TRAFFIC:
            signal_impact = impact * 0.30
            perturbed[i, SIGNAL_TIMING] *= (1.0 - signal_impact * 0.20)

    return perturbed, envelope


# ---------------------------------------------------------------------------
# Perturbation scenario 2: Compound shock (weather + localized event)
# ---------------------------------------------------------------------------

@dataclass
class CompoundShockConfig:
    """
    Parameters for a compound shock: weather degrading all nodes simultaneously
    while a localized demand spike hits the approaching traffic node.

    The NON-LINEARITY is the critical property:
      Weather alone: reduces capacity by 15-30% across all nodes.
      Event alone: creates a demand spike of 30-50% on approach.
      Combined: the spike hits a REDUCED CAPACITY network, causing
        queue overflow and spillback — this is qualitatively different
        from either effect alone. The v/c ratio jumps from ~0.60 to >1.0,
        triggering oversaturation (queue grows without bound each cycle).

    Calibration from field studies:
      Rain intensity >25 mm/hr reduces freeway capacity ~14%,
      urban arterial capacity ~20% (reduced visibility, increased headways).
      (Maze et al. 2006, TRB; Ibrahim & Hall 1994)
      Stadium event dispersal: 20,000-person venue, 40% departure in first
      20 minutes → ~8000 person-trips, ~70% vehicle occupancy → ~5700 vehicles,
      distributed across 3-4 routes → ~1400-1900 vehicles on one arterial leg,
      spread over 30 min → 2800-3800 veh/hr additional demand. Massive.
    """
    # Weather capacity reduction range (uniform across nodes)
    weather_reduction_min: float = 0.15
    weather_reduction_max: float = 0.28
    # Which node receives the event demand spike
    event_node: int = APPROACHING_TRAFFIC
    # Event demand spike magnitude (fraction of baseline added ON TOP)
    event_spike_fraction: float = 0.40  # 40% above baseline
    # Interval when weather begins (gradual onset, unlike accidents)
    weather_onset_interval: int = 6   # 30 minutes in
    weather_onset_duration: int = 4   # 20 minutes to full rain
    weather_duration: int = 36        # 3 hours of rain
    weather_recovery: int = 8         # 40 minutes for conditions to improve
    # Event timing (event demand spike): starts after weather is established
    event_onset_interval: int = 18    # 1.5 hours in (rain already active)
    event_duration_intervals: int = 8  # 40 minutes of event dispersal


def generate_compound_shock(
    baseline_volumes: NDArray[np.float64],
    config: CompoundShockConfig,
    rng: Generator,
) -> NDArray[np.float64]:
    """
    Generate compound shock: weather capacity reduction + event demand spike.

    The non-linear interaction between weather and the event:
      Under normal conditions, the network can absorb a 40% demand spike
      because it has spare capacity (v/c ≈ 0.50 in midday). With weather
      reducing capacity 20%, effective capacity drops to 0.80 * nominal.
      The spike then pushes v/c to (1.0 + 0.40) / (1.0 - 0.20) = 1.75.
      Above v/c = 1.0, the queue grows without bound each cycle —
      a phase transition from undersaturated to oversaturated flow.

    We model this non-linearity explicitly: when combined v/c > 1.0,
    throughput is capped at capacity and the excess demand becomes a
    growing queue that further degrades throughput (spillback).

    The result: the compound scenario is WORSE than the sum of parts
    because oversaturation is a qualitatively different regime.
    """
    num_intervals = baseline_volumes.shape[0]
    perturbed = baseline_volumes.copy()

    # Compute weather envelope (gradual onset, not step)
    weather_env = _shock_envelope(
        num_intervals,
        config.weather_onset_interval,
        config.weather_onset_duration,
        config.weather_duration,
        config.weather_recovery,
    )

    # Weather reduction magnitude varies within the configured range
    # (rain intensity fluctuates — it doesn't stay perfectly constant).
    # Use a smooth random variation: baseline + low-frequency modulation.
    weather_intensity = rng.uniform(
        config.weather_reduction_min,
        config.weather_reduction_max,
    )

    # Queue accumulator: models spillback from oversaturated flow.
    # When v/c > 1, vehicles that can't clear add to this queue.
    # The queue re-enters as additional demand in subsequent intervals.
    spillback_queue: float = 0.0

    for i in range(num_intervals):
        w = weather_env[i]

        # Weather affects all nodes — reduced visibility, longer headways,
        # driver hesitation. The effect is not perfectly uniform:
        # signal timing node (controller) is less directly affected by weather
        # than the vehicle flow nodes (0 and 2).
        weather_factor = np.array([
            1.0 - w * weather_intensity,          # Throughput: full weather impact
            1.0 - w * weather_intensity * 0.60,   # Signal timing: partial (controller adapts)
            1.0 - w * weather_intensity,           # Approaching: full weather impact
        ], dtype=np.float64)

        # Event demand spike: only on the event node, for the event window.
        event_factor = np.ones(3, dtype=np.float64)
        t_event = i - config.event_onset_interval
        if 0 <= t_event < config.event_duration_intervals:
            # Spike shape: sharp onset (events end at a fixed time — everyone
            # leaves simultaneously), gradual tail (some people linger, traffic
            # backs up and the release is staggered by intersection capacity).
            frac = t_event / config.event_duration_intervals
            # Triangular profile: rises quickly (first 20%), stays high (60%), falls (20%)
            if frac < 0.20:
                spike = config.event_spike_fraction * (frac / 0.20)
            elif frac < 0.80:
                spike = config.event_spike_fraction
            else:
                # The fall is not clean — spillback keeps it elevated
                spike = config.event_spike_fraction * (1.0 - (frac - 0.80) / 0.20)

            # Add queue spillback from previous interval overflow
            effective_demand_fraction = spike + (spillback_queue / baseline_volumes[i, APPROACHING_TRAFFIC])
            event_factor[config.event_node] = 1.0 + effective_demand_fraction

        # Compute raw volume under both effects
        raw_volume = perturbed[i] * weather_factor * event_factor

        # NON-LINEAR INTERACTION: oversaturation spillback.
        # Capacity at this node under weather conditions:
        capacity_estimate = baseline_volumes[i, config.event_node] * weather_factor[config.event_node]
        demand_estimate = raw_volume[config.event_node]

        if demand_estimate > capacity_estimate:
            # Queue grows: vehicles that can't clear become residual demand
            overflow = demand_estimate - capacity_estimate
            spillback_queue += overflow * 0.30  # Not all overflow recycles — some divert
            # Clamp throughput at weather-degraded capacity
            raw_volume[config.event_node] = capacity_estimate
            # Throughput at the intersection is also capped (queue blocking)
            raw_volume[INTERSECTION_THROUGHPUT] = min(
                raw_volume[INTERSECTION_THROUGHPUT],
                capacity_estimate * 0.90,  # 10% additional throughput loss from queuing
            )
        else:
            # Drain queue as vehicles clear the backup
            queue_drain = min(spillback_queue, capacity_estimate - demand_estimate)
            spillback_queue = max(0.0, spillback_queue - queue_drain)

        perturbed[i] = raw_volume

    return perturbed


# ---------------------------------------------------------------------------
# Perturbation scenario 3: Slow decay (construction zone setup)
# ---------------------------------------------------------------------------

@dataclass
class SlowDecayConfig:
    """
    Parameters for a gradual capacity reduction over hours.

    Models construction zone setup: a maintenance crew begins narrowing
    lanes, setting up signage, and positioning equipment. The impact is
    not noticeable in the first few intervals — this is the hard part
    for any detection system.

    Calibration:
      Construction zone capacity reduction when active: 25-45%.
      (HCM 7th, Exhibit 10-21: work zone capacity tables)
      Setup rate: 1-2% per 10-minute interval (gradual lane narrowing,
      sign placement, equipment positioning).
      This means 50 minutes to 2.5 hours to reach full impact — the
      signal is genuinely subtle at the start.

    The detection challenge: in the first 30 minutes, the volume drop
    is ~3-6%, which is well within the natural noise CV of 10%. A naive
    threshold detector would miss it entirely. Only by comparing the
    TREND (sustained downward drift) to the expected diurnal pattern
    can the perturbation be detected early.
    """
    # Node where construction begins
    affected_node: int = APPROACHING_TRAFFIC
    # Interval when workers arrive and setup begins
    onset_interval: int = 6  # 30 minutes into the simulation
    # Rate of capacity loss per 5-min interval during setup
    # 1% per 5-min = 2% per 10-min (within the 1-2% target range)
    decay_rate_per_interval: float = 0.01
    # Maximum capacity reduction when fully established (fraction)
    max_reduction: float = 0.35  # 35% — one lane of two fully closed
    # Duration at max before any recovery (e.g., work finishes at night)
    plateau_duration_intervals: int = 36  # 3 hours at full impact


def generate_slow_decay(
    baseline_volumes: NDArray[np.float64],
    config: SlowDecayConfig,
    rng: Generator,
) -> NDArray[np.float64]:
    """
    Generate a slow capacity decay scenario.

    The signal is intentionally subtle: 1% loss per interval competes with
    10% natural noise CV. Only trend-aware detection (looking at running
    average residuals, not point-in-time deviations) will catch the
    early-stage decay.

    The decay is NOT monotonic — construction workers take breaks,
    adjust their setup, and sometimes reopen a lane briefly for a
    delivery vehicle. We model this with small random reversals (~0.5%
    magnitude) superimposed on the downward trend. These reversals are
    realistic and make the scenario harder to detect via simple thresholding.
    """
    num_intervals = baseline_volumes.shape[0]
    perturbed = baseline_volumes.copy()
    current_reduction = 0.0

    for i in range(num_intervals):
        t = i - config.onset_interval

        if t < 0:
            continue

        if current_reduction < config.max_reduction and t < int(config.max_reduction / config.decay_rate_per_interval):
            # Still in setup phase: accumulate capacity loss.
            # Small random reversals model the non-monotonic reality.
            step = config.decay_rate_per_interval
            # Occasional brief partial reopening: ~20% of intervals during setup
            if rng.random() < 0.20:
                # Workers briefly pull back a barricade, or a signal truck
                # temporarily clears the area. Partial reversal, not full recovery.
                step -= rng.uniform(0.003, 0.008)
            current_reduction = np.clip(current_reduction + step, 0.0, config.max_reduction)

        elif t >= int(config.max_reduction / config.decay_rate_per_interval) + config.plateau_duration_intervals:
            # Beyond plateau: scenario ends (construction wraps up at midnight).
            # Recovery is not modeled here — left for a separate recovery scenario.
            pass

        # Apply the current reduction to the affected node only.
        # Adjacent nodes feel this through the web's propagation, not here —
        # the simulator should NOT pre-compute inter-node effects.
        # That's the web's job.
        capacity_factor = 1.0 - current_reduction
        perturbed[i, config.affected_node] *= capacity_factor

        # Minor secondary effect: as approach volume drops due to the
        # construction taper, signal timing slightly misallocates green time.
        # This is a proportional artifact: ~15% of approach reduction bleeds
        # into timing efficiency. Much smaller than the approach signal.
        timing_bleed = current_reduction * 0.15
        perturbed[i, SIGNAL_TIMING] *= (1.0 - timing_bleed)

    return perturbed


# ---------------------------------------------------------------------------
# Perturbation scenario 4: Unmapped shock (stadium event discharge)
# ---------------------------------------------------------------------------

@dataclass
class UnmappedShockConfig:
    """
    Parameters for a perturbation originating OUTSIDE the three-node model.

    The unmapped shock is the most important scenario for stress-testing
    the web's incoherence detection. A stadium 0.5 miles from the
    intersection lets out after a game. The resulting traffic surge:
      1. Appears as anomalous volume on the approaching traffic node —
         demand far exceeds what the signal timing and throughput nodes
         would predict from their own historical correlation.
      2. Cannot be explained by any tension propagation within the
         three-node web — none of the mapped strands could account for it.
      3. Creates residual tension that looks locally incoherent:
         Node 2 shows high tension but nodes 0 and 1 are near baseline.

    This is the signature of an unmapped strand: tension concentrated at
    one node with no correlated upstream cause visible within the web.

    Key signature properties:
      - Sharp onset (events end at a fixed clock time, most people leave
        within the first 10-15 minutes after final whistle)
      - Much higher volume than historical patterns for that hour
      - Pattern does NOT follow the normal diurnal correlation between
        nodes — approach is high, but throughput is lower than expected
        because the intersection can't process the queue fast enough
      - Signal timing looks WRONG: controller is trying to serve demand
        it wasn't designed for, and its response looks incoherent with
        both approach and throughput nodes
    """
    # Unmapped demand surge: fraction above baseline
    surge_fraction: float = 0.65  # 65% above baseline — from an 18,000-seat venue
    # Duration of surge (intervals)
    surge_duration_intervals: int = 6  # 30 minutes for main wave
    # When surge begins (interval index)
    surge_onset_interval: int = 10
    # Spatial signature: which node receives the unmapped demand
    # It's ONLY Node 2 (Approaching Traffic) — the stadium is outside
    # the model, so its effect enters only through the approach detector.
    # This is what makes it "unmapped": no internal node caused it.
    affected_node: int = APPROACHING_TRAFFIC
    # The incoherence signature: node 1 (Signal Timing) is NOT prepared
    # for this demand pattern. Its response will be anomalous relative to
    # what the approach volume would predict from the historical profile.
    timing_incoherence_fraction: float = 0.25  # Controller is 25% "wrong" given this pattern


def generate_unmapped_shock(
    baseline_volumes: NDArray[np.float64],
    config: UnmappedShockConfig,
    rng: Generator,
) -> NDArray[np.float64]:
    """
    Generate an unmapped shock from an external force (stadium discharge).

    The key design constraint: the volume anomaly on Node 2 must be
    LOCALLY INEXPLICABLE from the three-node topology. Specifically:
      - Node 2 volume is 65% above baseline (unmapped surge).
      - Node 0 throughput does NOT scale with Node 2 — the intersection
        is saturated, so it's capped at ~110% of nominal capacity.
        This creates a tension GRADIENT across the Node2->Node0 strand
        that looks anomalous: approach is high but throughput didn't rise.
      - Node 1 signal timing is in the WRONG state: the controller is
        cycling based on its current program, which wasn't designed for
        this demand. Its proxy volume shows underutilization of signal
        resources (green time waste) at the same moment Node 2 is maxed out.

    The resulting web state: Node 2 has extreme positive tension
    (demand >> baseline), Node 0 has moderate positive tension (throughput
    near capacity), Node 1 has near-zero or slightly negative tension
    (timing is running normal cycles, neither using its capacity efficiently
    nor overwhelmed). This three-way inconsistency is incoherent under
    any propagation model using only the three mapped strands.
    """
    num_intervals = baseline_volumes.shape[0]
    perturbed = baseline_volumes.copy()

    for i in range(num_intervals):
        t = i - config.surge_onset_interval

        if t < 0 or t >= config.surge_duration_intervals:
            continue

        # Surge profile: sharp triangular peak (most people leave in first 10 min,
        # then it drains as the parking lot empties and routes clog).
        frac = t / config.surge_duration_intervals
        if frac < 0.25:
            # Fast rise: parking lot exits are all opening simultaneously
            surge = config.surge_fraction * (frac / 0.25)
        else:
            # Exponential-ish decay: main wave passes, stragglers trickle out
            surge = config.surge_fraction * np.exp(-3.0 * (frac - 0.25))

        # Node 2 sees the full surge
        perturbed[i, APPROACHING_TRAFFIC] = baseline_volumes[i, APPROACHING_TRAFFIC] * (1.0 + surge)

        # Node 0 (Throughput) is CAPPED because the intersection saturates.
        # The crucial non-linearity: more approach demand does NOT produce
        # proportionally more throughput when v/c > 1.
        # We cap at 115% of baseline throughput (oversaturated but not zero).
        intersection_capacity = baseline_volumes[i, INTERSECTION_THROUGHPUT]
        perturbed[i, INTERSECTION_THROUGHPUT] = min(
            perturbed[i, INTERSECTION_THROUGHPUT],
            intersection_capacity * 1.15,
        )

        # Node 1 (Signal Timing) is INCOHERENT with both of the above.
        # The controller is running its standard timing plan, which was
        # designed for historical demand patterns. It under-allocates
        # green time to the approach because its actuated logic doesn't
        # see a pattern like this in its memory. The timing proxy shows
        # normal-to-slightly-below baseline — neither responding to the
        # surge nor to the intersection saturation.
        # This is the diagnostic signature: timing_proxy is DECOUPLED
        # from what you'd predict from approach or throughput.
        timing_noise = rng.normal(0, config.timing_incoherence_fraction * 0.3)
        perturbed[i, SIGNAL_TIMING] = baseline_volumes[i, SIGNAL_TIMING] * (
            1.0 - config.timing_incoherence_fraction + timing_noise
        )

    return perturbed


# ---------------------------------------------------------------------------
# Scenario composers
# ---------------------------------------------------------------------------

@dataclass
class ScenarioConfig:
    """Top-level configuration for a complete simulation run."""
    seed: int = 42
    start_hour: float = 7.0
    num_intervals: int = 144  # 12 hours at 5-minute resolution
    baseline: BaselineConfig = field(default_factory=BaselineConfig)


def compose_scenario_accident(
    seed: int = 42,
    start_hour: float = 7.0,
    num_intervals: int = 144,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Complete accident shock scenario: baseline + single-node shock.

    Returns:
        volumes: (num_intervals, 3) volume time series.
        envelope: (num_intervals,) perturbation impact [0, 1].
    """
    rng = np.random.default_rng(seed)
    cfg = BaselineConfig(start_hour=start_hour, num_intervals=num_intervals)
    baseline = generate_baseline(cfg, rng)
    shock_cfg = AccidentShockConfig()
    return generate_accident_shock(baseline, shock_cfg, rng)


def compose_scenario_compound(
    seed: int = 137,
    start_hour: float = 11.0,
    num_intervals: int = 144,
) -> NDArray[np.float64]:
    """
    Complete compound shock scenario: baseline + weather + event spike.

    Uses a different default seed from the accident scenario so the
    two runs are independently comparable.
    """
    rng = np.random.default_rng(seed)
    cfg = BaselineConfig(start_hour=start_hour, num_intervals=num_intervals)
    baseline = generate_baseline(cfg, rng)
    compound_cfg = CompoundShockConfig()
    return generate_compound_shock(baseline, compound_cfg, rng)


def compose_scenario_slow_decay(
    seed: int = 271,
    start_hour: float = 6.0,
    num_intervals: int = 288,
) -> NDArray[np.float64]:
    """
    Complete slow decay scenario: baseline + construction zone setup.

    Uses a longer window (24h) so the detector can see both the
    pre-decay baseline and the full extent of the degradation.
    The early-phase signal (first 30-60 min) is deliberately subtle.
    """
    rng = np.random.default_rng(seed)
    cfg = BaselineConfig(start_hour=start_hour, num_intervals=num_intervals)
    baseline = generate_baseline(cfg, rng)
    decay_cfg = SlowDecayConfig()
    return generate_slow_decay(baseline, decay_cfg, rng)


def compose_scenario_unmapped(
    seed: int = 314,
    start_hour: float = 20.5,  # 8:30 PM — game ends after evening peak
    num_intervals: int = 36,   # 3 hours around the event
) -> NDArray[np.float64]:
    """
    Complete unmapped shock scenario: baseline + stadium discharge.

    Start hour chosen for 8:30 PM because:
      - Evening peak has just ended, so baseline volumes are declining.
      - The surge hits a declining-volume period, making the anomaly
        starker (approach volume goes UP while historical pattern says DOWN).
      - Signal timing is set for evening recovery — the mismatch with
        actual demand is most incoherent in this period.
    """
    rng = np.random.default_rng(seed)
    cfg = BaselineConfig(start_hour=start_hour, num_intervals=num_intervals)
    baseline = generate_baseline(cfg, rng)
    unmapped_cfg = UnmappedShockConfig()
    return generate_unmapped_shock(baseline, unmapped_cfg, rng)


# ---------------------------------------------------------------------------
# Tension delta generation: translate volumes to web perturbations
# ---------------------------------------------------------------------------

def compute_reference_baseline(
    start_hour: float,
    num_intervals: int,
    lag_intervals: int = 2,
) -> NDArray[np.float64]:
    """
    Compute the noiseless, lag-adjusted reference baseline for tension deviation.

    This must use the SAME lag logic as generate_baseline() so that normal
    (unperturbed) traffic produces near-zero tension deltas. If the reference
    is computed from raw time-of-day profiles without accounting for the lag,
    Node 0 (Throughput) will show systematic negative drift because its
    generated value is a lagged composite of Node 2 + local demand, which
    is structurally lower than the raw time-of-day profile for Node 0.

    The lag-adjusted reference for Node 0 at interval i is:
        ref_0[i] = 0.60 * baseline_vol(hour[i - lag])[2] * 0.85
                 + 0.40 * baseline_vol(hour[i])[0]

    This mirrors exactly the blend in apply_upstream_lag().

    Args:
        start_hour: Hour of day at the start of the series.
        num_intervals: Number of 5-minute intervals.
        lag_intervals: Upstream-to-stop-bar lag (must match BaselineConfig.lag_intervals).

    Returns:
        (num_intervals, 3) noiseless reference volume array.
    """
    reference = np.zeros((num_intervals, 3), dtype=np.float64)

    for i in range(num_intervals):
        hour = (start_hour + i * 5.0 / 60.0) % 24.0
        clean = baseline_volume(hour)

        if i >= lag_intervals:
            hour_lagged = (start_hour + (i - lag_intervals) * 5.0 / 60.0) % 24.0
            clean_lagged = baseline_volume(hour_lagged)
            # Mirror the blend in apply_upstream_lag():
            # Node 0 = 60% lagged Node 2 * 0.85 attenuation + 40% current Node 0
            clean[INTERSECTION_THROUGHPUT] = (
                0.60 * clean_lagged[APPROACHING_TRAFFIC] * 0.85
                + 0.40 * clean[INTERSECTION_THROUGHPUT]
            )

        reference[i] = clean

    return reference


def volumes_to_perturbation_series(
    volumes: NDArray[np.float64],
    start_hour: float,
    lag_intervals: int = 2,
) -> NDArray[np.float64]:
    """
    Translate a volume time series into a perturbation delta series for the web.

    For each interval, compute the fractional deviation from the EXPECTED
    baseline for that time of day, using the lag-adjusted reference so that
    normal traffic produces near-zero tension deltas. Apply sensitivity
    scaling. Return a (num_intervals, 3) array of tension deltas ready for
    perturb_vector().

    Critical: the reference must account for the same upstream lag used in
    generate_baseline(). Without this, Node 0 shows systematic negative drift
    because its generated value is a lagged composite that naturally falls
    below the raw time-of-day profile during the ramp-up phase.

    This is the bridge between the traffic domain and the web physics.
    The output is dimensionless tension — the web doesn't care about veh/hr.
    """
    num_intervals = volumes.shape[0]
    reference = compute_reference_baseline(start_hour, num_intervals, lag_intervals)
    deltas = np.zeros_like(volumes)

    for i in range(num_intervals):
        deltas[i] = volume_to_tension_delta(volumes[i], reference[i])

    return deltas


# ---------------------------------------------------------------------------
# Data pushers: web engine communication layer
# ---------------------------------------------------------------------------

def push_interval(
    web: TensionWeb,
    tension_delta: NDArray[np.float64],
    propagation_steps: int = 100,
) -> list:
    """
    Push one interval's worth of traffic data into the tension web.

    Single interval = 5 minutes of real traffic aggregated into one
    tension perturbation. After injection, the web propagates for
    propagation_steps steps to let the disturbance travel through
    the network before the next measurement.

    propagation_steps = 100 at dt=0.05 = 5.0 simulation time units per interval.
    Calibration: the triangle web with β=0.5 has damping timescale 1/(β/2) = 4.0
    simulation time units for its non-trivial Laplacian modes (λ=3). Setting
    the propagation window to 5.0 units gives ~71% decay of the wave before
    the next perturbation arrives. This means:
      - A single-interval perturbation leaves ~29% residual after one interval.
      - A sustained perturbation (accident, construction) builds tension at
        ~3.4x the per-interval injection rate (geometric series sum 1/(1-0.29)).
      - After the perturbation stops, tension decays with e-folding time ≈ 1.4
        intervals, which is fast enough for the web to recover between events.
    This propagation window is physically motivated: a 5-minute aggregation
    window is enough for signal controllers to partially adapt, queues to
    partially drain, and the network to move toward local equilibrium.

    Args:
        web: TensionWeb instance (modified in place).
        tension_delta: (3,) array of tension perturbations for this interval.
        propagation_steps: integration steps between observations.

    Returns:
        list of NodeState snapshots after propagation.
    """
    # Inject the perturbation at all nodes simultaneously
    web.perturb_vector(tension_delta)

    # Let the wave propagate
    web.propagate(propagation_steps)

    # Return a measurement snapshot
    return web.observe()


def push_scenario(
    web: TensionWeb,
    volumes: NDArray[np.float64],
    start_hour: float,
    realtime: bool = False,
    interval_sleep_seconds: float = 1.0,
    verbose: bool = True,
) -> list[list]:
    """
    Push a complete scenario volume series into the tension web.

    IMPORTANT — web state accumulation:
    The Laplacian diffusion conserves total tension (the zero eigenvalue of L
    is undamped — uniform tension shifts persist indefinitely). A sustained
    perturbation over many intervals WILL build up accumulated tension in the
    web. This is correct physics: a 90-minute accident creates a sustained
    reduction in the network's operating state, and the web should reflect that.

    For single-event stress testing, use a fresh TensionWeb per scenario
    (call create_triangle_web() before each push_scenario()). For ongoing
    monitoring, the coherence.py layer (Phase 2) must track the RUNNING
    BASELINE of web tension and detect deviations from it — the simulator
    feeds raw perturbations, not pre-baseline-subtracted signals.

    The incoherence detection signal lives in the TENSION DELTA at injection
    time (see volumes_to_perturbation_series output), not in the post-
    equalization web state. The Laplacian quickly equalizes tension across
    nodes — within ~10 propagation steps for this 3-node triangle. Incoherence
    is the tension that CANNOT equalize because it lacks a mapped strand to
    travel through: that's the residual, not the wave.

    Args:
        web: TensionWeb instance (modified in place).
        volumes: (num_intervals, 3) volume time series from any compose_scenario_*().
        start_hour: Hour of day at the start of the scenario (for baseline calc).
        realtime: If True, sleep between intervals to simulate real-time cadence.
                  If False, run as fast as possible (for testing/analysis).
        interval_sleep_seconds: Seconds to sleep between intervals in realtime mode.
                                 Default 1.0 gives one interval/second — a 144-interval
                                 (12-hour) scenario runs in ~2.5 minutes.
        verbose: Print interval summary if True.

    Returns:
        all_states: list of NodeState lists, one per interval.
    """
    deltas = volumes_to_perturbation_series(volumes, start_hour)
    num_intervals = volumes.shape[0]
    all_states: list[list] = []

    for i in range(num_intervals):
        states = push_interval(web, deltas[i])
        all_states.append(states)

        if verbose:
            hour = (start_hour + i * 5.0 / 60.0) % 24.0
            tensions = [f"{s.label_short}={s.tension:.3f}" for s in states]
            print(f"  [{hour:05.2f}h] interval {i:03d} | " + " | ".join(tensions))

        if realtime:
            time.sleep(interval_sleep_seconds)

    return all_states


# ---------------------------------------------------------------------------
# Module entry point: demonstration run
# ---------------------------------------------------------------------------

def _run_demo() -> None:
    """
    Demonstration: run the unmapped shock scenario (most diagnostic scenario)
    and print the tension evolution.

    Shows how the stadium discharge creates incoherent tension across nodes
    that cannot be explained by the three-node topology alone.
    """
    print("=" * 70)
    print("Ayin Traffic Simulator — Unmapped Shock Demo (Stadium Discharge)")
    print("=" * 70)
    print()
    print("Scenario: 8:30 PM game ends at a nearby stadium.")
    print("Expected: Node 2 (Approach) surges. Node 0 (Throughput) saturates.")
    print("          Node 1 (Signal Timing) stays near normal — incoherent.")
    print()

    web = create_triangle_web(strand_strength=1.0, propagation_rate=1.0, damping_coefficient=0.5)
    volumes = compose_scenario_unmapped(seed=314, start_hour=20.5, num_intervals=36)

    print(f"Initial web energy: {web.total_energy():.6f}")
    print(f"Initial total tension: {web.total_tension():.6f}")
    print()

    all_states = push_scenario(
        web,
        volumes,
        start_hour=20.5,
        realtime=False,
        verbose=True,
    )

    print()
    print(f"Final web energy: {web.total_energy():.6f}")
    print(f"Final total tension: {web.total_tension():.6f}")
    print(f"Max tension gradient: {web.max_tension_gradient():.6f}")
    print()
    print("Incoherence signature: if Node 2 tension >> Node 0 tension")
    print("and Node 1 tension is near-zero or negative, the web has detected")
    print("an unexplained tension concentration — candidate for unmapped strand.")

    final_states = web.observe()
    tensions = {s.label: s.tension for s in final_states}
    print()
    for label, t in tensions.items():
        print(f"  {label}: {t:+.4f}")


if __name__ == "__main__":
    _run_demo()
