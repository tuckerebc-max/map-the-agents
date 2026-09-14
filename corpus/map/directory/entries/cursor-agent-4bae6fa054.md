# cursor-agent (`cursor-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: civai-technologies
- License: MIT
- Language: Python
- Interface: install=pip install cursor-agent-tools; or git clone + pip install -e .
- Model providers: Anthropic, OpenAI, Ollama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [civai-technologies/cursor-agent](../../repos/civai-technologies/cursor-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Python-based AI agent replicating Cursor's coding assistant capabilities; function calling with registered tools; codebase semantic search, grep, fuzzy file search, web search; image analysis via LLM vision; terminal command execution with permission system (YOLO mode, allowlists/denylists)

(captured site page body (agents/cursor-agent.md), not a verified repo-code finding)
cursor-agent packages the mechanics of Cursor's coding assistant into a pip-installable Python library: a function-calling loop with registered tools for reading and editing files, semantic and regex codebase search, web search, image analysis, and terminal commands gated by a permission system. It supports Anthropic, OpenAI, and locally hosted Ollama models, and developers can extend it by registering custom tools in code. The project, authored by the founder of CIVAI Technologies, reached about 130 stars but shows no recent commits or releases and one stale pull request, so it now serves mainly as a reference implementation of an agentic coding loop in Python.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cursor-agent.md)
