# stoneforge-ai/stoneforge -- full detail

[Back to orientation](stoneforge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stoneforge-ai/stoneforge/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/ad29787df384c1d7.json](../../../wiki/dossiers/stoneforge-ai/stoneforge/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/ad29787df384c1d7.json)

## specifications (1 claim(s))

- [observation/documented] Stoneforge is described as a web dashboard and runtime for orchestrating AI coding agents, positioned for developers already running 3-5 agents in parallel. -- evidence: [README.md#L7-L9](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L7-L9), [README.md#L36-L36](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L36-L36) (`clm_ddfbd4100a876f12270c3055b39781e6b24d89358bbd588fd2cbc745d2654861`)

## components (2 claim(s))

- [observation/documented] The product has two layers: Smithy (@stoneforge/smithy), the installable orchestrator that spawns agents and manages sessions and worktree isolation, and Quarry (@stoneforge/quarry), an event-sourced data SDK usable standalone. -- evidence: [README.md#L63-L64](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L63-L64) (`clm_125e6c956836aeae5d6945b60ac9b51680ce49f13f182fa4b78058e7adcbf20f`)
- [observation/documented] The monorepo ships packages core, storage, quarry, smithy, ui, and shared-routes, plus apps quarry-server (port 3456), quarry-web (5173), smithy-server (3457), and smithy-web (5174). -- evidence: [README.md#L461-L466](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L461-L466), [README.md#L450-L457](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L450-L457) (`clm_281e75c677be867fea42ae3a06df879445c059e55c95c4ecb1acf166bc175f27`)

## design-choices (2 claim(s))

- [observation/documented] Storage uses a dual model: SQLite serves as an ephemeral cache with FTS5 full-text search and indexes, while git-tracked append-only JSONL is the durable source of truth, rebuilt into SQLite on sync. -- evidence: [README.md#L298-L298](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L298-L298), [README.md#L280-L296](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L280-L296) (`clm_b678268bb6752e6f5e8045026ce3c21efa6fd8b13f5ca6275bce2261a614c11f`)
- [observation/documented] Built-in role prompts can be overridden per project via .stoneforge/prompts/ files such as director.md, worker.md, and steward-merge.md. -- evidence: [README.md#L255-L255](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L255-L255), [README.md#L257-L258](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L257-L258) (`clm_39bea180497cf7073bc8827e3689cd8bdf12a1874fcecad99635f7f520ebc521`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use pnpm/bun commands (pnpm install, pnpm build, pnpm test, pnpm lint, pnpm typecheck; bun test), tests are colocated as *.test.ts files, and contributors must sign a CLA before PR merge. -- evidence: [README.md#L494-L494](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L494-L494), [AGENTS.md#L213-L216](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/AGENTS.md#L213-L216), [README.md#L360-L360](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L360-L360), [README.md#L374-L380](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L374-L380) (`clm_224d3d55407bf5fc0c65faf1b780c3052e184494adc9ed038876eeead23dde96`)
- [observation/documented] Repository development practice: AGENTS.md instructs contributing agents that 'blocked' status is computed from dependencies and must never be set directly, and that api.addDependency() does not detect cycles, so DependencyService.detectCycle() should be used. -- evidence: [AGENTS.md#L152-L161](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/AGENTS.md#L152-L161), [AGENTS.md#L102-L104](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/AGENTS.md#L102-L104) (`clm_7c56c7cf7b30f6e6c8c4677e548db929e732a690a8cee8139cde65cfd2001b01`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The web dashboard offers pages for Activity, Inbox, a Monaco-based Editor, Tasks with Kanban views and status tabs, Merge Requests, Plans, Workflows, Agents, Workspaces (terminal multiplexer), Messages, Documents, and Metrics. -- evidence: [README.md#L226-L229](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L226-L229), [README.md#L220-L222](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L220-L222), [README.md#L243-L243](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L243-L243), [README.md#L233-L234](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L233-L234), [README.md#L238-L239](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L238-L239) (`clm_e1146bed7f8f328610232e25c76a377a09fbedd7b65472afa2d09c7eeca423ed`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The orchestration loop: a Director plans tasks with priorities and dependencies, a dispatch daemon assigns ready tasks to idle workers, workers execute in isolated git worktrees, and a merge steward runs tests and squash-merges or hands off on failure. -- evidence: [README.md#L57-L57](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L57-L57), [README.md#L179-L185](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L179-L185) (`clm_1fea9e832046b980b7ecf0b2dc11b657626b7bc9d41f00914d2e4969bff2ed00`)
- [observation/documented] Agent roles include Director (persistent planner), ephemeral workers spawned by the daemon, persistent workers started manually, and stewards for merge review, docs, recovery, and custom workflows; the dispatch daemon is a background process started with 'sf daemon start'. -- evidence: [README.md#L197-L202](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L197-L202), [README.md#L134-L139](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L134-L139), [README.md#L141-L141](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L141-L141) (`clm_7c359d0fb0a3cda1145b8a5bb26913d4ec3ed9c7b05f26b572c837b0fd36f30d`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents run autonomously with permissions bypassed and no human approval gates before actions, an intentional design the README says means agents read, write, execute, and push code without asking. -- evidence: [README.md#L40-L42](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L40-L42) (`clm_23bb1ff9568a05d3c83aed532a32eb42daebd231da28e9a5116aa979e439365e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Agents can use Claude Code (default), OpenCode, or OpenAI Codex as providers, selected via --provider at registration or session start; API keys are configured in the underlying harness CLI, not in Stoneforge. -- evidence: [README.md#L272-L272](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L272-L272), [README.md#L270-L270](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L270-L270), [README.md#L126-L126](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L126-L126) (`clm_bef2246f8bbb735e7ea0f60ff28b66e30a58b2b4510eed9a5659dbf39f3b3d34`)

## limitations (1 claim(s))

- [observation/documented] The README states Stoneforge is early-stage experimental software under active development, with high token consumption by design and documentation that sometimes lags the code. -- evidence: [README.md#L40-L42](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L40-L42), [README.md#L34-L34](https://github.com/stoneforge-ai/stoneforge/blob/0a7052a9ffa1fb42fafbff9d9b6b83fa48cdad95/README.md#L34-L34) (`clm_ce47c23cf3a14a4ed600acd0fe74802545d60c349b63988dd734add01695d408`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

