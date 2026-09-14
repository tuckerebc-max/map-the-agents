# locoremind/locooperator -- full detail

[Back to orientation](locooperator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/locoremind/locooperator/b185a4198e4a3a2d8655120513326d8b1b487872/85279ae690b3ef4c.json](../../../wiki/dossiers/locoremind/locooperator/b185a4198e4a3a2d8655120513326d8b1b487872/85279ae690b3ef4c.json)

## specifications (1 claim(s))

- [observation/documented] LocoOperator-4B is a 4B-parameter tool-calling agent distilled from Qwen3-Coder-Next, built on the Qwen3-4B-Instruct-2507 base model. -- evidence: [README.md#L41-L41](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L41-L41), [README.md#L18-L18](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L18-L18), [README.md#L45-L54](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L45-L54) (`clm_0993b4af6c095cc5124645c59b6fcd4b99886fc948ad352c6eaa03527cf6dfb7`)

## components (1 claim(s))

- [observation/documented] The repo ships a hybrid pipeline: a proxy (scripts/proxy.py) converts Anthropic Messages API to OpenAI Chat Completions, parses the model's tool-call output into tool_use blocks, and falls back to OpenRouter on context overflow. -- evidence: [README.md#L166-L169](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L166-L169), [README.md#L157-L157](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L157-L157) (`clm_7664f79761b24b9ab9cea6dd5b3d33437142cac1bb29d32e9128551814cbcdfe`)

## design-choices (1 claim(s))

- [observation/documented] The model is positioned as a local sub-agent (explorer) in a two-tier agent loop, with a main agent delegating codebase exploration to keep API cost and latency low. -- evidence: [README.md#L74-L74](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L74-L74), [README.md#L68-L68](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L68-L68) (`clm_b02a476a0dfbb18f01cc3b71b5deca095c97b00cf6ce02eb71edc75de09e3ce6`)

## workflows (2 claim(s))

- [observation/documented] Usage workflow: place the GGUF at models/LocoOperator-4B-GGUF, put target repos under data/repos, add tab-separated query files, then run scripts/test_single.sh or scripts/analyze.sh for batch analysis. -- evidence: [README.md#L188-L188](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L188-L188), [README.md#L200-L202](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L200-L202), [README.md#L190-L190](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L190-L190), [README.md#L208-L214](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L208-L214), [README.md#L194-L196](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L194-L196) (`clm_c74efa6312f11121d44a7a5a049b647d331fb2a431241ad2f6716133d8c8c2dd`)
- [observation/documented] Recommended serving settings are a ~50K context size, max 10 turns, and temperature 0.7; .claude/settings.local.json is auto-generated from the .env key on first run. -- evidence: [README.md#L149-L153](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L149-L153), [README.md#L186-L186](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L186-L186) (`clm_c7dd26b7a0105a853a231a9ba4375e1d5e8a67b7cdc618c597857a4a32c58814`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] It emits structured tool-call JSON for Read, Grep, Glob, Bash, Write, Edit, and Task (subagent delegation). -- evidence: [README.md#L60-L64](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L60-L64) (`clm_367a37b5379998ad680ae90c2b1c408c7ea602ca61c80eb850debe2d38079dd8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] In the pipeline, the main agent runs as a cloud model while spawned subagents are routed by the proxy to the local llama-server, with automatic OpenRouter fallback if context limits or a 10-turn cap are exceeded. -- evidence: [README.md#L164-L164](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L164-L164), [README.md#L159-L162](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L159-L162) (`clm_8a07b94d8fed15e8b9b202c016b90a93384161f0581dda102024bb09ff62c2ef`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] On 65 multi-turn samples from open-source projects, the model scored 100% tool-call presence alignment, 65.6% first tool-type match, and 100% JSON validity and argument syntax correctness. -- evidence: [README.md#L78-L78](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L78-L78), [README.md#L84-L89](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L84-L89) (`clm_71361a60c2d41794e71d6adcdf9eb27e66304d60d3c6b55b5469ffa5d9d9354c`)
- [observation/documented] Compared to its teacher, the model produced 76 tool calls versus 89 across the 65 eval samples, and the teacher showed 87.6% argument syntax validity versus the student's 100%. -- evidence: [README.md#L115-L118](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L115-L118), [README.md#L99-L107](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L99-L107) (`clm_ba6295096fdfb15d005fb5c48dd1b768537b3c70e09873b0e95c77ae704eac4d`)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites include Claude Code, llama.cpp, uv, and an OpenRouter API key; the GGUF model is served locally via llama-server. -- evidence: [README.md#L140-L145](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L140-L145), [README.md#L128-L131](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L128-L131) (`clm_c0e79c87b4f9b3c6f52bedd60f4ee6a40b21622c60e02dcb8b27e3aae6a492de`)
- [observation/documented] Training used full-parameter SFT on 170,356 multi-turn samples with MS-SWIFT on 4x NVIDIA H200 GPUs, BF16 precision, max sequence length 16,384, for about 25 hours. -- evidence: [README.md#L246-L262](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L246-L262), [README.md#L45-L54](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L45-L54) (`clm_854347d60cd9f8d6b8234e4a261cd441eafaa2551a0213e5c9df0df8a1d8f8a3`)

## limitations (1 claim(s))

- [observation/documented] Documented limitations include imperfect first-tool-type match (65.6%), fewer parallel tool calls than the teacher, a possible over-preference for Bash over Read, and evaluation limited to only 65 samples. -- evidence: [README.md#L268-L271](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L268-L271) (`clm_f92bfeddde648372087d7ce0ce0413f84d064a6b86bac9e6f438a012dae5937a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

