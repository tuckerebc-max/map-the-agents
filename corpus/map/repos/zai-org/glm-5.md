# zai-org/glm-5

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 008de4dbcc22 @ 2d38f9b696eeac7f

## Summary (orientation draft, not independently verified)

The repository is a README-centric release hub for the GLM-5 model family (GLM-5 through GLM-5.3-Flash), documenting model sizes, architectures, benchmark results, deployment and fine-tuning frameworks, and inference parameters. No agent runtime code is evidenced in the provided slices.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] GLM-5 scales from GLM-4.5's 355B parameters (32B active) to 744B parameters (40B active), with pre-training data increased from 23T to 28.5T tokens. -- evidence: [README.md#L59-L59](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L59-L59)
  - [observation/documented] Downloadable checkpoints include GLM-5.3 and GLM-5.3-BF16 at 744B-A40B, and GLM-5.3-Flash and its BF16 variant at 320B-A18B, hosted on Hugging Face and ModelScope. -- evidence: [README.md#L75-L86](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L75-L86)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] GLM-5.3-Flash uses a newly trained base model with a hybrid sparse-plus-linear attention architecture and Manifold-Constrained Hyper-Connections (mHC), trained on a 30T-token multimodal corpus. -- evidence: [README.md#L28-L28](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L28-L28)
  - [observation/documented] GLM-5.2 introduces IndexShare, reusing one indexer across every four sparse attention layers to cut per-token FLOPs 2.9x at 1M context, plus an improved MTP layer for speculative decoding. -- evidence: [README.md#L36-L39](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L36-L39)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] GLM-5.3 and GLM-5.3-Flash accept a reasoning_effort parameter with low, high, and max levels, defaulting to max when unset or invalid; GLM-5.2 accepts only high and max. -- evidence: [README.md#L111-L113](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L111-L113)
  - [observation/documented] In the GLM-5.3 and GLM-5.3-Flash chat template, clear_thinking defaults to false when not passed, and users are told to pass true explicitly for chat scenarios. -- evidence: [README.md#L111-L113](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L111-L113)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports GLM-5.2 scoring 81.0 on Terminal-Bench 2.1 and 62.1 on SWE-bench Pro, and GLM-5 ranking first among open-source models on Vending Bench 2 with a $4,432 final balance. -- evidence: [README.md#L43-L43](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L43-L43), [README.md#L69-L69](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L69-L69)
- dependencies (3 claim(s)):
  - [observation/documented] The repository's requirements.txt pins transformers>=5.15.0, pre-commit>=4.6.2, and accelerate>=1.14.0. -- evidence: [requirements.txt#L1-L3](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/requirements.txt#L1-L3)
  - [observation/documented] Inference is documented for SGLang, vLLM, TokenSpeed, Transformers, KTransformers, and Unsloth, with Ascend NPU deployment via vLLM-Ascend, xLLM, and SGLang. -- evidence: [README.md#L92-L97](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L92-L97), [README.md#L101-L106](https://github.com/zai-org/GLM-5/blob/008de4dbcc220032eb9b80a9a9802afad46a4053/README.md#L101-L106)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](glm-5.detail.md) for every claim.)

Metadata and full claim list: [full detail](glm-5.detail.md)
Human notes ([notes](glm-5.notes.md), never overwritten by build)

[Back to map index](../../index.md)
