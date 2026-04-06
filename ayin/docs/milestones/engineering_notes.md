## Larry Notes

The architecture is seems to be working, the physics is sustained.

● The stadium scenario ran end-to-end. Here are the key results:

  Incoherence Detection — It Works

  The coherence monitor fires at step 51 — one step after the first surge injection. All three nodes score 1.000 incoherence simultaneously. This is a sharp point event (the accident
  scenario produced 21 events across many steps because successive negative perturbations kept re-triggering).

  The Unmapped Signature

  The core pattern: N2 positive, N1 negative, N0 near zero — simultaneously. Under Laplacian diffusion, a positive N2 perturbation should propagate as positive tension to all neighbors.
  Seeing N1 go negative at the same moment is only possible if an independent external force is acting on N1 (the controller running the wrong timing plan). The coherence monitor catches
  this as positive correlation where anti-correlation was expected → incoherence score near 1.0.

  Comparison with Accident Scenario

  ┌───────────────────────────┬───────────────────────────┬─────────────────────────────────┐
  │          Metric           │         Accident          │             Stadium             │
  ├───────────────────────────┼───────────────────────────┼─────────────────────────────────┤
  │ Peak energy               │ 1.834                     │ 1.954                           │
  ├───────────────────────────┼───────────────────────────┼─────────────────────────────────┤
  │ Recovery steps            │ ~276                      │ 503                             │
  ├───────────────────────────┼───────────────────────────┼─────────────────────────────────┤
  │ Incoherence events        │ 21 (sustained)            │ 1 (sharp)                       │
  ├───────────────────────────┼───────────────────────────┼─────────────────────────────────┤
  │ Damping ratio (empirical) │ 0.087                     │ 0.087                           │
  ├───────────────────────────┼───────────────────────────┼─────────────────────────────────┤
  │ Signature                 │ Single-node capacity drop │ Multi-node contradictory motion │
  └───────────────────────────┴───────────────────────────┴─────────────────────────────────┘

  Key Insight

  The stadium shock produces a qualitatively different incoherence signature — contradictory motion across nodes that can't be explained by any propagation model using only the three
  mapped strands. This is exactly what Phase 2's strand discovery agent would investigate.

  The full entry is appended to ayin/docs/logbook.md. The run script is at run_stadium_shock.py if you want to re-run with different parameters.