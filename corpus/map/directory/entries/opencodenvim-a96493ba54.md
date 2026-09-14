# opencode.nvim (`opencodenvim`)

[Back to directory index](../index.md)

Directory membership: backing-only.

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

(backing feed `description`, not a verified repo-code finding)
Running opencode in a terminal while editing in Neovim splits attention and loses editor context the agent needs. This Lua plugin, a fork of goose.nvim, embeds the agent in Neovim: a chat panel holds
Sources: [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
