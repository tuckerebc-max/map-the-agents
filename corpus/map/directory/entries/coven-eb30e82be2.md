# Coven (`coven`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: 2389-research
- License: MIT
- Language: Rust
- Interface: platforms=CLI, Web; install=cargo build
- Model providers: Anthropic (Claude)
- Feature flags (directory-reported):
  - mcp_support: yes (mcp-bridge-pack) (yes)
  - plugin_support: yes (tool packs via Pack SDK) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (coven-swarm supervises agents across workspaces) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/coven](../../repos/2389-research/coven.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Rust platform for orchestrating AI agents with tool capabilities and gRPC streaming. coven-agent runs a single-workspace agent, coven-swarm supervises agents across multiple workspaces, and the Go gateway handles routing, SQLite thread/message storage, and tool pack registry. Supports TUI, HTTP API, Matrix bridge, and CLI frontends with modular tool packs.

(captured site page body (agents/coven.md), not a verified repo-code finding)
Coven is a Rust platform for orchestrating AI agents that need tool capabilities and gRPC streaming. The architecture splits cleanly: coven-agent runs a single-workspace agent, coven-swarm supervises agents across multiple workspaces, and a separate Go gateway (coven-gateway) handles routing, persists threads and messages in SQLite, and serves as the tool pack registry. Tool packs built via the Pack SDK extend agent capabilities, and an mcp-bridge-pack bridges MCP tools into the same surface. Frontends are pluggable — a TUI, an HTTP API, a Matrix bridge, and a CLI all talk to the gateway — so the same agents can be driven from a terminal or a chat room. The audience is developers coordinating multiple Claude-backed agents across workspaces who want the orchestration layer in Rust.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coven.md)
