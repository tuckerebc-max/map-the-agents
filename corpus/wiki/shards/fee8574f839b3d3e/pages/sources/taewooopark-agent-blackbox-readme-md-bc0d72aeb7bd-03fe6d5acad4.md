---
access: public
aliases: []
claim_ids:
- clm_062370861cdd5ab35fbf58fed6e8452a2a3f7cc7c6a508654d41a0e560dbd1d2
- clm_12f13c80794a1a8f93e670803b6f658f767eed577946354ecad0dd24403b93f9
- clm_6a60365ebcd502faa2e53d437e4669f664236f85a8aeebaba5f803b8ce390fe9
- clm_a794377b2bad8343a8c4f35d9f365e6276afdf23ccb509ca0976e56b8852d2c8
- clm_b1f68b8b8ba845459519310f48fdf548e93370e821f479c6f46c9b3564af049e
- clm_b5f198f73dc0088679c14b48dd4f4ebfa98971f00ea5553189d2d0e128094d29
- clm_c2decc638fa2562d9d676a11a312c10a4ae8196c9a15982679078f16dfc2384b
- clm_cd6f5e3869d695a55f7581f2edd1457452d9643bc2504a975c96126fd306a15d
- clm_d95179693433f6e4cc8ecf5a778323fab8dcd762bd93956618b0893fc385c61b
- clm_e39737b91b6e09ba70fe7c58c1a642d25d0bced4601545e00e4799ab2fb39a19
- clm_e4e0abd88e8e672d33d44eb30180af85aaf23c46b913889314c15c7498028a0c
- clm_e829cadecbc23b4c288b514c7f1eb8d3e15fedbcdf3909832860ce1579cde254
- clm_f49202013566048b84cd714605fd918c9620197862d786968d930348f88e0cd2
maturity: draft
page_id: pg_4fad39c3b2ba5d8ebe0f03fe6d5acad4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_87511458ed385af19711913115392a41
title: TaewoooPark/Agent-Blackbox/README.md @ bc0d72aeb7bd
updated_at: '2026-09-14T04:25:51Z'
---

# TaewoooPark/Agent-Blackbox/README.md @ bc0d72aeb7bd

<!-- rcw:begin owner=source:src_87511458ed385af19711913115392a41 block=evidence -->
- The session map renders subagent genealogy: real delegations (task tool, child sessions, workflow fan-out) fork into their own lanes attributed to the subagent, with lanes named by role distilled from the spawn type or task prompt. [@claim:clm_062370861cdd5ab35fbf58fed6e8452a2a3f7cc7c6a508654d41a0e560dbd1d2]
- Post-compaction re-reads currently fall back to being served in full rather than as diffs; keeping a local content cache to enable diff-serving across compaction is listed as future work. [@claim:clm_12f13c80794a1a8f93e670803b6f658f767eed577946354ecad0dd24403b93f9]
- Repository development practice: to build from source, clone the repo, run npm install and npm run build:cli, then run node packages/cli/dist/cli.js; development checks use npm run check (typecheck + tests) and npm run build. [@claim:clm_6a60365ebcd502faa2e53d437e4669f664236f85a8aeebaba5f803b8ce390fe9]
- Scoring is task-tailored: a task archetype (research/debug/ops/feature/edit) conditions the efficiency score, a separate effectiveness score judges whether the task landed, and scores are baselined against the user's past runs of the same kind in the same project. [@claim:clm_a794377b2bad8343a8c4f35d9f365e6276afdf23ccb509ca0976e56b8852d2c8]
- The tool is local-first with no API key: traces stay on the machine, raw prompts, secrets, and file contents are redacted by default, and even model-based suggestions receive only a redacted digest (metric statuses, counts, file basenames, command verbs). [@claim:clm_b1f68b8b8ba845459519310f48fdf548e93370e821f479c6f46c9b3564af049e]
- The repository is organized into packages/core (canonical TraceEvents, graph, redaction, replay, audit, handoff, efficiency engine), host adapters for claude-code, codex, and opencode, apps/daemon, and apps/dashboard. [@claim:clm_b5f198f73dc0088679c14b48dd4f4ebfa98971f00ea5553189d2d0e128094d29]
- The stated philosophy is to derive truth from observed events rather than the agent's self-report, with every node being an event the agent actually emitted (read, edit, command with exit code, delegation). [@claim:clm_c2decc638fa2562d9d676a11a312c10a4ae8196c9a15982679078f16dfc2384b]
- The quickstart requires Node 20+; suggestion tailoring can use a free/local model (Ollama, any OpenAI-compatible localhost server, OpenCode's free models) with no API key, while rule-based suggestions work with no dependencies by default. [@claim:clm_cd6f5e3869d695a55f7581f2edd1457452d9643bc2504a975c96126fd306a15d]
- Agent-Blackbox is described as a local-first flight recorder and context-efficiency profiler for coding agents, rebuilding each run as a live, replayable operational graph from observed events rather than the agent's own summary. [@claim:clm_d95179693433f6e4cc8ecf5a778323fab8dcd762bd93956618b0893fc385c61b]
- The daemon exposes an HTTP/WebSocket API including POST /events, GET /graph?seq, GET /snapshot, GET /audit, GET /efficiency, POST /suggest, GET/POST /optimize[/apply|/revert], GET /handoff, and WS /stream for live snapshots. [@claim:clm_e39737b91b6e09ba70fe7c58c1a642d25d0bced4601545e00e4799ab2fb39a19]
- Per-project state lives under <project>/.agent-blackbox/ (optimization.json, efficiency-profile.json, optional rules.json), with cross-run baselines stored as baselines.json next to the daemon's event store. [@claim:clm_e4e0abd88e8e672d33d44eb30180af85aaf23c46b913889314c15c7498028a0c]
- An opt-in in-run optimizer (AGENT_BLACKBOX_OPTIMIZE=1 or --install --optimize) serves re-reads as a no-op or diff via OpenCode tool hooks, never blocking re-reads and only firing when no compaction has occurred since the file was last served. [@claim:clm_e829cadecbc23b4c288b514c7f1eb8d3e15fedbcdf3909832860ce1579cde254]
- Each run receives a context-efficiency score computed from observed sizes and token snapshots, covering metrics like context pressure, cache hit ratio, redundant re-reads, read amplification, retry waste, and yield density. [@claim:clm_f49202013566048b84cd714605fd918c9620197862d786968d930348f88e0cd2]
<!-- rcw:end owner=source:src_87511458ed385af19711913115392a41 block=evidence -->

## Researcher notes

