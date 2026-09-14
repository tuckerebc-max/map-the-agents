# mahawi1992/letta-deepseek -- full detail

[Back to orientation](letta-deepseek.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mahawi1992/letta-deepseek/f202d8c2b44b9841fd3c5aade9117cccddf873e0/7f950fd4c66053ce.json](../../../wiki/dossiers/mahawi1992/letta-deepseek/f202d8c2b44b9841fd3c5aade9117cccddf873e0/7f950fd4c66053ce.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The system comprises a Research Agent using Tavily, a Coding Agent using DeepSeek, a Memory Manager for knowledge optimization, and a Documentation System for storage and retrieval. -- evidence: [docs/setup.md#L59-L63](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L59-L63) (`clm_3e21a11ab306624a231b700b37102a498f90efce06fad435263a60b11ce6baa9`)
- [observation/documented] The README describes a multi-agent setup including a Research Agent with Tavily integration, a Coding Agent with DeepSeek, a Documentation Agent, and an Orchestrator for coordination. -- evidence: [README.md#L13-L17](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L13-L17) (`clm_d073bd2eaf8e9b381e0bfff3085229729edbcb7eae3d820c2f6c960fa7e48b7f`)

## design-choices (1 claim(s))

- [observation/documented] Memory consolidation is described as automatically merging similar memories, maintaining version history, and optimizing storage efficiency. -- evidence: [docs/enhanced_features.md#L6-L8](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/enhanced_features.md#L6-L8) (`clm_fc40c07be42d802ed45664362e0abe7bc40e1ffd56a66bbc1e670dd0ac3d22fa`)

## workflows (3 claim(s))

- [observation/documented] Setup involves cloning the repo, creating and activating a Python virtual environment, installing dependencies with pip install -r requirements.txt, and copying .env.example to .env for API keys. -- evidence: [README.md#L40-L42](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L40-L42), [README.md#L27-L33](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L27-L33), [README.md#L35-L38](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L35-L38) (`clm_4022dfdb2c7a1122704692fc6b290dd23d4e359a9097abf4aa6b599dfc95c939`)
- [observation/documented] Deployment to Lightning AI is done by creating a project, importing from GitHub, setting DEEPSEEK_API_KEY and TAVILY_API_KEY environment variables, and deploying. -- evidence: [docs/deployment.md#L25-L31](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/deployment.md#L25-L31) (`clm_4fbf3923be7232e1f6bb667e6496ce0baab67624b87a1f7559af3d7b9d0a41c3`)
- [observation/documented] The documented development workflow is: make changes locally, test with python app.py, deploy to Lightning AI, and monitor the deployment. -- evidence: [docs/setup.md#L67-L70](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L67-L70) (`clm_19a65dcf1c71fb834664d92449924517d886c82cad07bcb01fceabf0b1adccf9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The application is run via python app.py, and required environment variables are DEEPSEEK_API_KEY and TAVILY_API_KEY. -- evidence: [docs/setup.md#L46-L48](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L46-L48), [docs/setup.md#L31-L34](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L31-L34) (`clm_0476bc7c396c7816626cd034613ffeb768b7397af8743a905c3a842f17f9bb03`)

## memory-state (3 claim(s))

- [observation/documented] The memory system is documented as having core memory (coding standards, language guidelines, security patterns), archival memory, and message history that maintains conversation context. -- evidence: [docs/memory.md#L14-L14](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L14-L14), [docs/memory.md#L8-L11](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L8-L11), [docs/memory.md#L37-L39](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L37-L39) (`clm_50a02074f3ed9254c72ff6210c8b317cf9b9937b3f95b0a10074ab8cb70f2c41`)
- [observation/documented] Archival memory stores typed records such as CODE_SNIPPET entries with code, description, and category fields, and LEARNING_INSIGHT entries with category, insight, and optional code example. -- evidence: [docs/memory.md#L17-L24](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L17-L24), [docs/memory.md#L27-L34](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L27-L34) (`clm_3103b37c82fb1f4e6e73a09b98d20cdd3e8b02723538e7f7de4bc73d618f738d`)
- [observation/documented] A memory_manager API is documented with methods like save_code_snippet and record_pattern_usage, the latter taking a pattern name, success rating, and context. -- evidence: [docs/memory.md#L45-L49](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L45-L49), [docs/memory.md#L52-L57](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L52-L57) (`clm_b567a94edcd7426ab72aaf2a0e2dc3e11cb6c89b97a73a3fc10fdce9f1346c5c`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt lists letta>=0.2.0, gradio>=4.0.0, lightning>=2.1.0, python-dotenv, requests, langchain, langchain-community, and tavily-python. -- evidence: [requirements.txt#L1-L8](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/requirements.txt#L1-L8) (`clm_0e58d78cd4524a468b23d1f600d9fc296dafd744d36db88e0b72f8b341647e65`)

## limitations (1 claim(s))

- [inference/documented] The evidence consists only of documentation and requirements; no implementation code appears in the snapshot, so runtime behavior beyond what docs describe cannot be verified. -- evidence: [README.md#L3-L3](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L3-L3), [requirements.txt#L1-L8](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/requirements.txt#L1-L8) (`clm_2d76cbfc461155ceff0246fc07716df319ac0671d21463ee5508af0aa791918d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

