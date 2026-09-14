# damocles (`damocles`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: AizenvoltPrime
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=Clone repo, npm install, npm run build, press F5 in VS Code; or package as .vsix and install via Extensions menu
- Model providers: Anthropic, OpenAI, StepFun, DeepSeek, OpenRouter, Google Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [aizenvoltprime/damocles](../../repos/aizenvoltprime/damocles.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): VS Code extension embedding an AI coding agent powered by the Pi agent runtime, with deep editor integration including inline diff previews, subagent visualization, persistent SQLite-backed memory, collaborative multi-agent teams, a workspace knowledge graph (Compass), integrated stealth browser automation, and hands-free voice input (Jarvis mode).

(captured site page body (agents/damocles.md), not a verified repo-code finding)
Damocles embeds a full coding agent into VS Code by building on the Pi agent runtime, so the loop, tools, and subagent machinery come from Pi while the extension adds deep editor integration: inline diff previews, checkpointed rewinds and forking, and real-time subagent visualization. Its model providers include Claude, GPT/Codex, StepFun, and DeepSeek, and its MCP client merges servers from Claude Code, Codex, and its own config files with OAuth and auto-reconnect. Beyond single-agent use it supports nested subagents with mid-task steering and optional 2–5 agent collaborative teams with scratchpads and verification ledgers, plus extras such as a knowledge graph over the codebase, browser automation, and voice control. It is a solo-maintained MIT project aimed at developers who want Claude Code-class behavior inside the editor with local, inspectable state.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/damocles.md)
