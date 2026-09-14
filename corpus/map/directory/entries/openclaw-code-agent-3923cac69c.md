# openclaw-code-agent (`openclaw-code-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: goldmar
- License: MIT
- Language: TypeScript (with shell scripts)
- Interface: install=openclaw plugins install openclaw-code-agent, then openclaw plugins enable openclaw-code-agent
- Model providers: Claude Code, Codex, OpenCode
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [goldmar/openclaw-code-agent](../../repos/goldmar/openclaw-code-agent.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Stateful coding agent plugin for OpenClaw that runs Claude Code, Codex, and experimental OpenCode as managed background coding sessions launched from Telegram, Discord, or other OpenClaw-supported chat channels. Adds plan approval, session lifecycle, wake routing, worktree isolation, merge/PR follow-through, and explicit goal loops. Default launch mode is 'plan' with delegate plan review. Modes: plan, ask, off, manual, auto-merge, auto-pr. Session ...

(captured site page body (agents/openclaw-code-agent.md), not a verified repo-code finding)
Coding-agent sessions are ephemeral by default, which makes them a poor fit for chat platforms where a task spans hours and multiple follow-ups. This OpenClaw plugin treats each launched task as a managed session: Claude Code, Codex, or OpenCode runs in a git worktree in the background, the plan appears in the Telegram or Discord thread for approval, and subsequent plain-language replies steer the session — 'add unit tests', 'stop this session' — with wake routing deciding which session handles each message. Lifecycle operations go beyond launch: sessions suspend, resume, fork, and recover after restarts, and completed work surfaces as Merge, Open PR, Later, or Discard buttons. Optional goal loops run verifier-driven or 'Ralph-style' iterations unattended. Cost visibility comes from agent_stats, which reports per-session USD spend. OpenClaw users who want durable, approvable coding sessions from messaging apps are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openclaw-code-agent.md)
