# PKU_MDAgent (`pku-mdagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: FredericVAN
- License: GPL-3.0
- Language: Python
- Interface: install=pip install -r requirements.txt (Python 3.11 recommended)
- Model providers: OpenAI, Ollama, Qwen
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [fredericvan/pku_mdagent](../../repos/fredericvan/pku_mdagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Molecular Dynamics Agent — a fine-tuned LLM-based multi-agent system for generating, executing, and refining LAMMPS thermodynamic simulation code in materials science. Uses Actor-Critic model (Worker + Evaluator loop) with human-in-the-loop. Achieves 42.22% reduction in task time. Curated LAMMPS fine-tuning datasets. Supports fine-tuning and RAG. Built on AutoGen. Published in Scientific Reports. NOTE: This is a domain-specific research agent, not a ...

(captured site page body (agents/pku-mdagent.md), not a verified repo-code finding)
MDAgent came out of Peking University to automate molecular-dynamics simulation setup, where materials scientists otherwise hand-write and iteratively debug LAMMPS scripts to extract thermodynamic parameters like heat capacity and thermal conductivity. Built on Microsoft AutoGen, a Planner decomposes the task, a Worker agent generates LAMMPS code executed in Docker containers, and an Evaluator scores each script on a 0–10 deduction rubric, looping until scripts score at least 8, with humans able to intervene mid-loop. Domain knowledge enters through QLoRA fine-tuning on a published 167-script LAMMPS dataset (with an expert-scored benchmark, LEQS, alongside) and optional RagFlow-based retrieval. The paper reports a 42.22% reduction in task time, and the code, datasets, and a Panel web UI shipped alongside the Scientific Reports publication. Its users are computational materials-science researchers, and the code is a research artifact rather than a maintained product.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pku-mdagent.md)
