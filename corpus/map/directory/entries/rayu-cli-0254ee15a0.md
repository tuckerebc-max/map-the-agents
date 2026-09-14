# rayu-cli (`rayu-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Choeng-Rayu
- License: MIT
- Language: TypeScript (CLI), Go (gateway), NestJS (backend), Next.js (web)
- Interface: platforms=CLI, IDE; install=npm install -g @rayu-dev/rayu-cli; run rayu. Or npx @rayu-dev/rayu-cli without installing.
- Model providers: Anthropic, OpenAI, DeepSeek, Google Gemini, Kimi, Ollama, LM Studio (local models)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [choeng-rayu/rayu-cli](../../repos/choeng-rayu/rayu-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal AI coding agent with native real-time P2P collaboration (no cloud intermediaries), sub-500ms time-to-first-token via a custom React/Ink renderer and Go gateway, zero-data-retention privacy, built-in Agent Swarms for parallel multi-agent execution, offline capabilities via Ollama/LM Studio, and multi-provider BYOK across 6+ providers with mid-session model switching.

(captured site page body (agents/rayu-cli.md), not a verified repo-code finding)
Rayu CLI is a terminal coding agent built around a claim most competitors lack: native peer-to-peer collaboration, where two developers share a live agent session directly rather than relaying through cloud intermediaries. The client is a TypeScript/Ink application with a custom renderer, fronted by a Go gateway and a NestJS backend, with model access via BYOK across Anthropic, OpenAI, DeepSeek, Gemini, Kimi, and local Ollama or LM Studio deployments. Beyond collaboration, it runs parallel 'agent swarms' of specialized subagents and offers an optional hosted gateway with a zero-data-retention policy for users who prefer not to manage keys. The project markets aggressively against Claude Code, OpenCode, and Codex, though its performance and superiority claims remain its own rather than independently verified. It is aimed at teams and enterprises that want terminal agents without routing code through a vendor's cloud.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rayu-cli.md)
