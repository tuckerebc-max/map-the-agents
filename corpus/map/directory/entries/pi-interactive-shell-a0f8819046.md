# pi-interactive-shell (`pi-interactive-shell`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: nicobailon
- License: unknown
- Language: TypeScript
- Interface: platforms=Autonomous, CLI; install=npm
- Model providers: Pi, Codex, Claude, Cursor, Aider
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [nicobailon/pi-interactive-shell](../../repos/nicobailon/pi-interactive-shell.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Full PTY emulation without tmux; observable TUI overlay where the user can take over control anytime; token-efficient; four modes (interactive, hands-free, dispatch, monitor) with event-driven triggers; structured spawn for multiple coding agents; headless background dispatch for parallel work

(captured site page body (agents/pi-interactive-shell.md), not a verified repo-code finding)
pi-interactive-shell solves a specific failure mode in coding agents: their shell tools time out on anything interactive, so vim, REPLs, SSH sessions, and long-running dev servers stay out of reach. The extension runs a full PTY stack — zigpty binaries plus headless terminal emulation — so subprocesses believe they have a real terminal, while a TUI overlay shows the user exactly what the agent sees and allows typing to take over at any moment. Four modes fit different workflows: interactive for back-and-forth editors, hands-free for servers the agent polls, dispatch for fire-and-forget work that wakes the agent on completion, and monitor for event-driven triggers like regex matches or file changes. Structured spawn parameters can launch entire coding agents (pi, codex, claude, cursor) as subagents, optionally in isolated worktrees, with output transferable back to the parent session. Pi users who want the agent handling interactive workflows rather than just one-shot commands are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-interactive-shell.md)
