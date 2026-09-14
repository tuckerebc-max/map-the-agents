---
access: public
aliases: []
claim_ids:
- clm_125e6c956836aeae5d6945b60ac9b51680ce49f13f182fa4b78058e7adcbf20f
- clm_1fea9e832046b980b7ecf0b2dc11b657626b7bc9d41f00914d2e4969bff2ed00
- clm_224d3d55407bf5fc0c65faf1b780c3052e184494adc9ed038876eeead23dde96
- clm_23bb1ff9568a05d3c83aed532a32eb42daebd231da28e9a5116aa979e439365e
- clm_281e75c677be867fea42ae3a06df879445c059e55c95c4ecb1acf166bc175f27
- clm_39bea180497cf7073bc8827e3689cd8bdf12a1874fcecad99635f7f520ebc521
- clm_7c359d0fb0a3cda1145b8a5bb26913d4ec3ed9c7b05f26b572c837b0fd36f30d
- clm_b678268bb6752e6f5e8045026ce3c21efa6fd8b13f5ca6275bce2261a614c11f
- clm_bef2246f8bbb735e7ea0f60ff28b66e30a58b2b4510eed9a5659dbf39f3b3d34
- clm_ce47c23cf3a14a4ed600acd0fe74802545d60c349b63988dd734add01695d408
- clm_ddfbd4100a876f12270c3055b39781e6b24d89358bbd588fd2cbc745d2654861
- clm_e1146bed7f8f328610232e25c76a377a09fbedd7b65472afa2d09c7eeca423ed
maturity: draft
page_id: pg_bf5792b268685f26b6251223794cb0ff
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4ee8cc5628b157a682b6ca9e26d76140
title: stoneforge-ai/stoneforge/README.md @ 0a7052a9ffa1
updated_at: '2026-09-14T02:43:53Z'
---

# stoneforge-ai/stoneforge/README.md @ 0a7052a9ffa1

<!-- rcw:begin owner=source:src_4ee8cc5628b157a682b6ca9e26d76140 block=evidence -->
- The product has two layers: Smithy (@stoneforge/smithy), the installable orchestrator that spawns agents and manages sessions and worktree isolation, and Quarry (@stoneforge/quarry), an event-sourced data SDK usable standalone. [@claim:clm_125e6c956836aeae5d6945b60ac9b51680ce49f13f182fa4b78058e7adcbf20f]
- The orchestration loop: a Director plans tasks with priorities and dependencies, a dispatch daemon assigns ready tasks to idle workers, workers execute in isolated git worktrees, and a merge steward runs tests and squash-merges or hands off on failure. [@claim:clm_1fea9e832046b980b7ecf0b2dc11b657626b7bc9d41f00914d2e4969bff2ed00]
- Repository development practice: contributors use pnpm/bun commands (pnpm install, pnpm build, pnpm test, pnpm lint, pnpm typecheck; bun test), tests are colocated as *.test.ts files, and contributors must sign a CLA before PR merge. [@claim:clm_224d3d55407bf5fc0c65faf1b780c3052e184494adc9ed038876eeead23dde96]
- Agents run autonomously with permissions bypassed and no human approval gates before actions, an intentional design the README says means agents read, write, execute, and push code without asking. [@claim:clm_23bb1ff9568a05d3c83aed532a32eb42daebd231da28e9a5116aa979e439365e]
- The monorepo ships packages core, storage, quarry, smithy, ui, and shared-routes, plus apps quarry-server (port 3456), quarry-web (5173), smithy-server (3457), and smithy-web (5174). [@claim:clm_281e75c677be867fea42ae3a06df879445c059e55c95c4ecb1acf166bc175f27]
- Built-in role prompts can be overridden per project via .stoneforge/prompts/ files such as director.md, worker.md, and steward-merge.md. [@claim:clm_39bea180497cf7073bc8827e3689cd8bdf12a1874fcecad99635f7f520ebc521]
- Agent roles include Director (persistent planner), ephemeral workers spawned by the daemon, persistent workers started manually, and stewards for merge review, docs, recovery, and custom workflows; the dispatch daemon is a background process started with 'sf daemon start'. [@claim:clm_7c359d0fb0a3cda1145b8a5bb26913d4ec3ed9c7b05f26b572c837b0fd36f30d]
- Storage uses a dual model: SQLite serves as an ephemeral cache with FTS5 full-text search and indexes, while git-tracked append-only JSONL is the durable source of truth, rebuilt into SQLite on sync. [@claim:clm_b678268bb6752e6f5e8045026ce3c21efa6fd8b13f5ca6275bce2261a614c11f]
- Agents can use Claude Code (default), OpenCode, or OpenAI Codex as providers, selected via --provider at registration or session start; API keys are configured in the underlying harness CLI, not in Stoneforge. [@claim:clm_bef2246f8bbb735e7ea0f60ff28b66e30a58b2b4510eed9a5659dbf39f3b3d34]
- The README states Stoneforge is early-stage experimental software under active development, with high token consumption by design and documentation that sometimes lags the code. [@claim:clm_ce47c23cf3a14a4ed600acd0fe74802545d60c349b63988dd734add01695d408]
- Stoneforge is described as a web dashboard and runtime for orchestrating AI coding agents, positioned for developers already running 3-5 agents in parallel. [@claim:clm_ddfbd4100a876f12270c3055b39781e6b24d89358bbd588fd2cbc745d2654861]
- The web dashboard offers pages for Activity, Inbox, a Monaco-based Editor, Tasks with Kanban views and status tabs, Merge Requests, Plans, Workflows, Agents, Workspaces (terminal multiplexer), Messages, Documents, and Metrics. [@claim:clm_e1146bed7f8f328610232e25c76a377a09fbedd7b65472afa2d09c7eeca423ed]
<!-- rcw:end owner=source:src_4ee8cc5628b157a682b6ca9e26d76140 block=evidence -->

## Researcher notes

