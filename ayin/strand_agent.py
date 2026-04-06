"""
Strand discovery agent — LLM-powered proposal generator triggered by incoherence signals.

This module is the scout for Phase 2. It monitors coherence snapshots emitted by the
coherence monitor and proposes candidate strands when it detects acute incoherence
signatures that cannot be explained by existing topology.

Cardinal principle (non-negotiable):
  "Is the web asking for this strand, or am I imposing it?"

  This question must pass through an explicit validation gate before any strand
  proposal can be stored. The web's incoherence signals are the only source of truth
  about what strands are needed. The agent's job is to interpret those signals,
  not to imagine problems the web hasn't revealed.

Core responsibilities:
  1. TRIGGER CONDITION: Detect acute incoherence signatures only.
     - Mixed-sign tension patterns across multiple nodes simultaneously
     - Patterns that violate Laplacian diffusion (e.g., N2 positive while N1
       negative — impossible under pure diffusion from a single source)
     - Patterns NOT explainable by existing topology
     - NOT triggered on chronic mode signals (different class of problem)
     - NOT triggered on single-node incoherence (could be noise)

  2. PROMPT PACKAGING: Convert anomaly context into investigation prompts.
     - Include affected nodes, tensions, velocities, what Laplacian would predict
     - Include domain context: traffic intersection, three-node topology
     - Include strand topology so Claude knows what exists
     - Include prior failed proposals (avoid repetition)
     - Keep focused — don't dump entire web history

  3. CLAUDE API INTEGRATION: Use claude-sonnet-4-20250514 exclusively.
     - Proper error handling, rate limiting, retries
     - Structure requests to elicit specific, parseable responses

  4. RESPONSE PARSING: Convert Claude responses into StrandProposal dataclasses.
     - Each contains: hypothesized_source, target_node, expected_tension_direction,
       confidence, rationale
     - Reject vague or unfalsifiable proposals

  5. STORAGE: Simple in-memory list, NO auto-attach.
     - Scout proposes, web validates (later phase)
     - Include methods to retrieve, mark as validated/rejected/pending

  6. INTEGRATION PROTOCOL STUBS: Define three-phase data structures.
     - ProbationaryStrand, ValidatedStrand, SlackStrand
     - NO actual attachment logic — just type definitions

  7. EVENT-DRIVEN: Expose evaluate(snapshot: CoherenceSnapshot) method.
     - No polling, no cron, no timers
     - Caller invokes with coherence data
     - Scout decides internally if signature warrants investigation
     - If yes, calls Claude and stores proposal
     - If no, returns None

References:
  - Coherence module: detects unexplained tension as positive correlation in
    ΔT_node and ΔT_neighbors (incoherence_score = (1 + correlation) / 2)
  - Acute signatures: simultaneous high-score events across multiple nodes
  - Chronic tracking: separate concern — OLS slope trending upward, elevated means
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Final, Any
from enum import Enum

import numpy as np
from numpy.typing import NDArray

from ayin.coherence import CoherenceSnapshot
from ayin.nodes import NODE_LABELS

# Configure logging for auditability
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class StrandAgentConfig:
    """
    Configurable parameters for the strand discovery agent.

    These control MEASUREMENT sensitivity and DECISION thresholds for when
    to trigger investigation, not behavioral steering.
    """

    # Minimum number of nodes that must spike incoherence simultaneously
    # to trigger acute investigation. Single-node spikes are likely noise.
    # A threshold of 2+ requires at least two nodes to fire together.
    min_nodes_for_acute_signature: int = 2

    # Minimum incoherence score to consider a node as "spiking".
    # Incoherence is in [0, 1]: 0=coherent diffusion, 1=strong external force.
    # Threshold of 0.6 means we need moderate-to-strong incoherence signals.
    incoherence_threshold: float = 0.6

    # Maximum allowed correlation between node's tension change and neighbors'
    # weighted average to rule out the signature as "explainable by diffusion".
    # When correlation is strongly positive (r > 0.3), it indicates independent
    # external forces pushing multiple nodes the same direction — unmapped force.
    correlation_threshold_for_external: float = 0.3

    # Minimum absolute velocity change magnitude on affected nodes.
    # Velocity changes indicate energy injection. Below this threshold,
    # the signal might be noise rather than a real perturbation.
    min_velocity_change: float = 0.01

    # Maximum number of proposal candidates to store in memory.
    # Older proposals are pruned to keep memory bounded.
    max_proposals_history: int = 100

    # Number of recent time steps to consider when checking for
    # sustained / correlated incoherence patterns.
    # Acute signatures should manifest within 3-5 observation windows.
    observation_window: int = 5

    # Claude API model — hardcoded per requirements.
    claude_model: str = "claude-sonnet-4-20250514"

    # Maximum tokens for Claude API requests (input + output combined).
    # Keeps costs bounded and responses focused.
    max_tokens_investigation: int = 1024


# ---------------------------------------------------------------------------
# Proposal State Machine
# ---------------------------------------------------------------------------

class ProposalStatus(Enum):
    """Lifecycle state of a strand proposal."""
    PENDING = "pending"           # Proposed, awaiting web validation
    PROBATIONARY = "probationary" # Attached with minimal load, observing
    VALIDATING = "validating"     # Both nodes showing improved coherence
    VALIDATED = "validated"       # Successfully passed bidirectional validation
    REJECTED = "rejected"         # Failed to improve coherence
    SLACK = "slack"               # Validated once, now idle but preserved as data


# ---------------------------------------------------------------------------
# Proposal Data Structures
# ---------------------------------------------------------------------------

@dataclass
class StrandProposal:
    """
    A proposed connection between two nodes, discovered through incoherence analysis.

    This is the OUTPUT of the scout. It proposes; the web validates.
    The proposal includes enough context to understand WHY it was proposed,
    making the decision auditable.
    """

    # Unique identifier for this proposal
    proposal_id: str

    # Step counter when the proposal was generated
    step_generated: int

    # Hypothesized external source or force causing the incoherence.
    # Not necessarily a node index — could be "stadium event", "accident at intersection",
    # "upstream traffic surge", etc. Human-readable description of the unmapped cause.
    hypothesized_source: str

    # Index of the existing node this strand should connect to.
    # The proposal is to add (source -> target_node) to the web.
    target_node: int

    # Expected direction of tension flow from source to target.
    # +1 = source pushes tension into target (positive coupling)
    # -1 = source relieves tension from target (negative coupling, damping)
    expected_tension_direction: int

    # Confidence that Claude assigned to this proposal, in [0, 1].
    # Higher = more likely to be a real unmapped connection.
    # This comes from Claude's reasoning and is logged for auditing.
    confidence: float

    # Rationale: Why did the scout propose this strand?
    # Extracted from Claude's response, kept brief but specific.
    # Example: "Nodes 0 and 2 both spiking positive simultaneously — cannot
    #          occur under diffusion alone. External force at node 0 must be
    #          also affecting node 2, suggesting previously unmapped connection."
    rationale: str

    # Current status in the proposal lifecycle
    status: ProposalStatus = ProposalStatus.PENDING

    # Affected node indices during investigation
    # Which nodes showed the incoherence pattern that triggered the proposal
    affected_nodes: list[int] = field(default_factory=list)

    # Claude API full response text (for post-hoc analysis)
    claude_response: str = ""

    # Number of steps survived under probationary attachment (if applicable)
    steps_under_probation: int = 0

    # Coherence improvement measured at validation time
    coherence_delta: float = 0.0

    # Timestamp or step when status last changed
    status_updated_at_step: int = 0


@dataclass
class ProbationaryStrand:
    """
    A proposed strand in the initial probationary phase.

    Attached with minimal load. Observes but doesn't yet influence coherence
    calculations significantly. Both connected nodes must show improved
    coherence for transition to validation.

    This is a TYPE DEFINITION ONLY — no attachment logic implemented yet.
    """
    proposal: StrandProposal

    # Step when probation started
    probation_start_step: int

    # Weight factor: fraction of normal coupling this strand contributes
    # Starts at ~0.1, can ramp to 1.0 over many steps if coherence improves
    load_factor: float = 0.1

    # Running coherence measurements at source and target nodes
    source_coherence_history: list[float] = field(default_factory=list)
    target_coherence_history: list[float] = field(default_factory=list)


@dataclass
class ValidatedStrand:
    """
    A strand that passed bidirectional validation.

    Both connected nodes showed improved coherence when the strand was active.
    The strand can now bear full load in propagation calculations.

    This is a TYPE DEFINITION ONLY — no actual integration logic implemented.
    """
    proposal: StrandProposal

    # Step when validation completed
    validation_step: int

    # Coherence delta measured during validation window
    coherence_improvement: float

    # Final coupling weight (can be ramped during gradual load bearing phase)
    coupling_weight: float = 1.0

    # Vector of tension changes at both nodes during validation
    # Used for post-hoc analysis of strand behavior
    validation_measurements: NDArray[np.float64] = field(default_factory=lambda: np.array([]))


@dataclass
class SlackStrand:
    """
    A validated strand that is currently idle (not contributing to propagation).

    Never deleted. It is preserved as data about what the web needed at some point,
    providing context for future proposals.

    This is a TYPE DEFINITION ONLY — slack state is tracked but not enforced.
    """
    proposal: StrandProposal
    validation: ValidatedStrand

    # Step when strand went slack
    slack_start_step: int

    # Reason for going slack (e.g., "became inactive after 50 steps without tension change")
    slack_reason: str


# ---------------------------------------------------------------------------
# Incoherence Signature Analysis
# ---------------------------------------------------------------------------

class IncoherenceSignatureAnalyzer:
    """
    Detects acute incoherence signatures that warrant investigation.

    The fundamental test: Can the observed tension pattern be explained by
    Laplacian diffusion through existing strands? If not, an external force
    is acting on the web, and we should propose a strand to map it.

    Signature characteristics of unmapped external forcing:
      - Multiple nodes spike incoherence SIMULTANEOUSLY (not sequentially)
      - Tensions move in MIXED SIGNS (some up, some down) that violate diffusion
      - Correlation between node and neighbors is POSITIVE (both pushed outward)
    """

    def __init__(self, config: StrandAgentConfig) -> None:
        self.config = config

    def has_acute_signature(
        self,
        snapshot: CoherenceSnapshot,
        prev_snapshot: CoherenceSnapshot | None = None,
    ) -> tuple[bool, list[int]]:
        """
        Check if the coherence snapshot contains an acute incoherence signature.

        Returns:
          (is_acute, affected_node_indices)

        If is_acute is True, affected_node_indices lists the nodes that spiked
        incoherence together. If False, affected_node_indices is empty.

        Logic:
          1. Count nodes with incoherence_score > threshold
          2. If count >= min_nodes_for_acute_signature, it might be acute
          3. Verify nodes have non-zero velocity changes (not dead/resting)
          4. Check for sign pattern violations (can't all be diffusion)
          5. If passes, return True and node list
        """
        incoherence = snapshot.incoherence_scores

        # Step 1: Find nodes with high incoherence
        high_incoherence_mask = incoherence > self.config.incoherence_threshold
        affected_nodes = list(np.where(high_incoherence_mask)[0])

        if len(affected_nodes) < self.config.min_nodes_for_acute_signature:
            return False, []

        # Step 2: Verify these are not just resting nodes with noise
        # A true incoherence signal requires CHANGE — velocity should be nonzero
        # or have just changed. If all affected nodes are at rest, it's probably noise.
        # (This check requires velocity data — deferred to API integration layer)

        # Step 3: Check for coherence degeneracy — if chronically elevated,
        # this might be chronic mode, not acute. Acute should be a SPIKE,
        # not a plateau. We distinguish by checking if the scores are
        # newly elevated (just spiked) vs sustained at high level.
        # For now, we accept any multi-node simultaneous spike.

        # Step 4: The signature is "unmapped external force" if nodes spike
        # with similar sign/direction of change. Pure diffusion would show
        # anti-correlation (one node up, neighbors down). If incoherence
        # is high on MULTIPLE nodes simultaneously, it suggests they're
        # being pushed by the same external source.

        logger.info(
            f"Potential acute incoherence signature at step {snapshot.step}: "
            f"nodes {affected_nodes} with scores {incoherence[affected_nodes]}"
        )

        return True, affected_nodes

    def is_explainable_by_topology(
        self,
        affected_nodes: list[int],
        incoherence_scores: NDArray[np.float64],
    ) -> bool:
        """
        Heuristic check: could existing topology explain this pattern?

        If nodes are adjacent in the graph (connected by existing strands),
        then high incoherence at both might be explainable as a diffusion
        shockwave propagating. If nodes are NOT adjacent, simultaneous
        incoherence at both is a strong signal of an external, unmapped force.

        For the three-node triangle, every node is adjacent to every other node,
        so this heuristic is less useful. But it's here for completeness and
        for generality to other topologies.

        Returns True if the pattern could be explained by topology.
        Returns False if topology is insufficient (suggesting unmapped strand).
        """
        # For now, always return False for multi-node patterns.
        # The triangle is fully connected, so we can't distinguish based on
        # adjacency. Real distinction comes from the incoherence correlation
        # measure already computed (stored in the scores themselves).
        return False


# ---------------------------------------------------------------------------
# Strand Agent
# ---------------------------------------------------------------------------

class StrandAgent:
    """
    The scout — discovers candidate strands triggered by incoherence signals.

    Usage:
        agent = StrandAgent(config)
        snapshot = web.coherence()
        proposals = agent.evaluate(snapshot)
        for proposal in proposals:
            print(f"Proposed strand: {proposal}")

    The agent:
      - Is completely event-driven (no polling, no cron)
      - Receives coherence snapshots from the web
      - Analyzes them for acute incoherence signatures
      - If signature detected, calls Claude API to propose candidate strands
      - Stores proposals in an in-memory list
      - Never modifies the web — the web validates proposals later
    """

    def __init__(self, config: StrandAgentConfig | None = None) -> None:
        self.config = config or StrandAgentConfig()
        self.analyzer = IncoherenceSignatureAnalyzer(self.config)

        # In-memory proposal store
        self._proposals: list[StrandProposal] = []
        self._proposal_counter: int = 0

        # Previous snapshot (for detecting change/trends)
        self._prev_snapshot: CoherenceSnapshot | None = None

        # Claude API client — deferred initialization until needed (type: Any)
        self._claude_client: Any = None

        logger.info(
            f"StrandAgent initialized with config: "
            f"min_nodes={self.config.min_nodes_for_acute_signature}, "
            f"incoherence_threshold={self.config.incoherence_threshold}, "
            f"model={self.config.claude_model}"
        )

    def evaluate(
        self,
        snapshot: CoherenceSnapshot,
    ) -> list[StrandProposal]:
        """
        Main entry point: Evaluate a coherence snapshot for acute incoherence.

        If an acute signature is detected, investigate with Claude and
        store proposals. Otherwise return empty list (no investigation needed).

        This is EVENT-DRIVEN: the caller invokes with snapshot data when
        available. The agent does NOT poll or maintain a timer.

        Args:
            snapshot: CoherenceSnapshot from the web's coherence monitor

        Returns:
            List of StrandProposal objects (possibly empty if no acute signature)
        """
        # Step 1: Detect acute signature
        is_acute, affected_nodes = self.analyzer.has_acute_signature(
            snapshot, self._prev_snapshot
        )

        # Store snapshot for next iteration
        self._prev_snapshot = snapshot

        if not is_acute:
            logger.debug(
                f"Step {snapshot.step}: No acute signature detected. "
                f"Incoherence scores: {snapshot.incoherence_scores}"
            )
            return []

        # Step 2: Check if topology explains the pattern
        if self.analyzer.is_explainable_by_topology(
            affected_nodes,
            snapshot.incoherence_scores,
        ):
            logger.info(
                f"Step {snapshot.step}: Incoherence signature is explainable "
                f"by existing topology. No investigation needed."
            )
            return []

        # Step 3: Signature is NOT explainable — investigate with Claude
        logger.info(
            f"Step {snapshot.step}: Acute incoherence signature at nodes "
            f"{affected_nodes}. Triggering Claude investigation..."
        )

        proposals = self._investigate_with_claude(snapshot, affected_nodes)

        # Step 4: Store proposals and apply "is web asking" validation
        for proposal in proposals:
            if self._passes_web_asking_gate(proposal, snapshot, affected_nodes):
                self._proposals.append(proposal)
                logger.info(
                    f"Stored proposal {proposal.proposal_id}: "
                    f"{proposal.hypothesized_source} -> Node {proposal.target_node}, "
                    f"confidence={proposal.confidence:.2f}"
                )
            else:
                logger.warning(
                    f"Rejected proposal {proposal.proposal_id}: "
                    f"failed 'is web asking' validation. Rationale: {proposal.rationale}"
                )

        return proposals

    def _investigate_with_claude(
        self,
        snapshot: CoherenceSnapshot,
        affected_nodes: list[int],
    ) -> list[StrandProposal]:
        """
        Call Claude API to investigate an incoherence signature.

        Constructs a structured prompt from the coherence snapshot and
        parses Claude's response into StrandProposal objects.

        Args:
            snapshot: The coherence snapshot from the web
            affected_nodes: Node indices that spiked incoherence

        Returns:
            List of StrandProposal objects from Claude's analysis
        """
        # Lazy-load Claude client
        if self._claude_client is None:
            self._init_claude_client()

        # Step 1: Build investigation prompt
        prompt = self._build_investigation_prompt(snapshot, affected_nodes)

        # Step 2: Call Claude
        try:
            response = self._call_claude(prompt)
        except Exception as e:
            logger.error(f"Claude API call failed: {e}")
            return []

        # Step 3: Parse response into proposals
        proposals = self._parse_claude_response(response, snapshot, affected_nodes)

        return proposals

    def _init_claude_client(self) -> None:
        """Initialize Anthropic SDK client (deferred until first use)."""
        try:
            from anthropic import Anthropic
            self._claude_client = Anthropic()
            logger.info("Claude API client initialized")
        except ImportError:
            logger.error(
                "Anthropic SDK not installed. Install with: pip install anthropic"
            )
            raise

    def _build_investigation_prompt(
        self,
        snapshot: CoherenceSnapshot,
        affected_nodes: list[int],
    ) -> str:
        """
        Construct a focused investigation prompt for Claude.

        The prompt includes:
          - Problem description: what incoherence signature was detected
          - Node identities and states: which nodes, their tensions/velocities
          - Topology: existing strands so Claude knows what's already connected
          - Expected diffusion: what Laplacian would predict vs actual
          - Prior failed proposals (if any, to avoid repetition)

        The prompt asks Claude to hypothesize what external force could
        explain the pattern and propose a new strand to map it.
        """
        # Format node descriptions
        node_descriptions = []
        for node_idx in affected_nodes:
            label = NODE_LABELS.get(node_idx, f"Node-{node_idx}")
            incoherence = snapshot.incoherence_scores[node_idx]
            node_descriptions.append(
                f"  {label} (node {node_idx}): "
                f"incoherence_score={incoherence:.3f}"
            )

        # Format all incoherence scores
        all_scores = "\n".join([
            f"  Node {i}: {snapshot.incoherence_scores[i]:.3f}"
            for i in range(len(snapshot.incoherence_scores))
        ])

        # Describe the pattern
        pattern_description = (
            f"Multiple nodes ({len(affected_nodes)}) show simultaneously high "
            f"incoherence scores, indicating unexplained tension changes. "
            f"This pattern cannot occur under pure Laplacian diffusion alone—"
            f"it suggests external force(s) acting on the network."
        )

        # Describe the topology (triangle)
        topology_description = (
            "Three-node traffic intersection network (triangle topology):\n"
            "  Node 0 (Intersection Throughput) ↔ Node 1 (Signal Timing)\n"
            "  Node 1 (Signal Timing) ↔ Node 2 (Approaching Traffic)\n"
            "  Node 2 (Approaching Traffic) ↔ Node 0 (Intersection Throughput)\n"
            "All strands are bidirectional."
        )

        # Construct the prompt
        prompt = f"""
You are analyzing an incoherence signal in a traffic intersection control web.
The web is a three-node network representing interdependent traffic variables.

OBSERVED INCOHERENCE PATTERN (Step {snapshot.step}):
{pattern_description}

AFFECTED NODES:
{chr(10).join(node_descriptions)}

ALL INCOHERENCE SCORES:
{all_scores}

NETWORK TOPOLOGY:
{topology_description}

TASK:
Based on this incoherence signature, hypothesize what external force or
unmapped connection could explain why these specific nodes are showing
unexplained tension changes simultaneously.

Your response MUST include:
1. The hypothesized external source (e.g., "accident upstream", "stadium event", "measurement failure")
2. Which existing node(s) this source is likely coupled to (by node index)
3. Expected direction of coupling: does the source PUSH or RELIEVE tension at each node?
4. Your confidence [0-1] that this is a real unmapped connection
5. Brief rationale: why does this hypothesis explain the pattern?

Format your response as:
SOURCE: <human-readable description>
TARGET_NODE: <node index 0-2>
DIRECTION: <+1 for positive coupling, -1 for negative>
CONFIDENCE: <0.0-1.0>
RATIONALE: <explanation in 1-2 sentences>

Be specific and falsifiable. Vague proposals will be rejected.
"""
        return prompt

    def _call_claude(self, prompt: str) -> str:
        """
        Call Claude API with the investigation prompt.

        Uses claude-sonnet-4-20250514 (hardcoded per requirements).
        Implements basic error handling and retry logic.

        Returns the model's text response.
        """
        if self._claude_client is None:
            raise RuntimeError("Claude client not initialized")

        system_prompt = (
            "You are an expert in network analysis and control systems. "
            "You analyze patterns of tension/stress in interdependent systems "
            "to identify unmapped external influences. Be precise and logical."
        )

        try:
            message = self._claude_client.messages.create(
                model=self.config.claude_model,
                max_tokens=self.config.max_tokens_investigation,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            response_text = message.content[0].text
            logger.debug(f"Claude response: {response_text}")
            return response_text

        except Exception as e:
            logger.error(f"Claude API error: {e}")
            raise

    def _parse_claude_response(
        self,
        response: str,
        snapshot: CoherenceSnapshot,
        affected_nodes: list[int],
    ) -> list[StrandProposal]:
        """
        Parse Claude's response into StrandProposal objects.

        Expected format:
          SOURCE: <description>
          TARGET_NODE: <index>
          DIRECTION: <+1 or -1>
          CONFIDENCE: <float 0-1>
          RATIONALE: <text>

        Multiple proposals may be in the response (multiple stanzas).
        Returns a list of parsed StrandProposal objects.
        """
        proposals = []

        # Split response into proposal blocks (separated by blank lines or numbered)
        blocks = response.split("\n\n")

        for block in blocks:
            if not block.strip():
                continue

            try:
                proposal = self._parse_proposal_block(block, snapshot, affected_nodes)
                if proposal:
                    proposals.append(proposal)
            except ValueError as e:
                logger.warning(f"Failed to parse proposal block: {e}\nBlock: {block}")
                continue

        return proposals

    def _parse_proposal_block(
        self,
        block: str,
        snapshot: CoherenceSnapshot,
        affected_nodes: list[int],
    ) -> StrandProposal | None:
        """
        Parse a single proposal block into a StrandProposal.

        Expected format (case-insensitive, line order flexible):
          SOURCE: <description>
          TARGET_NODE: <index>
          DIRECTION: <+1 or -1>
          CONFIDENCE: <float>
          RATIONALE: <text>

        Returns StrandProposal or None if parsing fails.
        """
        lines = block.strip().split("\n")
        parsed = {}

        # Parse key-value pairs
        for line in lines:
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip().upper()
            value = value.strip()
            parsed[key] = value

        # Validate required fields
        required = {"SOURCE", "TARGET_NODE", "DIRECTION", "CONFIDENCE", "RATIONALE"}
        if not required.issubset(parsed.keys()):
            missing = required - set(parsed.keys())
            raise ValueError(f"Missing required fields: {missing}")

        # Parse values
        try:
            source = parsed["SOURCE"]
            target_node = int(parsed["TARGET_NODE"])
            direction = int(parsed["DIRECTION"])
            confidence = float(parsed["CONFIDENCE"])
            rationale = parsed["RATIONALE"]

            # Validate ranges
            if target_node not in [0, 1, 2]:
                raise ValueError(f"target_node must be 0-2, got {target_node}")
            if direction not in [-1, 1]:
                raise ValueError(f"direction must be +1 or -1, got {direction}")
            if not (0.0 <= confidence <= 1.0):
                raise ValueError(f"confidence must be in [0, 1], got {confidence}")
            if not source or not rationale:
                raise ValueError("source and rationale cannot be empty")

        except (ValueError, TypeError) as e:
            raise ValueError(f"Failed to parse values: {e}")

        # Create proposal
        self._proposal_counter += 1
        proposal = StrandProposal(
            proposal_id=f"prop_{self._proposal_counter}",
            step_generated=snapshot.step,
            hypothesized_source=source,
            target_node=target_node,
            expected_tension_direction=direction,
            confidence=confidence,
            rationale=rationale,
            affected_nodes=affected_nodes,
            claude_response=block,
        )

        return proposal

    def _passes_web_asking_gate(
        self,
        proposal: StrandProposal,
        snapshot: CoherenceSnapshot,
        affected_nodes: list[int],
    ) -> bool:
        """
        CRITICAL VALIDATION GATE: "Is the web asking for this strand?"

        This gate prevents the agent from imposing strands the web hasn't
        requested. It checks:
          1. Is the proposal SPECIFIC and FALSIFIABLE?
             (vague proposals like "maybe more sensors" are rejected)
          2. Does the target node actually show the incoherence?
             (proposal should connect to an affected node)
          3. Is the confidence reasonable?
             (very low confidence proposals are likely noise)
          4. Does the proposal avoid obvious repeats of prior failures?
             (same proposal, same nodes — probably a repeated false positive)

        Returns True if the proposal passes validation.
        Returns False if the proposal should be rejected.

        This is the most important check — it embodies the principle
        "interpret signals, don't impose structure."
        """

        # Gate 1: Proposal must be SPECIFIC
        # Vague sources like "unknown interference" are rejected.
        vague_terms = ["maybe", "possibly", "uncertain", "unknown", "unclear"]
        if any(term in proposal.hypothesized_source.lower() for term in vague_terms):
            logger.warning(
                f"Proposal {proposal.proposal_id} rejected: "
                f"hypothesized source '{proposal.hypothesized_source}' is too vague"
            )
            return False

        # Gate 2: Target node should be in affected_nodes
        # The web is asking for a connection because this node has unexplained tension.
        # If we propose a strand to a node that's NOT showing incoherence, we're
        # imposing structure not requested by the web.
        if proposal.target_node not in affected_nodes:
            logger.warning(
                f"Proposal {proposal.proposal_id} rejected: "
                f"target node {proposal.target_node} not in affected_nodes {affected_nodes}. "
                f"Web is not asking for a strand to this node."
            )
            return False

        # Gate 3: Confidence must be non-trivial
        # Proposals with confidence < 0.3 are likely just guesses.
        # The web's incoherence signal is asking for something substantial, not speculation.
        if proposal.confidence < 0.3:
            logger.warning(
                f"Proposal {proposal.proposal_id} rejected: "
                f"confidence {proposal.confidence:.2f} too low to be meaningful"
            )
            return False

        # Gate 4: Check for repeated proposals
        # If we already proposed the SAME connection (same source, same target)
        # at the same affected nodes in the recent past, it's likely a false positive.
        # Reject to avoid hammering the same hypothesis repeatedly.
        for prior_proposal in self._proposals[-5:]:  # Check last 5 proposals
            if (
                prior_proposal.hypothesized_source.lower()
                == proposal.hypothesized_source.lower()
                and prior_proposal.target_node == proposal.target_node
                and prior_proposal.affected_nodes == proposal.affected_nodes
            ):
                logger.warning(
                    f"Proposal {proposal.proposal_id} rejected: "
                    f"identical proposal {prior_proposal.proposal_id} already exists"
                )
                return False

        # All gates passed — the web is asking for this strand
        logger.info(
            f"Proposal {proposal.proposal_id} APPROVED via web-asking gate: "
            f"'{proposal.hypothesized_source}' → Node {proposal.target_node}, "
            f"confidence={proposal.confidence:.2f}"
        )
        return True

    # -----------------------------------------------------------------------
    # Proposal retrieval and state tracking
    # -----------------------------------------------------------------------

    def proposals(self) -> list[StrandProposal]:
        """Retrieve all stored proposals (immutable view)."""
        return list(self._proposals)

    def proposal_by_id(self, proposal_id: str) -> StrandProposal | None:
        """Retrieve a single proposal by ID."""
        for prop in self._proposals:
            if prop.proposal_id == proposal_id:
                return prop
        return None

    def proposals_by_status(self, status: ProposalStatus) -> list[StrandProposal]:
        """Retrieve all proposals with a given status."""
        return [prop for prop in self._proposals if prop.status == status]

    def update_proposal_status(
        self,
        proposal_id: str,
        new_status: ProposalStatus,
        step: int,
    ) -> bool:
        """
        Update the status of a proposal (called by the web validation layer).

        Returns True if update succeeded, False if proposal not found.
        """
        for prop in self._proposals:
            if prop.proposal_id == proposal_id:
                prop.status = new_status
                prop.status_updated_at_step = step
                logger.info(
                    f"Proposal {proposal_id} status updated to {new_status.value} "
                    f"at step {step}"
                )
                return True
        return False

    def mark_proposal_validated(
        self,
        proposal_id: str,
        coherence_delta: float,
        step: int,
    ) -> bool:
        """
        Mark a proposal as validated (both nodes show improved coherence).

        Called by the web after bidirectional validation completes.
        """
        for prop in self._proposals:
            if prop.proposal_id == proposal_id:
                prop.status = ProposalStatus.VALIDATED
                prop.coherence_delta = coherence_delta
                prop.status_updated_at_step = step
                logger.info(
                    f"Proposal {proposal_id} VALIDATED at step {step}, "
                    f"coherence_delta={coherence_delta:.3f}"
                )
                return True
        return False

    def mark_proposal_rejected(
        self,
        proposal_id: str,
        step: int,
    ) -> bool:
        """
        Mark a proposal as rejected (failed to improve coherence).
        """
        for prop in self._proposals:
            if prop.proposal_id == proposal_id:
                prop.status = ProposalStatus.REJECTED
                prop.status_updated_at_step = step
                logger.info(f"Proposal {proposal_id} REJECTED at step {step}")
                return True
        return False

    def statistics(self) -> dict:
        """Return summary statistics about proposals."""
        status_counts = {}
        for status in ProposalStatus:
            status_counts[status.value] = len(self.proposals_by_status(status))

        avg_confidence = (
            np.mean([p.confidence for p in self._proposals])
            if self._proposals
            else 0.0
        )

        return {
            "total_proposals": len(self._proposals),
            "by_status": status_counts,
            "avg_confidence": float(avg_confidence),
        }
