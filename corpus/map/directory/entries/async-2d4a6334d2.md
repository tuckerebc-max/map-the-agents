# Async (`async`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ZYKJShadow
- License: Apache-2.0
- Language: TypeScript, React, Electron
- Interface: platforms=Desktop, IDE; install=git clone https://github.com/ZYKJShadow/Async.git; cd Async; npm install; npm run desktop
- Model providers: Anthropic, OpenAI, Google Gemini, OpenAI-compatible (Ollama, vLLM, self-hosted)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (extensibility via MCP servers, local skills, and IM adapters instead) (no)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [zykjshadow/async](../../repos/zykjshadow/async.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent-first AI-native desktop shell built entirely from scratch (not a VS Code fork) on Electron + React + Monaco, where the agent is the center of gravity with a transparent Think -\> Plan -\> Execute -\> Observe loop. Uniquely includes an IM bot bridge to control the agent workspace externally via Telegram, Slack, Discord, and Feishu. Four Composer modes: Agent, ...

(captured site page body (agents/async.md), not a verified repo-code finding)
Async (ZYKJShadow/Async) is an agent-first desktop shell built on Electron, React, and Monaco, deliberately not a VS Code fork, so the agent rather than the editor is the primary surface. Its agent loop runs a visible Think-Plan-Execute-Observe cycle with streaming tool parameter cards, approval gates for sensitive operations, and nested sub-agents, backed by Read/Write/Edit/Glob/Grep/Shell tools and MCP server support. Four Composer modes (Agent, Plan, Ask, Debug) control autonomy, and a Team mode coordinates Lead, specialist, and reviewer agents. Multi-model support spans Anthropic, OpenAI, Gemini, and OpenAI-compatible endpoints (Ollama, vLLM) under a BYOK model, with Telegram, Slack, Discord, and Feishu adapters reusing the same agent runtime from chat apps. It is Apache-2.0, actively developed, and aimed at developers who want a local-first, hackable IDE where the agent is the primary interface.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/async.md)
