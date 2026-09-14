# pi-gui (`pi-gui`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: minghinmatthewlam
- License: MIT
- Language: TypeScript
- Interface: install=binary (dmg/AppImage), brew
- Model providers: multiple (via pi runtime; OAuth or API key)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [minghinmatthewlam/pi-gui](../../repos/minghinmatthewlam/pi-gui.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native desktop (Electron) shell around the pi coding agent runtime with a Codex-style threaded timeline UI, git worktrees per thread, multi-agent orchestration (supervisor/worker), integrated PTY terminal, and inline diff viewer. Uses pi's JSONL session files as the source of truth via a thin pi-sdk-driver adapter.

(captured site page body (agents/pi-gui.md), not a verified repo-code finding)
pi-gui exists because pi's terminal-first interface limits visibility once developers run several threads, supervise workers, or review diffs across parallel work. The Electron app wraps the pi runtime without forking it: a Codex-style timeline shows threaded sessions, each thread can run in an isolated git worktree, and an orchestrator thread spawns and supervises worker threads for multi-agent runs. An integrated PTY terminal, inline diff viewer, session archive, and notification system cover the day-to-day loop, while pi's JSONL session files stay the source of truth so CLI and GUI sessions interoperate. Public beta builds ship signed and notarized for Apple Silicon Macs and Linux, with a Homebrew cask and source build for contributors. Its users are pi users who want desktop ergonomics and structured orchestration instead of a raw terminal.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-gui.md)
