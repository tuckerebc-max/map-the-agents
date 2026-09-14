# Mux (Rust) (`mux-rs`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent-sdk
- Provider/maker: 2389-research
- License: MIT
- Language: Rust
- Interface: install=cargo install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (MCP client integration) (yes)
  - plugin_support: yes (extensible tool definitions) (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/mux-rs](../../repos/2389-research/mux-rs.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent SDK / agentic infrastructure library for Rust providing tool execution with structured input/output, MCP client integration, permission-gated approval flows via a policy engine, and async-first architecture on tokio. Type-safe tool definitions using Rust's type system, with an FFI crate (mux-ffi) for cross-language use.

(captured site page body (agents/mux-rs.md), not a verified repo-code finding)
Mux is an agentic infrastructure library for Rust, not a coding agent. It provides the building blocks — tool execution with structured input and output, MCP client integration to pull in external tools, and a permission-gated approval flow run through a policy engine — so that an agent built on top of it can ask a human before risky actions and stay async-first on tokio. Tool definitions are type-safe, expressed in Rust's type system rather than loose JSON, and an FFI crate (mux-ffi) exposes the same primitives to other languages. Mux ships no coding agent of its own; developers compose it into their own agent or harness. The audience is Rust developers who want a foundation for agent tooling and approval flows without reinventing the glue.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mux-rs.md)
