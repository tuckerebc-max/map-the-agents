# mikotokawaii25/local-ai-code-assistant -- full detail

[Back to orientation](local-ai-code-assistant.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mikotokawaii25/local-ai-code-assistant/1ca5630df92515569ceae1f137f2453088c022b3/0b528688abe8a25c.json](../../../wiki/dossiers/mikotokawaii25/local-ai-code-assistant/1ca5630df92515569ceae1f137f2453088c022b3/0b528688abe8a25c.json)

## specifications (1 claim(s))

- [observation/documented] Stated system requirements: 16 GB RAM minimum (32 GB recommended), 6 GB VRAM minimum (12 GB+ recommended), 10 GB storage, on Windows 10, macOS 12+, or Linux kernel 5.x. -- evidence: [README.md#L80-L85](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L80-L85) (`clm_9ee4ea1bd53bc51a05e76708d5c818440eab719c683f18c2618a5c63107bc042`)

## components (1 claim(s))

- [observation/documented] A local-network collaboration feature shares loom sessions over WebSocket so team members can sync edits and model outputs without internet. -- evidence: [README.md#L44-L44](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L44-L44) (`clm_0c40d1f24190c39551ddf0eb50288376fb4e688991a5948ac280ddf563a1f0c2`)

## design-choices (1 claim(s))

- [observation/documented] CodeLoom is designed as an offline-only desktop tool that runs multiple open-source models locally with no cloud dependencies or data leaving the machine. -- evidence: [README.md#L5-L5](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L5-L5), [README.md#L7-L7](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L7-L7) (`clm_32a706b7df033f96e32085a3c5c379ef89a7b6dcd4cdf236c9b3d20a2ce2b8df`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Configuration is exposed through a loom_config.yaml file covering per-task model assignments, token budgets, sampling parameters, context-sharing rules, theme, and LAN-only remote access. -- evidence: [README.md#L99-L99](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L99-L99), [README.md#L101-L106](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L101-L106) (`clm_e23daa62e7c7ef158479c5e0c7640cd2454827c82c0006d018a3125029978433`)
- [observation/documented] Advanced users can write custom 'loom scripts' in Lua that define model interactions, thread switching, and output merging. -- evidence: [README.md#L108-L108](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L108-L108) (`clm_35c508f0a0ac363d91d79f270924eb2de42200a2c0f73dc8c1cd12c9d81d5a9a`)
- [observation/documented] The app indexes a codebase as context up to 100k tokens and splits it across model threads so each model sees a relevant slice. -- evidence: [README.md#L41-L41](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L41-L41) (`clm_5c841f4ee2958fee2f9985721b5678c5ba1ab77cfcd5b8451699182023252f48`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (3 claim(s))

- [observation/documented] The product supports up to five concurrent model sessions, each with its own context window, history, and parameters, and lets the user pick which thread's answer wins. -- evidence: [README.md#L26-L26](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L26-L26) (`clm_dc3d49f4d72e0242de79b014c31f7bc95b2f7ad73c8a491f7b2241555105694e`)
- [observation/documented] Context can be merged between model threads manually or automatically, e.g. passing a small model's draft to a larger model without copy/paste. -- evidence: [README.md#L29-L29](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L29-L29) (`clm_eede548c2c423cda8a9059c4286058050856f6a2402abcb014b28953613f2659`)
- [observation/documented] A 'loom' concept assigns a main 'warp' model for heavy tasks and auxiliary 'weft' models for fast tasks, with a cross-thread shuttle passing tokens between threads. -- evidence: [README.md#L57-L57](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L57-L57), [README.md#L59-L61](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L59-L61) (`clm_1f71f80423c143f50d67feb1216a3efc34453e6cfbfe1b8add349f0fc79d3414`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Inference runs via local backends including llama.cpp, ExLlama, and MLX, and models can be imported from Hugging Face, Ollama, or local GGUF/GPTQ files. -- evidence: [README.md#L17-L19](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L17-L19), [README.md#L35-L35](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L35-L35) (`clm_1aff519aae4c3939f1ef7a30b22f53aab0adc822cbaa6d4f0c5d110f2533646f`)
- [observation/documented] The project is MIT-licensed, and a disclaimer notes that orchestrated models carry their own licenses and usage terms for which users are responsible. -- evidence: [README.md#L164-L164](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L164-L164), [README.md#L143-L143](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L143-L143) (`clm_244f13b9d2eafcb0a93e09e9685de9f6edb0c1b608f1af51d9bcd9f6bdf14edd`)

## limitations (1 claim(s))

- [observation/documented] Per the FAQ, there is no cloud version by design, updates are manual downloads that only check a URL for version strings, and 7B models at 4-bit need at least 6 GB VRAM. -- evidence: [README.md#L135-L136](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L135-L136), [README.md#L138-L139](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L138-L139), [README.md#L129-L130](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L129-L130) (`clm_d6206c565ced58d367136d55323c4ceb868fff078f43f912fbc96d707a4d5259`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

