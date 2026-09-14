# pi-reflect (`pi-reflect`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: jo-inc
- License: MIT
- Language: TypeScript (Node.js)
- Interface: install=pi install git:github.com/jo-inc/pi-reflect (also on npm as @jo-inc/pi-reflect)
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [jo-inc/pi-reflect](../../repos/jo-inc/pi-reflect.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Iterative self-improvement for pi coding agents. Define a target behavior/personality and reflect iterates toward it by reading recent conversations and reference material, comparing actual behavior against the target, and making surgical edits to behavioral markdown files (AGENTS.md, MEMORY.md, SOUL.md). Over time corrections get absorbed as rules, memory accumulates durable facts, personality sharpens. Safety: backups, rejecting suspicious deletions, git auto-commit. Impact ...

(captured site page body (agents/pi-reflect.md), not a verified repo-code finding)
pi-reflect exists because behavioral rules for coding agents decay: instructions get ignored, the same mistakes recur, and nobody revisits the behavioral files that were supposed to prevent them. The extension runs a reflection cycle against a target file — collecting recent transcripts and reference material, sending them to a Sonnet-class model, and applying surgical edits that close the gap between observed and intended behavior — with backups, rejection of suspicious deletions, and git auto-commit making every change reversible. Metrics track whether the process works: correction-rate trends show whether the agent improves, and a rule-recidivism flag surfaces rules that keep being edited without effect. Runs can be scheduled via cron or launchd in headless mode, turning reflection into unattended maintenance. Developers running pi on long-lived projects use it to keep behavioral files honest instead of accreting stale instructions.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-reflect.md)
