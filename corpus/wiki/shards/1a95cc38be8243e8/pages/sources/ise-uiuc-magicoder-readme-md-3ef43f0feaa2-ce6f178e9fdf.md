---
access: public
aliases: []
claim_ids:
- clm_04fa35283f5d0c0c3668d9c5aa4cf857c01f2d7fda3b4a1354836c88e5dde203
- clm_1a68a9f0d6b5a2d0d26c942a2eba31ee0e0d6c44cb06f532f62b307e331429e7
- clm_57f7f21ada92fbd5dc6bbefac25de08c0dc646b357623b4aabcc0c5b5c4d25c2
- clm_6010f2b10222feb563e1e7d7fb1d7b46ac444feffd5a6e556c4031f159e92e69
- clm_7c6962959d5426a7c16d1f753046888594191b8984be38b6f421caae92ecbb35
- clm_9f4b7da26647e13d2ecd2c3335944c76fdc9e8f3b6fc80dc0ee7451009c16ce4
- clm_b2543392a1cc9d0e416791fb19e3e844107dd88aba2ae419e478b4f1a22be3f2
- clm_ba5ae804e9e253481c0f2304c95329e181bdde23b6ac3686015635cb5c2e7483
- clm_daf03888311fd7aa71a8380ff2f79d44d3182986256671abbee2febde7680be3
- clm_e77b1f1c9dfa1f589f71ad2f891fa3012967a4f90b32027f3153d3db17dbb278
maturity: draft
page_id: pg_9833333dc6245d10a7dace6f178e9fdf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0cbc439056455031a479acadd58a3459
title: ise-uiuc/magicoder/README.md @ 3ef43f0feaa2
updated_at: '2026-09-14T03:59:17Z'
---

# ise-uiuc/magicoder/README.md @ 3ef43f0feaa2

<!-- rcw:begin owner=source:src_0cbc439056455031a479acadd58a3459 block=evidence -->
- Models are trained on synthetic data from OpenAI models, so users are directed to consider OpenAI's terms of use; the models are stated not to compete with OpenAI commercial products. [@claim:clm_04fa35283f5d0c0c3668d9c5aa4cf857c01f2d7fda3b4a1354836c88e5dde203]
- Magicoder is a family of code models built with OSS-Instruct, an approach that uses open-source code snippets to generate instruction data for code. [@claim:clm_1a68a9f0d6b5a2d0d26c942a2eba31ee0e0d6c44cb06f532f62b307e331429e7]
- Models are prompted with a template containing a system-style preamble plus '@@ Instruction' and '@@ Response' sections, usable via a Hugging Face transformers text-generation pipeline. [@claim:clm_57f7f21ada92fbd5dc6bbefac25de08c0dc646b357623b4aabcc0c5b5c4d25c2]
- The quick-start and demo code imply runtime dependencies on transformers, torch (bfloat16, CUDA device), and gradio. [@claim:clm_6010f2b10222feb563e1e7d7fb1d7b46ac444feffd5a6e556c4031f159e92e69]
- The README warns that Magicoders may make errors, produce misleading content, or struggle with tasks unrelated to coding. [@claim:clm_7c6962959d5426a7c16d1f753046888594191b8984be38b6f421caae92ecbb35]
- Two datasets are published: Magicoder-OSS-Instruct-75K (generated with gpt-3.5-turbo-1106, used for both model series) and Magicoder-Evol-Instruct-110K (decontaminated redistribution of evol-codealpaca-v1, used for the -S models). [@claim:clm_9f4b7da26647e13d2ecd2c3335944c76fdc9e8f3b6fc80dc0ee7451009c16ce4]
- The README reports HumanEval(+) and MBPP(+) scores per model, with Magicoder-S-DS-6.7B at 76.8 (70.7) on HumanEval(+), and claims it outperforms gpt-3.5-turbo-1106 and Gemini Ultra on HumanEval. [@claim:clm_b2543392a1cc9d0e416791fb19e3e844107dd88aba2ae419e478b4f1a22be3f2]
- A hosted Gradio demo (Magicoder Playground) is available on Hugging Face Spaces, and a local Gradio demo server script is provided under demo/. [@claim:clm_ba5ae804e9e253481c0f2304c95329e181bdde23b6ac3686015635cb5c2e7483]
- Four released models are listed: Magicoder-CL-7B and Magicoder-S-CL-7B (Llama2 license) and Magicoder-DS-6.7B and Magicoder-S-DS-6.7B (DeepSeek license), hosted on Hugging Face. [@claim:clm_daf03888311fd7aa71a8380ff2f79d44d3182986256671abbee2febde7680be3]
- Magicoder-DS models are built on DeepSeek-Coder base models and Magicoder-CL models on CodeLlama; StarCoder is credited for data decontamination. [@claim:clm_e77b1f1c9dfa1f589f71ad2f891fa3012967a4f90b32027f3153d3db17dbb278]
<!-- rcw:end owner=source:src_0cbc439056455031a479acadd58a3459 block=evidence -->

## Researcher notes

