---
access: public
aliases: []
claim_ids:
- clm_0b36816531b234873ae6b87619536c3d41015b7014f52bae6ea833c7181fe4a4
- clm_0c374aeaa18fbc6ff6b01e3a2e06bef25ff39748067004a4a869353ca43ae0ea
- clm_3d7f16957cc3edf5b02e5eb85c29ab46993c957f3da6345feb27984c9b136078
- clm_40fc69a90fc002613f7a30a1c6064415511c6b0478f2b0a5eab373826fffe3c5
- clm_44cf8958e4c800f453c1a19c8554b615d2ed9a324fbda16a9e7d5ebf8ec742ec
- clm_5e8d6d2cd50de0453cfb951f727b93071589e7c5f0dbcc7b3e2ab91ab8bd7145
- clm_818463f4c2fa684eb98b22c72ada80d4bbad26936c4723c22692fa2849cc23b6
- clm_83ac5da94762939e603a1f3c8de18751326c883212be1f91ba75b9281a196049
- clm_a4795b7829a32e794d7ffaa6710fc796bae5316f23f6a7b22d0b3d60fba598e9
maturity: draft
page_id: pg_688508621263506586b3491a1416edcd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_52f9aac99ed75406b7827ef4d501d57b
title: the-open-engine/zeroshot/README.md @ b550c15279c9
updated_at: '2026-09-14T03:18:50Z'
---

# the-open-engine/zeroshot/README.md @ b550c15279c9

<!-- rcw:begin owner=source:src_52f9aac99ed75406b7827ef4d501d57b block=evidence -->
- Three execution targets share the same graph and runtime plan: local mode in the current Git worktree reusing Codex or Claude Code logins, a self-hosted Docker target image bundling the engine plus pinned Codex and Claude harness CLIs, and a managed Zeroshot Cloud target. [@claim:clm_0b36816531b234873ae6b87619536c3d41015b7014f52bae6ea833c7181fe4a4]
- The product is a native `zeroshot` executable (v8 hard cutover, former Node.js runtime retired), installed via npm and providing commands like `zeroshot run`, `zeroshot version`, and `zeroshot template list/show`. [@claim:clm_0c374aeaa18fbc6ff6b01e3a2e06bef25ff39748067004a4a869353ca43ae0ea]
- Repository development practice: contributors run `npm ci`, `npm run check`, and `cargo test --workspace`; Node.js is repository tooling and the npm delivery mechanism only. [@claim:clm_3d7f16957cc3edf5b02e5eb85c29ab46993c957f3da6345feb27984c9b136078]
- A Python SDK is provided with public objects including LocalTarget, DirectTarget, HostedTarget, Target, Preset, GraphSpec, UniformRuntime, RuntimePlan, RunRequest, and MergePlanRequest. [@claim:clm_40fc69a90fc002613f7a30a1c6064415511c6b0478f2b0a5eab373826fffe3c5]
- The built-in software-change graph gives the goal to a worker, runs acceptance and code review in parallel, routes rejections to a repair worker with repeated reviews, and delivers accepted changes through Git, CI, and merge, routing delivery conflicts back through repair. [@claim:clm_44cf8958e4c800f453c1a19c8554b615d2ed9a324fbda16a9e7d5ebf8ec742ec]
- The npm package installs a verified native binary for Linux x64/arm64, macOS x64/arm64, and Windows x64; native archives and SHA256 checksums are attached to each canonical vX.Y.Z GitHub Release. [@claim:clm_5e8d6d2cd50de0453cfb951f727b93071589e7c5f0dbcc7b3e2ab91ab8bd7145]
- Every graph transition event is written to a durable SQLite ledger; after validating graph, runtime plan, and input, Zeroshot opens a durable ledger recording each node result. [@claim:clm_818463f4c2fa684eb98b22c72ada80d4bbad26936c4723c22692fa2849cc23b6]
- Control flow is authored data rather than hidden in prompts: sequence, parallel review, retry paths, delivery, and exit conditions are explicit before a run starts, and no runtime agent chooses the next step. [@claim:clm_83ac5da94762939e603a1f3c8de18751326c883212be1f91ba75b9281a196049]
- Zeroshot turns a software goal into an explicit multi-agent graph: one agent implements, independent agents review, failures route into bounded repair, and delivery happens only after the graph's checks pass. [@claim:clm_a4795b7829a32e794d7ffaa6710fc796bae5316f23f6a7b22d0b3d60fba598e9]
<!-- rcw:end owner=source:src_52f9aac99ed75406b7827ef4d501d57b block=evidence -->

## Researcher notes

