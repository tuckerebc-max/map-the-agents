---
access: public
aliases: []
claim_ids:
- clm_79544db9a6dd960cbb0764a47337b6d8b58bb0b46c5b87effbfbcfc206148890
- clm_bcab83a0d9115abec8ffdc6c784f16baca14f9faa4ad507429688007dac9c093
maturity: draft
page_id: pg_f101fc1249a85f0c8eaeb079c9aad7d7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a50c3bd1b6a353988963cf933ebd8af6
title: JuliusBrussee/cavemem/docs/compression.md @ 166078dd7c46
updated_at: '2026-09-14T04:02:15Z'
---

# JuliusBrussee/cavemem/docs/compression.md @ 166078dd7c46

<!-- rcw:begin owner=source:src_a50c3bd1b6a353988963cf933ebd8af6 block=evidence -->
- Compression is deterministic and offline, never invoking a model; technical tokens (code, URLs, paths, commands, versions, dates, numbers, identifiers) are preserved byte-for-byte and prose is lossy only on filler/hedging words. [@claim:clm_79544db9a6dd960cbb0764a47337b6d8b58bb0b46c5b87effbfbcfc206148890]
- An evals/ harness measures compression performance: fixtures verify determinism and technical-token round-trip, and the benchmark corpus requires at least 30% average token reduction (targets of 40% at full and 55% at ultra intensity). [@claim:clm_bcab83a0d9115abec8ffdc6c784f16baca14f9faa4ad507429688007dac9c093]
<!-- rcw:end owner=source:src_a50c3bd1b6a353988963cf933ebd8af6 block=evidence -->

## Researcher notes

