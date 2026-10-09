# dinotty (`dinotty`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: xichan96
- License: MIT
- Language: Rust, TypeScript, Vue
- Interface: platforms=CLI, IDE, Web; install=Download platform installer from GitHub Releases (.dmg macOS / .deb Linux / .exe Windows); or build from source with pnpm + cargo
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [xichan96/dinotty](../../repos/xichan96/dinotty.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Server-side VTE terminal server for AI coding agents with multi-device sync (phone/iPad/desktop, one session), lightweight pure-text transmission (~1-10 KB/s), pane-based UI where terminals/plugins/files/SSH/git are all draggable splittable panes, built-in SSH/SFTP, file browser, and web preview.

(captured site page body (agents/dinotty.md), not a verified repo-code finding)
Terminal coding agents bind you to the machine and window where the session started, and losing SSH connectivity mid-task means losing context. dinotty runs the terminal server-side and streams a compact text protocol (~1-10 KB/s) to any device, so a session started on a desktop continues on a phone or tablet and restores after disconnects. Everything is a pane — terminals, file browser, SSH sessions, web previews, and hot-reloadable JS plugins — arranged by drag-and-drop across phone, tablet, and desktop layouts. Split-broadcast typing, command bookmarks, and an SFTP-backed file browser round out a desktop client comparable to a full terminal emulator. Its users are developers running agents on servers who want to supervise them from any device.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/dinotty.md)
