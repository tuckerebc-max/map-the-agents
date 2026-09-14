# fanbox (`fanbox`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: alchaincyf
- License: MIT
- Language: JavaScript
- Interface: install=binary
- Model providers: Claude Code, Codex, Hermes Agent, OpenClaw, Kimi Code, ZCode, opencode, pi, CodeBuddy, WorkBuddy, Qoder CLI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [alchaincyf/fanbox](../../repos/alchaincyf/fanbox.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=other, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Local-first, zero-config, zero-runtime-dependency desktop cockpit for coding agents that unifies the entire vibe-coding loop (find files, preview, light edit, command agent, see what changed) into a single window. No cloud, no accounts, no remote — data never leaves your machine. Live dashboard where file cards ripple/glow as the agent writes them, follow mode, session replay timeline, 5 independent reviewer subagents ...

(captured site page body (agents/fanbox.md), not a verified repo-code finding)
FanBox came out of indie developer Huashu's observation that agents now create projects faster than humans can track them — ten projects in an afternoon, and no way to see what changed where. The Electron app bundles a fuzzy-searching file browser with previews (Markdown, live HTML, code, images, video, PDF, archives), a real embedded terminal (node-pty + xterm.js), and a dashboard where agent file-writes light up cards in real time, with a cross-project inbox collecting changes across every running agent. Eleven built-in agent launchers cover Claude Code, Codex, Hermes Agent, OpenClaw, Kimi Code, opencode, pi, and other CLIs, extensible through ~/.fanbox/config.json. It targets individual developers juggling several concurrent agent sessions who need orientation and review rather than another agent.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fanbox.md)
