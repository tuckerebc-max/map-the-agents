# opencode-orchestrator (`opencode-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: agnusdei1207
- License: MIT
- Language: TypeScript, Rust
- Interface: install=npm install -g opencode-orchestrator
- Model providers: subagents inherit the primary agent's model unless per-agent overrides are set via agent.\<name\>.model
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [agnusdei1207/opencode-orchestrator](../../repos/agnusdei1207/opencode-orchestrator.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Multi-agent mission control plugin for OpenCode that coordinates AI-agent workflows (Commander, Planner, Worker, Reviewer roles) with autonomous verification and local-first memory. Install hook auto-registers in opencode.json.

(captured site page body (agents/opencode-orchestrator.md), not a verified repo-code finding)
OpenCode handles interactive sessions well, but long objectives — multi-file refactors, feature builds — lose structure and verification discipline as context grows. This plugin overlays a mission loop: /task starts a persisted mission under .opencode/, where a Commander orchestrates, a Planner decomposes the objective into ordered file-level tasks, Workers implement with isolated context and TDD, and a Reviewer gates completion on verified test evidence and builds. Memory is local-first and deliberately low-tech — BM25 retrieval, tags, and a graph with Ebbinghaus-style decay replace any external vector database — and a Rust companion CLI provides an optional TCP shell listener for control. Per-role concurrency and per-agent model overrides are configured in opencode.json. Install is one npm command with an auto-registering plugin hook; missions persist across restarts. Solo OpenCode users running autonomous multi-step work with review gates are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencode-orchestrator.md)
