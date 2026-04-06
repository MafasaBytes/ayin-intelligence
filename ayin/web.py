"""
Tension web — the propagation physics substrate.

Physical analogy: a network of masses connected by damped springs.
Each node is a mass point. Each strand is a spring with stiffness
proportional to coupling_strength. Tension at a node is its displacement
from rest. Perturbations propagate as damped waves through the network.

The governing equation is the DAMPED WAVE EQUATION ON A GRAPH:

    d²T/dt² = -α L T  -  β dT/dt

Where:
    T           = tension vector (one scalar per node)
    L           = graph Laplacian: L = D - W
    W           = symmetric weighted adjacency (strand coupling strengths)
    D           = degree matrix: D_ii = sum_j W_ij
    α (alpha)   = propagation rate (spring stiffness / mass ratio)
    β (beta)    = damping coefficient (viscous friction)

This is a second-order ODE system, integrated via Störmer-Verlet
(symplectic integrator — preserves the energy structure of the equation).

KEY PHYSICAL PROPERTIES (these emerge, they are not programmed):

1. EQUILIBRIUM-SEEKING: The Laplacian L has non-negative eigenvalues,
   and damping β > 0 dissipates energy. Every trajectory converges to
   a state where L*T = 0 (uniform tension across connected components).
   This is a mathematical consequence, not an enforced condition.

2. CONSERVATION (undamped limit): When β → 0, total energy
   E = 0.5 * v^T v + 0.5 * α * T^T L T is conserved.
   With β > 0, dE/dt = -β * ||v||² ≤ 0 (Lyapunov function).

3. SHOCKWAVE PROPAGATION: Perturbation at one node creates a wave
   that travels through the graph. Wave speed ~ sqrt(α * w_ij).
   The wave reflects at boundaries and interferes constructively/destructively.

4. TOTAL TENSION CONSERVATION: The Laplacian has row-sums of zero,
   so d(sum T_i)/dt is driven only by velocity, and velocity is damped.
   Total tension converges to the initial sum (perturbation redistributes,
   not creates/destroys).

WSN reference: This is the continuous-time analog of consensus-based
diffusion in wireless sensor networks, extended to second-order dynamics
for wave propagation. See Olfati-Saber & Murray (2004) "Consensus problems
in networks of agents with switching topology and time-delays."
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final

import numpy as np
from numpy.typing import NDArray

from ayin.nodes import (
    NODE_LABELS,
    measure_all_nodes,
    NodeState,
    total_kinetic_energy,
    total_tension,
)
from ayin.coherence import CoherenceConfig, CoherenceMonitor, CoherenceSnapshot


# --- Propagation Parameters ---

@dataclass(frozen=True)
class PropagationParams:
    """
    Physical constants governing wave propagation in the web.

    These are material properties of the substrate, not tuning knobs
    for desired behavior. Changing them changes the physics — the same
    way changing spring stiffness changes how a physical web vibrates.
    """

    # Propagation rate: controls wave speed through the web.
    # Higher α = faster propagation, higher-frequency oscillations.
    # Physically: stiffness-to-mass ratio of the spring-mass system.
    propagation_rate: float = 1.0

    # Damping coefficient: controls energy dissipation rate.
    # Higher β = faster decay of oscillations toward equilibrium.
    # Physically: viscous friction opposing velocity.
    # Critical damping for eigenmode i occurs at β = 2√(α λ_i).
    damping_coefficient: float = 0.5

    # Integration timestep for the Verlet integrator.
    # Must satisfy dt < 2/√(α λ_max) for stability (CFL condition).
    # Smaller dt = more accurate but slower simulation.
    dt: float = 0.05


# --- Topology Constructors ---

def triangle_coupling_matrix(
    strand_strength: float = 1.0,
) -> NDArray[np.float64]:
    """
    Construct the coupling (adjacency) matrix for a 3-node triangle.

    All strands are bidirectional with equal coupling strength.
    The matrix is symmetric because strand tension is mutual —
    if node A is coupled to node B, B is equally coupled to A.

    For the POC traffic domain:
        Node 0 (Throughput) <-> Node 1 (Signal Timing)
        Node 1 (Signal Timing) <-> Node 2 (Approaching Traffic)
        Node 2 (Approaching Traffic) <-> Node 0 (Throughput)
    """
    coupling_matrix: NDArray[np.float64] = np.array([
        [0.0, strand_strength, strand_strength],
        [strand_strength, 0.0, strand_strength],
        [strand_strength, strand_strength, 0.0],
    ], dtype=np.float64)
    return coupling_matrix


def graph_laplacian(
    coupling_matrix: NDArray[np.float64],
) -> NDArray[np.float64]:
    """
    Compute the graph Laplacian: L = D - W.

    The Laplacian encodes the diffusion structure of the network.
    Its eigenvalues are all non-negative (L is positive semidefinite).
    The smallest eigenvalue is always 0 with eigenvector [1,1,...,1],
    corresponding to the uniform-tension equilibrium.

    For our 3-node triangle with unit weights:
        L = [[2, -1, -1],
             [-1, 2, -1],
             [-1, -1, 2]]
        Eigenvalues: 0, 3, 3
    """
    # D_ii = sum of coupling strengths at node i (weighted degree)
    degree_matrix: NDArray[np.float64] = np.diag(np.sum(coupling_matrix, axis=1))
    laplacian: NDArray[np.float64] = degree_matrix - coupling_matrix
    return laplacian


# --- The Tension Web ---

class TensionWeb:
    """
    The tensioned web substrate. All intelligence lives here.

    State variables:
        tension:  T(t) — tension at each node (displacement from uniform)
        velocity: V(t) = dT/dt — rate of tension change at each node

    The web evolves by integrating the damped wave equation:
        dV/dt = -α L T  -  β V
        dT/dt = V

    This class IS the physics. It contains no decision logic, no thresholds,
    no special cases. Feed it a perturbation and it will propagate, oscillate,
    dissipate, and settle — because that is what the equation does.
    """

    def __init__(
        self,
        coupling_matrix: NDArray[np.float64],
        params: PropagationParams | None = None,
    ) -> None:
        self._params: Final[PropagationParams] = params or PropagationParams()
        self._coupling_matrix: NDArray[np.float64] = coupling_matrix.copy()
        self._num_nodes: Final[int] = coupling_matrix.shape[0]

        # Verify the coupling matrix is symmetric — strands are bidirectional
        assert np.allclose(coupling_matrix, coupling_matrix.T), \
            "Coupling matrix must be symmetric (bidirectional strands only)"

        # Compute the Laplacian once (topology is fixed between strand changes)
        self._laplacian: NDArray[np.float64] = graph_laplacian(coupling_matrix)

        # Precompute eigenvalues for stability verification and diagnostics.
        # The Laplacian is real symmetric, so eigenvalues are real and non-negative.
        self._eigenvalues: NDArray[np.float64] = np.linalg.eigvalsh(self._laplacian)

        # CFL stability check: dt must be small enough for the Verlet integrator.
        # For the undamped wave equation, stability requires dt < 2/sqrt(α * λ_max).
        lambda_max: float = float(self._eigenvalues[-1])
        if lambda_max > 0:
            dt_critical: float = 2.0 / np.sqrt(self._params.propagation_rate * lambda_max)
            assert self._params.dt < dt_critical, (
                f"Timestep {self._params.dt} exceeds CFL limit {dt_critical:.4f}. "
                f"Reduce dt or propagation_rate for stable integration."
            )

        # --- State vectors ---
        # Tension: displacement of each node from the eventual uniform equilibrium
        self._tension: NDArray[np.float64] = np.zeros(self._num_nodes, dtype=np.float64)
        # Velocity: rate of tension change (momentum in the wave equation)
        self._velocity: NDArray[np.float64] = np.zeros(self._num_nodes, dtype=np.float64)
        # Net flux: tension flow into each node during the last propagation step
        # (measurement variable, not part of the physics)
        self._net_flux: NDArray[np.float64] = np.zeros(self._num_nodes, dtype=np.float64)

        # Simulation clock
        self._time: float = 0.0
        self._step_count: int = 0

        # --- Coherence monitor (passive instrument, not physics) ---
        # Compute the analytical damping ratio for the dominant eigenmode
        # so the monitor can compare empirical vs predicted behavior.
        nonzero_eigenvalues = self._eigenvalues[self._eigenvalues > 1e-12]
        if len(nonzero_eigenvalues) > 0:
            # Use the smallest non-trivial eigenvalue — the slowest mode
            # dominates the late-time decay and is easiest to measure.
            lambda_min_nontrivial = float(nonzero_eigenvalues[0])
            analytical_zeta = self._params.damping_coefficient / (
                2.0 * np.sqrt(self._params.propagation_rate * lambda_min_nontrivial)
            )
        else:
            analytical_zeta = 0.0
        self._monitor: CoherenceMonitor = CoherenceMonitor(
            num_nodes=self._num_nodes,
            coupling_matrix=self._coupling_matrix,
            analytical_damping_ratio=analytical_zeta,
        )

    # --- Properties (read-only observation of state) ---

    @property
    def num_nodes(self) -> int:
        return self._num_nodes

    @property
    def tension(self) -> NDArray[np.float64]:
        """Current tension vector. Read-only view."""
        return self._tension.copy()

    @property
    def velocity(self) -> NDArray[np.float64]:
        """Current velocity vector. Read-only view."""
        return self._velocity.copy()

    @property
    def coupling_matrix(self) -> NDArray[np.float64]:
        """Current strand coupling strengths. Read-only view."""
        return self._coupling_matrix.copy()

    @property
    def laplacian(self) -> NDArray[np.float64]:
        """Graph Laplacian. Read-only view."""
        return self._laplacian.copy()

    @property
    def eigenvalues(self) -> NDArray[np.float64]:
        """Laplacian eigenvalues — characterize the web's resonant frequencies."""
        return self._eigenvalues.copy()

    @property
    def time(self) -> float:
        return self._time

    @property
    def step_count(self) -> int:
        return self._step_count

    # --- Perturbation (energy injection) ---

    def perturb(self, node_index: int, magnitude: float) -> None:
        """
        Inject a perturbation at a single node.

        Physically: an external force strikes the web at one point,
        displacing that mass from equilibrium. The web's own dynamics
        then propagate and dissipate the disturbance.

        This is the ONLY way external signals enter the web.
        The perturbation adds to existing tension (superposition principle).
        """
        if not (0 <= node_index < self._num_nodes):
            raise IndexError(f"Node index {node_index} out of range [0, {self._num_nodes})")
        self._tension[node_index] += magnitude

    def perturb_vector(self, perturbation: NDArray[np.float64]) -> None:
        """
        Inject perturbation at multiple nodes simultaneously.
        Useful for correlated external signals that affect several nodes at once.
        """
        assert perturbation.shape == (self._num_nodes,), \
            f"Perturbation vector must have shape ({self._num_nodes},)"
        self._tension += perturbation

    # --- Propagation (the core physics) ---

    def step(self) -> None:
        """
        Advance the web by one timestep using Velocity Verlet integration.

        The equation being integrated:
            d²T/dt² = -α L T  -  β dT/dt

        Rewritten as a first-order system:
            dT/dt = V
            dV/dt = -α L T  -  β V       ... (*)

        Velocity Verlet is a symplectic integrator — it preserves the
        geometric structure of Hamiltonian dynamics, giving excellent
        long-term energy behavior even with moderate timestep sizes.
        This matters because we need the web to conserve total tension
        accurately over many steps.

        Verlet steps:
            1. T(t + dt) = T(t) + V(t)*dt + 0.5*a(t)*dt²
            2. a(t + dt) = acceleration from T(t + dt), V(t) [predictor]
            3. V(t + dt) = V(t) + 0.5*(a(t) + a(t+dt))*dt

        For the damped system (*), the acceleration depends on velocity,
        which complicates Verlet. We use the standard approach: compute
        the velocity-dependent damping at the half-step.
        """
        alpha: float = self._params.propagation_rate
        beta: float = self._params.damping_coefficient
        dt: float = self._params.dt

        # --- Current acceleration ---
        # a(t) = -α L T(t)  -  β V(t)
        # The Laplacian term drives tension from high to low (diffusion).
        # The damping term opposes velocity (viscous friction).
        laplacian_force: NDArray[np.float64] = -alpha * (self._laplacian @ self._tension)
        damping_force: NDArray[np.float64] = -beta * self._velocity
        acceleration: NDArray[np.float64] = laplacian_force + damping_force

        # Record net flux as measurement: the Laplacian force shows
        # how much tension is flowing into/out of each node from its neighbors.
        # Positive = neighbors are pushing tension toward this node.
        self._net_flux = laplacian_force.copy()

        # --- Verlet step 1: update tension (position) ---
        # T(t + dt) = T(t) + V(t)*dt + 0.5*a(t)*dt²
        self._tension = (
            self._tension
            + self._velocity * dt
            + 0.5 * acceleration * dt * dt
        )

        # --- Verlet step 2: predicted velocity at half-step ---
        # V_half = V(t) + 0.5*a(t)*dt  (used for damping in new acceleration)
        velocity_half: NDArray[np.float64] = self._velocity + 0.5 * acceleration * dt

        # --- Verlet step 3: new acceleration from updated tension ---
        # a(t+dt) = -α L T(t+dt)  -  β V_half
        laplacian_force_new: NDArray[np.float64] = -alpha * (self._laplacian @ self._tension)
        damping_force_new: NDArray[np.float64] = -beta * velocity_half
        acceleration_new: NDArray[np.float64] = laplacian_force_new + damping_force_new

        # --- Verlet step 4: update velocity ---
        # V(t+dt) = V(t) + 0.5*(a(t) + a(t+dt))*dt
        self._velocity = self._velocity + 0.5 * (acceleration + acceleration_new) * dt

        # Advance the clock
        self._time += dt
        self._step_count += 1

        # --- Feed the coherence monitor (passive observation) ---
        # This happens AFTER the physics step is complete. The monitor
        # reads the new state but never modifies it.
        self._monitor.observe(
            tension=self._tension,
            velocity=self._velocity,
            energy=self.total_energy(),
            step=self._step_count,
        )

    def propagate(self, num_steps: int) -> None:
        """Run the propagation physics for multiple timesteps."""
        for _ in range(num_steps):
            self.step()

    # --- Measurements (read the state, never steer it) ---

    def observe(self) -> list[NodeState]:
        """Snapshot all node states. Pure measurement, no side effects."""
        return measure_all_nodes(self._tension, self._velocity, self._net_flux)

    def total_tension(self) -> float:
        """
        Sum of tension across all nodes. In a conservative system
        (no sources/sinks), this should remain approximately constant.
        Drift here indicates numerical integration error.
        """
        return total_tension(self._tension)

    def total_energy(self) -> float:
        """
        Total mechanical energy: kinetic + potential.

        E = 0.5 * V^T V  +  0.5 * α * T^T L T

        In the undamped system (β=0) this is exactly conserved.
        With damping, dE/dt = -β ||V||² ≤ 0 (always decreasing).
        This is the Lyapunov function proving equilibrium-seeking
        is a mathematical property, not a programmed behavior.
        """
        kinetic: float = 0.5 * float(np.dot(self._velocity, self._velocity))
        potential: float = 0.5 * self._params.propagation_rate * float(
            self._tension @ self._laplacian @ self._tension
        )
        return kinetic + potential

    def tension_gradient_across_strands(self) -> NDArray[np.float64]:
        """
        Tension difference across each strand: |T_i - T_j| for each edge.

        Returns the upper triangle of the pairwise difference matrix,
        weighted by coupling strength. When all gradients approach zero,
        the web is at equilibrium (uniform tension across connected nodes).
        This is a measurement of how far from equilibrium the web is.
        """
        # Pairwise tension differences, masked to active strands only
        tension_diff: NDArray[np.float64] = np.abs(
            self._tension[:, np.newaxis] - self._tension[np.newaxis, :]
        )
        # Weight by coupling strength (inactive strands contribute zero)
        weighted_gradient: NDArray[np.float64] = tension_diff * self._coupling_matrix
        return weighted_gradient

    def max_tension_gradient(self) -> float:
        """
        Largest tension difference across any strand.
        A scalar measure of disequilibrium in the web.
        """
        gradients = self.tension_gradient_across_strands()
        return float(np.max(gradients))

    def coherence(self) -> CoherenceSnapshot:
        """
        Current coherence diagnostics from the embedded monitor.
        Pure measurement — the monitor reads state, never writes it.
        """
        return self._monitor.snapshot()

    @property
    def monitor(self) -> CoherenceMonitor:
        """Direct access to the coherence monitor for detailed queries."""
        return self._monitor

    def damping_ratio_per_mode(self) -> NDArray[np.float64]:
        """
        Damping ratio ζ for each eigenmode of the Laplacian.

        ζ_i = β / (2 √(α λ_i))

        ζ < 1: underdamped (oscillatory decay)
        ζ = 1: critically damped (fastest non-oscillatory decay)
        ζ > 1: overdamped (exponential decay, no oscillation)

        This characterizes the web's intrinsic recovery dynamics.
        The eigenvalues are physical properties of the topology.
        """
        alpha: float = self._params.propagation_rate
        beta: float = self._params.damping_coefficient

        # Skip the zero eigenvalue (rigid-body mode — uniform translation)
        nonzero_mask = self._eigenvalues > 1e-12
        ratios = np.zeros_like(self._eigenvalues)
        ratios[nonzero_mask] = beta / (
            2.0 * np.sqrt(alpha * self._eigenvalues[nonzero_mask])
        )
        return ratios


# --- Factory ---

def create_triangle_web(
    strand_strength: float = 1.0,
    propagation_rate: float = 1.0,
    damping_coefficient: float = 0.5,
    dt: float = 0.05,
) -> TensionWeb:
    """
    Construct the POC 3-node triangle web.

    Default parameters produce an underdamped system (ζ ≈ 0.14 for
    the triangle's non-trivial modes with λ = 3), meaning perturbations
    will oscillate several times before settling. This makes the
    wave-like propagation visible and measurable.
    """
    coupling = triangle_coupling_matrix(strand_strength)
    params = PropagationParams(
        propagation_rate=propagation_rate,
        damping_coefficient=damping_coefficient,
        dt=dt,
    )
    return TensionWeb(coupling, params)
