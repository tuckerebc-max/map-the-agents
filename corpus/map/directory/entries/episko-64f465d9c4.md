# Episko (`episko`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: respeak-io
- License: MIT
- Language: TypeScript
- Interface: platforms=Desktop; install=Download the macOS .dmg (Apple silicon) or Windows .msi from episko.dev; requires Claude Code on PATH
- Model providers: delegates to Claude Code
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [respeak-io/episko](../../repos/respeak-io/episko.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A cockpit that gives every Claude Code session its own live terminal gathered into one dashboard, with per-session model, context usage, cost, tokens, and the exact tool currently running, permission prompts surfaced with risk indication, and Claude usage-limit tracking with pace warnings — built on Tauri, MIT, no accounts or telemetry.

(captured site page body (agents/episko.md), not a verified repo-code finding)
Episko — from the Greek episkopos, the one who watches over — is a desktop cockpit for herding Claude Code agents. Each Claude Code session gets its own live terminal (or connects to Ghostty, Terminal, or iTerm), and all of them gather into a single dashboard where you can see model, context usage, cost, token counts, and the exact tool currently running per session, with urgency-colored states and cmd+K search to jump to whatever needs attention. Permission prompts surface as allow/deny cards with risk indication, agents launch on repos, branches, or git worktrees with GitHub issue integration that creates a worktree and writes a claim so teammates' agents don't duplicate work, and local analytics track spend, tokens by model, and cost per session. It reuses Claude's --session-id so restarts rebuild panes with scrollback intact, and it tracks the 5-hour and weekly usage windows with pace warnings. Built by Respeak in Karlsruhe on Tauri, it is free and open source with no accounts and no telemetry.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/episko.md)
