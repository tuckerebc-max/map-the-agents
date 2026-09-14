---
access: public
aliases: []
claim_ids:
- clm_0f50bed936b6fc60509ea0e8b8d7d94566b07b5b4d2867ac1d73cd3d2f39ab92
- clm_15225373ab6b02a6af098e07a169e0a5aa2f6ba02c934a6530438c73814fdc7d
- clm_29582caaf9aedfa78efd3a4230eac6e1066a8f2ee7f545876e6701f67e65a4af
- clm_2e5120412b67d99a363c9b4edaa7bf8681742c6f76b597211d28532052539922
- clm_32364b222df719e40fd2e48be29d5c9ca7c53d662de9924a8909da76ae209da2
- clm_4b10608e03fa060cc427caeffe794bb1cba4d8925a4f63f3512eeb8293bc3a72
- clm_4cb5528cc858b142a1e00a21ac72b53e9f968f7194bc9fa3ca3afe9365390f04
- clm_5db375e6b40cc3363d2140b9963afcbb6b97a1faf6f0e37e5b11c157dd77f179
- clm_61f0ab74046a003e9bd27cf0dccf5598431c983ca2ded4a7cb8e660c3a7ded68
- clm_7b239d677e81d5bad0bf75d57813e850864128d9aadddcb48431cd4cf282433b
- clm_86a075e7da57ae83010dcf9de999afdef9831d5b0de9cd8aec2dd112cd4206d0
- clm_92d08e7f9a3d19c66058ecbcc597a4ed095523fe9bd7c25a79065c9a4f003228
- clm_a169b42cad96c90d024c64f201eb6f40dc7020eafa8754bcbee1736b3c3bb3f2
- clm_a7080b3703565d8b5a43fe31ae27a8510f61c4f828239fbba6c4fa6d57ae6a8f
- clm_dcdda32e4dbac06c570c984ed78c7cec22eb23061d113a462954f60d903b7125
- clm_dd3d1ea9dbd43065766d47abd7e66349d5ae4bea51c911098a3641f819e1b4d6
maturity: draft
page_id: pg_33f9fa693146518b91b257ab7ca2a8e7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8c23b6cca15054ec917d1dd3aa036b5c
title: FredericVAN/PKU_MDAgent/README.md @ 83fc74947c72
updated_at: '2026-09-14T01:49:11Z'
---

# FredericVAN/PKU_MDAgent/README.md @ 83fc74947c72

<!-- rcw:begin owner=source:src_8c23b6cca15054ec917d1dd3aa036b5c block=evidence -->
- Two Hugging Face datasets (MDAgent_LEQS_DATASET and MDAgent_LSCF_DATASET) are also provided in the PaperDataset folder. [@claim:clm_0f50bed936b6fc60509ea0e8b8d7d94566b07b5b4d2867ac1d73cd3d2f39ab92]
- The system comprises a User Proxy Agent, Planner Agent, LAMMPS Worker Agent, LAMMPS Evaluator Agent, and a GroupChatManager coordinating agent communication and workflow. [@claim:clm_15225373ab6b02a6af098e07a169e0a5aa2f6ba02c934a6530438c73814fdc7d]
- MDAgent is a multi-agent collaborative system built on Microsoft's AutoGen framework for materials-science simulation and analysis tasks. [@claim:clm_29582caaf9aedfa78efd3a4230eac6e1066a8f2ee7f545876e6701f67e65a4af]
- The README reports expert evaluations showing significant improvement in code quality and a 42.22% reduction in task time versus traditional approaches. [@claim:clm_2e5120412b67d99a363c9b4edaa7bf8681742c6f76b597211d28532052539922]
- The user interacts through a Panel web UI served via 'panel serve material_system_UI.py', accessible by default at http://localhost:5006/material_system_UI, using dialogue-based interaction. [@claim:clm_32364b222df719e40fd2e48be29d5c9ca7c53d662de9924a8909da76ae209da2]
- Generated code is executed via AutoGen's code executor in Docker containers, which extract code blocks, write them to files, run each in a container, and read console output. [@claim:clm_4b10608e03fa060cc427caeffe794bb1cba4d8925a4f63f3512eeb8293bc3a72]
- Fine-tuning uses the unsloth framework with QLoRA 4-bit quantization, 4096-token context, on Meta-Llama-3.1-8B-Instruct as the LammpsWorker LLM, with an alpaca-style prompt template. [@claim:clm_4cb5528cc858b142a1e00a21ac72b53e9f968f7194bc9fa3ca3afe9365390f04]
- The underlying LLM is selectable: an online model such as GPT-4o-mini via OPENAI_API_KEY, or a local model deployed with Ollama (e.g., llama3.1:8b-instruct-q6_K with api_type 'ollama'). [@claim:clm_5db375e6b40cc3363d2140b9963afcbb6b97a1faf6f0e37e5b11c157dd77f179]
- To mitigate LLM hallucinations and factual errors, the design uses an Actor-Critic (Worker-Evaluator) loop plus human-in-the-loop review, with the Evaluator prompt augmented by expert-summarized error types. [@claim:clm_61f0ab74046a003e9bd27cf0dccf5598431c983ca2ded4a7cb8e660c3a7ded68]
- The LEQS dataset is an expert-built benchmark with 0-10 expert scores, deductions, and rationale for evaluating LLM-generated LAMMPS scripts, structured for supervised fine-tuning. [@claim:clm_7b239d677e81d5bad0bf75d57813e850864128d9aadddcb48431cd4cf282433b]
- A RAGFlow-based RAG API is encapsulated as an AutoGen Tool and provided to the Worker agent, which may call it to acquire knowledge before answering. [@claim:clm_86a075e7da57ae83010dcf9de999afdef9831d5b0de9cd8aec2dd112cd4206d0]
- The LSCF dataset contains 167 LAMMPS scripts with instruction/input/output fields, organized into Initialization, Modeling, and Computation sections, sourced from manual work, official docs, and online repositories. [@claim:clm_92d08e7f9a3d19c66058ecbcc597a4ed095523fe9bd7c25a79065c9a4f003228]
- The README acknowledges MDAgent cannot fully avoid LLM hallucinations, one-shot failures, and factual errors, which motivated the Actor-Critic and human-in-the-loop design. [@claim:clm_a169b42cad96c90d024c64f201eb6f40dc7020eafa8754bcbee1736b3c3bb3f2]
- The workflow proceeds through planning, script generation, and evaluation phases; the Evaluator scores scripts and scores below 8 loop back to generation, while the Manager oversees transitions. [@claim:clm_a7080b3703565d8b5a43fe31ae27a8510f61c4f828239fbba6c4fa6d57ae6a8f]
- Installation requires Python 3.11 (recommended), pip requirements, Azure CLI for authentication, autogen-agentchat~=0.2, azure-identity, azure-search-documents, and a locally deployed RAGFlow submodule. [@claim:clm_dcdda32e4dbac06c570c984ed78c7cec22eb23061d113a462954f60d903b7125]
- Fine-tuning was chosen over RAG as the primary knowledge-integration method because RAG could not provide the parameter-level syntactic understanding needed for valid LAMMPS code; RAG is kept as an optional alternative. [@claim:clm_dd3d1ea9dbd43065766d47abd7e66349d5ae4bea51c911098a3641f819e1b4d6]
<!-- rcw:end owner=source:src_8c23b6cca15054ec917d1dd3aa036b5c block=evidence -->

## Researcher notes

