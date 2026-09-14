# VibeAround (`vibearound`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: jazzenchen
- License: MIT
- Language: Rust, TypeScript
- Interface: platforms=CLI, IDE, Web; install=npm i @vibearound/cli  (or desktop app: macOS dmg, Windows exe/msi/zip, Linux AppImage/deb)
- Model providers: DeepSeek, Alibaba DashScope, Moonshot/Kimi, MiniMax, Xiaomi MiMo, xAI/Grok, NVIDIA NIM, Z.AI/GLM, Google Gemini, OpenRouter, Azure OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [jazzenchen/vibearound](../../repos/jazzenchen/vibearound.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): All-in-one hub that launches multiple AI coding agents (Claude Code, Codex CLI, Gemini CLI, Pi, OpenCode, etc.) from a single UI with an API bridge that translates between incompatible provider protocols (OpenAI Responses, Chat Completions, Anthropic Messages, Gemini Generate Content). Enables session continuity across desktop/CLI/web/mobile/IM channels (Feishu, Discord, Slack, Telegram).

(captured site page body (agents/vibearound.md), not a verified repo-code finding)
VibeAround exists because the agent ecosystem fragmented: every CLI has its own config format and protocol, subscriptions overlap, and a session is trapped on the device where it started. The hub launches Claude Code, Codex, Gemini CLI, Pi, OpenCode, and desktop variants from one desktop/CLI/web surface with per-agent profiles, workspaces, and terminals, without modifying the agents' own configs. Its standalone API bridge translates between OpenAI Responses, Chat Completions, Anthropic Messages, and Gemini shapes — with model aliases, provider presets, and a live request recorder — and can expose local agents as OpenAI/Anthropic-compatible endpoints. Sessions continue across devices and IM channels (Feishu/Lark, Discord, Slack, Telegram, WeChat) via /pickup handover, with host-side web search injected when a provider lacks it. Individual developers running several agents — largely a single active maintainer's project — use it to keep subscriptions and sessions unified; it is MIT-licensed and local-first.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibearound.md)
