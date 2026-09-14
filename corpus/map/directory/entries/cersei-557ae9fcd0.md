# cersei (`cersei`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: pacifio
- License: MIT
- Language: Rust
- Interface: install=cargo install --path crates/abstract-cli, or add as Cargo dependency
- Model providers: Anthropic, OpenAI, Ollama, Azure, vLLM
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [pacifio/cersei](../../repos/pacifio/cersei.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): "Reverse-engineered Rust port of Claude Code architecture as an embeddable SDK; graph memory (Grafeo) with 98us recall vs Claude Code's 7.5s LM call; 6MB binary, 4.9MB RSS; 30+ built-in tools;

(captured site page body (agents/cersei.md), not a verified repo-code finding)
cersei came from reverse-engineering Claude Code's architecture and rebuilding it in Rust as a library: tool execution, LLM streaming, subagent orchestration, persistent memory, skills, and MCP integration all exposed as composable crates for embedding agents in applications. Its pitch is efficiency at the systems level — the companion Abstract CLI binary measures roughly 6MB with 4.9MB RSS and 32ms startup — alongside a three-tier memory design that combines flat files, CLAUDE.md-style context, and an optional graph memory backed by Grafeo, which answers recall queries in microseconds without an LLM call. Developers use it to build custom agents with Claude Code-like capability without Node.js, or to embed agent behavior in products where binary size and memory matter. It is MIT-licensed, Rust-based, installable via Cargo, and actively maintained with published docs and benchmark suites against Claude Code and competing agent frameworks.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cersei.md)
