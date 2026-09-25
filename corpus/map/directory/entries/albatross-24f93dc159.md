# Albatross (`albatross`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: morganlinton
- License: MIT
- Language: Rust
- Interface: platforms=CLI, Web; install=brew install morganlinton/tap/albatross
- Model providers: Ollama,LM Studio,MLX,llama.cpp,OpenRouter,OpenAI,Anthropic,OpenAI Codex,Grok
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [morganlinton/albatross](../../repos/morganlinton/albatross.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-first AI coding agent/harness with multi-model routing; supports local (Ollama, LM Studio, MLX, llama.cpp) or cloud providers with one TUI. MCP-native; hooks via agent.config.json; /plan commands for plan mode.

(captured site page body (agents/albatross.md), not a verified repo-code finding)
Albatross is a Rust TUI whose pitch is 'no black box': every routing decision, token spend, and provider switch is itemized. Work is planned through /plan, which expands an intent into a spec file (.albatross/spec.md) and can build routed task graphs across configured model tiers; /iterate adds a critic-scored generate-evaluate loop and /auto runs batches overnight. MCP servers plug in through mcpServers in agent.config.json with trust gating, and lifecycle hooks can allow, deny, or block tool calls. It is MIT-licensed, installed via Homebrew or cargo, embeds an SDK for building other tools, and stays on a fast release cadence (v2.4.x, 224 stars) as a solo project.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/albatross.md)
