# fredericvan/pku_mdagent -- full detail

[Back to orientation](pku_mdagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fredericvan/pku_mdagent/83fc74947c72042c61c386adbc4faa5da1a44917/ba6c3f9e62616f21.json](../../../wiki/dossiers/fredericvan/pku_mdagent/83fc74947c72042c61c386adbc4faa5da1a44917/ba6c3f9e62616f21.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The system comprises a User Proxy Agent, Planner Agent, LAMMPS Worker Agent, LAMMPS Evaluator Agent, and a GroupChatManager coordinating agent communication and workflow. -- evidence: [README.md#L312-L330](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L312-L330) (`clm_15225373ab6b02a6af098e07a169e0a5aa2f6ba02c934a6530438c73814fdc7d`)

## design-choices (2 claim(s))

- [observation/documented] To mitigate LLM hallucinations and factual errors, the design uses an Actor-Critic (Worker-Evaluator) loop plus human-in-the-loop review, with the Evaluator prompt augmented by expert-summarized error types. -- evidence: [README.md#L365-L365](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L365-L365), [README.md#L367-L367](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L367-L367), [README.md#L361-L361](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L361-L361), [README.md#L363-L363](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L363-L363) (`clm_61f0ab74046a003e9bd27cf0dccf5598431c983ca2ded4a7cb8e660c3a7ded68`)
- [observation/documented] Fine-tuning was chosen over RAG as the primary knowledge-integration method because RAG could not provide the parameter-level syntactic understanding needed for valid LAMMPS code; RAG is kept as an optional alternative. -- evidence: [README.md#L260-L260](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L260-L260), [README.md#L236-L236](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L236-L236), [README.md#L254-L254](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L254-L254) (`clm_dd3d1ea9dbd43065766d47abd7e66349d5ae4bea51c911098a3641f819e1b4d6`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the docs site deploys via GitHub Actions on pushes to main (or alternatively directly from the /docs folder), and can be previewed locally with 'python -m http.server 8000' from the docs directory. -- evidence: [docs/README.md#L13-L13](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L13-L13), [docs/DEPLOY.md#L29-L31](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/DEPLOY.md#L29-L31), [docs/README.md#L11-L11](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L11-L11), [docs/DEPLOY.md#L16-L21](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/DEPLOY.md#L16-L21), [docs/DEPLOY.md#L5-L8](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/DEPLOY.md#L5-L8), [docs/README.md#L17-L17](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L17-L17), [docs/README.md#L7-L9](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L7-L9), [docs/README.md#L19-L22](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L19-L22) (`clm_b1b0719b7a11d7c61f556fd1b7ee0bcb78d16113457a49f774caf2b46da18428`)

## skills-patterns (2 claim(s))

- [observation/documented] The LSCF dataset contains 167 LAMMPS scripts with instruction/input/output fields, organized into Initialization, Modeling, and Computation sections, sourced from manual work, official docs, and online repositories. -- evidence: [README.md#L55-L55](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L55-L55), [README.md#L61-L63](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L61-L63), [README.md#L67-L72](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L67-L72), [README.md#L57-L57](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L57-L57) (`clm_92d08e7f9a3d19c66058ecbcc597a4ed095523fe9bd7c25a79065c9a4f003228`)
- [observation/documented] Fine-tuning uses the unsloth framework with QLoRA 4-bit quantization, 4096-token context, on Meta-Llama-3.1-8B-Instruct as the LammpsWorker LLM, with an alpaca-style prompt template. -- evidence: [README.md#L248-L248](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L248-L248), [README.md#L242-L242](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L242-L242), [README.md#L244-L244](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L244-L244) (`clm_4cb5528cc858b142a1e00a21ac72b53e9f968f7194bc9fa3ca3afe9365390f04`)

## interfaces (2 claim(s))

- [observation/documented] The user interacts through a Panel web UI served via 'panel serve material_system_UI.py', accessible by default at http://localhost:5006/material_system_UI, using dialogue-based interaction. -- evidence: [README.md#L214-L214](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L214-L214), [README.md#L210-L210](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L210-L210), [README.md#L206-L208](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L206-L208) (`clm_32364b222df719e40fd2e48be29d5c9ca7c53d662de9924a8909da76ae209da2`)
- [observation/documented] The underlying LLM is selectable: an online model such as GPT-4o-mini via OPENAI_API_KEY, or a local model deployed with Ollama (e.g., llama3.1:8b-instruct-q6_K with api_type 'ollama'). -- evidence: [README.md#L190-L190](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L190-L190), [README.md#L182-L182](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L182-L182), [README.md#L184-L184](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L184-L184), [README.md#L192-L202](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L192-L202) (`clm_5db375e6b40cc3363d2140b9963afcbb6b97a1faf6f0e37e5b11c157dd77f179`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] MDAgent is a multi-agent collaborative system built on Microsoft's AutoGen framework for materials-science simulation and analysis tasks. -- evidence: [README.md#L304-L304](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L304-L304) (`clm_29582caaf9aedfa78efd3a4230eac6e1066a8f2ee7f545876e6701f67e65a4af`)
- [observation/documented] The workflow proceeds through planning, script generation, and evaluation phases; the Evaluator scores scripts and scores below 8 loop back to generation, while the Manager oversees transitions. -- evidence: [README.md#L346-L350](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L346-L350), [README.md#L352-L357](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L352-L357), [README.md#L337-L340](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L337-L340), [README.md#L342-L344](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L342-L344), [README.md#L334-L335](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L334-L335) (`clm_a7080b3703565d8b5a43fe31ae27a8510f61c4f828239fbba6c4fa6d57ae6a8f`)

## tools-permissions (2 claim(s))

- [observation/documented] Generated code is executed via AutoGen's code executor in Docker containers, which extract code blocks, write them to files, run each in a container, and read console output. -- evidence: [README.md#L373-L373](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L373-L373), [README.md#L383-L383](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L383-L383) (`clm_4b10608e03fa060cc427caeffe794bb1cba4d8925a4f63f3512eeb8293bc3a72`)
- [observation/documented] A RAGFlow-based RAG API is encapsulated as an AutoGen Tool and provided to the Worker agent, which may call it to acquire knowledge before answering. -- evidence: [README.md#L391-L391](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L391-L391), [README.md#L296-L296](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L296-L296), [README.md#L258-L258](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L258-L258) (`clm_86a075e7da57ae83010dcf9de999afdef9831d5b0de9cd8aec2dd112cd4206d0`)

## evaluation (2 claim(s))

- [observation/documented] The LEQS dataset is an expert-built benchmark with 0-10 expert scores, deductions, and rationale for evaluating LLM-generated LAMMPS scripts, structured for supervised fine-tuning. -- evidence: [README.md#L101-L101](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L101-L101), [README.md#L84-L84](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L84-L84), [README.md#L86-L86](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L86-L86), [README.md#L92-L99](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L92-L99) (`clm_7b239d677e81d5bad0bf75d57813e850864128d9aadddcb48431cd4cf282433b`)
- [observation/documented] The README reports expert evaluations showing significant improvement in code quality and a 42.22% reduction in task time versus traditional approaches. -- evidence: [README.md#L29-L33](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L29-L33) (`clm_2e5120412b67d99a363c9b4edaa7bf8681742c6f76b597211d28532052539922`)

## dependencies (2 claim(s))

- [observation/documented] Installation requires Python 3.11 (recommended), pip requirements, Azure CLI for authentication, autogen-agentchat~=0.2, azure-identity, azure-search-documents, and a locally deployed RAGFlow submodule. -- evidence: [README.md#L169-L169](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L169-L169), [README.md#L122-L122](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L122-L122), [README.md#L133-L133](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L133-L133), [README.md#L165-L165](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L165-L165), [README.md#L114-L116](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L114-L116), [README.md#L143-L148](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L143-L148), [README.md#L112-L112](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L112-L112) (`clm_dcdda32e4dbac06c570c984ed78c7cec22eb23061d113a462954f60d903b7125`)
- [observation/documented] Two Hugging Face datasets (MDAgent_LEQS_DATASET and MDAgent_LSCF_DATASET) are also provided in the PaperDataset folder. -- evidence: [README.md#L50-L51](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L50-L51), [README.md#L13-L13](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L13-L13), [README.md#L15-L16](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L15-L16), [README.md#L48-L48](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L48-L48) (`clm_0f50bed936b6fc60509ea0e8b8d7d94566b07b5b4d2867ac1d73cd3d2f39ab92`)

## limitations (1 claim(s))

- [observation/documented] The README acknowledges MDAgent cannot fully avoid LLM hallucinations, one-shot failures, and factual errors, which motivated the Actor-Critic and human-in-the-loop design. -- evidence: [README.md#L361-L361](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L361-L361) (`clm_a169b42cad96c90d024c64f201eb6f40dc7020eafa8754bcbee1736b3c3bb3f2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

