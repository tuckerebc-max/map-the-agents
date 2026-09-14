# Kimi CLI (`kimi-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: unknown
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI, IDE; install=pip install kimi-cli (PyPI package)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Terminal-based AI coding agent and shell by Moonshot AI that can read/edit code, execute shell commands, search/fetch web pages, and autonomously plan actions. Supports MCP (stdio + HTTP with OAuth), zsh and VS Code integrations. Note: evolving into Kimi Code CLI; this project will be gradually wound down.

(captured site page body (agents/kimi-cli.md), not a verified repo-code finding)
Moonshot AI built Kimi CLI as a terminal agent that reads and edits code, runs commands, and fetches web pages while planning and adjusting its actions mid-task. It integrates with editors through the Agent Client Protocol (kimi acp for Zed and JetBrains IDEs), a VS Code extension, and a zsh plugin, and its kimi mcp subcommands add stdio or HTTP MCP servers with header or OAuth authentication. The project is Apache-2.0 and installable via pip or uv, but the README states it is being wound down in favor of Kimi Code CLI, the team's next-generation agent; existing configurations and sessions migrate automatically. Developers already using it can continue, while new users are pointed at the successor.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/kimi-cli.md)
