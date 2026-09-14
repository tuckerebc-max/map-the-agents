---
access: public
aliases: []
claim_ids:
- clm_0993b4af6c095cc5124645c59b6fcd4b99886fc948ad352c6eaa03527cf6dfb7
- clm_367a37b5379998ad680ae90c2b1c408c7ea602ca61c80eb850debe2d38079dd8
- clm_71361a60c2d41794e71d6adcdf9eb27e66304d60d3c6b55b5469ffa5d9d9354c
- clm_7664f79761b24b9ab9cea6dd5b3d33437142cac1bb29d32e9128551814cbcdfe
- clm_854347d60cd9f8d6b8234e4a261cd441eafaa2551a0213e5c9df0df8a1d8f8a3
- clm_8a07b94d8fed15e8b9b202c016b90a93384161f0581dda102024bb09ff62c2ef
- clm_b02a476a0dfbb18f01cc3b71b5deca095c97b00cf6ce02eb71edc75de09e3ce6
- clm_ba6295096fdfb15d005fb5c48dd1b768537b3c70e09873b0e95c77ae704eac4d
- clm_c0e79c87b4f9b3c6f52bedd60f4ee6a40b21622c60e02dcb8b27e3aae6a492de
- clm_c74efa6312f11121d44a7a5a049b647d331fb2a431241ad2f6716133d8c8c2dd
- clm_c7dd26b7a0105a853a231a9ba4375e1d5e8a67b7cdc618c597857a4a32c58814
- clm_f92bfeddde648372087d7ce0ce0413f84d064a6b86bac9e6f438a012dae5937a
maturity: draft
page_id: pg_16b1e0c47893528f83a3f085780e3854
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6589a788ac4d5c7f918a12146947a234
title: LocoreMind/LocoOperator/README.md @ b185a4198e4a
updated_at: '2026-09-14T04:06:56Z'
---

# LocoreMind/LocoOperator/README.md @ b185a4198e4a

<!-- rcw:begin owner=source:src_6589a788ac4d5c7f918a12146947a234 block=evidence -->
- LocoOperator-4B is a 4B-parameter tool-calling agent distilled from Qwen3-Coder-Next, built on the Qwen3-4B-Instruct-2507 base model. [@claim:clm_0993b4af6c095cc5124645c59b6fcd4b99886fc948ad352c6eaa03527cf6dfb7]
- It emits structured tool-call JSON for Read, Grep, Glob, Bash, Write, Edit, and Task (subagent delegation). [@claim:clm_367a37b5379998ad680ae90c2b1c408c7ea602ca61c80eb850debe2d38079dd8]
- On 65 multi-turn samples from open-source projects, the model scored 100% tool-call presence alignment, 65.6% first tool-type match, and 100% JSON validity and argument syntax correctness. [@claim:clm_71361a60c2d41794e71d6adcdf9eb27e66304d60d3c6b55b5469ffa5d9d9354c]
- The repo ships a hybrid pipeline: a proxy (scripts/proxy.py) converts Anthropic Messages API to OpenAI Chat Completions, parses the model's tool-call output into tool_use blocks, and falls back to OpenRouter on context overflow. [@claim:clm_7664f79761b24b9ab9cea6dd5b3d33437142cac1bb29d32e9128551814cbcdfe]
- Training used full-parameter SFT on 170,356 multi-turn samples with MS-SWIFT on 4x NVIDIA H200 GPUs, BF16 precision, max sequence length 16,384, for about 25 hours. [@claim:clm_854347d60cd9f8d6b8234e4a261cd441eafaa2551a0213e5c9df0df8a1d8f8a3]
- In the pipeline, the main agent runs as a cloud model while spawned subagents are routed by the proxy to the local llama-server, with automatic OpenRouter fallback if context limits or a 10-turn cap are exceeded. [@claim:clm_8a07b94d8fed15e8b9b202c016b90a93384161f0581dda102024bb09ff62c2ef]
- The model is positioned as a local sub-agent (explorer) in a two-tier agent loop, with a main agent delegating codebase exploration to keep API cost and latency low. [@claim:clm_b02a476a0dfbb18f01cc3b71b5deca095c97b00cf6ce02eb71edc75de09e3ce6]
- Compared to its teacher, the model produced 76 tool calls versus 89 across the 65 eval samples, and the teacher showed 87.6% argument syntax validity versus the student's 100%. [@claim:clm_ba6295096fdfb15d005fb5c48dd1b768537b3c70e09873b0e95c77ae704eac4d]
- Prerequisites include Claude Code, llama.cpp, uv, and an OpenRouter API key; the GGUF model is served locally via llama-server. [@claim:clm_c0e79c87b4f9b3c6f52bedd60f4ee6a40b21622c60e02dcb8b27e3aae6a492de]
- Usage workflow: place the GGUF at models/LocoOperator-4B-GGUF, put target repos under data/repos, add tab-separated query files, then run scripts/test_single.sh or scripts/analyze.sh for batch analysis. [@claim:clm_c74efa6312f11121d44a7a5a049b647d331fb2a431241ad2f6716133d8c8c2dd]
- Recommended serving settings are a ~50K context size, max 10 turns, and temperature 0.7; .claude/settings.local.json is auto-generated from the .env key on first run. [@claim:clm_c7dd26b7a0105a853a231a9ba4375e1d5e8a67b7cdc618c597857a4a32c58814]
- Documented limitations include imperfect first-tool-type match (65.6%), fewer parallel tool calls than the teacher, a possible over-preference for Bash over Read, and evaluation limited to only 65 samples. [@claim:clm_f92bfeddde648372087d7ce0ce0413f84d064a6b86bac9e6f438a012dae5937a]
<!-- rcw:end owner=source:src_6589a788ac4d5c7f918a12146947a234 block=evidence -->

## Researcher notes

