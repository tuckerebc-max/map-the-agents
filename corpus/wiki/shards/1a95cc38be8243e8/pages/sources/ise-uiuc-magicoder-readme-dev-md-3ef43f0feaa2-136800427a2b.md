---
access: public
aliases: []
claim_ids:
- clm_2c5bc321221fb56ffdaaaf4560e09b682c5d42a313497f8b70fc25ab2d8d611e
- clm_7fde25c7385eb3c15f5ebabe7518367c9517bcbbd40d955c36827bb3fbb654cc
maturity: draft
page_id: pg_aa497cdb819453afbf86136800427a2b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5b76a10c0c335058b120b52b342f74fd
title: ise-uiuc/magicoder/README-DEV.md @ 3ef43f0feaa2
updated_at: '2026-09-14T03:59:17Z'
---

# ise-uiuc/magicoder/README-DEV.md @ 3ef43f0feaa2

<!-- rcw:begin owner=source:src_5b76a10c0c335058b120b52b342f74fd block=evidence -->
- Repository development practice: Magicoder-S is produced by continuing training from the Magicoder checkpoint on Evol-Instruct data with a shorter max sequence length (1024 vs 1216), using bf16, adafactor, and linear LR scheduling. [@claim:clm_2c5bc321221fb56ffdaaaf4560e09b682c5d42a313497f8b70fc25ab2d8d611e]
- Repository development practice: the developer guide (marked WIP) documents a pipeline of scripts for data generation (generate_data.py with OPENAI_API_KEY), cleaning/decontamination, preprocessing, and instruction tuning via accelerate launch of magicoder.train. [@claim:clm_7fde25c7385eb3c15f5ebabe7518367c9517bcbbd40d955c36827bb3fbb654cc]
<!-- rcw:end owner=source:src_5b76a10c0c335058b120b52b342f74fd block=evidence -->

## Researcher notes

