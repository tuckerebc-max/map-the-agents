# claude-code-viewer (`claude-code-viewer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: d-kimuson
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE, Web; install=npm
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [d-kimuson/claude-code-viewer](../../repos/d-kimuson/claude-code-viewer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Full-featured web-based Claude Code client for managing projects — start conversations, resume sessions, monitor tasks in real-time, browse history via modern web UI. Zero data loss via Zod schema validation; MCP Server Viewer; built-in Git operations; session flow analysis; PWA with mobile support; built-in terminal and browser preview; multi-language (EN/JA/ZH).

(captured site page body (agents/claude-code-viewer.md), not a verified repo-code finding)
Claude Code records every session as JSONL files that are painful to read after the fact, and resuming old work means returning to the terminal. ccv runs a local Node server that renders those logs as a searchable web UI and, in full mode, drives Claude Code through the Agent SDK for chat, approvals, uploads, and git operations from the browser. After Anthropic's April 2026 ToS change restricted Agent SDK use on subscription accounts, chat features became opt-in: API-key users get everything, subscription users degrade to log viewing plus a copy-CLI-command flow. Developers reviewing long agent histories, working from mobile, or wiring sessions into automation (an --api-only mode exists for n8n) are the core users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-code-viewer.md)
