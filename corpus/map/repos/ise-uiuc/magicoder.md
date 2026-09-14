# ise-uiuc/magicoder

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3ef43f0feaa2 @ bc9c10f2a873c504

## Summary (orientation draft, not independently verified)

The snapshot is README-only documentation for Magicoder, a family of code LLMs trained via OSS-Instruct, with model checkpoints, benchmark numbers, demo/quick-start usage, and a WIP developer guide describing the data-generation and training pipeline.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Two datasets are published: Magicoder-OSS-Instruct-75K (generated with gpt-3.5-turbo-1106, used for both model series) and Magicoder-Evol-Instruct-110K (decontaminated redistribution of evol-codealpaca-v1, used for the -S models). -- evidence: [README.md#L71-L72](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L71-L72)
- components (2 claim(s)):
  - [observation/documented] Magicoder is a family of code models built with OSS-Instruct, an approach that uses open-source code snippets to generate instruction data for code. -- evidence: [README.md#L32-L33](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L32-L33)
  - [observation/documented] Four released models are listed: Magicoder-CL-7B and Magicoder-S-CL-7B (Llama2 license) and Magicoder-DS-6.7B and Magicoder-S-DS-6.7B (DeepSeek license), hosted on Hugging Face. -- evidence: [README.md#L45-L50](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L45-L50)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the developer guide (marked WIP) documents a pipeline of scripts for data generation (generate_data.py with OPENAI_API_KEY), cleaning/decontamination, preprocessing, and instruction tuning via accelerate launch of magicoder.train. -- evidence: [README-DEV.md#L63-L84](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L63-L84), [README-DEV.md#L10-L16](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L10-L16), [README-DEV.md#L8-L8](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L8-L8), [README-DEV.md#L35-L41](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L35-L41), [README-DEV.md#L61-L61](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L61-L61), [README-DEV.md#L49-L55](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L49-L55), [README-DEV.md#L32-L33](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L32-L33), [README-DEV.md#L3-L4](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L3-L4)
  - [observation/documented] Repository development practice: Magicoder-S is produced by continuing training from the Magicoder checkpoint on Evol-Instruct data with a shorter max sequence length (1024 vs 1216), using bf16, adafactor, and linear LR scheduling. -- evidence: [README-DEV.md#L63-L84](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L63-L84), [README-DEV.md#L86-L86](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L86-L86), [README-DEV.md#L88-L110](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L88-L110)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Models are prompted with a template containing a system-style preamble plus '@@ Instruction' and '@@ Response' sections, usable via a Hugging Face transformers text-generation pipeline. -- evidence: [README.md#L80-L80](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L80-L80), [README.md#L76-L78](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L76-L78), [README.md#L85-L86](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L85-L86), [README.md#L90-L99](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L90-L99), [README.md#L82-L83](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L82-L83)
  - [observation/documented] A hosted Gradio demo (Magicoder Playground) is available on Hugging Face Spaces, and a local Gradio demo server script is provided under demo/. -- evidence: [README.md#L55-L55](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L55-L55), [README.md#L59-L59](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L59-L59)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports HumanEval(+) and MBPP(+) scores per model, with Magicoder-S-DS-6.7B at 76.8 (70.7) on HumanEval(+), and claims it outperforms gpt-3.5-turbo-1106 and Gemini Ultra on HumanEval. -- evidence: [README.md#L45-L50](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L45-L50), [README.md#L36-L38](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L36-L38)
- dependencies (2 claim(s)):
  - [inference/documented] The quick-start and demo code imply runtime dependencies on transformers, torch (bfloat16, CUDA device), and gradio. -- evidence: [README.md#L61-L67](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L61-L67), [README.md#L76-L78](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L76-L78), [README.md#L90-L99](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L90-L99)
More evidence: [full detail](magicoder.detail.md)

Metadata and full claim list: [full detail](magicoder.detail.md)
Human notes ([notes](magicoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
