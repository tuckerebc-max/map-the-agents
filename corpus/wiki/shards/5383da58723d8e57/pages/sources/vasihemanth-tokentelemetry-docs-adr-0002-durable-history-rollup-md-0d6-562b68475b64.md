---
access: public
aliases: []
claim_ids:
- clm_3b105f84ba2154e987ae0ed3ec93550f58bb04873265bde7e0d18ddc587a405a
- clm_e21e58a6811eb912023a3110359ae1675479d67c3a55ac9a7443bc11a165363a
maturity: draft
page_id: pg_926fa1f690ba5f8fa735562b68475b64
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8b22c0c487725df3a006c5c586923d12
title: VasiHemanth/tokentelemetry/docs/adr/0002-durable-history-rollup.md @ 0d691ae343ed
updated_at: '2026-09-14T04:30:01Z'
---

# VasiHemanth/tokentelemetry/docs/adr/0002-durable-history-rollup.md @ 0d691ae343ed

<!-- rcw:begin owner=source:src_8b22c0c487725df3a006c5c586923d12 block=evidence -->
- Per ADR-0002, a durable local SQLite store at ~/.tokentelemetry/history.db is upserted on every background scan, storing raw facts so analytics history survives agents pruning their transcripts; derived insights are recomputed at read time. [@claim:clm_3b105f84ba2154e987ae0ed3ec93550f58bb04873265bde7e0d18ddc587a405a]
- Per ADR-0002, history capture starts from the first run (already-pruned transcripts are unrecoverable), pruned sessions without archival show only in aggregates, and transcript archival currently resolves single-file transcripts only for claude/codex. [@claim:clm_e21e58a6811eb912023a3110359ae1675479d67c3a55ac9a7443bc11a165363a]
<!-- rcw:end owner=source:src_8b22c0c487725df3a006c5c586923d12 block=evidence -->

## Researcher notes

