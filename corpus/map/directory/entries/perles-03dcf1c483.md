# perles (`perles`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: zjrosen
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl -sSL https://raw.githubusercontent.com/zjrosen/perles/main/install.sh | bash; or brew tap zjrosen/perles && brew install perles
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [zjrosen/perles](../../repos/zjrosen/perles.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal UI for Beads issue tracking with custom BQL (Beads Query Language) supporting boolean logic, date filtering, dependency tree traversal, and customizable kanban board views. Also described as a multi-agent orchestration control plane workflow runner, though specific agent orchestration features are not detailed in the README.

(captured site page body (agents/perles.md), not a verified repo-code finding)
perles exists for developers who manage their work in Beads, Steve Yegge's local-first issue tracker, and want a richer interface than its CLI offers. The Go-based terminal UI renders issues as customizable kanban boards and supports searching through BQL, a query language with boolean logic, date filtering, and traversal of dependency trees between issues. It runs inside any project containing a .beads directory and requires a beads database of version 0.62 or newer, upgrading via a migration command where needed. The repository's description also references a multi-agent orchestration control plane aspect, with an ORCHESTRATION.md exploring workflow-runner ideas, but the shipped product is the issue TUI. Its users are Beads adopters — often developers running AI coding agents that file and consume Beads issues as their task queue.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/perles.md)
