# sandbox-agent (`sandbox-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: rivet-dev
- License: Apache-2.0
- Language: Rust (server) + TypeScript (SDK)
- Interface: install=npm
- Model providers: OpenAI, Anthropic (via supported agents)
- Feature flags (directory-reported):
  - mcp_support: partial - planned (roadmap: automatic MCP/skill/hook configuration) (reported)
  - plugin_support: yes - skill-based system (npx skills add) (yes)
  - claude_code_plugin: n/a - Claude Code is a supported agent; .claude config dir present (reported)
  - subagents: no (no)
  - hooks: partial - planned (roadmap) (reported)
  - plan_mode: no (no)

Repository map entry: [rivet-dev/sandbox-agent](../../repos/rivet-dev/sandbox-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Server that runs inside sandboxes to remotely control coding agents (Claude Code, Codex, OpenCode, Cursor, Amp, Pi) over HTTP/SSE. Universal Agent API - one HTTP interface controls six different agents, swappable via config. Universal Session Schema normalizes all agent event formats for storage/replay (Postgres, ClickHouse, Rivet). Single Rust static binary, fast startup, runs anywhere (E2B, Daytona, Modal, Cloudflare Containers, Docker). ...

(captured site page body (agents/sandbox-agent.md), not a verified repo-code finding)
Product teams embedding coding agents in their own apps hit the same wall six times: each harness has a proprietary API, event format, and permission model. Rivet's sandbox-agent runs as a static Rust binary inside a sandbox (E2B, Daytona, Modal, Cloudflare Containers, plain Docker) and translates all of them into one HTTP plus SSE interface covering streaming events, permission requests, and session management, with an embedded SDK mode for local subprocess use. An Inspector UI replays sessions for debugging, and a CLI mirrors the HTTP endpoints. It is Apache-2.0, ships a TypeScript SDK alongside the server, and is under active development at version 0.4.x with MCP configuration automation on the roadmap. The audience is platform engineers building agent-hosting products rather than end-user developers.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sandbox-agent.md)
