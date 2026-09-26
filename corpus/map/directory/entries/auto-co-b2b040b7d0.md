# auto-co (`auto-co`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: NikitaDmitrieff
- License: MIT
- Language: Bash
- Interface: platforms=Autonomous, Web; install=npx create-auto-co my-company then cd my-company then make start (or git clone + make start)
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [nikitadmitrieff/auto-co-meta](../../repos/nikitadmitrieff/auto-co-meta.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Run an autonomous AI company from a ~50 line bash loop that calls Claude Code every 2 minutes. 14 expert-modeled agents (Jeff Bezos as CEO, Werner Vogels as CTO, Charlie Munger as Critic, etc.) debate, decide, build, and deploy software 24/7. No database, server, or framework — just files, git, and a loop. State carried via a 'relay baton' markdown ...

(captured site page body (agents/auto-co.md), not a verified repo-code finding)
auto-co runs an autonomous AI company from the terminal using roughly 50 lines of bash plus markdown state files, with Claude Code as the only real dependency. The auto-loop.sh script (about 3,000 lines with monitoring) reads shared state from memories/consensus.md, builds a prompt, calls claude -p, and updates consensus for the next cycle, with 3-5 of 14 expert-persona agents (Bezos, Vogels, Munger, DHH, Seth Godin) participating per cycle. Safety limits bar deletions, database resets, force pushes, credential leaks, and spending without human approval, with Telegram escalations roughly every 20-30 cycles. State lives in markdown files and JSONL logs rather than a database, and templates cover SaaS, docs-site, and API-backend projects. It is MIT-licensed, free software whose operating cost is Claude API usage, and suits tinkerers running always-on product experiments.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/auto-co.md)
