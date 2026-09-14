# ocean-luna/hmrag

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d0712d463da4 @ a890c5839d1bf4bd

## Summary (orientation draft, not independently verified)

The snapshot is the README and dependency list of HM-RAG, a hierarchical multi-agent multimodal RAG framework with a paper accepted at ACM MM2025. Evidence covers the described architecture, installation, and usage instructions; no source code is included in the slices.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] HM-RAG is described as a hierarchical multi-agent multimodal RAG framework for dynamic knowledge synthesis across structured, unstructured, and graph-based data. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23)
- components (3 claim(s)):
  - [observation/documented] A Decomposition Agent splits complex queries into coherent sub-tasks via semantic-aware query rewriting and schema-guided context augmentation. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23)
  - [observation/documented] Retrieval agents run parallel, modality-specific retrieval using plug-and-play modules for vector, graph, and web-based databases. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: setup is via a Python 3.10 conda environment with pip install -r requirements.txt, or alternatively conda env create -f environment.yml. -- evidence: [README.md#L29-L38](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L29-L38)
  - [observation/documented] Repository development practice: the README recommends installing Ollama to download models, with Hugging Face offered as an alternative source for LLMs. -- evidence: [README.md#L40-L40](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L40-L40)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Multi-agent inference is launched with python main.py taking a working directory, a Serper API key, and an OpenAI key as arguments. -- evidence: [README.md#L56-L58](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L56-L58)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The framework uses a three-tier agent architecture: a Decomposition Agent, parallel modality-specific Multi-source Retrieval Agents, and a Decision Agent. -- evidence: [README.md#L23-L23](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L23-L23)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] requirements.txt lists libraries including torch, transformers, openai, ollama, neo4j, pymilvus, clip-interrogator 0.6.0, deepspeed, and opencv-python. -- evidence: [requirements.txt#L1-L38](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/requirements.txt#L1-L38)
  - [observation/documented] The project uses LightRAG, a lightweight framework, to construct multimodal knowledge graphs, referencing LightRAG's official repository for details. -- evidence: [README.md#L53-L53](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L53-L53)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The paper was released on arXiv (2504.12330) in April 2025 and accepted at ACM MM2025, per the README news section. -- evidence: [README.md#L15-L15](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L15-L15), [README.md#L13-L13](https://github.com/ocean-luna/HMRAG/blob/d0712d463da4b2b6a95e6428cd9a9d1c39c7583e/README.md#L13-L13)

(2 additional claim(s) omitted for length; see [full detail](hmrag.detail.md) for every claim.)

Metadata and full claim list: [full detail](hmrag.detail.md)
Human notes ([notes](hmrag.notes.md), never overwritten by build)

[Back to map index](../../index.md)
