# herdrm (`herdrm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: missuo
- License: MIT
- Language: Swift
- Interface: platforms=CLI, Desktop; install=Homebrew (brew install owo-network/brew/herdrm) or manual download of .zip from Releases
- Model providers: none (attaches to herdr-hosted agents: Claude Code, Codex, Gemini, Grok, OpenCode)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [missuo/herdrm](../../repos/missuo/herdrm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native macOS console for herdr that aggregates all herdr-managed coding agents across local and remote (SSH) machines in one window with live PTY attachment, notifications, and Cmd-K search; auto-reconnects remote machines via SSH tunneling

(captured site page body (agents/herdrm.md), not a verified repo-code finding)
herdrm is a native macOS client for herdr, the background daemon that keeps coding-agent sessions alive. It presents one window listing every herdr-managed agent across the local machine and SSH-connected servers, with live status for spaces, agents, and terminals, and Cmd-K search across all devices. Attachment happens over the genuine PTY through a SwiftTerm-based terminal view, preserving the full TUI rendering of Claude Code, Codex, Gemini, Grok, and OpenCode sessions rather than reducing them to a chat-style transcript. Beyond observation it supports interaction: pasting files and images into agents, a two-pane file manager for local and SSH transfers, and system notifications when an agent finishes or blocks. The app is signed and notarized with Sparkle auto-updates, ships as a universal binary, and is explicitly early-stage software under active development.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/herdrm.md)
