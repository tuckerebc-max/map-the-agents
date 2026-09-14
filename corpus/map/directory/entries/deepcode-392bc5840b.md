# DeepCode (`deepcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: HKUDS
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, CLI, Web; install=uv tool install --python 3.12 deepcode-hku
- Model providers: OpenRouter, OpenAI, Anthropic, DeepSeek, Gemini, Ollama, vLLM, OpenAI-compatible, Requesty, Forge, MiniMax
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [hkuds/deepcode](../../repos/hkuds/deepcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Paper2Code workflow reproduces research papers into runnable code (75.9% on PaperBench, beating commercial agents by 26 points); Loop Engineering with durable steerable Goals; parallel agents in isolated Git worktrees; same agent runtime across CLI and Desktop.

(captured site page body (agents/deepcode.md), not a verified repo-code finding)
DeepCode came out of HKU's Data Intelligence Lab as a multi-agent system whose orchestrator coordinates specialist agents for intent understanding, document parsing, code planning, reference mining, indexing, and generation, backed by CodeRAG and iterative verification. That pipeline reproduces machine-learning research papers as executable code, and the lab reports PaperBench results ahead of commercial agents on the commercial-agent subset. The project has since broadened into a general coding agent (v2.0) with a CLI/TUI and a Tauri-based desktop app sharing one runtime, full MCP client support with lazy loading and per-tool approvals, skills, plugins, subagents, and sandboxed sessions. Researchers use it for paper reproduction while developers adopt it as a general open-source harness; it is MIT-licensed, Python-based, and actively released.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepcode.md)
