# HolyClaude (`holyclaude`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: CoderLuii
- License: MIT
- Language: Shell
- Interface: platforms=Autonomous, CLI, Web; install=docker
- Model providers: Anthropic, Google, OpenAI, OpenRouter, Ollama, BYOK
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [coderluii/holyclaude](../../repos/coderluii/holyclaude.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Containerized AI development workstation bundling Claude Code + 8 AI CLIs + headless browser (Chromium/Playwright) + 50+ dev tools, all pre-configured and ready via one \`docker compose up\` command.

(captured site page body (agents/holyclaude.md), not a verified repo-code finding)
HolyClaude packages a full AI development environment into a single docker compose command. The container runs the genuine Claude Code CLI behind a browser-based web UI, alongside eight other AI CLIs, a headless Chromium with Playwright for browser tasks, and roughly fifty preconfigured development tools, so an agent can edit code, run tests, and drive a browser without host setup. The project's value is in the operational details it has already solved: correct shared-memory sizing for Chromium, UID/GID mapping for volume permissions, SQLite locking on NAS mounts, and supervision via s6-overlay, plus Apprise notifications when agents finish. It uses the user's own Anthropic subscription or API keys directly rather than proxying them, ships multi-arch images with a slim variant, and targets self-hosting enthusiasts running on macOS, Linux, WSL2, and NAS hardware.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/holyclaude.md)
