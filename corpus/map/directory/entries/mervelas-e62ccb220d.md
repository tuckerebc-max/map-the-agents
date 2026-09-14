# Mervelas (`mervelas`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: swadhinbiswas
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=git clone + bun install + bun run scripts/build.ts + node dist/cli.mjs (requires Bun)
- Model providers: OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, local models
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [swadhinbiswas/mervelas](../../repos/swadhinbiswas/mervelas.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Independent open-source AI coding CLI built for freedom and zero telemetry, local-first, built with Bun and rendered via a custom React Ink abstraction; supports custom local coding agents and MCP integration.

(captured site page body (agents/mervelas.md), not a verified repo-code finding)
Mervelas exists for developers who reject the telemetry and lock-in of mainstream assistants: it stores session history only in ~/.mervelas/projects/ as JSONL, ships with no analytics, and lets the user point it at OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, or locally hosted endpoints. The interface is a terminal UI rendered through a custom React Ink abstraction built on Bun, with commands for configuration, context inspection, agent switching, and MCP server attachment. Custom agents are defined and switched through /agents, letting one binary wrap different local coding agents under a single interface. Distribution is deliberately absent from npm: the README requires cloning, building with Bun, and running the bundle directly, and the repository holds exactly five commits with no releases. Its audience is developers who want provider sovereignty and zero telemetry and are comfortable building a CLI from source; the project is experimental and its trajectory depends on a single maintainer.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mervelas.md)
