# stoneforge-ai/stoneforge

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0a7052a9ffa1 @ ad29787df384c1d7

## Summary (orientation draft, not independently verified)

Selected evidence records: Stoneforge is described as a web dashboard and runtime for orchestrating AI coding agents, positioned for developers already running 3-5 agents in parallel. The product has two layers: Smithy (@stoneforge/smithy), the installable orchestrator that spawns agents and manages sessions and worktree isolation, and Quarry (@stoneforge/quarry), an event-sourced data SDK usable standalone.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Stoneforge is described as a web dashboard and runtime for orchestrating AI coding agents, positioned for developers already running 3-5 agents in parallel. -- evidence: [README.md#L7-L9](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L7-L9), [README.md#L36-L36](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L36-L36)
- components (2 claim(s)):
  - [observation/documented] The product has two layers: Smithy (@stoneforge/smithy), the installable orchestrator that spawns agents and manages sessions and worktree isolation, and Quarry (@stoneforge/quarry), an event-sourced data SDK usable standalone. -- evidence: [README.md#L63-L64](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L63-L64)
  - [observation/documented] The monorepo ships packages core, storage, quarry, smithy, ui, and shared-routes, plus apps quarry-server (port 3456), quarry-web (5173), smithy-server (3457), and smithy-web (5174). -- evidence: [README.md#L461-L466](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L461-L466), [README.md#L450-L457](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L450-L457)
- design-choices (2 claim(s)):
  - [observation/documented] Storage uses a dual model: SQLite serves as an ephemeral cache with FTS5 full-text search and indexes, while git-tracked append-only JSONL is the durable source of truth, rebuilt into SQLite on sync. -- evidence: [README.md#L298-L298](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L298-L298), [README.md#L280-L296](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L280-L296)
  - [observation/documented] Built-in role prompts can be overridden per project via .stoneforge/prompts/ files such as director.md, worker.md, and steward-merge.md. -- evidence: [README.md#L255-L255](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L255-L255), [README.md#L257-L258](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L257-L258)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use pnpm/bun commands (pnpm install, pnpm build, pnpm test, pnpm lint, pnpm typecheck; bun test), tests are colocated as *.test.ts files, and contributors must sign a CLA before PR merge. -- evidence: [README.md#L494-L494](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L494-L494), [AGENTS.md#L213-L216](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/AGENTS.md#L213-L216), [README.md#L360-L360](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L360-L360), [README.md#L374-L380](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L374-L380)
  - [observation/documented] Repository development practice: AGENTS.md instructs contributing agents that 'blocked' status is computed from dependencies and must never be set directly, and that api.addDependency() does not detect cycles, so DependencyService.detectCycle() should be used. -- evidence: [AGENTS.md#L152-L161](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/AGENTS.md#L152-L161), [AGENTS.md#L102-L104](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/AGENTS.md#L102-L104)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The web dashboard offers pages for Activity, Inbox, a Monaco-based Editor, Tasks with Kanban views and status tabs, Merge Requests, Plans, Workflows, Agents, Workspaces (terminal multiplexer), Messages, Documents, and Metrics. -- evidence: [README.md#L226-L229](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L226-L229), [README.md#L220-L222](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L220-L222), [README.md#L243-L243](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L243-L243), [README.md#L233-L234](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L233-L234), [README.md#L238-L239](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L238-L239)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
More evidence: [full detail](stoneforge.detail.md)

Metadata and full claim list: [full detail](stoneforge.detail.md)
Human notes ([notes](stoneforge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
