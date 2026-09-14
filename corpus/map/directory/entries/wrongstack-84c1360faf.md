# WrongStack (`wrongstack`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: WrongStack
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Web; install=npm i -g wrongstack (or pnpm add -g wrongstack), then run wrongstack (alias: wstack)
- Model providers: ~140 providers from 4 API-key wire families (Anthropic, OpenAI, Google, ~125 OpenAI-compatible endpoints) + OAuth sign-in with ChatGPT/Codex, Claude Pro/Max, GitHub Copilot; local presets for Ollama, vLLM, LM Studio
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [wrongstack/wrongstack](../../repos/wrongstack/wrongstack.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A complete, from-scratch agent (not a wrapper or orchestration kit) with its own compact kernel (~1,670 lines), 61 built-in tools, 77-role multi-agent fleet, SAGE persistent memory (SQLite/FTS5), inter-agent mailbox, Chimera auto-review, 6 surfaces (REPL, TUI, WebUI, SimpleUI, Desktop, HQ), all working standalone with no third-party CLI dependency. --no-features runs fully offline.

(captured site page body (agents/wrongstack.md), not a verified repo-code finding)
WrongStack exists to demonstrate a complete coding agent built from scratch rather than wrapping third-party agent CLIs. Its compact kernel (~1,670 lines) rests on four primitives (Container, Pipeline, EventBus, RunController) and can boot fully offline with --no-features. Around it run 61 first-party built-in tools, a 77-role multi-agent fleet dispatched under a Director with per-subagent budgets and JSONL transcripts, SAGE persistent memory (SQLite/FTS5) that stores typed facts, decisions, conventions, and bug root causes anchored to files, symbols, and commits, and a SQLite-backed inter-agent mailbox. Support extends to roughly 140 model providers, OAuth sign-in via ChatGPT or Claude subscriptions, per-role model routing with fallback chains, and six surfaces from REPL and TUI to an Electron desktop app. It is MIT-licensed, npm-installable, and heavily tested with tens of thousands of tests.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/wrongstack.md)
