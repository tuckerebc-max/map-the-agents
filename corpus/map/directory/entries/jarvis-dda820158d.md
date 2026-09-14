# jarvis (`jarvis`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: danilofalcao
- License: MIT
- Language: Python
- Interface: install=source
- Model providers: DeepSeek, Codestral, Google, Grok, Anthropic, OpenAI, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [danilofalcao/jarvis](../../repos/danilofalcao/jarvis.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-model AI coding assistant with integrated cross-platform terminal (xterm.js), file attachments (PDF/Word/Excel/OCR), WebSocket real-time updates, workspace management, diff-based code modification previews, and context-aware chat

(captured site page body (agents/jarvis.md), not a verified repo-code finding)
jarvis is a DIY control panel for code work across models: a browser workspace shows files, diffs, and a real terminal side by side, so generating a change, reviewing its diff, and running it happen in one screen. Document attachments with OCR feed PDFs, spreadsheets, and screenshots into context, and WebSocket streaming keeps generation live. The backend is a single Flask app with Flask-SocketIO; the frontend is plain JS with CodeMirror and Tailwind. All provider keys are configured in .env, and the tool is BYOK end to end. Activity stopped around early 2025 — 140 commits, no releases — making it a snapshot of the 2025 local-coding-chat wave.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/jarvis.md)
