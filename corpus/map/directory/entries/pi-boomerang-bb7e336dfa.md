# pi-boomerang (`pi-boomerang`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: nicobailon
- License: unknown
- Language: TypeScript
- Interface: platforms=Autonomous; install=pi install npm:pi-boomerang
- Model providers: whatever the host pi session uses (pi is multi-provider)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [nicobailon/pi-boomerang](../../repos/nicobailon/pi-boomerang.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Token-efficient autonomous task execution with automatic context summarization for pi coding agent. Executes tasks autonomously, then replaces raw turn history in future context with an expanded handoff summary (changed files, relevant reads, commands, failures, outcome) — saving tokens while preserving work. Supports chain execution, rethrow/loop execution, prompt templates, anchor mode, and an agent-callable tool.

(captured site page body (agents/pi-boomerang.md), not a verified repo-code finding)
pi-boomerang exists because autonomous agent tasks generate enormous turn histories that crowd out useful context in every later turn. The extension runs a task from start to finish without questions, then a heuristic summarizer condenses the recorded tool calls and results into a handoff block — outcome, changed files, relevant reads, commands, validation results, failures — which replaces the raw history for all subsequent turns while the full session tree remains navigable. Templates with frontmatter configure model, skills, and thinking level per task, chaining turns multi-stage flows into pipelines, and rethrow or loop modes re-run failed tasks with accumulated context. An optional agent-callable tool lets the model boomerang its own subtasks, and file state is never touched, only context. Pi users running long autonomous tasks use it to keep later turns cheap without losing the work record.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-boomerang.md)
