# LegalGraphRAG (`legalgraphrag`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: XMUDeepLIT
- License: unknown
- Language: Python
- Interface: install=pip install -r requirements.txt; cp env.example .env; python run.py --model \<model\> --datasets \<dataset\>
- Model providers: Qwen3-8B, Qwen2.5-7B-Instruct, DeepSeek-V3, GPT-4o-mini, InternLM3, GLM-4
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [xmudeeplit/legalgraphrag](../../repos/xmudeeplit/legalgraphrag.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Evaluation framework for legal judgment prediction integrating multi-agent graph retrieval-augmented generation (RAG); computes charge, law-article, and imprisonment prediction metrics on CAIL/CMDL datasets using a 14,049-case graph corpus.

(captured site page body (agents/legalgraphrag.md), not a verified repo-code finding)
LegalGraphRAG addresses reliability of legal reasoning with retrieval-audgment generation structured as a graph over a 14,049-case corpus of Chinese criminal law, evaluated on charge prediction, law-article prediction, and imprisonment-sentence metrics against CAIL (568 cases) and CMDL (1,374 records) benchmarks. The repository reproduces the paper's main experiment table and supports a range of open and hosted models (Qwen3-8B, Qwen2.5-7B, DeepSeek-V3, GPT-4o-mini, InternLM3, GLM-4, Gemma3) with multi-GPU execution and a local Ollama embedding service. It is research code accompanying an academic paper rather than a tool: fifteen commits, no releases, and no license file. Legal-NLP researchers use it to reproduce the paper's Table 2 results.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/legalgraphrag.md)
