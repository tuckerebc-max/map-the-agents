# koder (`koder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: feiskyer
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=uv tool install koder | pip install koder
- Model providers: OpenAI, Anthropic, Google/Gemini, GitHub Copilot, Azure, OpenRouter, 100+ LiteLLM providers, custom OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: yes (yes)

Repository map entry: [feiskyer/koder](../../repos/feiskyer/koder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first (no session uploads), bring-your-own-model across 100+ providers with universal KODER_* env vars and OAuth-backed subscription logins (Google, Claude, ChatGPT, Antigravity, GitHub Copilot); durable long-running work with goals, token budgets, cron-backed scheduled loops, and resume; SQLite sessions with rewind/thinkback/AutoDream consolidation; rich multi-agent workflows (subagents, teams, tmux teammates, mailbox routing); extensible via skills/plugins/MCP/channels/Magic Docs; sandbox-aware permissions; optional voice dictation. Alpha/experimental, learning-focused.

(captured site page body (agents/koder.md), not a verified repo-code finding)
koder is an alpha-stage, single-author Python terminal agent built around local inspectability: sessions, transcripts, tokens, and permissions live in SQLite under ~/.koder, and a /privacy-settings surface shows exactly what leaves the machine. Subscription access is handled through OAuth logins (koder auth login claude|chatgpt|github-copilot|...) while OpenAI, Anthropic, Gemini, OpenRouter, Azure, and LiteLLM providers work via API keys or KODER_* environment variables. Background subagents, tmux teammates, mailbox routing, cron-backed scheduled loops, and goal continuation with token budgets support longer-running work. As an explicitly experimental project by feiskyer, it is used for learning agentic-system design and for BYO-model terminal work rather than production deployment.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/koder.md)
