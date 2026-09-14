# ise-uiuc/magicoder -- full detail

[Back to orientation](magicoder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ise-uiuc/magicoder/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/bc9c10f2a873c504.json](../../../wiki/dossiers/ise-uiuc/magicoder/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/bc9c10f2a873c504.json)

## specifications (1 claim(s))

- [observation/documented] Two datasets are published: Magicoder-OSS-Instruct-75K (generated with gpt-3.5-turbo-1106, used for both model series) and Magicoder-Evol-Instruct-110K (decontaminated redistribution of evol-codealpaca-v1, used for the -S models). -- evidence: [README.md#L71-L72](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L71-L72) (`clm_9f4b7da26647e13d2ecd2c3335944c76fdc9e8f3b6fc80dc0ee7451009c16ce4`)

## components (2 claim(s))

- [observation/documented] Magicoder is a family of code models built with OSS-Instruct, an approach that uses open-source code snippets to generate instruction data for code. -- evidence: [README.md#L32-L33](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L32-L33) (`clm_1a68a9f0d6b5a2d0d26c942a2eba31ee0e0d6c44cb06f532f62b307e331429e7`)
- [observation/documented] Four released models are listed: Magicoder-CL-7B and Magicoder-S-CL-7B (Llama2 license) and Magicoder-DS-6.7B and Magicoder-S-DS-6.7B (DeepSeek license), hosted on Hugging Face. -- evidence: [README.md#L45-L50](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L45-L50) (`clm_daf03888311fd7aa71a8380ff2f79d44d3182986256671abbee2febde7680be3`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the developer guide (marked WIP) documents a pipeline of scripts for data generation (generate_data.py with OPENAI_API_KEY), cleaning/decontamination, preprocessing, and instruction tuning via accelerate launch of magicoder.train. -- evidence: [README-DEV.md#L63-L84](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L63-L84), [README-DEV.md#L10-L16](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L10-L16), [README-DEV.md#L8-L8](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L8-L8), [README-DEV.md#L35-L41](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L35-L41), [README-DEV.md#L61-L61](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L61-L61), [README-DEV.md#L49-L55](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L49-L55), [README-DEV.md#L32-L33](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L32-L33), [README-DEV.md#L3-L4](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L3-L4) (`clm_7fde25c7385eb3c15f5ebabe7518367c9517bcbbd40d955c36827bb3fbb654cc`)
- [observation/documented] Repository development practice: Magicoder-S is produced by continuing training from the Magicoder checkpoint on Evol-Instruct data with a shorter max sequence length (1024 vs 1216), using bf16, adafactor, and linear LR scheduling. -- evidence: [README-DEV.md#L63-L84](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L63-L84), [README-DEV.md#L86-L86](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L86-L86), [README-DEV.md#L88-L110](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README-DEV.md#L88-L110) (`clm_2c5bc321221fb56ffdaaaf4560e09b682c5d42a313497f8b70fc25ab2d8d611e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Models are prompted with a template containing a system-style preamble plus '@@ Instruction' and '@@ Response' sections, usable via a Hugging Face transformers text-generation pipeline. -- evidence: [README.md#L80-L80](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L80-L80), [README.md#L76-L78](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L76-L78), [README.md#L85-L86](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L85-L86), [README.md#L90-L99](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L90-L99), [README.md#L82-L83](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L82-L83) (`clm_57f7f21ada92fbd5dc6bbefac25de08c0dc646b357623b4aabcc0c5b5c4d25c2`)
- [observation/documented] A hosted Gradio demo (Magicoder Playground) is available on Hugging Face Spaces, and a local Gradio demo server script is provided under demo/. -- evidence: [README.md#L55-L55](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L55-L55), [README.md#L59-L59](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L59-L59) (`clm_ba5ae804e9e253481c0f2304c95329e181bdde23b6ac3686015635cb5c2e7483`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports HumanEval(+) and MBPP(+) scores per model, with Magicoder-S-DS-6.7B at 76.8 (70.7) on HumanEval(+), and claims it outperforms gpt-3.5-turbo-1106 and Gemini Ultra on HumanEval. -- evidence: [README.md#L45-L50](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L45-L50), [README.md#L36-L38](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L36-L38) (`clm_b2543392a1cc9d0e416791fb19e3e844107dd88aba2ae419e478b4f1a22be3f2`)

## dependencies (2 claim(s))

- [inference/documented] The quick-start and demo code imply runtime dependencies on transformers, torch (bfloat16, CUDA device), and gradio. -- evidence: [README.md#L61-L67](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L61-L67), [README.md#L76-L78](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L76-L78), [README.md#L90-L99](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L90-L99) (`clm_6010f2b10222feb563e1e7d7fb1d7b46ac444feffd5a6e556c4031f159e92e69`)
- [observation/documented] Magicoder-DS models are built on DeepSeek-Coder base models and Magicoder-CL models on CodeLlama; StarCoder is credited for data decontamination. -- evidence: [README.md#L188-L191](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L188-L191) (`clm_e77b1f1c9dfa1f589f71ad2f891fa3012967a4f90b32027f3153d3db17dbb278`)

## limitations (2 claim(s))

- [observation/documented] The README warns that Magicoders may make errors, produce misleading content, or struggle with tasks unrelated to coding. -- evidence: [README.md#L195-L195](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L195-L195) (`clm_7c6962959d5426a7c16d1f753046888594191b8984be38b6f421caae92ecbb35`)
- [observation/documented] Models are trained on synthetic data from OpenAI models, so users are directed to consider OpenAI's terms of use; the models are stated not to compete with OpenAI commercial products. -- evidence: [README.md#L197-L197](https://github.com/ise-uiuc/magicoder/blob/3ef43f0feaa2a48c3bb86d0b1f0d4482912d2e18/README.md#L197-L197) (`clm_04fa35283f5d0c0c3668d9c5aa4cf857c01f2d7fda3b4a1354836c88e5dde203`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

