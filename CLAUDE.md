# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ayin Intelligence is a closed-loop perception-response system architected as a tensioned web. Interdependent nodes represent functional entities within a domain. Perturbations propagate across the web as shockwaves through tensioned strands. The web's natural redistribution toward equilibrium constitutes both the perception AND the response — no external optimization or decision layer exists.

This is a solo engineering project. Prioritize clarity, debuggability, and single-engineer readability.

## Commands

```bash
# Run the API server
uvicorn ayin.api:app --reload

# Run the simulator (pushes synthetic data to the API)
python -m ayin.simulator

# Run tests (validate physics properties, not code paths)
pytest

# Type checking
mypy ayin/
```

## Tech Stack

- Python 3.12+, NumPy (core)
- FastAPI + uvicorn, websockets (API/streaming)
- Single HTML file, vanilla JS, websocket client (visualization)
- Anthropic Claude API with claude-sonnet-4-20250514 (Phase 2 strand discovery only)
- **Explicitly banned:** Kafka, Spark, Databricks, TensorFlow, PyTorch, React, graph databases, microservices

## Architecture

```
ayin/
    web.py          — Tension matrix (NumPy), propagation physics, equilibrium seeking
    nodes.py        — Node state representation, tension measurement
    coherence.py    — Recovery dynamics tracking, incoherence detection
    simulator.py    — Synthetic data generation, perturbation injection
    api.py          — FastAPI ingestion + websocket state broadcasting
    strand_agent.py — LLM-powered strand discovery (Phase 2 only)
    static/
        visualize.html  — Single-page real-time web state visualization
```

**Tension substrate:** Web state is a symmetric NumPy tension matrix. Nodes are vertices, strands are edges with continuous tension values representing absorptive capacity.

**Propagation engine:** Perturbations distribute to adjacent nodes proportional to strand tension with damping. Follows diffusion-inspired dynamics from WSN distributed detection models. Core loop: read signals → update nodes → propagate tension → measure recovery → detect incoherence → broadcast state.

**Coherence monitor:** Embedded in the propagation loop (not a separate service). Tracks recovery time, damping ratio, residual tension, and unexplained tension (incoherence). Incoherence = tension at a node with no correlated change at adjacent nodes through mapped strands.

**Strand discovery (Phase 2):** Triggered by incoherence detection, not scheduled. Uses Claude API to propose candidate strands. New strands integrate through: probationary → bidirectional validation → gradual load bearing. Failed strands go slack (never deleted).

## POC Domain: Traffic Intersection (Three-Node Triangle)

- **Node 1:** Intersection Throughput — vehicles/cycle, queue depth, clearance rate
- **Node 2:** Signal Timing — phase allocation, green time distribution
- **Node 3:** Approaching Traffic — vehicle density on each approach, upstream measurement
- **Three bidirectional strands** connecting all pairs

**POC must prove:** (1) Self-redistribution without external optimization, (2) Recovery dynamics reveal coherence decay before individual nodes show abnormal values, (3) Unexplained tension reliably signals unmapped strands.

## Core Principles — Non-Negotiable

1. **The web IS the intelligence.** Never build a separate decision/optimization layer. If the web can't produce the correct response through tension redistribution, the propagation physics are wrong — fix those.
2. **Perception and response are the same motion.** The shockwave that reveals the disturbance simultaneously redistributes tension to absorb it. Not two steps.
3. **Normalcy is not static.** Normal = capacity to absorb perturbations and recover. Measure recovery dynamics, not fixed thresholds.
4. **Incoherence is signal, not noise.** Unexplained tension = unmapped external force. Never suppress it.
5. **No ML in the perception loop.** Hand-written physics only. LLM used solely in strand discovery agent.
6. **Bidirectional strands only.** Unidirectional connections belong in monitoring, not the web.

## Code Style

- Variable names map to domain vocabulary: `tension`, `strand`, `node`, `perturbation`, `propagation`, `damping`, `coherence`, `incoherence`, `recovery_time`, `equilibrium`
- Comments explain WHY, not WHAT. Code should read as physics.
- No abstraction for abstraction's sake. If a function is called once and clear inline, keep it inline.
- Type hints everywhere.
- Tests validate physics properties ("does perturbation distribute proportionally to strand tensions?"), not code paths.

## Specialized Agents

Four specialized agents are configured in `.claude/agents/`:
- **tension-propagation-architect** (Opus) — Physics design in web.py, nodes.py, coherence.py. Propagation equations, equilibrium, recovery dynamics, incoherence detection.
- **traffic-simulator** (Sonnet) — Synthetic data in simulator.py. Baseline traffic, perturbation scenarios, stress testing.
- **nerve** (Sonnet) — Live integration in api.py and static/visualize.html. FastAPI endpoints, websocket streaming, real-time visualization.
- **strand-scout** (Haiku) — Strand discovery in strand_agent.py. Phase 2 only, after POC validation.

## Research References

- WSN distributed detection and diffusion models
- Continuous-time dynamical systems for equilibrium-seeking
- Field theory concepts for tension representation
- Spider web structural mechanics for redistribution under load
