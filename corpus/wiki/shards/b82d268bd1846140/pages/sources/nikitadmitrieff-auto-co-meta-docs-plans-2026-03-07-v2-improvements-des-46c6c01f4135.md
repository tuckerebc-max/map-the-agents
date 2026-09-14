---
access: public
aliases: []
claim_ids:
- clm_7cf8828ffe631e7bb38aec20284d51442fb3deade8d44cbc03745b551e94ba6f
maturity: draft
page_id: pg_d582e0717a8859feb56546c6c01f4135
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_93d3b59ca8435889a4804e3064894c54
title: NikitaDmitrieff/auto-co-meta/docs/plans/2026-03-07-v2-improvements-design.md
  @ 5e6bb8a8765e
updated_at: '2026-09-14T04:12:54Z'
---

# NikitaDmitrieff/auto-co-meta/docs/plans/2026-03-07-v2-improvements-design.md @ 5e6bb8a8765e

<!-- rcw:begin owner=source:src_93d3b59ca8435889a4804e3064894c54 block=evidence -->
- Agents append structured records to four append-only JSONL files under state/: decisions, tasks, metrics, and artifacts, each with a defined schema; these files must never be overwritten or truncated. [@claim:clm_7cf8828ffe631e7bb38aec20284d51442fb3deade8d44cbc03745b551e94ba6f]
<!-- rcw:end owner=source:src_93d3b59ca8435889a4804e3064894c54 block=evidence -->

## Researcher notes

