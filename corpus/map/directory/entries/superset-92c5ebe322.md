# Superset (`superset`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: superset-sh
- License: Elastic License 2.0 (ELv2)
- Language: TypeScript (Bun, React, Electron)
- Interface: platforms=CLI, IDE; install=brew
- Model providers: OpenRouter, Bedrock, Vertex, Vercel AI Gateway (BYO providers); Claude, OpenAI/Codex, Gemini, Grok, Mistral, Kimi
- Feature flags (directory-reported):
  - mcp_support: yes (MCP server; transport not specified) (yes)
  - plugin_support: yes (custom agents, skills, terminal presets, themes) (yes)
  - claude_code_plugin: yes (fully supported agent; .claude-plugin and .claude directories present) (yes)
  - subagents: yes (.agents directory; built-in orchestration skills for parallel agents) (yes)
  - hooks: yes (setup/teardown/run scripts) (yes)
  - plan_mode: yes (inline tool approvals and plan review) (yes)

Repository map entry: [superset-sh/superset](../../repos/superset-sh/superset.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic IDE that orchestrates 100+ CLI coding agents (Claude Code, Codex, Cursor, etc.) in parallel across isolated git worktrees, with built-in terminal, diff viewer, in-app browser, MCP server, CLI, and SDK — all free forever for local use.

(captured site page body (agents/superset.md), not a verified repo-code finding)
Superset is structured around the workflow of running many CLI agents at once: every agent works in its own git worktree with an isolated branch and terminal, the app provides diff viewing, in-app browsing with per-workspace port detection, and scheduled automations, and Slack/Linear integrations tie agent output into team tooling. It treats any terminal agent as a workload — Claude Code, Codex, Cursor Agent, Gemini CLI, OpenCode — and exposes an MCP server and TypeScript SDK so those agents can create and manage Superset workspaces themselves. The desktop app is free under the Elastic License 2.0, with the restriction limited to reselling Superset itself as a service. It is YC-backed, ships daily, and publishes an iOS companion for remote monitoring of workspaces.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/superset.md)
