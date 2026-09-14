---
access: public
aliases: []
claim_ids:
- clm_4e6d0dcfda74efaaaa32a88ce824bed5daef8bfe4a891d2b072463f372f747a9
- clm_aaeb50c938b30d1eb43a048573f133afc3ef11d77e5125f031c6535936f6de5e
- clm_c8099bb7d88629e43b01524e418d0c8503408ca30ffca88a56a4aa6ea049e035
maturity: draft
page_id: pg_f3656d98511d55958445d29d1836142a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e71291c5e30b5f149db5da9d32b19cb8
title: jcz2020/par/docs/sdk/memory.md @ 4b593db4465d
updated_at: '2026-09-14T02:07:13Z'
---

# jcz2020/par/docs/sdk/memory.md @ 4b593db4465d

<!-- rcw:begin owner=source:src_e71291c5e30b5f149db5da9d32b19cb8 block=evidence -->
- A Memory_service provides cross-session memory with a default SQLite+FTS5 backend, search modes (keyword, vector, hybrid with RRF, auto), and get_fn/upsert_fn for stable-ID plan-then-execute updates. [@claim:clm_4e6d0dcfda74efaaaa32a88ce824bed5daef8bfe4a891d2b072463f372f747a9]
- When memory is configured, three builtin tools (recall_memory, remember_memory, search_history) are auto-registered and scoped per session via invoke_context.session_id. [@claim:clm_aaeb50c938b30d1eb43a048573f133afc3ef11d77e5125f031c6535936f6de5e]
- Each Runtime has its own memory service; cross-agent knowledge sharing requires a shared SQLite file or a future remote backend, per the memory docs. [@claim:clm_c8099bb7d88629e43b01524e418d0c8503408ca30ffca88a56a4aa6ea049e035]
<!-- rcw:end owner=source:src_e71291c5e30b5f149db5da9d32b19cb8 block=evidence -->

## Researcher notes

