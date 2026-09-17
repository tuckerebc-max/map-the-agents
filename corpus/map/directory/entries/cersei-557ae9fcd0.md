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
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
