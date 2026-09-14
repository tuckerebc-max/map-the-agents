---
access: public
aliases: []
claim_ids:
- clm_bb86068238d8c481dce6683e1a576c19b52f099c16b234acf533f3c3189763e4
- clm_d459809a90f8e3cb3877a46ae4678c5148ef17fd01d65c9a5428fc1bdb399ea9
maturity: draft
page_id: pg_16d5076123c8556e83021f15bd9f8cde
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_85f7c8213a41561784ca11f14eda6720
title: lajosdeme/mole/RELEASING.md @ fcb92379120d
updated_at: '2026-09-14T04:05:07Z'
---

# lajosdeme/mole/RELEASING.md @ fcb92379120d

<!-- rcw:begin owner=source:src_85f7c8213a41561784ca11f14eda6720 block=evidence -->
- Local-data analysis supports CSV, TSV, JSON and JSONL but not Parquet; release binaries are unsigned, so macOS users may need to clear the Gatekeeper quarantine attribute manually. [@claim:clm_bb86068238d8c481dce6683e1a576c19b52f099c16b234acf533f3c3189763e4]
- The database schema migrates forward automatically but has no down-migrations, so downgrading across a schema change requires restoring a database copy. [@claim:clm_d459809a90f8e3cb3877a46ae4678c5148ef17fd01d65c9a5428fc1bdb399ea9]
<!-- rcw:end owner=source:src_85f7c8213a41561784ca11f14eda6720 block=evidence -->

## Researcher notes

