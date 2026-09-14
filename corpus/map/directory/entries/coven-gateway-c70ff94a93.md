# Coven Gateway (`coven-gateway`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: Go
- Interface: platforms=CLI, Web; install=go install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/coven-gateway](../../repos/2389-research/coven-gateway.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): gRPC control plane for Coven agents that routes messages from frontends (TUI, web, Matrix bridge) to connected agents with sticky channel bindings, streams responses back via HTTP/SSE, persists threads and messages in SQLite, and includes an admin CLI (coven-admin), JWT auth, health checks, and Tailscale/tsnet integration.

(captured site page body (agents/coven-gateway.md), not a verified repo-code finding)
Coven Gateway is the gRPC control plane and message router for the Coven agent platform — infrastructure rather than an agent. Frontends (a TUI, a web client, a Matrix bridge) send messages in, and the gateway routes them to connected agents with sticky channel bindings so a conversation stays pinned to the right agent, then streams responses back over HTTP/SSE. Threads and messages persist in SQLite, and an admin CLI (coven-admin) handles operations alongside JWT auth, health checks, and Tailscale/tsnet integration for private networking. The agent loop lives in the Coven agents; the gateway only routes, stores, and authenticates. The audience is operators running a Coven deployment who need the routing and persistence layer as its own service.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coven-gateway.md)
