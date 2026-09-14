# Trae Agent (`trae-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: bytedance
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, CLI; install=git clone, uv sync --all-extras, uv run trae-cli
- Model providers: OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Google Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [bytedance/trae-agent](../../repos/bytedance/trae-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Transparent, modular, research-friendly architecture designed for studying AI agent architectures and ablation studies; includes trajectory recording, Lakeview summarization, and Docker sandbox execution mode.

(captured site page body (agents/trae-agent.md), not a verified repo-code finding)
Trae Agent exists to make agent research practical: production harnesses obscure their internals, which prevents controlled comparison of prompts, tools, and orchestration strategies. It provides a modular Python CLI in which a natural-language engineering task is executed through a small tool set — bash, str_replace-based file editing, sequential thinking — with interactive mode for iterative work and Docker mode for reproducible, isolated execution from an image, existing container, Dockerfile, or archive. Every run emits a trajectory log capturing LLM calls, tool usage, and step-by-step state, and Lakeview summarizes those steps for analysis; YAML configuration with environment-variable overrides keeps experiments scriptable. Agent researchers and engineers studying harness design are its primary users, and an accompanying arXiv technical report documents the architecture.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/trae-agent.md)
