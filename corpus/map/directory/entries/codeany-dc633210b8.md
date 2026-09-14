# codeany (`codeany`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: codeany-ai
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/codeany-ai/codeany/main/install.sh | sh, or go install github.com/codeany-ai/codeany/cmd/codeany@latest
- Model providers: Anthropic, OpenRouter, custom (via CODEANY_BASE_URL/CODEANY_MODEL env vars)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [codeany-ai/codeany](../../repos/codeany-ai/codeany.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI-powered terminal agent built with Go, Bubble Tea TUI, and Open Agent SDK. Features 78 built-in slash commands, custom Skills system (user-defined sub-agents via SKILL.md files), plugin architecture, pre/post tool use hooks, plan mode, Chinese/IME input support, self-update capability, and compatibility with both CODEANY.md and CLAUDE.md project instruction files.

(captured site page body (agents/codeany.md), not a verified repo-code finding)
Codeany is a terminal coding agent built in Go on the Open Agent SDK with a Bubble Tea interface, covering codebase explanation, test execution, commits, review, and bug investigation through an agentic loop with maxTurns bounds and permission modes. Its configuration surface mirrors Claude Code conventions: project instructions come from CODEANY.md or CLAUDE.md plus .codeany/rules/ markdown files, and per-user state lives under ~/.codeany/ with settings, permissions, memory, sessions, skills, and plugins directories. Extensibility covers stdio MCP servers managed through /mcp, pre/post tool-use hooks, SKILL.md-defined skills, and plugins loaded from ~/.codeany/plugins/. Models default to Anthropic with OpenRouter or custom endpoints configured through environment variables, sessions resume or export as JSON, and non-interactive pipe and print modes support scripting. The project is young — a small commit history and no releases — with Chinese/IME input support among its distinguishing features.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codeany.md)
