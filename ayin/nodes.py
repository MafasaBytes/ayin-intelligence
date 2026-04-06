"""
Node state representation and tension measurement.

A node is a vertex in the tension web. Each node carries:
  - A tension value T_i(t): the current load/activation at this point in the web.
  - A velocity dT_i/dt: the rate of tension change (momentum in the wave equation).

Tension is a continuous scalar representing how much perturbation energy
is concentrated at this point. At equilibrium, tension gradients across
strands vanish — the web is at rest.

Nodes do NOT decide anything. They are mass points in a spring network.
Their state evolves entirely through the propagation equation in web.py.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final

import numpy as np
from numpy.typing import NDArray


# --- Domain Constants ---

# POC traffic intersection node identifiers.
# These are semantic labels, not behavioral controllers.
INTERSECTION_THROUGHPUT: Final[int] = 0
SIGNAL_TIMING: Final[int] = 1
APPROACHING_TRAFFIC: Final[int] = 2

NODE_LABELS: Final[dict[int, str]] = {
    INTERSECTION_THROUGHPUT: "Intersection Throughput",
    SIGNAL_TIMING: "Signal Timing",
    APPROACHING_TRAFFIC: "Approaching Traffic",
}


@dataclass
class NodeState:
    """
    Observable state of a single node at a moment in time.

    This is a READ-ONLY measurement snapshot — it never feeds back
    into the propagation equation. The physics operates on raw arrays
    in the TensionWeb; this exists for human-readable observation.
    """

    index: int
    label: str
    tension: float
    velocity: float  # dT/dt — rate of tension change
    # Tension absorbed from neighbors minus tension radiated to neighbors
    # in the most recent propagation step. Positive = net inflow.
    net_flux: float = 0.0

    @property
    def is_at_rest(self) -> bool:
        """
        A node is at rest when its velocity is negligible.
        This is a measurement, not a control signal.
        """
        return abs(self.velocity) < 1e-10

    @property
    def kinetic_energy(self) -> float:
        """
        Energy stored in the node's rate of change.
        In the damped wave equation, kinetic energy dissipates over time —
        this measures how much is left. When total kinetic energy across
        all nodes approaches zero, the web has reached equilibrium.
        """
        return 0.5 * self.velocity ** 2

    @property
    def label_short(self) -> str:
        return self.label.split()[0] if self.label else f"Node-{self.index}"


def measure_node(
    index: int,
    tension_vector: NDArray[np.float64],
    velocity_vector: NDArray[np.float64],
    flux_vector: NDArray[np.float64] | None = None,
) -> NodeState:
    """
    Take a measurement of node state from the raw physics arrays.
    Pure observation — no side effects on the web.
    """
    return NodeState(
        index=index,
        label=NODE_LABELS.get(index, f"Node-{index}"),
        tension=float(tension_vector[index]),
        velocity=float(velocity_vector[index]),
        net_flux=float(flux_vector[index]) if flux_vector is not None else 0.0,
    )


def measure_all_nodes(
    tension_vector: NDArray[np.float64],
    velocity_vector: NDArray[np.float64],
    flux_vector: NDArray[np.float64] | None = None,
) -> list[NodeState]:
    """Snapshot every node in the web. Observation only."""
    n = tension_vector.shape[0]
    return [
        measure_node(i, tension_vector, velocity_vector, flux_vector)
        for i in range(n)
    ]


def total_tension(tension_vector: NDArray[np.float64]) -> float:
    """
    Sum of all node tensions. In pure Laplacian diffusion (no sources/sinks),
    total tension is conserved — this measurement verifies that invariant.
    """
    return float(np.sum(tension_vector))


def total_kinetic_energy(velocity_vector: NDArray[np.float64]) -> float:
    """
    Total kinetic energy across all nodes: sum of 0.5 * v_i^2.
    In a damped system this must monotonically decrease (Lyapunov function).
    If it increases, the propagation equation has a bug.
    """
    return float(0.5 * np.dot(velocity_vector, velocity_vector))
