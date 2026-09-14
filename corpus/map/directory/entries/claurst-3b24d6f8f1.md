# Claurst (`claurst`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Kuberwastaken
- License: GPL-3.0
- Language: Rust
- Interface: install=npm
- Model providers: Anthropic, Google Gemini
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [kuberwastaken/claurst](../../repos/kuberwastaken/claurst.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Clean-room Rust reimplementation of Claude Code as a terminal coding agent (TUI pair programmer). Multi-provider routing with no telemetry/tracking. Agent Client Protocol (ACP) support for editor integration (Zed, Neovim, JetBrains). Ultracode mode runs a plan -\> delegate -\> integrate -\> verify multi-agent workflow. Unique features: /share (GitHub Gist sharing), /goal for sustained multi-turn objectives, chat forking, memory consolidation.

(captured site page body (agents/claurst.md), not a verified repo-code finding)
Claurst demonstrates that a production-grade agent harness can be specified behaviorally and rebuilt without copying code: the repository contains no proprietary source, only spec files derived from analysis and an independent Rust implementation. The result is a GPL-3.0 terminal agent with tool-call streaming, approval flows, subagent and swarm spawning, background tasks, and editor integration through ACP so Zed, Neovim, or JetBrains can drive it. An experimental Free Mode lowers the entry cost, and /share publishes sessions as GitHub Gists. With over ten thousand stars and active releases, it is one of the most successful Claude Code reimplementations in this census.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claurst.md)
