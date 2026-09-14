# qwengate (`qwengate`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: youssefvdel
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=curl -sSL https://raw.githubusercontent.com/youssefvdel/qwen-gate/main/install.sh | bash (Linux/macOS); PowerShell script (Windows); or manual git clone + bun install
- Model providers: Qwen (qwen3-7-max, qwen3-6-plus, qwen3-max, qwen3-coder, qwen3-5-plus, qwen3-5-flash, and more, via chat.qwen.ai automation)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [youssefvdel/qwengate](../../repos/youssefvdel/qwengate.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted OpenAI-compatible API gateway providing free access to Qwen models via browser automation of chat.qwen.ai; multi-account rotation, session pooling, streaming SSE, tool calling parsed from text, and a real-time web dashboard; drop-in for Cursor, Continue.dev, Claude Code, VS Code Copilot, or any OpenAI-compatible client.

(captured site page body (agents/qwengate.md), not a verified repo-code finding)
QwenGate solves a specific gap: Alibaba offers capable Qwen models free in its web chat, but provides no API endpoint, so tools like Claude Code, Cursor, or any OpenAI SDK client cannot use them directly. The gateway logs into chat.qwen.ai accounts via Playwright browser automation once, pools those sessions, and exposes standard /v1/chat/completions endpoints backed by a browserless transport for per-request speed. Multiple accounts rotate round-robin with cooldown tracking and automatic failover to stay under rate limits, and because Qwen's chat models lack native tool calling, the gateway parses JSON tool-call text from responses and re-emits it as OpenAI-format tool calls with schema validation. SSE streaming, a content filter that strips thinking tags, and a five-page observability dashboard round out the server. Self-hosters use it as a free backend for coding agents, with the README noting it is unaffiliated with Alibaba and subject to chat.qwen.ai's terms of service.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qwengate.md)
