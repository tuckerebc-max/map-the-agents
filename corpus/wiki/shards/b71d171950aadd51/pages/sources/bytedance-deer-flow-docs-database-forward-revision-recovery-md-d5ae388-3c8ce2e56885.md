---
access: public
aliases: []
claim_ids:
- clm_6a04b155903f19f5b046e4ae4f7776ab66023f67f7c4f29fbf6b9da5a599080a
maturity: draft
page_id: pg_7e56ee1e24185426a34c3c8ce2e56885
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b745213444965d178f5b1193177bbf59
title: bytedance/deer-flow/docs/database-forward-revision-recovery.md @ d5ae3882b670
updated_at: '2026-09-14T01:38:55Z'
---

# bytedance/deer-flow/docs/database-forward-revision-recovery.md @ d5ae3882b670

<!-- rcw:begin owner=source:src_b745213444965d178f5b1193177bbf59 block=evidence -->
- A database recovery doc states that an older deployment stamped with revision 0019_thread_incarnations but lacking the projects table and threads_meta.project_id cannot serve the current build; startup rejects that schema without changing it and reports the missing tables/columns. [@claim:clm_6a04b155903f19f5b046e4ae4f7776ab66023f67f7c4f29fbf6b9da5a599080a]
<!-- rcw:end owner=source:src_b745213444965d178f5b1193177bbf59 block=evidence -->

## Researcher notes

