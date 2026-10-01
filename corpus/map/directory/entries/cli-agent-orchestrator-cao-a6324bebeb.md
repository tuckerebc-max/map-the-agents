# CLI Agent Orchestrator (CAO) (`cli-agent-orchestrator-cao`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: awslabs
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI; install=pip
- Model providers: Kiro CLI, Claude Code, Codex CLI, Antigravity CLI, Hermes, Kimi CLI, GitHub Copilot CLI, OpenCode CLI, Oh My Pi (OMP) CLI, Cursor CLI, Grok Build CLI
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [awslabs/cli-agent-orchestrator](../../repos/awslabs/cli-agent-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Orchestrates multiple AI coding CLI agents simultaneously in isolated tmux sessions, allowing a supervisor to delegate work to specialist agents in parallel or sequence. Supports 11+ provider CLIs, offers a Web UI, MCP server, plugins, flows/workflows, skills, persistent memory with self-learning, and agent profiles — all while keeping each agent as a full native CLI process with its own authentication.

(captured site page body (agents/cli-agent-orchestrator-cao.md), not a verified repo-code finding)
CAO solves the coordination problem when a team uses several CLI coding agents at once: each provider CLI keeps its own authentication and full native capability, while CAO handles tmux session isolation, delegation from a supervisor profile to specialist workers, and lifecycle management through a server with a Web UI, HTTP API, PTY WebSocket, and MCP surface. Flows extend ad-hoc delegation into scheduled multi-step pipelines, and profiles can restrict which tools an agent may use. It is Apache-2.0, pip-installable from awslabs, documented with courses, and under active development, making it the most institutional entry among the CLI-agent orchestrators.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/cli-agent-orchestrator-cao.md)
