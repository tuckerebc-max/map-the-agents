# Coro Code (`coro-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Blushyes
- License: Apache-2.0, MIT (dual)
- Language: Rust
- Interface: platforms=CLI; install=cargo install --git https://github.com/Blushyes/coro-code --bin coro
- Model providers: OpenAI, Anthropic, Google, Azure OpenAI, OpenAI-compatible (DeepSeek)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [blushyes/coro-code](../../repos/blushyes/coro-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): High-performance AI coding agent in Rust with rich terminal UI; cross-platform; extensible tool system; context export/restore persistence; OpenAI-compatible API support. MCP and plugin systems planned on roadmap. Positioned as a free alternative to Claude Code.

(captured site page body (agents/coro-code.md), not a verified repo-code finding)
Claude Code established the terminal-agent workflow, but it is proprietary and tied to one vendor's models, leaving room for an open, inspectable equivalent. Coro Code implements that workflow in Rust: a single cross-platform binary runs an agent loop with bash execution, file operations, and an extensible tool system, presented through a rich terminal UI with real-time streaming. Session state persists via JSON context export and restore, and token compression keeps long sessions within budget. The LLM layer targets OpenAI and OpenAI-compatible endpoints (DeepSeek among them), with Anthropic and Google support on the roadmap alongside permission systems, sandboxing, and MCP extension. Developers wanting a self-hosted terminal agent they can inspect and modify - particularly in Rust ecosystems - are the audience; the project is early but actively developed.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coro-code.md)
