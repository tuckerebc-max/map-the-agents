# vibeproxy (`vibeproxy`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: automazeio
- License: MIT
- Language: Swift
- Interface: platforms=Desktop; install=binary
- Model providers: Anthropic, OpenAI, Google, Moonshot, Alibaba, Z.AI, GitHub Copilot
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [automazeio/vibeproxy](../../repos/automazeio/vibeproxy.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native macOS menu bar app that lets you reuse existing AI subscriptions (Claude Code, Codex, Gemini, Kimi, Qwen, Z.AI GLM) with AI coding tools like Factory Droids by handling OAuth, token management, and API routing automatically.

(captured site page body (agents/vibeproxy.md), not a verified repo-code finding)
Subscription plans for Claude, ChatGPT, Gemini, Kimi, Qwen, and GLM cost far less than API usage, but third-party coding tools cannot authenticate with a subscription — they expect API keys, so developers end up paying twice. VibeProxy closes that gap: a signed macOS menu-bar app runs a local proxy (built on CLIProxyAPIPlus) that performs each provider's OAuth flow, manages token refresh, and exposes the subscriptions as API-compatible endpoints that coding tools like Factory Droids or Amp CLI call as if they were ordinary APIs. Multiple accounts per provider rotate round-robin with rate-limit failover, provider priorities hot-reload, and a Vercel AI Gateway mode routes Claude traffic through a sanctioned gateway specifically to avoid account flags. macOS developers stretching their existing subscriptions across tools are the users; it is MIT-licensed, free, code-signed, and auto-updates via Sparkle.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibeproxy.md)
