# opendev (`opendev`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: opendev-to
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=cargo, brew, binary
- Model providers: OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, Azure OpenAI; local via Ollama, LM Studio, llama-server
- Feature flags (directory-reported):
  - mcp_support: yes (dynamic tool discovery; opendev mcp add/list/enable/disable) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [opendev-to/opendev](../../repos/opendev-to/opendev.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Most coding agents lock a session to one model, which wastes frontier tokens on summarization and under-provisions hard reasoning. OpenDev, a Rust CLI, treats the agent as a compound AI system: five w
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
