# AgentsView (`agentsview`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: kenn-io
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=binary
- Model providers: LiteLLM, OpenRouter (for cost calculation); reads sessions from 20+ agents
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [kenn-io/agentsview](../../repos/kenn-io/agentsview.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first analytics tool (single Go binary) that browses, searches, and tracks costs across 20+ AI coding agents' session data. SQLite-indexed for 100x faster queries vs re-parsing raw files. Multi-backend (SQLite, PostgreSQL, DuckDB), full-text + semantic search, SSE live updates, privacy-focused (loopback binding, disableable telemetry), Tauri desktop wrapper.

(captured site page body (agents/agentsview.md), not a verified repo-code finding)
Session logs from coding agents pile up in vendor-specific formats, making cost tracking and history search a per-tool chore. AgentsView discovers sessions from a long list of agents (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, Windsurf, OpenCode, Goose, Aider, Devin CLI, Zed, Warp, and dozens more), normalizes them into a local SQLite database with FTS5 search, and serves a local web UI with usage dashboards, activity heatmaps, and live SSE updates. Everything stays on the machine by default; optional PostgreSQL push supports team dashboards and DuckDB offers a read-only analytical mirror. Cost analytics are cache-aware with LiteLLM/OpenRouter pricing, positioned as a dramatically faster replacement for ccusage-style accounting. Distribution is a single binary via install script, Homebrew cask, GitHub releases, or Docker.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentsview.md)
