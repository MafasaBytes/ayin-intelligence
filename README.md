# Ayin Intelligence

Start Codex or Claude in this Git root and ask it to read this README. Ayin helps engineers understand systems, trace evidence to the components it describes, and preserve engineering and practitioner knowledge as systems change. It serves different kinds of engineered systems.

The first design discussion concerns the **Sources workbench**. An engineer should be able to find a source record, see what Ayin retained and what extraction produced, inspect the available evidence, and understand whether the evidence has an explicit link to a modeled component. Broader product and implementation decisions are open.

## Repository map

These locations and revisions were verified during setup. The four supporting directories are independent Git checkouts ignored by Ayin's Git repository.

| Repository | Verified location and revision | Role and editing boundary |
| --- | --- | --- |
| Ayin Intelligence | [This Git root](./), `main` at `7d67c74` when setup began | Shared frontend workspace. This setup covers the README and the supplied visual reference. |
| frontend-GOD | [frontend-GOD](frontend-GOD/), `main` at `73514fb` | Frontend design direction and UI review guidance. Read in place. |
| Impeccable | [impeccable](impeccable/), `main` at `b49177d32` | UI/UX shaping and critique guidance for both agents. Read in place. |
| Superpowers | [superpowers](superpowers/), `main` at `22f0b46` | Brainstorming and collaboration workflow guidance. Read in place. |
| Everything Claude Code | [everything-claude-code](everything-claude-code/), `main` at `432485b` | Claude-oriented frontend patterns and engineering guidance. Read in place. |
| Operation Housekeeping | [Backend Git repository](https://github.com/MafasaBytes/operation-house-keeping.git), [reviewed published revision `c2f8c01`](https://github.com/MafasaBytes/operation-house-keeping/tree/c2f8c01d6504df44cc07dbe2b90ab9671b5b0b7f) | Read-only backend reference for evidence ingestion, identity binding, model state, and bounded assessments. |

Setup inspected the existing temporary backend clone at `/tmp/ayin-backend-ref-5nxqom66i`, `main` at `c2f8c01d6504df44cc07dbe2b90ab9671b5b0b7f`. It has Git objects and no checked-out source files. Use the published revision link if the temporary clone expires. Start with the [source ingestion guide](https://github.com/MafasaBytes/operation-house-keeping/blob/c2f8c01d6504df44cc07dbe2b90ab9671b5b0b7f/backend/data_sources/README.md) and the [identity binding guide](https://github.com/MafasaBytes/operation-house-keeping/blob/c2f8c01d6504df44cc07dbe2b90ab9671b5b0b7f/backend/identity_binding/README.md).

## Local skill entry points

Both agents can read these files directly from the Ayin root. Resolve a skill's companion references from the directory containing its `SKILL.md`. Use the guidance relevant to the task the Product Owner has authorized. For a local, read-only design discussion, use Impeccable's written playbooks. Its launcher can download a runtime.

| Skill | Codex | Claude | Use in Ayin |
| --- | --- | --- | --- |
| Frontend Design Director | [Skill entry](frontend-GOD/skills/frontend-design-director/SKILL.md) | [Same file as a reference](frontend-GOD/skills/frontend-design-director/SKILL.md) | Compare visual hierarchy, interaction clarity, and accessible states. Its native packaging targets Codex. |
| Impeccable | [Codex entry](impeccable/.agents/skills/impeccable/SKILL.md) | [Claude entry](impeccable/.claude/skills/impeccable/SKILL.md) | Use the Operate guidance for an engineering workbench and the critique playbook when there are variants to review. |
| Superpowers | [Brainstorming](superpowers/skills/brainstorming/SKILL.md) | [Brainstorming](superpowers/skills/brainstorming/SKILL.md) | Surface meaningful design tradeoffs and confirm direction with the Product Owner. |
| Everything Claude Code | [Frontend patterns as a reference](everything-claude-code/skills/frontend-patterns/SKILL.md) | [Frontend patterns](everything-claude-code/skills/frontend-patterns/SKILL.md) and [coding standards](everything-claude-code/skills/coding-standards/SKILL.md) | Consult for UI composition and state handling when implementation is authorized and the patterns fit the chosen stack. |

All four supporting checkouts and the listed skill entries were present. The nested repositories, their Git histories, and their agent configurations belong to their respective projects.

### Browse the skill catalogs

- **Frontend Design Director** has one skill. Its [mode playbooks](frontend-GOD/skills/frontend-design-director/references/mode-playbooks.md) cover building, redesigning, reviewing, design systems, and UX debugging.
- **Impeccable** has one skill packaged for multiple agents. Use the Commands table in your agent's entry above to find the shaping, critique, accessibility audit, and refinement playbooks.
- **Superpowers** has [15 skill entries](superpowers/skills/). Use them for planning and execution, systematic debugging, test-driven development, code review, verification, Git worktree isolation, or skill authoring as the task calls for them.
- **Everything Claude Code** has [11 skill entries](everything-claude-code/skills/). Alongside frontend and coding patterns, it covers backend patterns, ClickHouse, security review, testing and evaluation, verification, context compaction, and learning from sessions.
- **Operation Housekeeping** has backend-owned Claude agent profiles. Keep Ayin's workflow in this README and use the backend checkout as a read-only reference. [Backend agent profiles at the reviewed revision](https://github.com/MafasaBytes/operation-house-keeping/tree/c2f8c01d6504df44cc07dbe2b90ab9671b5b0b7f/.claude/agents)

## Shared design comparison brief

Use the [workbench JPEG](references/operation_housekeeping_workbench_1795125708407.jpg) as the **partially approved visual reference**. The Product Owner has yet to specify which parts carry approval. The screenshot shows a source and assembly rail, a central preview, and an evidence inspector. Its status labels and actions are illustrative. Adviser sketches are discussion material.

### Common evidence

Use this same illustrative set in every variant unless the Product Owner supplies one retained read-only set to use across all variants. The IDs below are sample labels. Keep the record order, values, statuses, and starting selection (`S-01`) the same in each comparison.

| Source record | Raw retention | Extraction outcome | Component binding |
| --- | --- | --- | --- |
| `S-01` · Assembly BOM (CSV) | Retained as `R-01` | Succeeded. Row 12 describes a mounting bracket. | Explicit sample binding from row 12 to component `C-01`. |
| `S-02` · Assembly geometry (STEP) | Retained as `R-02` | Partial. An assembly occurrence for the mounting bracket is available. The 3D derivative is unavailable. | Unresolved. The similar label gives the engineer a lead, and an explicit binding decision is still needed. |
| `S-03` · Service manual (PDF) | Retained as `R-03` | Quarantined after a parse error. A diagnostic is available. | Unavailable. This record has no extracted item to inspect for binding. |
| `S-04` · Operational snapshot attempt | No raw payload captured | Extraction did not run after acquisition failed. | Unavailable for this attempt. |

### Common tasks

1. Find `S-01`, open the extracted BOM row, and identify its raw record, source locator, and linked component.
2. Open `S-02`. Find the available assembly evidence and explain the missing preview and unresolved binding.
3. Compare `S-03` and `S-04`. Identify which raw payload remains inspectable and where each attempt stopped.

Compare how easily an engineer can complete these tasks, trace the evidence, and distinguish the three statuses. Evaluate the variants at the same viewport and starting state. Use separate, readable status labels that remain understandable without color. Treat canonical component identity as an explicit decision, with unresolved candidates clearly shown. Sample and retained evidence are both read-only for the comparison.

## Milestone workflow

Use Superpowers to keep the plan and progress visible to both agents. This table records the current milestones. Once an implementation milestone has an agreed scope, link its plan here and track the implementation steps as checkboxes in that plan.

| Milestone | Completion evidence | Status |
| --- | --- | --- |
| Frontend workspace setup | README readback, verified local paths, and the project-local visual reference | Verified. |
| Sources design comparison | Variants evaluated against the shared records and tasks, with the Product Owner's decision recorded | Queued for the Product Owner's design session. |

1. Use [Brainstorming](superpowers/skills/brainstorming/SKILL.md) to agree on the milestone outcome and how to recognize completion. Use [Writing Plans](superpowers/skills/writing-plans/SKILL.md) for multi-step implementation after the design is agreed.
2. Update the plan as work progresses. At the milestone boundary, run the checks that demonstrate the agreed outcome and record their results using [Verification Before Completion](superpowers/skills/verification-before-completion/SKILL.md).
3. Make one local Git commit for each verified milestone that changes files, when local commits are authorized. Stage only the milestone's files and use a clear, scoped message. The [local Git workflow guide](everything-claude-code/rules/git-workflow.md) has commit message examples. GitHub publication is a separate step.

## Next session

When the Product Owner returns for the design comparison, start with this README, the linked JPEG, and the common evidence and tasks above. Confirm which visual elements carry approval and what form the variants should take. Bring in any adviser sketches the Product Owner wants discussed. No separate sketch file was located during setup. The sample set above is available if a retained dataset has yet to be selected.

Workspace setup ends with README readback. Variant creation is the next task. Frontend scaffolding, dependency installation, global agent configuration, live source connections, backend execution, and Git publication are outside this setup.
