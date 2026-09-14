# Untether (`untether`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: littlebearapps
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=uv tool install untether (recommended) or pipx install untether
- Model providers: Claude Code (Anthropic), Codex (OpenAI), OpenCode, Pi, Gemini CLI (Google), Amp (Sourcegraph)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [littlebearapps/untether](../../repos/littlebearapps/untether.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Telegram bridge for AI coding agents — send tasks by voice/text from your phone, stream progress live, approve changes remotely; supports custom engines, transports, and commands

(captured site page body (agents/untether.md), not a verified repo-code finding)
Untether solves the away-from-desk problem in agent-driven development: tasks finish or stall while the developer is away, and there is no mobile surface for progress or approvals. A local Python process bridges agent CLIs — Claude Code, Codex, OpenCode, Pi, Gemini CLI, Amp — to a Telegram bot, streaming tool calls and file changes in real time, converting permission requests into inline buttons, and transcribing voice notes through a configurable Whisper-compatible endpoint. It adds scheduled tasks (cron, webhooks, one-shot /at delays), cost tracking against per-run and daily budgets, projects and worktrees organized as forum topics, file transfer, session export, and cross-environment resume so work started in a terminal can continue in Telegram. Developers managing agents from their phone use it; it installs via uv/pipx, drives agents through their existing subscriptions, and ships with no telemetry and token redaction in logs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/untether.md)
