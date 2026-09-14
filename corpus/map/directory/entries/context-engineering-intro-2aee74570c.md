# context-engineering-intro (`context-engineering-intro`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: coleam00
- License: MIT
- Language: Python (examples)
- Interface: install=binary (git clone)
- Model providers: Anthropic (via Claude Code); strategy applies to any AI coding assistant
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (uses Claude Code custom slash commands, not a plugin) (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (has a PRP workflow with planning steps, not a formal plan mode) (no)

Repository map entry: [coleam00/context-engineering-intro](../../repos/coleam00/context-engineering-intro.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A comprehensive template for Context Engineering — a methodology that provides AI coding assistants with structured context (rules, examples, documentation, validation) via a PRP (Product Requirements Prompt) workflow, claiming to be 10x better than prompt engineering and 100x better than vibe coding.

(captured site page body (agents/context-engineering-intro.md), not a verified repo-code finding)
Agents fail most often not from weak models but from missing context, and prompt tweaks do not fix structural gaps. This repository packages a context-engineering workflow as a cloneable template: a developer writes a feature request in INITIAL.md, runs a /generate-prp command that researches the codebase and assembles a PRP (Product Requirements Prompt) with relevant documentation and validation criteria, then runs /execute-prp to implement it through validation gates that iterate until tests pass. Global rules templates in CLAUDE.md, feature-request formats, and example code patterns round out the kit, and a multi-agent variant exists for larger work. The templates target Claude Code but the method ports to other assistants, and adoption means copying the templates into a project rather than installing a tool. It is used by teams institutionalizing disciplined agent workflows.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/context-engineering-intro.md)
