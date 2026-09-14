# HMRAG (`hmrag`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ocean-luna
- License: Apache-2.0
- Language: Python
- Interface: install=conda create --name hmrag python=3.10; conda activate hmrag; pip install -r requirements.txt (or conda env create -f environment.yml)
- Model providers: Ollama,Hugging Face,OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ocean-luna/hmrag](../../repos/ocean-luna/hmrag.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Hierarchical Multi-Agent Multimodal RAG framework with three-tiered architecture (Decomposition Agent -\> Multi-source Retrieval Agents -\> Decision Agent); plug-and-play retrieval modules for vector/graph/web databases; consistency voting + Expert Model Refinement to resolve discrepancies; accepted at ACM MM 2025; built on LightRAG; demonstrated zero-shot multimodal QA on ScienceQA.

(captured site page body (agents/hmrag.md), not a verified repo-code finding)
HMRAG is the research code accompanying a peer-reviewed paper on hierarchical multi-agent retrieval-augmented generation. A Decomposition Agent rewrites complex queries into sub-tasks; retrieval agents work in parallel across three source types — vector databases, multimodal knowledge graphs via LightRAG, and web search — with plug-and-play retrieval modules; and a Decision Agent fuses candidate answers through consistency voting plus an expert-model refinement step when sources conflict. The framework was evaluated on multimodal QA benchmarks (notably ScienceQA), demonstrating gains from combining structured, unstructured, and graph-based retrieval in one pipeline. It is a research artifact with light maintenance, distributed via conda/pip, and is not aimed at coding workflows.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hmrag.md)
