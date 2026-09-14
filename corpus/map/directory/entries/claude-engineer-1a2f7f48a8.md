# Claude Engineer (`claude-engineer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Doriandarko
- License: MIT
- Language: Python
- Interface: platforms=CLI, Web; install=git clone, uv venv, uv run app.py (web) or uv run ce3.py (CLI)
- Model providers: Anthropic (Claude 3.5 Sonnet)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [doriandarko/claude-engineer](../../repos/doriandarko/claude-engineer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-improving architecture — Claude can autonomously identify capability gaps, design, and implement new tools during conversations, making the framework more powerful with continued use; available as both CLI and web interface.

(captured site page body (agents/claude-engineer.md), not a verified repo-code finding)
Claude Engineer was an early (2024) demonstration that an agent's toolset could be emergent rather than fixed: when a task exceeds the built-in tools (file operations, E2B code execution, web search), the model designs and implements a new tool during the conversation, and the runtime loads it without restart. Both a web UI and CLI expose the same agent, with image analysis and token-usage visualization. The approach trades reliability for extensibility, since self-written tools vary in quality. It attracted a large following (over 11k stars) as a reference design for self-improving agents, but the maintainer stopped committing in December 2024, leaving many pull requests unmerged.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-engineer.md)
