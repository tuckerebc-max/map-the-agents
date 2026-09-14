---
access: public
aliases: []
claim_ids:
- clm_3a40fa0208bb18e5513f35db0e9746a1e7c454a6c705c37c1d65d401f8d9120c
maturity: draft
page_id: pg_dbf856918ad159fa97666a22217636c2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b8ec8cca1475590ea11ce2aa10062ce8
title: JuliusBrussee/cavemem/docs/architecture.md @ 166078dd7c46
updated_at: '2026-09-14T04:02:15Z'
---

# JuliusBrussee/cavemem/docs/architecture.md @ 166078dd7c46

<!-- rcw:begin owner=source:src_b8ec8cca1475590ea11ce2aa10062ce8 block=evidence -->
- Memory persists in a local SQLite database with FTS5 updated via triggers; embeddings are computed out-of-band by a background worker that auto-spawns on the first hook and self-exits when idle. [@claim:clm_3a40fa0208bb18e5513f35db0e9746a1e7c454a6c705c37c1d65d401f8d9120c]
<!-- rcw:end owner=source:src_b8ec8cca1475590ea11ce2aa10062ce8 block=evidence -->

## Researcher notes

