# devctx (`devctx`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: IAmUnbounded
- License: MIT
- Language: TypeScript/JavaScript (Node.js)
- Interface: platforms=IDE; install=npm install -g devctx
- Model providers: OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [iamunbounded/devctx](../../repos/iamunbounded/devctx.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): CLI tool that captures and restores AI coding context (task, goal, approaches, decisions, state) scoped to repo and branch, enabling persistence across sessions, editors, and team members. Provides an MCP server for Claude Code & Windsurf with tools devctx_save, devctx_resume, devctx_log.

(captured site page body (agents/devctx.md), not a verified repo-code finding)
Every AI coding session starts from zero context, and the problem compounds when a teammate or a different editor takes over. devctx treats the prompt itself as the interface: a .devctx/ directory in the repo stores task, goal, approaches tried, decisions, and stopping state, and \`devctx resume\` emits a formatted prompt that any assistant can ingest. Core commands run locally with no API key; optional AI commands (summarize, suggest, compress) use an OpenAI-compatible endpoint. An MCP server exposes the same context natively to Claude Code and Windsurf, and a VS Code extension auto-resumes context on project open. Teams commit the folder to git so intent history syncs alongside code.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/devctx.md)
