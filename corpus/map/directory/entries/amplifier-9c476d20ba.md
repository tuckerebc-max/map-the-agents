# Amplifier (`amplifier`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: microsoft
- License: MIT
- Language: Shell
- Interface: platforms=CLI; install=uv tool install git+https://github.com/microsoft/amplifier
- Model providers: Anthropic, OpenAI, Azure OpenAI, Ollama, GitHub Copilot, ChatGPT (OAuth), Chat Completions (OpenAI-compatible), Gemini, vLLM
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [microsoft/amplifier](../../repos/microsoft/amplifier.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Microsoft's modular AI development assistant. The CLI is one interface on top of a modular platform — bundles ship focused agents you invoke by name, and the amplifier-agent engine underneath provides the full agent loop with tools, sub-agents, skills, and MCP. Anything that can spawn a subprocess can use the engine. Nine model providers behind one interface with role-based routing ...

(captured site page body (agents/amplifier.md), not a verified repo-code finding)
Microsoft positions Amplifier as an open research demonstrator for modular agent design: the CLI is explicitly just one interface over a platform intended to grow web, mobile, and IDE surfaces. Bundles compose configuration — the foundation bundle ships filesystem/bash/web/search/task tools, fourteen agents (zen-architect, bug-hunter, modular-builder...), and behaviors like redaction and todo tracking — while external bundles install via amplifier bundle add from any git URL. Sessions persist per project and resume with amplifier continue, and a companion log viewer replays sessions for debugging. Providers are swappable at runtime (Anthropic, OpenAI, Azure OpenAI, Ollama); the MIT-licensed project is an early preview that explicitly warns safety systems are incomplete, is not accepting external contributions, and has 3.1k stars.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/amplifier.md)
