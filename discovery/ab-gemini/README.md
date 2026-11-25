# Sources Workbench A/B Visual Discovery (Gemini)

This directory contains the static A/B design sketches and comparative analysis for the **Ayin Intelligence Sources workbench**, framed at **1376 × 768 desktop viewport**.

This milestone is strictly visual discovery. Work is paused here for **Product Owner Review** before designing application flows or implementing backend integrations.

---

## Deliverables Index

| File | Purpose | Key Details |
| :--- | :--- | :--- |
| **[`COMPARISON_NOTE.md`](./COMPARISON_NOTE.md)** | **Product Owner Comparison Note** | Full evaluation of Variant A vs Variant B against review tasks 1, 2, 3, trade-offs, and state breakdown. |
| **[`index.html`](./index.html)** | **Master Visual Discovery Studio** | Interactive presentation viewer enabling 1-click toggling between Variant A, Variant B (Closed), Variant B (Open), and states `S-01`, `S-02`, `S-03`, `S-04`, and `Illustrative 3D preview`. |
| **[`variant-a.html`](./variant-a.html)** | **Static Variant A (1376 × 768)** | Starts at `S-01`. Shows persistent source details (retention & extraction summary) in the left rail. |
| **[`variant-b.html`](./variant-b.html)** | **Static Variant B (Closed, 1376 × 768)** | Starts at `S-01`. Places the source details summary behind a labeled `Source details ▾` control beside the canvas heading. Preserves full left rail height for the hierarchy tree. |
| **[`variant-b-open.html`](./variant-b-open.html)** | **Static Variant B (Open, 1376 × 768)** | Starts at `S-01`. Shows the static open detail view with an anchored popover dropdown revealing retention and extraction facts. |
| **[`illustrative-3d-preview.html`](./illustrative-3d-preview.html)** | **Illustrative 3D Preview (1376 × 768)** | Dedicated view demonstrating the approved visual direction (cyan-highlighted toolhead assembly) kept strictly separate from `S-02` evidence (where 3D derivative is unavailable). |

---

## How to Review

Preview the screens directly in your browser:

```bash
# Serve locally:
python3 -m http.server 8080 -d discovery/ab-gemini/
# Open in browser:
# http://localhost:8080/index.html
```

Or open the standalone files directly:
- `file:///home/eternal_/Desktop/eternal_/ayin-intelligence/discovery/ab-gemini/index.html`
- `file:///home/eternal_/Desktop/eternal_/ayin-intelligence/discovery/ab-gemini/variant-a.html`
- `file:///home/eternal_/Desktop/eternal_/ayin-intelligence/discovery/ab-gemini/variant-b.html`
- `file:///home/eternal_/Desktop/eternal_/ayin-intelligence/discovery/ab-gemini/variant-b-open.html`
- `file:///home/eternal_/Desktop/eternal_/ayin-intelligence/discovery/ab-gemini/illustrative-3d-preview.html`

---

## The Single A/B Difference

Both variants carry forward the approved visual composition from `discovery/ayin-evidence-workbench.html` and `references/operation_housekeeping_workbench_1795125708407.jpg` (compact context header, source and assembly rail, dominant central canvas, evidence inspector, provenance footer, and graphite-and-cyan palette).

- **Variant A — Persistent source details:** Retention (`Retained as R-01`) and extraction outcome (`Succeeded. Row 12 describes a mounting bracket.`) are permanently displayed in the left rail below the source list.
- **Variant B — Source details on demand:** The same summary is tucked behind a labeled `Source details ▾` control beside the canvas heading, freeing up vertical rail space for large mechanical and BOM trees. Includes a static open state showing the anchored popover.

---

## State Handling Across Benchmark Records

All screens use the agreed wording, IDs, and statuses from root `README.md`:

1. **`S-01` · Assembly BOM (CSV):** Retained as `R-01`, extraction succeeded. Row 12 describes mounting bracket with locator `CSV · Row 12` linked to component `C-01` (`Bound`).
2. **`S-02` · Assembly geometry (STEP):** Retained as `R-02`, partial extraction. Assembly occurrence for mounting bracket is present; 3D derivative is unavailable. Binding is `Unresolved`.
3. **`S-03` · Service manual (PDF):** Retained as `R-03`, quarantined after parse error. Diagnostic available. Raw payload remains inspectable. Binding is `Unavailable`.
4. **`S-04` · Operational snapshot attempt:** No raw payload captured. Extraction did not run after acquisition failed. Binding is `Unavailable`.
5. **Illustrative 3D preview:** Shows the toolhead with neon cyan bounding box on `Hotend_Heater_Block` as a separate illustrative view to demonstrate approved rendering without fabricating 3D data for `S-02`.
