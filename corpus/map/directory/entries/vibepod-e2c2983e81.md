# VibePod (`vibepod`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: VibePod
- License: MIT
- Language: Python
- Interface: platforms=CLI, IDE; install=pip install vibepod
- Model providers: Claude, Gemini, Codex, Devstral, Copilot, Auggie, Pi, Qwen, OpenCode
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [vibepod/vibepod-cli](../../repos/vibepod/vibepod-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unified CLI for running AI coding agents in isolated Docker/Podman containers with zero config; collects local metrics (HTTP traffic, token usage) and provides an analytics dashboard to compare agents side-by-side; privacy-first, all data stays local

(captured site page body (agents/vibepod.md), not a verified repo-code finding)
VibePod exists because evaluating or running several coding agents means installing a dozen CLIs, each with its own dependencies and permission flags, and no way to compare their behavior afterward. One Python CLI launches any supported agent — Claude, Gemini, Codex, Copilot, Auggie, Qwen, OpenCode, and others — inside a Docker or Podman container built from maintained images, with optional per-project overlay fragments adding dependencies without forking images. An --ikwid flag auto-appends each agent's auto-approval flag for hands-off runs, and while agents work, a local dashboard records HTTP traffic, token usage, and per-agent metrics for side-by-side comparison. Developers choosing between agents, or isolating them from their host machine, use it; it is MIT-licensed, installable via pip/Homebrew/conda, and under steady development with images published to Docker Hub.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibepod.md)
