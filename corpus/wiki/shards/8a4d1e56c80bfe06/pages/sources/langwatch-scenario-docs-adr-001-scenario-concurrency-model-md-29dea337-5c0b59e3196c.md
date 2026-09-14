---
access: public
aliases: []
claim_ids:
- clm_e5a3c19708be321cfb2b10e3c6bab24f61b70f189e7116de019ca46db314ecf5
maturity: draft
page_id: pg_799ff132cc975de995a45c0b59e3196c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_642eefa88dda54e9bbf9b569a6ac8f63
title: langwatch/scenario/docs/adr/001-scenario-concurrency-model.md @ 29dea3374ef4
updated_at: '2026-09-14T04:04:57Z'
---

# langwatch/scenario/docs/adr/001-scenario-concurrency-model.md @ 29dea3374ef4

<!-- rcw:begin owner=source:src_642eefa88dda54e9bbf9b569a6ac8f63 block=evidence -->
- An accepted ADR replaces environment-variable configuration with per-call programmatic config: each run() gets its own EventBus, config and batchRunId, removing process-wide shared state and the need for a mutex. [@claim:clm_e5a3c19708be321cfb2b10e3c6bab24f61b70f189e7116de019ca46db314ecf5]
<!-- rcw:end owner=source:src_642eefa88dda54e9bbf9b569a6ac8f63 block=evidence -->

## Researcher notes

