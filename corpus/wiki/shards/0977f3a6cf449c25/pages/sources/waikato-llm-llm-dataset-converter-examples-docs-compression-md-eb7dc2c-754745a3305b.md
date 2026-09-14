---
access: public
aliases: []
claim_ids:
- clm_1198a1110524e0bf1e0a7511e904ba0afce34b793bb7c1f01cfe09741826d494
- clm_591643db491590ae58d341a9aa42cd880e6c1752d25c5eb3b454303d9cf98370
- clm_9233bfa8b5195ddecb6fff0061f7d23b5ef99d909c018229bff6c6860d061a32
maturity: draft
page_id: pg_206317db957f5db298cb754745a3305b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2f0a0bbbb580552aa9f3922657ce0c01
title: waikato-llm/llm-dataset-converter-examples/docs/compression.md @ eb7dc2c462fa
updated_at: '2026-09-14T04:31:19Z'
---

# waikato-llm/llm-dataset-converter-examples/docs/compression.md @ eb7dc2c462fa

<!-- rcw:begin owner=source:src_2f0a0bbbb580552aa9f3922657ce0c01 block=evidence -->
- Input files are automatically decompressed based on their extension, provided the format supports that. [@claim:clm_1198a1110524e0bf1e0a7511e904ba0afce34b793bb7c1f01cfe09741826d494]
- Output files are automatically compressed when the format supports it, based on the extension used for the output, e.g. producing a .csv.gz via Gzip. [@claim:clm_591643db491590ae58d341a9aa42cd880e6c1752d25c5eb3b454303d9cf98370]
- The examples show a CLI command llm-convert that takes a source reader (e.g. from-alpaca) with --input and a writer (e.g. to-csv-pr) with --output. [@claim:clm_9233bfa8b5195ddecb6fff0061f7d23b5ef99d909c018229bff6c6860d061a32]
<!-- rcw:end owner=source:src_2f0a0bbbb580552aa9f3922657ce0c01 block=evidence -->

## Researcher notes

