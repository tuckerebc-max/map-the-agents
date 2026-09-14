# opencode.nvim (`opencodenvim`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: sudo-tee
- License: Apache-2.0
- Language: Lua
- Interface: platforms=CLI; install=neovim
- Model providers: delegated to the opencode CLI (opencode auth login / config.json); the plugin adds a provider/model picker and per-prompt overrides like model=github-copilot/gpt-4.1
- Feature flags (directory-reported):
  - mcp_support: yes — mcp_picker keymap and /mcp command to manage MCP server connections (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes — built-in agents (Build, Plan) and custom agents; child session navigation (yes)
  - hooks: yes — on_file_edited, on_session_loaded, on_done_thinking, on_permission_requested (yes)
  - plan_mode: yes — built-in Plan agent for planning/analysis without file changes (yes)

Repository map entry: [sudo-tee/opencode.nvim](../../repos/sudo-tee/opencode.nvim.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Tight Neovim integration with the opencode AI agent, capturing rich editor context automatically; snapshot/diff/restore system for safe code changes; support for external/containerized/WSL servers with path mapping.

(captured site page body (agents/opencodenvim.md), not a verified repo-code finding)
Running opencode in a terminal while editing in Neovim splits attention and loses editor context the agent needs. This Lua plugin, a fork of goose.nvim, embeds the agent in Neovim: a chat panel holds persistent sessions per workspace, and every prompt automatically carries the current file, visual selection, LSP diagnostics, and cursor position, with @-file mentions for explicit references. A snapshot system underpins safety — diffs are reviewable, reverts are one keystroke, and restore points let users back out of unwanted agent edits. It also surfaces opencode's build/plan agents and custom agents, MCP server support, and permission handling, and supports connecting to external, containerized, or WSL opencode servers rather than only a local CLI. Installation is a standard lazy.nvim spec with the opencode CLI (v0.6.3+) required; Apache-2.0 licensed and under active development with 931 stars, though the README warns of breaking changes. Neovim users who want Cursor-grade context sharing with a terminal agent are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencodenvim.md)
