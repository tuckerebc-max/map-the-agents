# ricochet (`ricochet`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Grik-ai
- License: Apache-2.0
- Language: Go, TypeScript
- Interface: platforms=Autonomous, IDE; install=VS Code Marketplace: ext install grik.ricochet; or installer script curl -fsSL https://grik.io/ricochet/install | sh
- Model providers: OpenRouter, OpenAI, Anthropic, Mistral, DeepSeek, Z.AI, xAI, MiniMax
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [grik-ai/ricochet](../../repos/grik-ai/ricochet.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first AI coding agent with a native Go core for VS Code-compatible editors and terminal; review-before-apply edits, checkpoints (workspace snapshots), and an optional Ether/Live Mode for remote control via Telegram/Discord.

(captured site page body (agents/ricochet.md), not a verified repo-code finding)
Ricochet exists for developers who want one agent across VS Code-compatible editors and the terminal without giving up control over what gets written to disk. The Go core runs the inspect-plan-edit-verify loop, routes to whichever provider the user configures — hosted Grik models or BYOK keys for OpenAI, Anthropic, OpenRouter, Mistral, DeepSeek, and others — while the TypeScript layer supplies the VS Code extension and webview UI. A task timeline records every read, search, command, edit, and approval, and checkpoints allow rolling the workspace back to any prior state. MCP servers and project instruction skills extend the tool surface, and remote steering over Telegram or Discord targets people who kick off long tasks and monitor from elsewhere. The project is young, with a small commit history and no GitHub releases yet.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ricochet.md)
