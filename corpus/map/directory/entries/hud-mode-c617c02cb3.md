# HUD (`hud-mode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: adrida
- License: MIT
- Language: JavaScript
- Interface: platforms=CLI; install=npm install -g adrida/hud-mode && hud install (Node \>= 18)
- Model providers: delegates to the connected agents (Claude Code, Codex, OpenCode)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [adrida/hud-mode](../../repos/adrida/hud-mode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A compact heads-up display that collapses a coding agent session into a live instrument deck — status flag, model, messages, elapsed time, tokens, cost, context size, subagents — plus an activity line showing READ/EDIT/EXEC, driving each CLI headless through its JSON event stream with zero dependencies and no forks or patches.

(captured site page body (agents/hud-mode.md), not a verified repo-code finding)
HUD is a terminal front-end for coding agents built by adrida at tracer: rather than a scrolling wall of tool-call output, it renders the session as gauges — status, model, message count, elapsed time, tokens, cost, context size, subagents — with an activity line showing what the agent is currently doing. The prompt bar is always writable so you can queue a message mid-turn that fires when the agent finishes, escape interrupts without killing the session, and the completed answer renders as markdown with clickable OSC 8 hyperlinks. It drives Claude Code, Codex, and OpenCode headless via their JSON event streams, and a lossless /hud toggle switches back to each engine's full native TUI mid-session through its own resume mechanism. It targets developers who run agent sessions constantly and want telemetry over transcript noise.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/hud-mode.md)
