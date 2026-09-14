# zhin (`zhin`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: zhinjs
- License: MIT
- Language: TypeScript
- Interface: install=npm create zhin-app my-bot -y; or pnpm add zhin.js + adapter
- Model providers: OpenAI, AI SDK vendor packages
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [zhinjs/zhin](../../repos/zhinjs/zhin.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-native TypeScript bot framework for building bots/assistants on 20+ chat platforms (QQ, WeChat, Discord, Telegram, Slack, etc.) with multi-account support and opt-in AI agent capabilities

(captured site page body (agents/zhin.md), not a verified repo-code finding)
zhin.js is a framework for building bots that live on instant-messaging platforms, and its design treats multi-platform reach as the primary problem: one TypeScript codebase, with adapters targeting more than twenty services including QQ, WeChat, Discord, Telegram, Slack, and DingTalk, packaged as a core library under 10MB. Applications are composed from file-convention plugins — commands, tools, and agent skills declared in directories and hot-reloaded on change — plus declarative APIs for adapters and commands, managed remotely through a browser console. The project positions AI deliberately: a plain install is a conventional IM framework, and agent capability arrives only by adding the @zhin.js/agent package alongside an AI SDK provider, at which point the bot gains chat, tools, memory, sessions, orchestration, and security policies such as bash allowlists and approval modes. MCP client support exists as a further opt-in tier, and LLM calls ride Vercel AI SDK providers. The README draws an explicit boundary — this is not a Cursor- or Claude Code-style coding agent — which is why it lands outside the agent harness category despite the agentic add-on. Its audience is bot developers, particularly in the Chinese IM ecosystem, who want a maintainable framework that can grow agent features into an existing bot rather than the reverse.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zhin.md)
