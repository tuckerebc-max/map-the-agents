# claude-code-plus (`claude-code-plus`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: touwaeriol
- License: MIT
- Language: Kotlin
- Interface: platforms=CLI, IDE; install=JetBrains Marketplace (search 'Claude Code Plus') or manual install via GitHub Releases zip
- Model providers: Anthropic, OpenAI, Google
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [touwaeriol/claude-code-plus](../../repos/touwaeriol/claude-code-plus.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Provides a rich GUI for Claude Code (and Codex/Gemini CLI) inside JetBrains IDEs with @-mention file context, tool call visualization, multi-session chat, permission dialogs, model switching, keyboard shortcuts, MCP support, and dark theme compatibility.

(captured site page body (agents/claude-code-plus.md), not a verified repo-code finding)
Running CLI coding agents in a raw terminal forfeits IDE navigation, diff review, and permission UX. Claude Code Plus embeds the agents as a JetBrains tool window and translates their activity into structured UI: chat with multi-session support, tool-call cards for reads/writes/edits with diffs, permission dialogs before writes, clickable file navigation, and interrupt handling. It bundles Claude and Codex agent SDKs and an MCP transport, and supports @-mentions to attach files as context. Developers who live in IntelliJ-family IDEs use it to keep agent work visible next to the editor; it is MIT-licensed and free, requiring the user's own Claude subscription or API key.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-code-plus.md)
