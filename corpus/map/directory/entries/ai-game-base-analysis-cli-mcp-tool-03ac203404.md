# ai_game_base_analysis_cli_mcp_tool (`ai-game-base-analysis-cli-mcp-tool`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

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

Highlight (site page `what_makes_it_special`): Game codebase analysis tool analyzing Unity/UE5/Axmol/.NET/C++ projects in \<0.5s; provides dependency graphs, impact analysis, circular dep detection, dead code detection, call flow tracing (C++ to Blueprint), lint (19 anti-pattern rules), architecture advice, wiki cache for AI agents

(captured site page body (agents/ai-game-base-analysis-cli-mcp-tool.md), not a verified repo-code finding)
Game codebases defeat ordinary static analysis because logic is split between scripts and engine assets, so the tool pairs a .NET parser (gdep.dll) with a Python CLI (gdep) and an npm-distributed MCP server (gdep-mcp). It builds dependency graphs, impact analysis, circular-dependency and dead-code detection, and call-flow tracing, then exposes them as MCP tools such as analyze_impact_and_risk and trace_gameplay_flow for Claude Desktop, Cursor, or any MCP client. A gdep init step writes a .gdep/AGENTS.md file so agents pick up project context automatically. Solo-dev team, 65 stars, Apache-2.0, distributed on PyPI and npm with multi-language READMEs.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/ai-game-base-analysis-cli-mcp-tool.md)
