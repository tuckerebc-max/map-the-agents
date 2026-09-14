# pairup.nvim (`pairupnvim`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Piotr1215
- License: MIT
- Language: Lua
- Interface: install=lazy.nvim: { 'Piotr1215/pairup.nvim', cmd = { 'Pairup' }, config = function() require('pairup').setup() end }
- Model providers: Anthropic (via Claude Code CLI)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: yes (yes)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [piotr1215/pairup.nvim](../../repos/piotr1215/pairup.nvim.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Inline AI pair programming Neovim plugin using cc: markers in code that Claude edits directly; supports plan markers (ccp:) with CURRENT/PROPOSED conflict review and a peripheral Claude mode running a second autonomous instance in a sibling git worktree.

(captured site page body (agents/pairupnvim.md), not a verified repo-code finding)
Chat-panel AI plugins force a copy-paste loop between conversation and buffer, and the file under edit never contains the instruction that motivated the change. pairup.nvim embeds the instructions in the code itself: developers write cc: markers (or apply gC{motion} operators), save, and the Claude Code CLI edits the file in place and removes the marker. Variants extend the pattern — cc!: extracts a durable rule into CLAUDE.md as it edits, ccp: wraps proposed changes in CURRENT/PROPOSED conflict markers so acceptance is a deliberate merge rather than an overwrite, and uu: surfaces Claude's clarifying questions inline. A 'peripheral Claude' mode runs a second autonomous instance in a sibling git worktree that implements spec-file changes in parallel, with statusline todo tracking and proposal diff views keeping state visible. Version 4.0 stripped overlays, sessions, and RPC in favor of this simpler inline model, with the legacy design on a branch. Neovim 0.11+ users with a Claude Code subscription who prefer editor-embedded, marker-driven AI editing are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pairupnvim.md)
