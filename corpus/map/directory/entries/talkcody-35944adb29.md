# talkcody (`talkcody`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: talkcody
- License: MIT
- Language: TypeScript, Rust
- Interface: install=Download installer (macOS, Windows, Linux AppImage) or build from source
- Model providers: OpenAI, Anthropic, Google, Ollama, LM Studio
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [talkcody/talkcody](../../repos/talkcody/talkcody.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Free, open-source AI coding agent with four-level parallelism (project, task, agent, tool), 100% local storage, offline capable, no vendor lock-in, with an agents & skills marketplace

(captured site page body (agents/talkcody.md), not a verified repo-code finding)
TalkCody is an open-source desktop coding agent aimed at users who want agent capability without sending code to a hosted service or adopting a single vendor. Built on Rust/Tauri with a React frontend, it runs tasks with parallelism at four levels — multiple projects, multiple tasks per project, multiple agents per task, and concurrent tool calls — and keeps all sessions, indexes, and settings on local disk, which also enables offline use with Ollama or LM Studio. Agent behavior is extensible through an agents-and-skills marketplace where community agents and workflows are downloaded and shared, and MCP servers extend the tool surface. Model access is deliberately flexible: OpenAI, Anthropic, Google, GitHub Copilot, or existing ChatGPT subscriptions, plus local models for fully offline operation. The installers cover macOS (both architectures), Windows, and Linux, and the project documents itself through talkcody.com/docs. Privacy-conscious individual developers and small teams are the primary users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/talkcody.md)
