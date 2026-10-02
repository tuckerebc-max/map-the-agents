# CodeActAgent (`codeactagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: xingyaoww
- License: MIT
- Language: Python
- Interface: install=docker
- Model providers: OpenAI-compatible (vLLM, llama.cpp)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [xingyaoww/code-act](../../repos/xingyaoww/code-act.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Research project (ICML 2024) proposing executable Python code as a unified action space for LLM agents instead of JSON/text. Agents can revise prior actions or emit new ones through multi-turn interpreter interactions. Up to 20% higher success rate vs Text/JSON across 17 LLMs. Ships CodeActInstruct (7k instruction-tuning dataset) and CodeActAgent models (Mistral-7b recommended, Llama-2-7b) plus a containerized Jupyter kernel execution ...

(captured site page body (agents/codeactagent.md), not a verified repo-code finding)
CodeAct demonstrated that letting an LLM emit executable Python instead of JSON or structured text produces stronger agents, because the model can compose actions, inspect results, and revise prior steps over multiple interpreter turns. The repository ships the full research stack: CodeActInstruct, a 7k multi-turn instruction-tuning dataset on Hugging Face; fine-tuned CodeActAgent models on Mistral-7B and Llama-2-7B; the M3ToolEval benchmark tooling; and a Dockerized Jupyter-kernel execution engine behind a chat UI, deployable with vLLM, llama.cpp, Ollama, or Kubernetes. It is a paper artifact rather than a maintained product: 31 commits, no releases, and no updates after April 2024. Its lasting influence is architectural — the code-as-action design carried into OpenHands, built by the same author.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/codeactagent.md)
