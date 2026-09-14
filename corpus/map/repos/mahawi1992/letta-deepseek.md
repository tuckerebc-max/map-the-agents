# mahawi1992/letta-deepseek

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f202d8c2b44b @ 7f950fd4c66053ce

## Summary (orientation draft, not independently verified)

The snapshot is documentation-only (README, docs/, requirements.txt) describing a Letta AI + DeepSeek multi-agent system with research, coding, documentation, and orchestrator agents plus a memory system; no source code is present in the evidence.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The system comprises a Research Agent using Tavily, a Coding Agent using DeepSeek, a Memory Manager for knowledge optimization, and a Documentation System for storage and retrieval. -- evidence: [docs/setup.md#L59-L63](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L59-L63)
  - [observation/documented] The README describes a multi-agent setup including a Research Agent with Tavily integration, a Coding Agent with DeepSeek, a Documentation Agent, and an Orchestrator for coordination. -- evidence: [README.md#L13-L17](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L13-L17)
- design-choices (1 claim(s)):
  - [observation/documented] Memory consolidation is described as automatically merging similar memories, maintaining version history, and optimizing storage efficiency. -- evidence: [docs/enhanced_features.md#L6-L8](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/enhanced_features.md#L6-L8)
- workflows (3 claim(s)):
  - [observation/documented] Setup involves cloning the repo, creating and activating a Python virtual environment, installing dependencies with pip install -r requirements.txt, and copying .env.example to .env for API keys. -- evidence: [README.md#L40-L42](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L40-L42), [README.md#L27-L33](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L27-L33), [README.md#L35-L38](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L35-L38)
  - [observation/documented] Deployment to Lightning AI is done by creating a project, importing from GitHub, setting DEEPSEEK_API_KEY and TAVILY_API_KEY environment variables, and deploying. -- evidence: [docs/deployment.md#L25-L31](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/deployment.md#L25-L31)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The application is run via python app.py, and required environment variables are DEEPSEEK_API_KEY and TAVILY_API_KEY. -- evidence: [docs/setup.md#L46-L48](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L46-L48), [docs/setup.md#L31-L34](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/setup.md#L31-L34)
- memory-state (3 claim(s)):
  - [observation/documented] The memory system is documented as having core memory (coding standards, language guidelines, security patterns), archival memory, and message history that maintains conversation context. -- evidence: [docs/memory.md#L14-L14](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L14-L14), [docs/memory.md#L8-L11](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L8-L11), [docs/memory.md#L37-L39](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L37-L39)
  - [observation/documented] Archival memory stores typed records such as CODE_SNIPPET entries with code, description, and category fields, and LEARNING_INSIGHT entries with category, insight, and optional code example. -- evidence: [docs/memory.md#L17-L24](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L17-L24), [docs/memory.md#L27-L34](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/docs/memory.md#L27-L34)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt lists letta>=0.2.0, gradio>=4.0.0, lightning>=2.1.0, python-dotenv, requests, langchain, langchain-community, and tavily-python. -- evidence: [requirements.txt#L1-L8](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/requirements.txt#L1-L8)
- limitations (1 claim(s)):
  - [inference/documented] The evidence consists only of documentation and requirements; no implementation code appears in the snapshot, so runtime behavior beyond what docs describe cannot be verified. -- evidence: [README.md#L3-L3](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/README.md#L3-L3), [requirements.txt#L1-L8](https://github.com/mahawi1992/letta-deepseek/blob/f202d8c2b44b9841fd3c5aade9117cccddf873e0/requirements.txt#L1-L8)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](letta-deepseek.detail.md) for every claim.)

Metadata and full claim list: [full detail](letta-deepseek.detail.md)
Human notes ([notes](letta-deepseek.notes.md), never overwritten by build)

[Back to map index](../../index.md)
