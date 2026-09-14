---
access: public
aliases: []
claim_ids:
- clm_aa12aa208a1ff22974cc318ae010668b8baf0dd422496c20ded7a076a57e66f6
- clm_c2d3c71a6b36fc0829c12dd768cde8d54a846dedccf7684b563c4e1a5d72316d
- clm_c56b90f92aa0978e189f9e3590f538c141f5fabaa805547a97a2a4b4e2c0b564
maturity: draft
page_id: pg_a7ebbb39092c5c9cbbc274418048b49d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cc6faa0dc9735747a21a887e38cdfb11
title: aurasgit/public-agent-framwork/docs/cache.md @ f3f27582c6a2
updated_at: '2026-09-14T01:59:36Z'
---

# aurasgit/public-agent-framwork/docs/cache.md @ f3f27582c6a2

<!-- rcw:begin owner=source:src_cc6faa0dc9735747a21a887e38cdfb11 block=evidence -->
- LLM adapters include OllamaChatLLM, configurable with modelId, generation parameters, and an optional cache. [@claim:clm_aa12aa208a1ff22974cc318ae010668b8baf0dd422496c20ded7a076a57e66f6]
- Tool and LLM caching keys are created by serializing function parameters, with object key order not mattering; identical inputs are served from cache. [@claim:clm_c2d3c71a6b36fc0829c12dd768cde8d54a846dedccf7684b563c4e1a5d72316d]
- Custom cache providers implement a BaseCache class with set, get, has, delete, clear, size, and snapshot methods. [@claim:clm_c56b90f92aa0978e189f9e3590f538c141f5fabaa805547a97a2a4b4e2c0b564]
<!-- rcw:end owner=source:src_cc6faa0dc9735747a21a887e38cdfb11 block=evidence -->

## Researcher notes

