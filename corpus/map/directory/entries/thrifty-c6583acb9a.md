# Thrifty (`thrifty`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=/plugin marketplace add 2389-research/thrifty, then /plugin install thrifty@thrifty
- Model providers: Claude (Sonnet plans, Haiku executes, Sonnet verifies)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Claude Code plugin) (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (cheap model executes sprints, mid model verifies) (yes)
  - hooks: yes (gate tests/checklist) (yes)
  - plan_mode: yes (strong model writes CONTRACT.md and sprint briefs) (yes)

Repository map entry: [2389-research/thrifty](../../repos/2389-research/thrifty.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Tiered-delegation task execution for Claude Code: a strong model (Sonnet) plans by writing a contract and sprint briefs with acceptance criteria, a cheap model (Haiku) executes each sprint and runs the gate (tests/checklist) self-fixing until green, and a mid model (Sonnet) does scoped verification only when the gate fails. Claims ~64% cost reduction vs Opus at equal gate quality.

(captured site page body (agents/thrifty.md), not a verified repo-code finding)
Thrifty is a Claude Code plugin that applies tiered delegation to task execution, and the agent loop belongs to Claude Code throughout. A strong model (Sonnet) plans by writing a CONTRACT.md and per-sprint briefs with explicit acceptance criteria, then hands off. A cheap model (Haiku) executes each sprint and runs the gate — tests and a checklist — self-fixing until the gate goes green. Only when a gate fails does a mid model (Sonnet) step in for scoped verification, so the expensive tiers are used sparingly. The reported payoff is roughly 64% cost reduction versus running Opus end-to-end at equal gate quality. The audience is Claude Code users who want to cut spend without giving up the gate discipline that makes agentic work trustworthy.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/thrifty.md)
