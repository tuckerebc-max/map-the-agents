# ocean-luna/hmrag -- full detail

[Back to orientation](hmrag.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ocean-luna/hmrag/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/a890c5839d1bf4bd.json](../../../wiki/dossiers/ocean-luna/hmrag/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/a890c5839d1bf4bd.json)

## specifications (1 claim(s))

- [observation/documented] HM-RAG is described as a hierarchical multi-agent multimodal RAG framework for dynamic knowledge synthesis across structured, unstructured, and graph-based data. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23) (`clm_b7bd87542f3903af72a6111697e29677ddbda843f37786df30d0a97fe639f0a9`)

## components (3 claim(s))

- [observation/documented] A Decomposition Agent splits complex queries into coherent sub-tasks via semantic-aware query rewriting and schema-guided context augmentation. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23) (`clm_c60cf8a768005ec37c0fde5cb9dbf8b9b3a227320923174f7b1c5e1eab8777b1`)
- [observation/documented] Retrieval agents run parallel, modality-specific retrieval using plug-and-play modules for vector, graph, and web-based databases. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23) (`clm_6500a2eff501ec3504b624bb2f3154cc2e48b0f6d25cd510ef7cd566417b1664`)
- [observation/documented] A Decision Agent integrates multi-source answers via consistency voting and resolves retrieval discrepancies through Expert Model Refinement. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23) (`clm_8041d4fc06299755ac133cfee761ed0e35550f61f1020be32a1055d72bdfeae4`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: setup is via a Python 3.10 conda environment with pip install -r requirements.txt, or alternatively conda env create -f environment.yml. -- evidence: [README.md#L29-L38](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L29-L38) (`clm_b4e0197916d477d714337bfdc12313428caf9a7f8e0db42dcd509c7ca5f00fa4`)
- [observation/documented] Repository development practice: the README recommends installing Ollama to download models, with Hugging Face offered as an alternative source for LLMs. -- evidence: [README.md#L40-L40](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L40-L40) (`clm_e8a0ec88b0d54e9c0178196742520a36c4331a66dc59a222e1bb385deebade52`)
- [observation/documented] Repository development practice: the ScienceQA dataset used for testing can be downloaded by running dataset/download_ScienceQA.sh. -- evidence: [README.md#L47-L50](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L47-L50) (`clm_23d5d1d858094fa1ea2eb5a9561ac4b067f8790fa99c7ba91c2b9f08afac5176`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Multi-agent inference is launched with python main.py taking a working directory, a Serper API key, and an OpenAI key as arguments. -- evidence: [README.md#L56-L58](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L56-L58) (`clm_2b699bf49d26b4aa4462c6fb93b996ff6e3874e7cad95d9124868cfe1402f169`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The framework uses a three-tier agent architecture: a Decomposition Agent, parallel modality-specific Multi-source Retrieval Agents, and a Decision Agent. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23) (`clm_b12c37f35091948c8423cc837122f60b4c39ff58ea73ca807a363db11c141177`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt lists libraries including torch, transformers, openai, ollama, neo4j, pymilvus, clip-interrogator 0.6.0, deepspeed, and opencv-python. -- evidence: [requirements.txt#L1-L38](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/requirements.txt#L1-L38) (`clm_4a75998128ac7c025fe37aaca03597bbea3a2621560e8fde7a85c07ca723b39b`)
- [observation/documented] The project uses LightRAG, a lightweight framework, to construct multimodal knowledge graphs, referencing LightRAG's official repository for details. -- evidence: [README.md#L53-L53](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L53-L53) (`clm_23afc82c21147d6aaa82dd5120445378ae2080283497de2d6808f6fc6126e9ba`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The paper was released on arXiv (2504.12330) in April 2025 and accepted at ACM MM2025, per the README news section. -- evidence: [README.md#L15-L15](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L15-L15), [README.md#L13-L13](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L13-L13) (`clm_bd4649302d11336fa7f89e0955635138f3644c48a7bc5379f57dd6f8dd32de75`)

