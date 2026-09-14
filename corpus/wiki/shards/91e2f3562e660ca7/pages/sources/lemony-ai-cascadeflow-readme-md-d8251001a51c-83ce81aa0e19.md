---
access: public
aliases: []
claim_ids:
- clm_1e1d1698d9b25d73fec4a6cd5cdb1cc13948cbf4bd3b41cd829227e10d5996d4
- clm_231d49f38fa674438b63ed81870c72d683bbaeb8a244a74cc71e880751107f4f
- clm_329a04d23f32e682d8a5bb4fe175a0a49de9f90baf8ac4b92fafd9a4b3fe54d4
- clm_650e40919bad9bc58ecb009b7e7abec0cf7b6bd1c3ff193cbd986c41e8cfae46
- clm_75614c2ff2fd8bcd4b4b1aca27120f9d8809b95a9f9c29763473896fcb64b32b
- clm_ac723b9c4e4dbb6552dde2862cc9d1013bf6ce726fe9214be03f9524f730f63f
- clm_d21b758dfb2ab084ea5668c40b8111cae9360a3e726c0cf1d78d8197bf184aa2
- clm_e6a7c744c8bae06c0de0284053194c022af1f65f2bed1cfc23ac739f5200a839
- clm_e79390dea62e5dc89e2dd661c9209b7e88afff7ff5de9e4ea2a6d65031ce9a30
- clm_ed6f8462c639ef3299732d00dbe13fb75379e32d87313b344511a0d45a778ee3
maturity: draft
page_id: pg_6b05e280ebc95d2892dc83ce81aa0e19
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4e7fb2ca145e59549b3c6c8f9fdd1c22
title: lemony-ai/cascadeflow/README.md @ d8251001a51c
updated_at: '2026-09-14T04:06:05Z'
---

# lemony-ai/cascadeflow/README.md @ d8251001a51c

<!-- rcw:begin owner=source:src_4e7fb2ca145e59549b3c6c8f9fdd1c22 block=evidence -->
- The harness API offers three tiers: cascadeflow.init(mode="observe") for zero-change tracking, cascadeflow.run(budget=..., max_tool_calls=...) sessions with summary() and trace(), and a @cascadeflow.agent decorator accepting budget, compliance, and KPI weights. [@claim:clm_1e1d1698d9b25d73fec4a6cd5cdb1cc13948cbf4bd3b41cd829227e10d5996d4]
- GPT-5 streaming requires OpenAI organization verification, while non-streaming GPT-5 works for all users; basic examples work without verification since GPT-5 is only called when needed. [@claim:clm_231d49f38fa674438b63ed81870c72d683bbaeb8a244a74cc71e880751107f4f]
- The README reports benchmark-based cost savings of 69% on MT-Bench, 93% on GSM8K, 52% on MMLU, and 80% on TruthfulQA while retaining 96% GPT-5 quality. [@claim:clm_329a04d23f32e682d8a5bb4fe175a0a49de9f90baf8ac4b92fafd9a4b3fe54d4]
- At runtime the harness can enforce decisions with four actions: allow, switch_model, deny_tool, and stop, based on current context and policy state. [@claim:clm_650e40919bad9bc58ecb009b7e7abec0cf7b6bd1c3ff193cbd986c41e8cfae46]
- The Hermes integration exposes HermesDelegationRouter and HermesDelegationRequest, returning a structured routing decision (reason, confidence, domain, complexity, model) before Hermes spawns a subagent, while Hermes keeps credentials, base URLs, and fallback chains. [@claim:clm_75614c2ff2fd8bcd4b4b1aca27120f9d8809b95a9f9c29763473896fcb64b32b]
- cascadeflow is positioned as an in-process intelligence layer operating inside the agent execution loop rather than at the HTTP request boundary like external proxies. [@claim:clm_ac723b9c4e4dbb6552dde2862cc9d1013bf6ce726fe9214be03f9524f730f63f]
- A drop-in gateway for existing OpenAI/Anthropic clients can be started with 'python -m cascadeflow.server --mode auto --port 8084'. [@claim:clm_d21b758dfb2ab084ea5668c40b8111cae9360a3e726c0cf1d78d8197bf184aa2]
- The core mechanism is speculative execution with quality validation: run a cheap drafter first, validate responses against configurable thresholds, and escalate to a larger model only when validation fails. [@claim:clm_e6a7c744c8bae06c0de0284053194c022af1f65f2bed1cfc23ac739f5200a839]
- ML-based semantic quality validation is optional: Python via cascadeflow[semantic] (FastEmbed, ~80MB model) and TypeScript via @cascadeflow/ml with @huggingface/transformers (BGE-small-en-v1.5 embeddings, auto-downloaded). [@claim:clm_e79390dea62e5dc89e2dd661c9209b7e88afff7ff5de9e4ea2a6d65031ce9a30]
- The n8n integration provides two community nodes: a CascadeFlow (Model) sub-node drop-in for Chain/LLM nodes and a standalone CascadeFlow Agent node supporting tool calling, memory, and multi-step reasoning. [@claim:clm_ed6f8462c639ef3299732d00dbe13fb75379e32d87313b344511a0d45a778ee3]
<!-- rcw:end owner=source:src_4e7fb2ca145e59549b3c6c8f9fdd1c22 block=evidence -->

## Researcher notes

