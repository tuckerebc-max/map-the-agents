# shotgun (`shotgun`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: shotgun-sh
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: OpenAI, Anthropic, Google Gemini
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [shotgun-sh/shotgun](../../repos/shotgun-sh/shotgun.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Spec-driven development CLI/TUI that reads your entire codebase (tree-sitter indexing), plans features upfront, and splits them into staged PRs with file-by-file instructions for AI coding agents (Cursor, Claude Code, Codex). Multi-phase structured workflow (Research, Specify, Plan, Tasks, Export) with dedicated sub-agents per phase managed by a Router. Starts with research to discover existing solutions/patterns before writing specs, preventing duplicate work. ...

(captured site page body (agents/shotgun.md), not a verified repo-code finding)
Large features derail coding agents because context arrives piecemeal; Shotgun front-loads the work by reading the entire repository, researching before specifying, and producing a full plan split into staged pull requests with file-by-file instructions. Internally a Router dispatches specialized sub-agents through Research, Specify, Plan, Tasks, and Export phases, and the user controls exactly two execution modes — planning with checkpoints, or drafting end-to-end. The index lives in ~/.shotgun-sh, telemetry is minimal and anonymous, and BYOK covers OpenAI, Anthropic, and Gemini or prepaid Shotgun credits. It installs via uvx as a Python TUI/CLI, integrates Context7 experimentally for current library docs, and targets teams handing substantial features to Cursor, Codex, or Claude Code who need the plan to survive the handoff.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/shotgun.md)
