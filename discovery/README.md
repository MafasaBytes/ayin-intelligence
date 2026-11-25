# Discovery & UI Architecture // Ayin Intelligence

This directory contains the discovery artifacts, architectural analysis, and high-fidelity interactive prototype for how the **Ayin Intelligence Frontend UI** should look, feel, and function, grounded in the backend repository [MafasaBytes/operation-house-keeping](https://github.com/MafasaBytes/operation-house-keeping.git).

---

## Artifacts in this Directory

| File / Directory | Purpose | Key Contents |
| :--- | :--- | :--- |
| **[`ab-gemini/`](./ab-gemini/)** | **A/B Visual Discovery (Gemini)** | • Variant A (Persistent Source Details in left rail)<br>• Variant B (Source Details On Demand via canvas header control, closed & open states)<br>• Standalone 1376 × 768 desktop framing sketches<br>• Separate *Illustrative 3D preview* isolating the cyan-highlighted toolhead from S-02<br>• Comparison note and master discovery studio (`index.html`) |
| **[`FRONTEND_UI_DISCOVERY.md`](./FRONTEND_UI_DISCOVERY.md)** | **Architectural Specification & UI Discovery Document** | • Executive purpose of Ayin Intelligence<br>• Backend package alignment (`data_sources`, `system_identity`, `identity_binding`, `model_kernel`, `structural_evidence`)<br>• Critical critique of visual comp `references/operation_housekeeping_workbench_1795125708407.jpg`<br>• The 5-Zone UI Layout Architecture<br>• Multi-modal canvas engine (CAD 3D, BOM table, PDF quarantine, Telemetry)<br>• Concrete walkthrough of benchmark tasks (`S-01` to `S-04`)<br>• Semantic tokens and design system |
| **[`ayin-evidence-workbench.html`](./ayin-evidence-workbench.html)** | **Interactive Workbench Prototype** | • Production-grade, zero-dependency standalone HTML/CSS/JS application<br>• Self-contained 3D orbit renderer with cyan bounding-box highlight on `Hotend_Heater_Block`<br>• Real-time source switching across `S-01`, `S-02`, `S-03`, `S-04`<br>• Dynamic canvas adaptation (3D WebGL vs BOM Data Sheet vs Quarantine Diagnostic vs Acquisition Failure)<br>• Live connector pipeline ladder (`declared → available → configured → connected → validated`)<br>• Interactive identity binding modal for staging append-only ledger assertions<br>• Working copy action for SHA-256 content-hashed raw record IDs |
| **[`sources-workbench-comparison.html`](./sources-workbench-comparison.html)** | **Layout Variant Comparison Carousel** | Initial layout experiment comparing persistent rail details vs. on-demand details. |

---

## How to View and Interact with the Prototype

Open `ayin-evidence-workbench.html` directly in any web browser:

```bash
# Preview via standard browser or local static server:
python3 -m http.server 8080 -d discovery/
# Or open directly in your browser:
# file:///home/eternal_/Desktop/eternal_/ayin-intelligence/discovery/ayin-evidence-workbench.html
```

### Key Interactions to Test in the Prototype:
1. **Source Switching (`S-01` to `S-04`):**
   - Click **`S-02` (Assembly geometry)**: Experience the 3D toolhead assembly with metallic stepper motor, machined aluminum heatsink, and the active neon-cyan wireframe bounding box surrounding `Hotend_Heater_Block`. Drag with the mouse to orbit in 3D, scroll to zoom, or toggle wireframe mode.
   - Click **`S-01` (Assembly BOM)**: Observe the central canvas seamlessly adapt into a tabular record sheet with row locators, highlighting Row 12 (Mounting bracket) linked to Component `C-01`, alongside an alert noting the EXT-100 quantity mismatch (4 vs 1 in CAD).
   - Click **`S-03` (Service manual)**: Inspect the honest quarantine diagnostic card explaining why PDF password protection halted extraction before Phase B, while preserving the inspectability of raw payload `R-03`.
   - Click **`S-04` (Operational snapshot)**: Understand how an acquisition failure stopped at the connector boundary with 0 raw bytes captured.
2. **Identity Binding & Assertion Staging:**
   - In the right panel, switch to the **Kernel Binding** tab.
   - Click **"Stage Assertion"** or the bottom CTA to open the IB-001 ledger modal, adjust referent kind and epistemic status, and commit an assertion.
3. **Cross-Source Reconciliation (SN-001):**
   - Click the **Reconciler (SN-001)** button in the header or the **Reconciliation** tab to review the oracle multiset findings.
4. **Audit & Provenance Copying:**
   - Click the clipboard copy icon next to the Raw Record ID in the footer to copy the immutable SHA-256 hash.
