# DeepSeek Reasonix (`deepseek-reasonix`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: esengine
- License: MIT
- Language: Go, TypeScript
- Interface: platforms=CLI; install=npm i -g reasonix, brew install esengine/reasonix/reasonix, desktop installer, VS Code extension, or make build from source
- Model providers: DeepSeek (preset), any OpenAI-compatible endpoint via config, optional dual-model (executor + planner)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [esengine/deepseek-reasonix](../../repos/esengine/deepseek-reasonix.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): DeepSeek-native AI coding agent engineered around prefix-cache stability for long-running sessions. Distributed as a self-contained static Go binary. Features plan mode, permissions, workspace sandbox, per-turn checkpoints, config-driven providers/tools/plugins, multi-model support (executor + planner), and Extension Protocol v1 sidecars.

(captured site page body (agents/deepseek-reasonix.md), not a verified repo-code finding)
Reasonix is a DeepSeek-native coding agent built for long autonomous runs, with mechanics tuned to that goal: cache-aware context maintenance aligned with DeepSeek's prefix-cache pricing, a workspace sandbox, per-turn checkpoints with rewind, and a permission system for unattended operation. It runs as a single static Go binary in terminal/TUI, desktop, browser, or editor via ACP, with a config-driven setup (reasonix.toml), a planner/executor model split, and support for any OpenAI-compatible endpoint. Extensibility goes beyond MCP servers to an Extension Protocol with a Go SDK for sidecars that intercept events and add providers, and subagent profiles are first-class. The project is one of the most popular DeepSeek-focused harnesses (35k+ stars, very active development, bilingual docs, npm/Homebrew/desktop distribution).
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepseek-reasonix.md)
