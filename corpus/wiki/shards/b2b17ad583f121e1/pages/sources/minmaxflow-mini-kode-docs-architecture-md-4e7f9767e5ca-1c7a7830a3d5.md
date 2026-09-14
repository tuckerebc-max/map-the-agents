---
access: public
aliases: []
claim_ids:
- clm_34c3bc6abd899a6c14329edbc25af68353be686c6b0b49df0a9c775fe72b2686
- clm_da860c0c35da3e3d9e1bc39de4d9a5d0bedc5456881e125e886b19be87792936
maturity: draft
page_id: pg_f168d45dfe435c879ce31c7a7830a3d5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cd593d3c4060529dbeb97e011701e34f
title: minmaxflow/mini-kode/docs/architecture.md @ 4e7f9767e5ca
updated_at: '2026-09-14T02:19:14Z'
---

# minmaxflow/mini-kode/docs/architecture.md @ 4e7f9767e5ca

<!-- rcw:begin owner=source:src_cd593d3c4060529dbeb97e011701e34f block=evidence -->
- The agent executor runs a loop: build context, send the request with tool descriptions to the LLM, parse text or tool calls, execute tools, feed results back, and repeat until a final response; conversation length is managed via auto-compaction. [@claim:clm_34c3bc6abd899a6c14329edbc25af68353be686c6b0b49df0a9c775fe72b2686]
- The architecture is layered: a terminal UI layer, an agent layer coordinating the LLM-plus-tool loop, an LLM layer with streaming and tool parsing, a tool layer, and an infrastructure layer for config and permissions. [@claim:clm_da860c0c35da3e3d9e1bc39de4d9a5d0bedc5456881e125e886b19be87792936]
<!-- rcw:end owner=source:src_cd593d3c4060529dbeb97e011701e34f block=evidence -->

## Researcher notes

