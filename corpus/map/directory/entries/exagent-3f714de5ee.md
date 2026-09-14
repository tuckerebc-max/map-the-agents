# ExAgent (`exagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: exqqstar
- License: Apache-2.0, MIT
- Language: Rust, TypeScript
- Interface: platforms=Desktop; install=Download signed/notarized macOS DMG from GitHub Releases; or npm ci + npm run tauri:dev for dev build
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [exqqstar/exagent](../../repos/exqqstar/exagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local desktop-first agent workbench with a Rust runtime and Tauri/React GUI; durable sessions, approval-gated tools, subagents, goal tracking, project memory, MCP tools, workflows, and live runtime inspection.

(captured site page body (agents/exagent.md), not a verified repo-code finding)
ExAgent is built for running a personal coding agent entirely on one's own workstation with no hosted component. The Rust runtime normalizes provider APIs into unified conversation, tool-call, and streaming types, configured per-provider in the GUI with API-key or OAuth credentials stored locally; the Tauri/React shell adds projects, durable sessions, and a live inspector over the agent's event stream. Tool use is approval-gated by default, subagents and workflow runs (such as deep search) extend capability, SKILL.md files define reusable procedures, and event replay makes past runs auditable. The project explicitly targets personal use — no production sandbox isolation, hosted collaboration, or public SDK — and remains a single-author, early-stage effort.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/exagent.md)
