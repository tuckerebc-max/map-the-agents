---
access: public
aliases: []
claim_ids:
- clm_192e39c4bf5178738fe73ddd1dcce0ae70694c825890fa2d490404e01ad6ce25
- clm_8e8afd0d0185b227560829480e5fd38d291249765313e1a7270d018b7791701b
- clm_c1c0a93c5ea8622c05d806f9a81c33113ed5f92d4aae11eb9b8102aabdb4efd3
maturity: draft
page_id: pg_d373c6b85f955fb48708495626c5baa8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4f3a3f0b20575ca38dd9b2aeff47c320
title: paean-ai/deeptide/docs/deepseek-v4-flash-q2.md @ b48688d56c3e
updated_at: '2026-09-14T02:28:52Z'
---

# paean-ai/deeptide/docs/deepseek-v4-flash-q2.md @ b48688d56c3e

<!-- rcw:begin owner=source:src_4f3a3f0b20575ca38dd9b2aeff47c320 block=evidence -->
- The shipped local DeepSeek V4 Flash Q2 build is documented as a technology-feasibility preview, not a production coding model, and is not a faithful approximation of cloud V4 behavior. [@claim:clm_192e39c4bf5178738fe73ddd1dcce0ae70694c825890fa2d490404e01ad6ce25]
- The local V4 Flash Q2 profile caps context at 64k, disables subagents, and forces serial tool execution, because Q2's attention quality degrades on long contexts and parallel tool calls compound state too quickly. [@claim:clm_8e8afd0d0185b227560829480e5fd38d291249765313e1a7270d018b7791701b]
- The repo references a local-agent benchmark suite under benchmarks/local-agent/ used to check long-context regressions (32k/64k/96k prompts) before raising the V4 Flash context window, and the quant doc prescribes four workload checks including long-context recall and expert-diversity testing. [@claim:clm_c1c0a93c5ea8622c05d806f9a81c33113ed5f92d4aae11eb9b8102aabdb4efd3]
<!-- rcw:end owner=source:src_4f3a3f0b20575ca38dd9b2aeff47c320 block=evidence -->

## Researcher notes

