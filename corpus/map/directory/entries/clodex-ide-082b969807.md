# clodex-ide (`clodex-ide`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: mereyabdenbekuly-ctrl
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=Autonomous, IDE; install=binary
- Model providers: CLODEx account (hosted models), BYOK, custom OpenAI-compatible endpoints, Ollama (local inference)
- Feature flags (directory-reported):
  - mcp_support: yes — user-configured stdio and remote MCP servers, HTTP/SSE transports, OAuth flows, tools, resources, prompts, approval-aware execution (yes)
  - plugin_support: yes — integration surfaces for plugins and extension metadata, MCP servers, and reusable skills/context files (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mereyabdenbekuly-ctrl/clodex-ide](../../repos/mereyabdenbekuly-ctrl/clodex-ide.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first agentic IDE for long-running engineering work with durable tasks that persist across restarts; zero-trust philosophy (model output is input, not authority) with explicit permission/approval/review surfaces; proof-based releases with SBOMs and checksums.

(captured site page body (agents/clodex-ide.md), not a verified repo-code finding)
CLODEx restructures agent interaction around persistence: a task carries workspace context, approval history, and pending edits across restarts, so long-running engineering work survives reboots and session switches instead of being reconstructed from messages. The agent runtime inspects files and executes local tools only through explicit permission checks, and every output - diffs, terminal logs, browser state - lands on review surfaces before it can be committed, enforcing the principle that model output is input rather than authority. It began as a Stagewise fork and diverged into an independent AGPL-3.0 project, accepting hosted accounts, BYOK, OpenAI-compatible endpoints, or local Ollama. The project is an actively developed single-maintainer technical preview.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/clodex-ide.md)
