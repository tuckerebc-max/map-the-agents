---
access: public
aliases: []
claim_ids:
- clm_0a9999bbecfbc32b5ad876ad92b8f80df1c1c23a3cb02262cdde6bcfe8d6b913
- clm_835405c6e6d8fa3adf1c998bdc9deffa9583ea1094a2bc657f7500bc30cf8bb4
- clm_a2cfc3d5e8b5fad6be3ea1ade00ae9e126b3ff59a102c5e335d9b7bb92917470
- clm_ac85fef8ab0b3c532266b493b6cbacd14a03c5af010738ce47bc22edfb44fd33
- clm_b0512fa8f2a4e24a724468625dae4e1396e9841d5f0c833e633d2e64e78ee19b
- clm_ca771bd2d75b19d4e5bd756e879dc1671c48ed1ebbffa94ae91b3d99a80670b1
maturity: draft
page_id: pg_7855e768518458fe9536a8163b488a28
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ba8e0574e1e75221a711e63385babdb3
title: nanocoai/nanoclaw/docs/architecture.md @ 3f9ed607b7e7
updated_at: '2026-09-14T02:22:07Z'
---

# nanocoai/nanoclaw/docs/architecture.md @ 3f9ed607b7e7

<!-- rcw:begin owner=source:src_ba8e0574e1e75221a711e63385babdb3 block=evidence -->
- Channel adapters return platform channel and thread IDs without knowing agent-group or session IDs; the host maps those to the entity model, and session mode (shared vs per-thread) is configured per channel. [@claim:clm_0a9999bbecfbc32b5ad876ad92b8f80df1c1c23a3cb02262cdde6bcfe8d6b913]
- The host acts as orchestrator: it spawns containers on wakeUpAgent when none exists, kills idle containers after a timeout, and runs a ~60s sweep for stale detection, due-message wake, delivery, and recurrence insertion. [@claim:clm_835405c6e6d8fa3adf1c998bdc9deffa9583ea1094a2bc657f7500bc30cf8bb4]
- Each session has a pair of mounted SQLite files as the only host-container IO mechanism: inbound.db (host-written, container read-only) and outbound.db (container-written), each with exactly one writer and journal_mode=DELETE rather than WAL. [@claim:clm_a2cfc3d5e8b5fad6be3ea1ade00ae9e126b3ff59a102c5e335d9b7bb92917470]
- Message sequence numbers use disjoint parity — even seqs written by the host in messages_in, odd by the container in messages_out — forming a single monotonic id across both tables. [@claim:clm_ac85fef8ab0b3c532266b493b6cbacd14a03c5af010738ce47bc22edfb44fd33]
- A single Node host process routes messages through an entity model (user → messaging group → agent group → session), writes to the session's inbound.db, and wakes the container; the agent-runner inside polls inbound.db and writes responses to outbound.db. [@claim:clm_b0512fa8f2a4e24a724468625dae4e1396e9841d5f0c833e633d2e64e78ee19b]
- Outbound file delivery is tool-based: the agent calls a dedicated send_file MCP tool, the runner stages files in an outbox directory per messages_out row, messages_out references filenames only, and the host delivers and cleans up after delivery. [@claim:clm_ca771bd2d75b19d4e5bd756e879dc1671c48ed1ebbffa94ae91b3d99a80670b1]
<!-- rcw:end owner=source:src_ba8e0574e1e75221a711e63385babdb3 block=evidence -->

## Researcher notes

