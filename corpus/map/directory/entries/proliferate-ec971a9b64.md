# Proliferate (`proliferate`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: proliferate-ai
- License: AGPL-3.0
- Language: Rust
- Interface: platforms=Desktop, Web; install=Desktop app for macOS, or self-host the control plane via Docker Compose, one-click AWS CloudFormation, GCP, Azure, Kubernetes, or air-gapped deployment
- Model providers: delegates to the connected agents (Claude Code, Codex, OpenCode, Cursor, Grok)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [proliferate-ai/proliferate](../../repos/proliferate-ai/proliferate.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An open-source AI IDE that runs Claude Code, Codex, OpenCode, Cursor, and Grok in parallel through their native harnesses, giving every task an isolated git worktree with its own branch, terminal, conversation, and review state, plus recurring and event-driven workflows — self-hostable all the way to air-gapped operation.

(captured site page body (agents/proliferate.md), not a verified repo-code finding)
Proliferate is a workspace for running many coding agents at once rather than a coding agent itself: each task gets an isolated git worktree and the agent of your choice drives it through its native harness, so subscriptions, logins, and MCP servers stay as configured. The control plane is fully self-hostable — Docker Compose, one-click AWS, GCP, Azure, Kubernetes, or air-gapped — with a macOS desktop app for local use, and the runtime itself is Rust with a TypeScript/Node frontend. Beyond parallel sessions it supports subagent delegation, integrations including MCP, skills, computer and browser use, and custom tools, plus workflows that run agents on schedules or events like nightly reviews and alert triage. Its audience is teams and self-hosters who want a Vercel-style control plane over the agent CLIs they already pay for.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/proliferate.md)
