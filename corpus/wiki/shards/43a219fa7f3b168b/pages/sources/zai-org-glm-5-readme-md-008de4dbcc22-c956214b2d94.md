---
access: public
aliases: []
claim_ids:
- clm_05dbf8b39d3e5d05976d17a83f1c330f7efe34e6b3bf64a06198fcf0d82e6253
- clm_125befeb9cf2ee0a43d6df375387ef907dc471cd44a6d8fb5fa91aa574b04450
- clm_19182cd407bcef9682c95b578e5e73ebbaecf6ea5fce6ed5d43ec4ba19d9682b
- clm_2b05b74e615f29dcd643d9df8a1fa4a0da0600d873fa8f4aeb63b4f2b38faaff
- clm_3f0181d94c292def495457ced165dce23bef3f86f86fe8261bc19b22ac2afbe8
- clm_68e9c18d840cbe2ae2ec4bdd665510bf5e9c75ba93dd4c8547dee11988d2f1c1
- clm_6a17be0bab0b2728b34e79532ea3aa27ece77e1500cb1b4cd5d6dcf7305239ac
- clm_84f7f367239052e1a5a0c827caddd4b5c2c28daf2e6a0881e5f089aaee0c5518
- clm_96f0de77cb416c42b2ebbd18d671be1973e10b6cedc0b326584c0b41c84be424
- clm_98f6fa89d48c61e4eb80d21f34eebcd512fe478febf0fadd79ab1613324a3b87
- clm_c5ad130415e8988127d72e927164221a73a5d5f0e6c34c74c062f1b562c4202f
maturity: draft
page_id: pg_9051d9cd7458525a8219c956214b2d94
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f04119a0333a56eba145d8a1fd343519
title: zai-org/GLM-5/README.md @ 008de4dbcc22
updated_at: '2026-09-14T04:33:37Z'
---

# zai-org/GLM-5/README.md @ 008de4dbcc22

<!-- rcw:begin owner=source:src_f04119a0333a56eba145d8a1fd343519 block=evidence -->
- GLM-5.3 and GLM-5.3-Flash accept a reasoning_effort parameter with low, high, and max levels, defaulting to max when unset or invalid; GLM-5.2 accepts only high and max. [@claim:clm_05dbf8b39d3e5d05976d17a83f1c330f7efe34e6b3bf64a06198fcf0d82e6253]
- GLM-5.2 delivers a solid 1M-token context and offers multiple thinking-effort levels to balance performance and latency. [@claim:clm_125befeb9cf2ee0a43d6df375387ef907dc471cd44a6d8fb5fa91aa574b04450]
- GLM-5.3-Flash uses a newly trained base model with a hybrid sparse-plus-linear attention architecture and Manifold-Constrained Hyper-Connections (mHC), trained on a 30T-token multimodal corpus. [@claim:clm_19182cd407bcef9682c95b578e5e73ebbaecf6ea5fce6ed5d43ec4ba19d9682b]
- Fine-tuning is supported via Slime (v0.3.0+), the GLM team's RL framework, and ms-swift (v4.4.0+) supporting SFT, PPO, and GRPO. [@claim:clm_2b05b74e615f29dcd643d9df8a1fa4a0da0600d873fa8f4aeb63b4f2b38faaff]
- Inference is documented for SGLang, vLLM, TokenSpeed, Transformers, KTransformers, and Unsloth, with Ascend NPU deployment via vLLM-Ascend, xLLM, and SGLang. [@claim:clm_3f0181d94c292def495457ced165dce23bef3f86f86fe8261bc19b22ac2afbe8]
- GLM-5 scales from GLM-4.5's 355B parameters (32B active) to 744B parameters (40B active), with pre-training data increased from 23T to 28.5T tokens. [@claim:clm_68e9c18d840cbe2ae2ec4bdd665510bf5e9c75ba93dd4c8547dee11988d2f1c1]
- Downloadable checkpoints include GLM-5.3 and GLM-5.3-BF16 at 744B-A40B, and GLM-5.3-Flash and its BF16 variant at 320B-A18B, hosted on Hugging Face and ModelScope. [@claim:clm_6a17be0bab0b2728b34e79532ea3aa27ece77e1500cb1b4cd5d6dcf7305239ac]
- In the GLM-5.3 and GLM-5.3-Flash chat template, clear_thinking defaults to false when not passed, and users are told to pass true explicitly for chat scenarios. [@claim:clm_84f7f367239052e1a5a0c827caddd4b5c2c28daf2e6a0881e5f089aaee0c5518]
- GLM-5.2 introduces IndexShare, reusing one indexer across every four sparse attention layers to cut per-token FLOPs 2.9x at 1M context, plus an improved MTP layer for speculative decoding. [@claim:clm_96f0de77cb416c42b2ebbd18d671be1973e10b6cedc0b326584c0b41c84be424]
- The README reports GLM-5.2 scoring 81.0 on Terminal-Bench 2.1 and 62.1 on SWE-bench Pro, and GLM-5 ranking first among open-source models on Vending Bench 2 with a $4,432 final balance. [@claim:clm_98f6fa89d48c61e4eb80d21f34eebcd512fe478febf0fadd79ab1613324a3b87]
- GLM-5 integrates DeepSeek Sparse Attention (DSA) to reduce deployment cost while preserving long-context capacity. [@claim:clm_c5ad130415e8988127d72e927164221a73a5d5f0e6c34c74c062f1b562c4202f]
<!-- rcw:end owner=source:src_f04119a0333a56eba145d8a1fd343519 block=evidence -->

## Researcher notes

