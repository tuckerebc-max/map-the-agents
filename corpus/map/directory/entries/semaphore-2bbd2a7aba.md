# semaphore (`semaphore`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: lucianodiisouza
- License: MIT
- Language: Rust
- Interface: install=Download pre-built binaries or build from source; semctl install --all for hooks
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [lucianodiisouza/semaphore](../../repos/lucianodiisouza/semaphore.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Floating traffic-light widget for AI coding agents. Always-on-top indicator shows green (idle), yellow (thinking/running tools), or red (writing/editing files) without switching windows. Cross-platform with Stream Deck integration, stealth mode (hidden from screen capture), multi-session state machine with priority-based color selection, themes, sounds, and i18n.

(captured site page body (agents/semaphore.md), not a verified repo-code finding)
The problem is mundane but constant: an agent has been running for ten minutes in a background window and the developer has no idea whether it is waiting for permission or editing files. Semaphore puts a traffic light on top of every workspace, colored by hooks that Cursor, Claude Code, Codex CLI, and Gemini CLI emit into a per-session state machine. The Rust core and Tauri widget are MIT-licensed, with theming, sounds, idle timeout, and a Node.js Stream Deck plugin as conveniences around the IPC protocol. It is cross-platform with signed builds from GitHub Releases and a semctl doctor command to verify hook wiring. The audience is solo developers and pairing sessions where a glanceable indicator beats alt-tabbing, and the project is a modestly maintained hobby-scale codebase with tagged releases.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/semaphore.md)
