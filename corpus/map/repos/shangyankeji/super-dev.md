# shangyankeji/super-dev

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d06e640153bd @ 352741a68f351de0

## Summary (orientation draft, not independently verified)

Selected evidence records: The terminal CLI is scoped to onboarding, updating, and uninstalling: `super-dev`, `super-dev update`, and `super-dev uninstall`, with `super-dev uninstall --dry-run` offered as a preview of what would be deleted. After onboarding, hosts trigger the pipeline via `/super-dev <request>`, `super-dev: <request>`, or a competition fast mode `/super-dev-seeai`, with the exact trigger varying by host (e.g. Codex CLI uses `$super-dev`).

## Source coverage

Source coverage (partial): 6 of 29 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The document engine generates initial frameworks for PRD, Architecture, and UIUX documents (covering user personas, data models, design tokens, etc.), which the host model then deepens using user requirements, web research, and expert knowledge. -- evidence: [README.md#L276-L276](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L276-L276), [README.md#L278-L282](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L278-L282), [README.md#L284-L284](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L284-L284)
- components (2 claim(s)):
  - [observation/documented] Eleven built-in domain expert agents (PRODUCT, PM, ARCHITECT, UI, UX, SECURITY, CODE, DBA, QA, DEVOPS, RCA) are injected into host prompts at specific pipeline stages, each with Profile, Knowledge, Rules, and Protocol layers. -- evidence: [README.md#L228-L228](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L228-L228), [README.md#L214-L226](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L214-L226), [README.md#L212-L212](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L212-L212)
  - [observation/documented] A built-in knowledge base under `knowledge/` is described as 270+ files across 23 domains, with staged loading (L1 index / L2 detail / L3 deep reference) under token budgeting and SQLite-tracked usage for data-driven weight optimization. -- evidence: [README.md#L337-L337](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L337-L337), [README.md#L350-L356](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L350-L356)
- design-choices (3 claim(s)):
  - [observation/documented] UI/UX decisions are frozen into contract artifacts (`output/*-ui-contract.json`, `design-tokens.css`, alignment reports) that host prompts, UI review, quality gates, proof-pack, and release readiness must stay consistent with. -- evidence: [README.md#L243-L247](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L243-L247), [README.md#L241-L241](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L241-L241), [README.md#L249-L249](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L249-L249)
  - [observation/documented] Quality governance uses 25 declarative YAML validation rules (14 default plus 11 red-team) with project-level custom overrides, plus default/balanced/enterprise policy presets. -- evidence: [README.md#L294-L304](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L294-L304)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The terminal CLI is scoped to onboarding, updating, and uninstalling: `super-dev`, `super-dev update`, and `super-dev uninstall`, with `super-dev uninstall --dry-run` offered as a preview of what would be deleted. -- evidence: [README.md#L129-L131](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L129-L131), [README.md#L180-L186](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L180-L186), [README.md#L172-L176](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L172-L176)
  - [observation/documented] After onboarding, hosts trigger the pipeline via `/super-dev <request>`, `super-dev: <request>`, or a competition fast mode `/super-dev-seeai`, with the exact trigger varying by host (e.g. Codex CLI uses `$super-dev`). -- evidence: [README.md#L416-L419](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L416-L419), [README.md#L135-L139](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L135-L139), [README.md#L577-L590](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L577-L590)
- memory-state (1 claim(s)):
  - [observation/documented] Session continuity is persisted in `.super-dev/SESSION_BRIEF.md` and `.super-dev/workflow-state.json` (current action, host first-sentence, machine-side actions, continuity rules), and recovery from `.super-dev/` and `output/` artifacts is the default scenario after interruption. -- evidence: [README.md#L145-L151](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L145-L151), [README.md#L261-L272](https://github.com/shangyankeji/super-dev/blob/d06e640153bd83fc63ef716e1149cf2b2bbf02ed/README.md#L261-L272)
- orchestration (2 claim(s)):
More evidence: [full detail](super-dev.detail.md)

Metadata and full claim list: [full detail](super-dev.detail.md)
Human notes ([notes](super-dev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
