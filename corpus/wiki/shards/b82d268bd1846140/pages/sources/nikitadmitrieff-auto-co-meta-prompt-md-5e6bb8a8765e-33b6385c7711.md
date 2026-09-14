---
access: public
aliases: []
claim_ids:
- clm_1798dfaec9bdee2883e3cd53b17f79eda74d5d6fc76f12dd61ff9effdf1f3568
- clm_7cf8828ffe631e7bb38aec20284d51442fb3deade8d44cbc03745b551e94ba6f
maturity: draft
page_id: pg_55281b5fb2f758b5811833b6385c7711
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d3897964fcf259719897dc37b935b802
title: NikitaDmitrieff/auto-co-meta/PROMPT.md @ 5e6bb8a8765e
updated_at: '2026-09-14T04:12:54Z'
---

# NikitaDmitrieff/auto-co-meta/PROMPT.md @ 5e6bb8a8765e

<!-- rcw:begin owner=source:src_d3897964fcf259719897dc37b935b802 block=evidence -->
- Consensus.md acts as the relay baton carrying state between cycles, written atomically via a .consensus.tmp temp file and rename, with a .bak backup restored automatically on cycle failure. [@claim:clm_1798dfaec9bdee2883e3cd53b17f79eda74d5d6fc76f12dd61ff9effdf1f3568]
- Agents append structured records to four append-only JSONL files under state/: decisions, tasks, metrics, and artifacts, each with a defined schema; these files must never be overwritten or truncated. [@claim:clm_7cf8828ffe631e7bb38aec20284d51442fb3deade8d44cbc03745b551e94ba6f]
<!-- rcw:end owner=source:src_d3897964fcf259719897dc37b935b802 block=evidence -->

## Researcher notes

