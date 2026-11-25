# Ayin Intelligence — Sources Workbench A/B Comparison Note

> **Document Type:** Visual Discovery & Design Variant Comparison  
> **Status:** Prepared for Product Owner Review (Application implementation & backend execution paused)  
> **Framing:** Exact 1376 × 768 Desktop Viewport  
> **Visual Reference Baseline:** `references/operation_housekeeping_workbench_1795125708407.jpg`  
> **Approved Composition Reference:** `discovery/ayin-evidence-workbench.html`  
> **Evidence Oracle:** Root `README.md` sample records (`S-01` through `S-04`) and common review tasks

---

## 1. The Single A/B Difference

In strict accordance with the visual discovery brief, both variants share the exact same **1376 × 768 desktop framing**, typography, graphite-and-cyan palette, record ordering, wording, provenance footer, and starting selection (`S-01`).

They differ in **exactly one architectural variable**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE SINGLE A/B VARIABLE                                   │
├────────────────────────────────────────┬───────────────────────────────────────────────┤
│ VARIANT A: Persistent Source Details   │ VARIANT B: Source Details On Demand           │
├────────────────────────────────────────┼───────────────────────────────────────────────┤
│ • Placement: Left navigation rail,     │ • Placement: Beside the "Evidence canvas"     │
│   directly underneath the source list. │   heading via a labeled dropdown control.     │
│ • State: Always visible and persistent.│ • State: Compact by default; reveals an       │
│ • Trade-off: Maximum immediate scan-   │   anchored popover overlay upon engagement.   │
│   ability; consumes vertical rail space│ • Trade-off: Maximizes left rail height for   │
│   from the assembly hierarchy tree.    │   deep assembly trees; keeps canvas uncluttered│
└────────────────────────────────────────┴───────────────────────────────────────────────┘
```

---

## 2. Variant Evaluation Across Common Review Tasks

Both variants were evaluated against the three benchmark tasks defined in `README.md`:

### Task 1: Find `S-01`, open the extracted BOM row, and identify raw record, locator, and linked component
- **Variant A (Persistent):** The engineer immediately sees `Raw retention: Retained as R-01` in the left rail while simultaneously scanning the BOM table in the canvas. Clicking Row 12 exposes locator `CSV · Row 12` in the canvas, while the right inspector displays Component `C-01` with status `Bound`. Retention and extraction remain in constant peripheral view.
- **Variant B (On Demand):** The engineer scans the BOM table and opens Row 12 in the canvas. To verify retention, the engineer clicks `Source details ▾` in the canvas header, revealing the anchored popover (`Retained as R-01`, `Succeeded`). While requiring one click, the left rail preserves full vertical height for large BOM containment trees.

### Task 2: Open `S-02`. Find available assembly evidence and explain missing preview and unresolved binding
- **Both Variants:**
  - **Honest Evidence Presentation:** `S-02` shows the assembly occurrence (`Mounting bracket` under `Toolhead_Mount`) and an explicit notice: `The 3D derivative is unavailable.`
  - **Unresolved Binding:** The right inspector displays status `Unresolved` (amber badge) with the exact prompt copy: *"The similar label gives the engineer a lead, and an explicit binding decision is still needed."*
  - **Illustrative 3D Preview Isolation:** In compliance with the discovery prompt, the 3D toolhead assembly is **not** conflated with `S-02` evidence. It is housed in a separate dedicated view labeled **`Illustrative 3D preview`** demonstrating the approved visual direction without fabricating 3D data for `S-02`.

### Task 3: Compare `S-03` and `S-04` — raw payload inspectability and failure boundaries
- **`S-03` (Service manual, PDF):**
  - Extraction: `Quarantined after a parse error. A diagnostic is available.`
  - Raw retention: `Retained as R-03` (inspectable raw payload preserved in write-once store).
  - Binding: `Unavailable. This record has no extracted item to inspect for binding.`
- **`S-04` (Operational snapshot attempt):**
  - Raw retention: `No raw payload captured`.
  - Extraction: `Extraction did not run after acquisition failed.`
  - Binding: `Unavailable for this attempt.`
- **Comparison Insight:** Both variants clearly distinguish between a parse failure *after* raw capture (`S-03`) versus an acquisition failure *before* raw capture (`S-04`). In Variant A, this is immediately visible in the persistent left panel; in Variant B, it is inspected via the canvas detail toggle.

---

## 3. Trade-Off Analysis for Product Owner Decision

| Dimension | Variant A: Persistent Source Details | Variant B: Source Details On Demand |
| :--- | :--- | :--- |
| **Cognitive Load on Selection** | Low (everything is visible simultaneously). | Lowest visual noise; canvas leads first. |
| **Vertical Rail Space** | Consumes ~140px of left rail height, compressing the assembly/occurrence tree. | Preserves 100% of left rail height for deep assembly hierarchies (XCAF Part 21 / BOM). |
| **Frequency of Use** | Best if engineers constantly check retention IDs on every click. | Best if engineers primarily inspect evidence content and only occasionally audit retention metadata. |
| **Mobile & Responsive Scaling** | Stacks vertically; requires scrolling on smaller screens. | Naturally collapses into an accessible popover or modal. |

---

## 4. Deliverables Manifest in `discovery/ab-gemini/`

1. **[`index.html`](./index.html)** — Interactive Master A/B Studio (allows side-by-side comparison, switching between A, B-closed, B-open, S-01 through S-04, and the Illustrative 3D Preview at 1376 × 768).
2. **[`variant-a.html`](./variant-a.html)** — Standalone static screen: Variant A starting at `S-01` (Persistent Left Rail Details).
3. **[`variant-b.html`](./variant-b.html)** — Standalone static screen: Variant B starting at `S-01` (Details On Demand, Closed State).
4. **[`variant-b-open.html`](./variant-b-open.html)** — Standalone static screen: Variant B starting at `S-01` (Details On Demand, Open Popover State).
5. **[`illustrative-3d-preview.html`](./illustrative-3d-preview.html)** — Dedicated view labeled *Illustrative 3D preview* showing the cyan-highlighted toolhead assembly.
6. **[`README.md`](./README.md)** — Navigation and review guide for the Product Owner.

---

## 5. Next Steps

Work is paused here for **Product Owner Review**. Once the Product Owner confirms whether Variant A or Variant B carries approval for source details, we will proceed with the detailed application flow and interaction specification.
