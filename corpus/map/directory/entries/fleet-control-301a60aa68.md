# Fleet Control (`fleet-control`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: 2389-research
- License: unknown
- Language: Go
- Interface: platforms=CLI; install=go install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (MCP server so agents can inspect/instruct each other) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (agents can send instructions to other agents via MCP) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/fleet-control](../../repos/2389-research/fleet-control.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Control plane / fleet management tool for AI coding agents running in tmux panes. A background daemon polls tmux sessions, captures pane scrollback, classifies each pane's status (running/idle/done), records session history to SQLite, and exposes a CLI, TUI dashboard, REST API over Unix socket, and MCP server so one agent can inspect, read conversations of, or send instructions to other ...

(captured site page body (agents/fleet-control.md), not a verified repo-code finding)
Fleet Control is a control plane for AI coding agents that live in tmux panes. A background daemon polls tmux sessions, captures each pane's scrollback, and classifies its status — running, idle, or done — so an operator can see the whole fleet at a glance from a TUI dashboard or a CLI. Session history is recorded to SQLite, and a REST API over a Unix socket exposes the same state programmatically. The notable piece is an MCP server: one agent can inspect another pane, read its conversation, or send it instructions, turning the fleet into something agents can drive themselves. Fleet Control owns no agent loop — the agents in the panes do — it just observes, classifies, and relays. The audience is anyone running many agent sessions side by side in tmux who wants visibility and inter-agent coordination without a heavier orchestrator.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fleet-control.md)
