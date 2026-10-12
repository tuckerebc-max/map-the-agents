# Free Repo Agent (`free-repo-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: SUMITKUMARSINGH
- License: MIT
- Language: unknown
- Interface: platforms=IDE; install=Install from Open VSX
- Model providers: OpenAI, Anthropic, DeepSeek
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [sumitsingh4411/repo-agent](../../repos/sumitsingh4411/repo-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Free repo-aware autonomous coding agent (DeepSeek) that edits files and runs commands

(captured site page body (agents/free-repo-agent.md), not a verified repo-code finding)
The extension targets developers who want Copilot-style autonomous editing without a subscription, using DeepSeek V4 Flash (default, 1M context) or V4 Pro models behind a user-supplied API key, with any OpenAI-compatible provider configurable as a fallback. It indexes the repository and injects relevant files into answers, applies edits across files with Keep/Undo inline controls, and runs shell commands behind an approval gate. After editing, it runs typecheck or build and repairs errors before declaring a task done, and it keeps project context in a memory.md file plus a generated codebase brief. Vision input routes through a free Gemini endpoint by default, and one-click MCP plugins add GitHub, web search, Postgres, Playwright, and filesystem tools.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/free-repo-agent.md)
