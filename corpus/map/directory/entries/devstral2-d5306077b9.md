# devstral2 (`devstral2`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Mistral AI
- License: Apache-2.0
- Language: Python
- Interface: install=curl -LsSf https://mistral.ai/vibe/install.sh | bash; or uv tool install mistral-vibe; or pip install mistral-vibe
- Model providers: Mistral AI
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Mistral Vibe CLI is a native terminal-based coding agent with MCP server support (HTTP, streamable-HTTP, stdio), a Skills plugin system with custom slash commands, subagents via task delegation with built-in explore agent, lifecycle hooks (pre_tool, post_tool, post_agent), and plan mode. Devstral 2 model achieves 72.2% on SWE-bench Verified with only 123B parameters, 256K context window, and up to 7x more ...

(captured site page body (agents/devstral2.md), not a verified repo-code finding)
Mistral built Vibe CLI as the reference client for Devstral 2 and as an open counterweight to proprietary terminal agents: it scans the project and git state for context, exposes @-file and !-shell references, and orchestrates multi-file edits with architecture-level reasoning. The extension points mirror the Claude Code model — MCP servers over stdio or HTTP, an Agent Skills spec directory tree that doubles as slash commands, TOML-declared hooks, and custom subagents declared in config with a read-only plan agent built in. It runs against the Mistral API or any compatible endpoint and integrates into IDEs through ACP. Teams already standardized on Devstral use it to keep both model and harness under their own control.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/devstral2.md)
