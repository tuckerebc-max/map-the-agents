---
access: public
aliases: []
claim_ids:
- clm_4079e9a5f95e0f3a68aeaa244c07444fee8c706f7b4003a5a4b6cf4148ffcd16
- clm_68bea434bb774ec6fbf41c2092ccdf970c965cb65b40e25e2843c39c2ed9d326
maturity: draft
page_id: pg_1b7cf6fd294a5cf0a2687267f9bdae67
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c3d7f5978f175f359db3bd11789d9095
title: agnusdei1207/opencode-orchestrator/docs/adr/0001-second-brain-knowledge-graph-rag.md
  @ 572c7bef8ca0
updated_at: '2026-09-14T03:31:50Z'
---

# agnusdei1207/opencode-orchestrator/docs/adr/0001-second-brain-knowledge-graph-rag.md @ 572c7bef8ca0

<!-- rcw:begin owner=source:src_c3d7f5978f175f359db3bd11789d9095 block=evidence -->
- Memory is local-first: an on-disk Ebbinghaus decay model combining BM25, tags, and graph connections, explicitly avoiding external vector databases. [@claim:clm_4079e9a5f95e0f3a68aeaa244c07444fee8c706f7b4003a5a4b6cf4148ffcd16]
- ADR-0001 established a constraint of no GPU, no external model, and no external API, keeping the knowledge plane CPU-only and local. [@claim:clm_68bea434bb774ec6fbf41c2092ccdf970c965cb65b40e25e2843c39c2ed9d326]
<!-- rcw:end owner=source:src_c3d7f5978f175f359db3bd11789d9095 block=evidence -->

## Researcher notes

