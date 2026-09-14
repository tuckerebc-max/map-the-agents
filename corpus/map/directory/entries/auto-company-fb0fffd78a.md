# auto-company (`auto-company`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: nicepkg
- License: MIT
- Language: Shell
- Interface: platforms=Autonomous, IDE; install=git clone then make start (foreground) or make install (launchd daemon). Requires macOS + Claude Code CLI.
- Model providers: Anthropic (Claude Code CLI required; Opus default, Sonnet via env var)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: no (no)

Repository map entry: [nicepkg/auto-company](../../repos/nicepkg/auto-company.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Fully autonomous AI company that runs 24/7 using 14 AI agents modeled after real-world legendary experts (Bezos, Munger, DHH, etc.) powered by Claude Code Agent Teams. Features 24/7 launchd daemon loop with crash auto-restart, consensus memory via consensus.md, auto-convergence cycles with GO/NO-GO decisions, 6 standard workflows, and hardcoded safety red lines. macOS-only, experimental.

(captured site page body (agents/auto-company.md), not a verified repo-code finding)
auto-company is an experimental project that runs a simulated software company around the clock using 14 AI agents modeled on real-world figures (Bezos, Munger, DHH, Werner Vogels) and powered by Claude Code Agent Teams. A launchd-managed bash loop invokes Claude Code every cycle; agents read a shared consensus file plus company charter, pick 3-5 agents per cycle, and update shared state before the next cycle, with convergence rules to prevent endless discussion. State lives in markdown files, with six standard workflows (new product eval, feature dev, release, pricing, weekly review, opportunity discovery) and safety red lines baked into CLAUDE.md. It is an early experimental project (about a dozen commits), macOS-only via launchd, MIT-licensed, and requires a Claude Code subscription to run.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/auto-company.md)
