# cersei (`cersei`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
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

- category: published=agent-sdk, backing=agent, page=

## Description

(published index `description`, not a verified repo-code finding)
cersei came from reverse-engineering Claude Code's architecture and rebuilding it in Rust as a library: tool execution, LLM streaming, subagent orchestration, persistent memory, skills, and MCP integr
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
