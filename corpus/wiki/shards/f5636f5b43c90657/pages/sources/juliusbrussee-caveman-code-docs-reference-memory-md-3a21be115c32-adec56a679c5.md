---
access: public
aliases: []
claim_ids:
- clm_145664b82c194b450e86b577f10792e6196286390cbdcc48db2c50a286b0d85b
- clm_343c0d65b2c8bcc244f58e17ffb1369dbb9470a8d0e9b69c46ec807d1bd20289
- clm_a3f77d9e288afad293aa0e484f6f1ae14a526b903672d42d0c2666e8ef90ed44
- clm_f19a047dbe6f6ef2795cde389907f7e20c4be49672d18557485ef0679ce1b95f
maturity: draft
page_id: pg_fadbdea6b1d25c369338adec56a679c5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_14d6a8cae1675fe4a0ca27d2a7fb3587
title: JuliusBrussee/caveman-code/docs/reference/memory.md @ 3a21be115c32
updated_at: '2026-09-14T02:08:09Z'
---

# JuliusBrussee/caveman-code/docs/reference/memory.md @ 3a21be115c32

<!-- rcw:begin owner=source:src_14d6a8cae1675fe4a0ca27d2a7fb3587 block=evidence -->
- Optional external dependencies include the RTK Rust binary (pipes bash output through compression before it enters context) and cavemem for memory; both are integrations the agent can use rather than hard requirements. [@claim:clm_145664b82c194b450e86b577f10792e6196286390cbdcc48db2c50a286b0d85b]
- Persistent memory is delegated to cavemem (hybrid BM25 + local vectors on SQLite/FTS5); the agent exposes memory_search and memory_save tools, auto-injects relevant recall each turn capped at 2k tokens by default, and can fall back to plain markdown files via memory.provider: files. [@claim:clm_343c0d65b2c8bcc244f58e17ffb1369dbb9470a8d0e9b69c46ec807d1bd20289]
- Episodic-to-semantic consolidation clusters recent observations, uses Haiku to extract semantic facts, and writes them back with provenance ids; it runs on demand via /memory consolidate or a nightly cron. [@claim:clm_a3f77d9e288afad293aa0e484f6f1ae14a526b903672d42d0c2666e8ef90ed44]
- When a tool call fails twice and then succeeds, the agent writes a 'lesson' observation capturing context, failure, and fix, mirroring Claude Code's Auto-Memory. [@claim:clm_f19a047dbe6f6ef2795cde389907f7e20c4be49672d18557485ef0679ce1b95f]
<!-- rcw:end owner=source:src_14d6a8cae1675fe4a0ca27d2a7fb3587 block=evidence -->

## Researcher notes

