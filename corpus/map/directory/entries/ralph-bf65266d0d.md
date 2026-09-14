# ralph (`ralph`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: snarktank
- License: MIT
- Language: Bash
- Interface: platforms=Autonomous; install=git clone (copy files), npm (Claude Code marketplace plugin)
- Model providers: Amp (ampcode.com), Claude Code (Anthropic)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (.claude-plugin manifest; Claude Code marketplace plugin) (yes)
  - claude_code_plugin: yes (/plugin marketplace add snarktank/ralph; /plugin install ralph-skills@ralph-marketplace) (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [snarktank/ralph](../../repos/snarktank/ralph.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An autonomous AI agent loop that repeatedly spawns a fresh, clean-context instance of Amp or Claude Code until every item in a prd.json is passing, carrying memory only through git history, an append-only progress.txt, and prd.json status file -- the 'fresh context + persistent memory' Ralph pattern.

(captured site page body (agents/ralph.md), not a verified repo-code finding)
Ralph operationalizes a simple claim about AI coding: an agent with fresh context every iteration outperforms one long session that degrades under context rot. The loop reads prd.json, spawns a clean instance of Amp or Claude Code for each iteration, and that instance picks the highest-priority story marked failing, implements it, runs typecheck and tests, and commits only when they pass — then marks the story done and appends what it learned to progress.txt and an evolving AGENTS.md. No state lives in the model's window between iterations; git history and flat files carry all memory, which is why the README insists stories be small enough to fit one context window. A completion phrase or iteration cap ends the run, and typecheck/test gates prevent broken code from compounding across iterations. Teams use it for long unattended pushes through a feature backlog, accepting the project's own warning to run it in isolated environments.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ralph.md)
