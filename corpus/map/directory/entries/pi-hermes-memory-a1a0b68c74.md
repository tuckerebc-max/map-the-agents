# pi-hermes-memory (`pi-hermes-memory`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: chandra447
- License: MIT
- Language: TypeScript
- Interface: install=pi install npm:pi-hermes-memory (or git:github.com/chandra447/pi-hermes-memory, or pi -e /path/to/src/index.ts for local testing)
- Model providers: OpenRouter, Pi (registered provider auth), configurable via llmModelOverride
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [chandra447/pi-hermes-memory](../../repos/chandra447/pi-hermes-memory.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Memory and learning extension for the Pi coding agent (ported from Hermes by Nous Research): persistent two-tier (global + per-project) memory, failure learning, correction detection, procedural skills saved as SKILL.md files, secret scanning to block API keys, and auto-consolidation. Hybrid Markdown + SQLite FTS5 storage.

(captured site page body (agents/pi-hermes-memory.md), not a verified repo-code finding)
pi-hermes-memory addresses the core complaint about coding agents — that each session starts ignorant of everything learned before. Ported from Nous Research's Hermes agent, it maintains a two-tier memory of global preferences and per-project knowledge as Markdown files, mirrors them into a SQLite FTS5 index, and makes entire past sessions searchable. The system learns from failures and corrections explicitly, categorizing memories by type (failure, correction, insight, preference, convention, tool-quirk), and it saves procedural skills as SKILL.md files with structured verification steps and duplicate detection, exposed through pi's resource-discovery hook. Background review runs every ten turns, session flush happens on compaction or shutdown, and consolidation triggers automatically when stores overflow. Secret scanning blocks API keys from ever entering memory files. Pi users who run long-lived projects adopt it to keep institutional knowledge — conventions, past failures, working procedures — alive across sessions.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-hermes-memory.md)
