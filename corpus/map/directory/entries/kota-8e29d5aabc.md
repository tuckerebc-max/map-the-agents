# kota (`kota`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: StepfenShawn
- License: MIT
- Language: Rust
- Interface: install=cargo install kota (CLI) or add as dependency in Cargo.toml (library)
- Model providers: OpenAI-compatible (gpt-4o, gpt-4-turbo, gpt-3.5-turbo), DeepSeek, Anthropic Claude, Ollama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [stepfenshawn/kota](../../repos/stepfenshawn/kota.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Vim-inspired philosophy-lightweight Rust build, Lua-based configuration (Neovim-style), built-in Skills system, usable as both CLI and embeddable Rust library, plan mode similar to Claude Code, multi-model support

(captured site page body (agents/kota.md), not a verified repo-code finding)
kota applies the Neovim philosophy — small, fast, configured in Lua — to terminal coding agents. Users configure models and custom commands in .kota/config.lua, extend behavior with SKILL.md-defined skills, and drive execution through an update_plan tool that tracks task dependencies and status the way Claude Code does. Because it builds as both a CLI (cargo install kota) and a Rust crate with AgentBuilder and ContextManager APIs, the same agent core can be embedded into larger tools. Model access covers OpenAI-compatible endpoints, DeepSeek, Anthropic, and Ollama. It suits Rust users and embedding scenarios; MCP support remains on the roadmap rather than in the binary.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/kota.md)
