# PATAPIM (`patapim`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: unknown
- License: Proprietary (main app); open-source TypeScript SDK (@patapim/sdk)
- Language: TypeScript (SDK)
- Interface: platforms=CLI, IDE, Web; install=patapim install; macOS: curl install-mac.sh | bash; Windows: PowerShell irm install.ps1 | iex
- Model providers: Claude, Codex, Antigravity, Gemini, or any custom CLI
- Feature flags (directory-reported):
  - mcp_support: yes (plugins can register MCP tools that automatically show up in Claude Code sessions) (yes)
  - plugin_support: yes (extensible plugin system with marketplace, local API, TypeScript SDK — @patapim/sdk is open-source) (yes)
  - claude_code_plugin: yes (enhancement layer for Claude Code) (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Terminal IDE enhancement for Claude Code with 9-terminal grid for running multiple CLI coding agents simultaneously; full computer control (drives mouse/keyboard) and embedded per-terminal Chrome browsers using existing AI subscription (zero extra API costs); 100% local Whisper voice dictation; zero-setup LAN remote control; organizes projects by folders rather than chats.

(captured site page body (agents/patapim.md), not a verified repo-code finding)
PATAPIM grew from a solo developer's setup into a terminal manager for people running multiple CLI coding agents, wrapping Claude Code, Codex, Antigravity, Gemini, or any custom CLI in a nine-terminal grid organized by project folder rather than chat history. Beyond window management it adds capabilities the underlying CLIs lack: a local Whisper dictation layer for voice input, an embedded Chrome instance per terminal that agents can see and drive, full mouse/keyboard computer control, and zero-configuration LAN remote access from a phone or second desktop. An isolated plugin system registers MCP tools that automatically appear in every Claude Code session, adds UI panels and scheduled tasks, and is extensible through a TypeScript SDK with a marketplace. Because it wraps the user's own subscriptions, there are no per-token charges beyond the app's own tiers. Its users are solo developers and small teams running several agent sessions at once.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/patapim.md)
