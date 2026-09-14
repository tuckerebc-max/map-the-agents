---
access: public
aliases: []
claim_ids:
- clm_109c939154c2848f0655334d8e7f4e02f92e7ba418b044de76fe53d1554f0f3a
- clm_2747031c25e77111c11080a40941f1a18fcaa0f43bf5a181fa5fd0e03855105a
- clm_31d31f36e450ceef441b1ec570d3babe5aa2f155f073fd14119d813267ebf1d8
- clm_3ea9906cd3d23c004b82d33d2d5e2f584774eb0e71cf86a17f410a8cfa6b8b40
- clm_551e8021d8b300c19859550e0f6a632af04b9a2db97bebc609283a06d515aea7
- clm_64e412b2c005ef9438889441f89bd7854a1102d5ea15c2b2a9bf018402042fd4
- clm_6712bf6b8efbdf9f184a2e304f9097b1f6b969f1075b6a640bead1ab0722c00a
- clm_6a5fea4bd8fa2828ee66c7536c3f72f1f1d98beb770e9abcc73f5ff48b1d8f54
- clm_a9dd57dcc2fb0b74edb57d8e2b922427260680631f908ecb86042c1e7b8bb5f5
- clm_acab2812b0ee0d6881c84aeb8ccc6062fc5252a31b1053ffef255cff5d0f61db
- clm_b1f8534d1555b0ab876b5c01db645fd21d2d954cd029ca2046b45c75c24182ce
- clm_bc7ccbc0df959e45dc347edad8608ea63890a4a67fd8df124293ea2872d20db0
- clm_cd71cf3373611f9938e2b1b7274e650c05672a270262bc71d954c9cecce32122
- clm_e5be4c02de8c9ba323c4fb83989fef0aadc87108d36825666249e0be78525ae7
- clm_e99f0be5ab3cbf2d4c0adff059ffc7308a9a90162d674837e07ef251bb01b3b7
- clm_f945930fdae2c8c9adc72bd9e504837dd99552fa1265daf776f39dd095db2385
maturity: draft
page_id: pg_632a2cb52ba5576181df8e8c4c65aa91
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b25a369e349f5972be07fea131245a25
title: juyterman1000/entroly/README.md @ 9bab5850955c
updated_at: '2026-09-14T04:02:43Z'
---

# juyterman1000/entroly/README.md @ 9bab5850955c

<!-- rcw:begin owner=source:src_b25a369e349f5972be07fea131245a25 block=evidence -->
- A Rust-accelerated engine is available via PyO3 and WASM, and a standalone Rust binary can be built from entroly-core with cargo using the proxy feature. [@claim:clm_109c939154c2848f0655334d8e7f4e02f92e7ba418b044de76fe53d1554f0f3a]
- Output token reduction uses a three-layer pipeline: effort classification steers verbosity directives, max_tokens budgets cap generation, and post-generation distillation trims filler. [@claim:clm_2747031c25e77111c11080a40941f1a18fcaa0f43bf5a181fa5fd0e03855105a]
- Repository development practice: contributors are directed to a reproducible development setup in CONTRIBUTING.md, and local installation plus the normal test suite need no API key. [@claim:clm_31d31f36e450ceef441b1ec570d3babe5aa2f155f073fd14119d813267ebf1d8]
- The MCP server is configured with environment flags such as ENTROLY_NO_DOCKER, ENTROLY_MCP_PASSIVE, and ENTROLY_MAX_FILES, and the MCP path is provider-neutral across many model vendors. [@claim:clm_3ea9906cd3d23c004b82d33d2d5e2f584774eb0e71cf86a17f410a8cfa6b8b40]
- Benchmark tables report accuracy retention with gpt-4o-mini and Wilson 95% CIs across NeedleInAHaystack, GSM8K, SQuAD 2.0, MMLU, TruthfulQA, and LongBench, with an average retention of 101.7%. [@claim:clm_551e8021d8b300c19859550e0f6a632af04b9a2db97bebc609283a06d515aea7]
- Stated good fits are large repos where agents see few files at a time, chatty multi-turn agents, and evidence-checked answers; tiny repos or prompts already within budget are cases to skip. [@claim:clm_64e412b2c005ef9438889441f89bd7854a1102d5ea15c2b2a9bf018402042fd4]
- If the native engine is missing, Entroly installs it from PyPI before measuring; this self-heal is the only outbound call of these commands and can be disabled with ENTROLY_NO_SELF_HEAL=1. [@claim:clm_6712bf6b8efbdf9f184a2e304f9097b1f6b969f1075b6a640bead1ab0722c00a]
- The README lists six research algorithms with named implementation files, including a provenance tracer (Python), and nkbe, causal, cognitive_bus, and resonance modules in a Rust core (entroly-core). [@claim:clm_6a5fea4bd8fa2828ee66c7536c3f72f1f1d98beb770e9abcc73f5ff48b1d8f54]
- The README candidly notes a regression: SQuAD 2.0 accuracy dropped from 80% to 72% with compression, and points users to entroly simulate for their own numbers. [@claim:clm_a9dd57dcc2fb0b74edb57d8e2b922427260680631f908ecb86042c1e7b8bb5f5]
- Cross-agent shared memory is a content-addressed store with SimHash deduplication and BM25 search, letting multiple agents share a knowledge base with provenance tracking. [@claim:clm_acab2812b0ee0d6881c84aeb8ccc6062fc5252a31b1053ffef255cff5d0f61db]
- The product runs as a CLI, Python/TypeScript SDK, MCP server, HTTP proxy, or library import, per the README's product-surface description. [@claim:clm_b1f8534d1555b0ab876b5c01db645fd21d2d954cd029ca2046b45c75c24182ce]
- The Python SDK exposes functions such as compress, compress_messages, optimize, shared_memory_write, and shared_memory_search, with budget and query parameters shown in examples. [@claim:clm_bc7ccbc0df959e45dc347edad8608ea63890a4a67fd8df124293ea2872d20db0]
- Entroly is described as a local-first AI token-efficiency and context-assurance layer offering budgeted evidence selection, recoverable compression, content-addressed recovery, and auditable receipts. [@claim:clm_cd71cf3373611f9938e2b1b7274e650c05672a270262bc71d954c9cecce32122]
- A WITNESS hallucination detector is reported at 84.92% accuracy and 0.7976 AUROC on 20,000 HaluEval-QA decisions, run locally without an API. [@claim:clm_e5be4c02de8c9ba323c4fb83989fef0aadc87108d36825666249e0be78525ae7]
- The README states savings are not a universal guarantee, that MCP-only integrations remain tools an agent may skip, and that provider-bound savings exist only when requests traverse an Entroly-controlled route. [@claim:clm_e99f0be5ab3cbf2d4c0adff059ffc7308a9a90162d674837e07ef251bb01b3b7]
- Authorization in the govern subsystem is deny-by-default, and every denial names the policy and reason; identity tokens are unsigned unless ENTROLY_IDENTITY_KEY is set. [@claim:clm_f945930fdae2c8c9adc72bd9e504837dd99552fa1265daf776f39dd095db2385]
<!-- rcw:end owner=source:src_b25a369e349f5972be07fea131245a25 block=evidence -->

## Researcher notes

