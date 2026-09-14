---
access: public
aliases: []
claim_ids:
- clm_0b36816531b234873ae6b87619536c3d41015b7014f52bae6ea833c7181fe4a4
- clm_0bf189be40418d5352fa500818c5d34366893c975a0305374c19194d3d815d4e
- clm_246f7f6c5217275aa6f4507f546b7ae82c5504c858d4240f3bc115fd1fce90a0
- clm_818463f4c2fa684eb98b22c72ada80d4bbad26936c4723c22692fa2849cc23b6
maturity: draft
page_id: pg_c6cea27f1c535db8b10c2072b80aca3c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9e6d59903dd75171b4088f2fa3c55749
title: the-open-engine/zeroshot/docs/index.md @ b550c15279c9
updated_at: '2026-09-14T03:18:50Z'
---

# the-open-engine/zeroshot/docs/index.md @ b550c15279c9

<!-- rcw:begin owner=source:src_9e6d59903dd75171b4088f2fa3c55749 block=evidence -->
- Three execution targets share the same graph and runtime plan: local mode in the current Git worktree reusing Codex or Claude Code logins, a self-hosted Docker target image bundling the engine plus pinned Codex and Claude harness CLIs, and a managed Zeroshot Cloud target. [@claim:clm_0b36816531b234873ae6b87619536c3d41015b7014f52bae6ea833c7181fe4a4]
- A run consists of three authored values: a graph defining control flow and typed state, a runtime plan binding each executable node to a harness, provider, model, and named connections, and caller-owned initial input validated against the graph before execution. [@claim:clm_0bf189be40418d5352fa500818c5d34366893c975a0305374c19194d3d815d4e]
- Besides the software-change template, a single-worker template exists for work that does not need the review loop, and custom graphs follow the same protocol contracts. [@claim:clm_246f7f6c5217275aa6f4507f546b7ae82c5504c858d4240f3bc115fd1fce90a0]
- Every graph transition event is written to a durable SQLite ledger; after validating graph, runtime plan, and input, Zeroshot opens a durable ledger recording each node result. [@claim:clm_818463f4c2fa684eb98b22c72ada80d4bbad26936c4723c22692fa2849cc23b6]
<!-- rcw:end owner=source:src_9e6d59903dd75171b4088f2fa3c55749 block=evidence -->

## Researcher notes

