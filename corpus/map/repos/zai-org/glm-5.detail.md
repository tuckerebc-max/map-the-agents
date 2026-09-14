# zai-org/glm-5 -- full detail

[Back to orientation](glm-5.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zai-org/glm-5/008de4dbcc220032eb9b80a9a9802afad46a4053/2d38f9b696eeac7f.json](../../../wiki/dossiers/zai-org/glm-5/008de4dbcc220032eb9b80a9a9802afad46a4053/2d38f9b696eeac7f.json)

## specifications (3 claim(s))

- [observation/documented] GLM-5 scales from GLM-4.5's 355B parameters (32B active) to 744B parameters (40B active), with pre-training data increased from 23T to 28.5T tokens. -- evidence: [README.md#L59-L59](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L59-L59) (`clm_68e9c18d840cbe2ae2ec4bdd665510bf5e9c75ba93dd4c8547dee11988d2f1c1`)
- [observation/documented] Downloadable checkpoints include GLM-5.3 and GLM-5.3-BF16 at 744B-A40B, and GLM-5.3-Flash and its BF16 variant at 320B-A18B, hosted on Hugging Face and ModelScope. -- evidence: [README.md#L75-L86](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L75-L86) (`clm_6a17be0bab0b2728b34e79532ea3aa27ece77e1500cb1b4cd5d6dcf7305239ac`)
- [observation/documented] GLM-5.2 delivers a solid 1M-token context and offers multiple thinking-effort levels to balance performance and latency. -- evidence: [README.md#L34-L34](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L34-L34), [README.md#L36-L39](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L36-L39) (`clm_125befeb9cf2ee0a43d6df375387ef907dc471cd44a6d8fb5fa91aa574b04450`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] GLM-5.3-Flash uses a newly trained base model with a hybrid sparse-plus-linear attention architecture and Manifold-Constrained Hyper-Connections (mHC), trained on a 30T-token multimodal corpus. -- evidence: [README.md#L28-L28](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L28-L28) (`clm_19182cd407bcef9682c95b578e5e73ebbaecf6ea5fce6ed5d43ec4ba19d9682b`)
- [observation/documented] GLM-5.2 introduces IndexShare, reusing one indexer across every four sparse attention layers to cut per-token FLOPs 2.9x at 1M context, plus an improved MTP layer for speculative decoding. -- evidence: [README.md#L36-L39](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L36-L39) (`clm_96f0de77cb416c42b2ebbd18d671be1973e10b6cedc0b326584c0b41c84be424`)
- [observation/documented] GLM-5 integrates DeepSeek Sparse Attention (DSA) to reduce deployment cost while preserving long-context capacity. -- evidence: [README.md#L59-L59](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L59-L59) (`clm_c5ad130415e8988127d72e927164221a73a5d5f0e6c34c74c062f1b562c4202f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] GLM-5.3 and GLM-5.3-Flash accept a reasoning_effort parameter with low, high, and max levels, defaulting to max when unset or invalid; GLM-5.2 accepts only high and max. -- evidence: [README.md#L111-L113](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L111-L113) (`clm_05dbf8b39d3e5d05976d17a83f1c330f7efe34e6b3bf64a06198fcf0d82e6253`)
- [observation/documented] In the GLM-5.3 and GLM-5.3-Flash chat template, clear_thinking defaults to false when not passed, and users are told to pass true explicitly for chat scenarios. -- evidence: [README.md#L111-L113](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L111-L113) (`clm_84f7f367239052e1a5a0c827caddd4b5c2c28daf2e6a0881e5f089aaee0c5518`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports GLM-5.2 scoring 81.0 on Terminal-Bench 2.1 and 62.1 on SWE-bench Pro, and GLM-5 ranking first among open-source models on Vending Bench 2 with a $4,432 final balance. -- evidence: [README.md#L43-L43](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L43-L43), [README.md#L69-L69](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L69-L69) (`clm_98f6fa89d48c61e4eb80d21f34eebcd512fe478febf0fadd79ab1613324a3b87`)

## dependencies (3 claim(s))

- [observation/documented] The repository's requirements.txt pins transformers>=5.15.0, pre-commit>=4.6.2, and accelerate>=1.14.0. -- evidence: [requirements.txt#L1-L3](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/requirements.txt#L1-L3) (`clm_18f6d5da58dff9d07dd1e6ebddc7e5e5a09cf36e5353e346548d860f91357a4d`)
- [observation/documented] Inference is documented for SGLang, vLLM, TokenSpeed, Transformers, KTransformers, and Unsloth, with Ascend NPU deployment via vLLM-Ascend, xLLM, and SGLang. -- evidence: [README.md#L92-L97](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L92-L97), [README.md#L101-L106](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L101-L106) (`clm_3f0181d94c292def495457ced165dce23bef3f86f86fe8261bc19b22ac2afbe8`)
- [observation/documented] Fine-tuning is supported via Slime (v0.3.0+), the GLM team's RL framework, and ms-swift (v4.4.0+) supporting SFT, PPO, and GRPO. -- evidence: [README.md#L119-L120](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L119-L120) (`clm_2b05b74e615f29dcd643d9df8a1fa4a0da0600d873fa8f4aeb63b4f2b38faaff`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

