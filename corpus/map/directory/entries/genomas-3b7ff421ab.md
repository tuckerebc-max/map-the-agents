# GenoMAS (`genomas`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Liu-Hy
- License: MIT
- Language: Python
- Interface: install=conda create -n genomas python=3.10; pip install -r requirements.txt; copy env.example to .env and fill API keys
- Model providers: OpenAI, Anthropic, Google Gemini, Ollama, Novita API
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [liu-hy/genomas](../../repos/liu-hy/genomas.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent framework for scientific discovery via code-driven gene expression analysis; official implementation of arXiv paper; achieves 60.38% F1 on GenoTEX benchmark; role-specific model assignment (Code Reviewer, Domain Expert, Data Engineer, Statistician, Planning)

(captured site page body (agents/genomas.md), not a verified repo-code finding)
GenoMAS automates gene-expression analysis — the kind of multi-step statistical and bioinformatics work that normally takes a trained analyst — by having LLM agents write and run the analysis code themselves. Its generic framework prescribes typed messaging between role-specialized agents, each of which can plan, write code, execute it, debug failures, and backtrack through a notebook-style workflow, with different models assigned per role from OpenAI, Anthropic, Gemini, Ollama, or Novita. The headline implementation analyzes GEO/TCGA transcriptomic data for gene-trait associations while controlling confounders, and the official implementation reproduces the paper's 60.38% F1 on GenoTEX. Published as the arXiv 2507.21035 artifact from UIUC and UC San Diego, it targets computational biology researchers rather than software developers.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/genomas.md)
