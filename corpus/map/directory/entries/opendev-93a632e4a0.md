# opendev (`opendev`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): Compound AI system: multiple models collaborate, each optimized for its role across 5 workflow slots (Normal, Thinking, Compact, Critique, VLM), each independently bindable to any model/provider. Parallel agent fleet via async Tokio tasks. Blazing fast (4.3 ms startup, 9.4 MB RAM, 18 MB single binary). Both TUI and Web UI with remote session support.

(captured site page body (agents/opendev.md), not a verified repo-code finding)
Most coding agents lock a session to one model, which wastes frontier tokens on summarization and under-provisions hard reasoning. OpenDev, a Rust CLI, treats the agent as a compound AI system: five workflow slots — Normal for execution, Thinking for planning, Compact for context summarization, Critique for self-review, VLM for vision — each bind independently to any of nine providers (OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, Azure) or to Ollama/LM Studio locally, with defined fallback chains when a slot's model is absent. An Agent Fleet runs parallel sub-agents, each with its own binding, and MCP integration connects external tools; a TUI and remote-accessible Web UI cover interaction. Distribution spans cargo, Homebrew, shell installers, and GitHub Release binaries for all three OSes. Its maintainers publish an arXiv technical report on the compound-AI design, and the performance pitch — 4.3 ms startup, 9.4 MB RAM — targets developers who find Node-based agents heavy.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/opendev.md)
