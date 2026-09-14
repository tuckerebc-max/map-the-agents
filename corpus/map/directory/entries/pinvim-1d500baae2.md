# pi.nvim (`pinvim`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: pablopunk
- License: MIT
- Language: Lua
- Interface: install=Via lazy.nvim, packer.nvim, or mini.deps (requires the pi CLI to be installed globally)
- Model providers: OpenRouter, OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [pablopunk/pi.nvim](../../repos/pablopunk/pi.nvim.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): The most minimal AI coding agent for Neovim, designed to embrace the simplicity of the CLI rather than imitating complex IDE features. Context-aware (sends buffer, cwd, selection, and optional diagnostics), unsaved-buffer aware (treats Neovim buffer content as the source of truth over stale disk files), and stays out of the user's way.

(captured site page body (agents/pinvim.md), not a verified repo-code finding)
pi.nvim exists because its author found most Neovim AI plugins recreate the IDE bloat that drove people to Neovim in the first place. The plugin instead wraps the globally installed pi CLI, passing provider, model, and thinking options while contributing just what the editor knows: the current buffer, working directory, selection, and optional diagnostics, with unsaved buffer content treated as authoritative over files on disk. Commands stay minimal — ask, ask-with-selection, cancel, log — with no default keymaps and async execution that never blocks editing. Skills and extensions can be toggled per invocation by mapping to pi's own flags rather than adding a parallel feature set. Distributed under MIT with tests and CI, it serves Neovim users who want pi's terminal-native agent loop one keypress away without an IDE-style sidebar.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pinvim.md)
