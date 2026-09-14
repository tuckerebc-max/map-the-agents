# Dexto (`dexto`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: truffle-ai
- License: Elastic License 2.0
- Language: TypeScript
- Interface: platforms=CLI, Web; install=binary
- Model providers: OpenAI, Anthropic, Google, Groq, xAI, Cohere, Ollama, AWS Bedrock, Vertex AI, OpenRouter, LiteLLM, Glama, node-llama-cpp
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [truffle-ai/dexto](../../repos/truffle-ai/dexto.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Configuration-driven (YAML) agent harness ('OS for AI agents'); batteries-included (sessions, memory, tools, observability); instant mid-conversation model switching; multi-agent sub-agent spawning; runs as CLI, Web UI, REST API, Discord/Telegram, or MCP server; ships with production-ready coding agent

(captured site page body (agents/dexto.md), not a verified repo-code finding)
Dexto treats the agent runtime as infrastructure: a YAML file defines the model, tools, and MCP servers, and the same harness exposes the agent through CLI, Web UI, REST API, or chat platforms. The bundled coding agent edits code, runs tests, spawns ephemeral explore subagents with unified approval forwarding, and swaps models mid-conversation — but the same YAML pattern builds non-coding agents, which is the point. An SDK embeds the runtime in Node applications with session management and observability included. It targets developers building their own agents who want the orchestration layer handled: state, tool orchestration, memory, and recovery instead of raw model calls.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/dexto.md)
