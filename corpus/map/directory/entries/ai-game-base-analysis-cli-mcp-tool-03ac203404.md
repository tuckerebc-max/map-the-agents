# ai_game_base_analysis_cli_mcp_tool (`ai-game-base-analysis-cli-mcp-tool`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: pirua-game
- License: Apache-2.0
- Language: Python, C#
- Interface: install=One-click: install.bat (Windows) / install.sh (macOS/Linux); Manual: pip install -e . in gdep-cli/; MCP: npm install -g gdep-mcp
- Model providers: Ollama (local LLM), configurable via gdep config
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [pirua-game/ai_game_base_analysis_cli_mcp_tool](../../repos/pirua-game/ai_game_base_analysis_cli_mcp_tool.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Game codebases defeat ordinary static analysis because logic is split between scripts and engine assets, so the tool pairs a .NET parser (gdep.dll) with a Python CLI (gdep) and an npm-distributed MCP
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
