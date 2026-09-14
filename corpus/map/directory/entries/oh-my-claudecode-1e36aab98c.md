# oh-my-claudecode (`oh-my-claudecode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Yeachan-Heo
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: Claude, Codex, Gemini, Antigravity, Grok, Cursor
- Feature flags (directory-reported):
  - mcp_support: partial (.mcp.json exists; v4.4.0 removed Codex/Gemini MCP servers in favor of CLI-first tmux workers) (reported)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (it is itself a Claude Code plugin) (yes)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [yeachan-heo/oh-my-claudecode](../../repos/yeachan-heo/oh-my-claudecode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Teams-first multi-agent orchestration for Claude Code with zero learning curve, offering multiple orchestration modes (Team, Autopilot, Ralph, Ultrawork, UltraQA, Pipeline), smart model routing for cost savings, and cross-provider orchestration via tmux CLI workers.

(captured site page body (agents/oh-my-claudecode.md), not a verified repo-code finding)
oh-my-claudecode extends Claude Code with a teams-first orchestration layer: a staged pipeline (plan, PRD, execute, verify, fix) using Claude Code's native agent teams, with autopilot and persistent verify-fix loops for autonomous runs. As a plugin plus companion CLI it also spawns tmux worker panes running Codex, Gemini, Antigravity, Grok, or Cursor CLIs, letting one model review another's output. Smart model routing downgrades cheap tasks to smaller models for token savings, and a skill-learning system extracts reusable procedures into project files. Natural-language shortcuts and zero-config defaults target users who do not want to study Claude Code's internals. Installation is via the Claude Code plugin marketplace or npm, with tmux required for team features.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/oh-my-claudecode.md)
