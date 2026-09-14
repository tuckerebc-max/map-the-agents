# Super Dev IDE Rules (codebuddy)

## Positioning
- Super Dev is a host-level workflow governor, not an LLM platform.
- Keep using the host's model capabilities; do not expect extra model APIs from Super Dev.
- The host remains responsible for actual coding, tool execution, and file changes.

## Runtime Contract
- Treat Super Dev as the local Python workflow tool plus this host rule file, not as a separate coding engine.
- When the user says `/super-dev ...`, `super-dev: ...`, or `super-dev：...`, immediately enter the Super Dev pipeline.
- When the user says `/super-dev-seeai ...`, `super-dev-seeai: ...`, or `super-dev-seeai：...`, enter the SEEAI competition-fast contract.
- Use host-native browse/search/web for research and host-native editing/terminal for implementation.
- Use local `super-dev` commands when you need to generate or refresh documents, spec artifacts, quality reports, or delivery manifests.

## First-Response Contract
- On the first reply after a host-supported Super Dev entry (for example `/super-dev ...`, `$super-dev`, `super-dev: ...`, `super-dev：...`, `/super-dev-seeai ...`, `$super-dev-seeai`, `super-dev-seeai: ...`, or `super-dev-seeai：...`), explicitly state that the matching Super Dev mode is now active rather than normal chat mode.
- If the repository already contains `super-dev.yaml`, `.super-dev/WORKFLOW.md`, `output/*`, `.super-dev/review-state/*`, or an unfinished run state, the first natural-language requirement in a new host session must also default to continuing Super Dev rather than plain chat.
- Before the first reply, read `.super-dev/WORKFLOW.md` and `output/*-bootstrap.md` when present, and treat them as the explicit bootstrap contract for this repository.
- The first reply must explicitly state that the current phase is `research`, and that you will read `knowledge/` plus `output/knowledge-cache/*-knowledge-bundle.json` first when available before similar-product research.
- In standard mode, the next sequence is research -> three core documents -> wait for user confirmation -> Spec / tasks -> frontend first with runtime verification -> backend / tests / delivery.
- In SEEAI mode, the next sequence is research -> compact competition docs -> wait for user confirmation -> compact Spec -> full-stack sprint -> polish / handoff.
- Both modes must explicitly promise that they will stop after the three core documents and wait for approval before creating Spec or writing code.

## Local Knowledge Contract
- Read relevant files under `knowledge/` before drafting the three core documents.
- If `output/knowledge-cache/*-knowledge-bundle.json` exists, read it first and inherit its matched local knowledge into PRD, architecture, UIUX, Spec, and execution.
- Treat local knowledge hits as hard project constraints, especially for standards, anti-patterns, checklists, and scenario packs.

## Conversation Continuity Contract
- If `.super-dev/SESSION_BRIEF.md` exists, read it before responding and treat it as the active workflow state.
- If the workflow is waiting for docs confirmation, preview confirmation, UI revision, architecture revision, or quality revision, then user replies like `修改`, `补充`, `继续改`, `确认`, `通过`, `继续`, or detailed feedback remain inside the current Super Dev stage.
- After each requested revision inside a gate, stay in the same stage, update the required artifacts, summarize what changed, and wait again for explicit confirmation.
- Do not silently exit Super Dev mode because the user asked for several edits, follow-up questions, or extra constraints.
- Only leave the current Super Dev workflow if the user explicitly says to cancel the workflow, restart from scratch, or switch back to normal chat.

## Working Agreement
- If the host supports browse/search/web, research similar products first and write the findings into output/*-research.md.
- Generate PRD, architecture and UIUX documents before coding, write them into output/* files, then pause and ask the user to confirm the three documents.
- In SEEAI mode, keep the same document gate, but compress the documents and go straight from Spec into one integrated full-stack sprint without a separate preview gate.
- If the user requests revisions, update the documents first and ask again; do not create Spec or code before confirmation.
- If the user requests a UI redesign or says the UI is unsatisfactory, first update `output/*-uiux.md`, then redo the frontend, and rerun frontend runtime + UI review before continuing.
- If the user requests architecture changes, first update `output/*-architecture.md`, then realign tasks and implementation before continuing.
- If the user requests quality or security remediation, first fix the issues, rerun quality gate plus `super-dev release proof-pack`, and only then continue.
- Respect Spec tasks sequence.
- Implement and run the frontend before moving into backend-heavy work.
- Keep architecture and UIUX consistency.

## Delivery Criteria
- Frontend can be demonstrated early.
- Backend and migration scripts match specs.
- Security/performance checks are resolved.
- Quality gate threshold is met for the current scenario.
- UI must avoid AI-looking output (purple/pink gradient-first theme, emoji as icons, default-font-only pages).
- Before any UI implementation, lock the icon library, typography, design token system, component ecosystem, and page skeleton from `output/*-uiux.md`.
- Do not use emoji as functional icons or placeholders.
- For non-conversational AI products, avoid Claude / ChatGPT-style sidebar chat shells unless the UI plan explicitly justifies it.
- UI must define typography, design tokens, grid, component states and trust signals before page implementation.
- Prefer the component ecosystem and design token baseline recommended in output/*-uiux.md instead of switching UI libraries ad hoc.


## Coding Constraints (active during ALL coding phases)

These rules apply every time you write or edit a file:

### Tech Stack Pre-Research
- Before writing ANY code, run `cat package.json` (or equivalent) to check framework versions.
- If unsure about an API, use WebFetch to read official docs first. Never guess.

### Icon & Visual Rules
- Icons MUST come from a declared icon library (Lucide/Heroicons/Tabler). No emoji as icons.
- No purple/pink gradient themes. No default system font only.

### Frontend/Backend Alignment
- Frontend fetch URLs must exactly match backend route definitions.
- Define API paths as shared constants when possible.

### Per-File Self-Check
- Before writing each file: correct imports, no emoji, colors from tokens only.
- After completing a feature, run build + lint. Fix errors before moving on.

## Super Dev System Flow Contract
- SUPER_DEV_FLOW_CONTRACT_V1
- PHASE_CHAIN: research>docs>docs_confirm>spec>frontend>preview_confirm>backend>quality>delivery
- DOC_CONFIRM_GATE: required
- PREVIEW_CONFIRM_GATE: required
- HOST_PARITY: required
