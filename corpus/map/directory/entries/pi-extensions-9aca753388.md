# pi-extensions (`pi-extensions`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ogulcancelik
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=pi install npm:@ogulcancelik/\<package-name\>
- Model providers: whatever the host pi session uses (pi is multi-provider)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [ogulcancelik/pi-extensions](../../repos/ogulcancelik/pi-extensions.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): A working collection of extensions for the pi terminal coding agent, ranging from core daily drivers to experimental utilities (e.g., pi-codex-subagents for session-scoped subagents, pi-goal for parallel worker agents, pi-model-thinking).

(captured site page body (agents/pi-extensions.md), not a verified repo-code finding)
pi-extensions grew out of one developer's daily use of pi, and the collection's organization reflects that: packages are ranked by how often the author actually uses them, from a minimal footer with context and subscription gauges to experimental utilities that may disappear. Functionally the packages fill gaps in pi's core — searching past sessions, context-aware Bash permissions with automated guardian review, session-scoped Codex-shaped subagents, Codex-style remote compaction via pi's compaction lifecycle, and Herdr worktree management. Each package installs individually through pi's package manager, so users pick only what they need rather than adopting a bundle. The MIT-licensed repo is moderately active with 400+ stars, and its audience is pi users who want the ecosystem's extensions from one maintained source rather than hunting across npm.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-extensions.md)
