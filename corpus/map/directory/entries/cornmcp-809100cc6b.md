# CornMCP (`cornmcp`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: yuki-20
- License: MIT
- Language: TypeScript
- Interface: install=npx corn-install (recommended) or manual git clone + pnpm + Docker
- Model providers: Voyage AI, OpenAI-compatible embedding APIs
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [yuki-20/cornmcp](../../repos/yuki-20/cornmcp.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): MCP server + analytics dashboard giving AI coding agents surgical, token-saving access to codebases via 18 tools: semantic memory, AST-based code intelligence, quality gates, session tracking, analytics

(captured site page body (agents/cornmcp.md), not a verified repo-code finding)
Coding agents waste tokens re-reading code, re-deriving call graphs, and repeating lessons from prior sessions, and nothing checks the quality of what they produce before it lands. CornMCP runs locally as a three-service stack - an MCP server exposing 18 tools, a Hono REST API with a native TypeScript AST engine, and a Next.js analytics dashboard - giving agents surgical codebase access instead of repeated full-file reads. Semantic memory stores persist lessons across sessions, impact analysis traces the blast radius of a proposed change, and quality gates reject agent plans scoring below a threshold before execution proceeds. Session tracking and tool-usage analytics surface in the dashboard for tuning. Developers running Claude Code, Cursor, Codex, or Windsurf against large codebases attach it to cut token spend and enforce standards.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cornmcp.md)
