# Codemini-CLI (`codemini-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: havingautism
- License: MIT
- Language: JavaScript (Node.js)
- Interface: platforms=CLI, Web; install=npm install -g codemini-cli
- Model providers: OpenAI-compatible, Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [havingautism/codemini-cli](../../repos/havingautism/codemini-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Restrained coding + tasks CLI with both TUI and browser Web UI sharing the same runtime; minimizes unnecessary context usage via managed compaction, lazy-loaded skills, project-aware retrieval (Tree-sitter AST, dependency/knowledge graphs, CodeWiki), proportional risk-based approvals, local persistence, and Microsandbox isolation. All sessions, memory, and state remain local.

(captured site page body (agents/codemini-cli.md), not a verified repo-code finding)
Codemini-CLI is a terminal-first agent for coding and operational tasks, built around minimizing unnecessary context consumption: managed compaction, lazy-loaded skills, and project-aware retrieval through Tree-sitter AST parsing, dependency and knowledge graphs, and a generated CodeWiki keep prompts small. Its tool runtime includes plans, todos, subagents, background tasks, and parallel tool calls, with approvals proportional to the risk of each change and sandbox modes from read-only through workspace-write to full access, optionally backed by Microsandbox microVMs with Landlock/Seatbelt fallbacks. Claude-compatible hooks observe or gate lifecycle events, and MCP servers extend the tool surface without runtime changes. A TUI and a browser Web UI share the same session engine and local persistence, so a session started in the terminal continues in the browser.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codemini-cli.md)
