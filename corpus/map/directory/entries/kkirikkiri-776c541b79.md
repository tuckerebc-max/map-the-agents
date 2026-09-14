# kkirikkiri (`kkirikkiri`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: fivetaku
- License: MIT
- Language: JavaScript
- Interface: install=/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git && /plugin install kkirikkiri; enable Agent Teams flag in ~/.claude/settings.json
- Model providers: Anthropic Claude, OpenAI Codex CLI, Antigravity CLI
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [fivetaku/kkirikkiri](../../repos/fivetaku/kkirikkiri.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Natural language team builder plugin for Claude Code Agent Teams - describe what you want in one sentence and it assembles a purpose-driven AI team with validation loops (up to 3 rounds) and shared memory for cross-session persistence.

(captured site page body (agents/kkirikkiri.md), not a verified repo-code finding)
Assembling a useful set of Claude Code subagents by hand is slow and error-prone, so kkirikkiri automates team construction: the user describes the goal in one sentence, the plugin interviews briefly, proposes members with strictly scoped roles, and delegates execution to a team leader that plans and validates but never writes code directly. Well-performing members can be saved back to .claude/agents/ for reuse, and shared state (plans, progress) persists in .kkirikkiri/teams/ across sessions. Validation loops of up to three rounds swap underperforming members or rebuild the team. It targets Claude Code users with the experimental Agent Teams flag enabled who want repeatable multi-agent setups without hand-editing agent definitions.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/kkirikkiri.md)
