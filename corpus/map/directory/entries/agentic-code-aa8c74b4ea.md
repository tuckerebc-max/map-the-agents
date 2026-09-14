# agentic-code (`agentic-code`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: shinpr
- License: MIT
- Language: TypeScript / JavaScript (Node.js)
- Interface: platforms=CLI; install=npx agentic-code my-project
- Model providers: model-agnostic (works with any LLM via AGENTS.md-compatible tools: Cursor, Codex CLI, Gemini CLI)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [shinpr/agentic-code](../../repos/shinpr/agentic-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Standardizes AI coding workflows via the open AGENTS.md standard with zero configuration, enforcing a test-first approach and progressive skill loading across multiple AI coding tools (Cursor, Codex, Gemini CLI). Provides pre-built workflows and quality gates (requirements analysis, architecture planning, test-first generation, implementation). Supports sub-agents-mcp for running isolated context reviews in Cursor.

(captured site page body (agents/agentic-code.md), not a verified repo-code finding)
Teams using several AI coding tools end up maintaining separate instruction files and workflows per tool, so agentic-code standardizes on the open AGENTS.md format and generates the scaffolding in one npx command with zero configuration. Its workflows impose a test-first discipline with quality gates between phases — requirements analysis, architecture planning, test-first generation, implementation — and skills install into Cursor or Codex CLI from the shared .agents/skills directory. For deeper review isolation it supports sub-agents-mcp, running reviews in a separate context window. It is MIT-licensed, model-agnostic, and built for teams that run Cursor, Codex, and Gemini CLI against the same repository without wanting per-tool workflow drift.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentic-code.md)
