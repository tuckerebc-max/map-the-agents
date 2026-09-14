# helixent (`helixent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: MagicCube
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: OpenAI-compatible (any OpenAI-compatible endpoint)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [magiccube/helixent](../../repos/magiccube/helixent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): TypeScript library and CLI for building ReAct-style AI agent loops. Three-layer architecture (Foundation, Agent Loop, Coding Agent) keeping provider integrations decoupled and reusable. Bun-powered (same runtime as Claude Code, fast cold starts, compiles to a single self-contained native binary). First-class middleware/hooks: 8 hooks (beforeAgentRun, afterAgentRun, beforeAgentStep, afterAgentStep, beforeModel, afterModel, beforeToolUse, afterToolUse). Human-in-the-loop approval of tool calls. Long-term memory via automatic ...

(captured site page body (agents/helixent.md), not a verified repo-code finding)
helixent is both a TypeScript library for building ReAct-style agent loops and a usable coding agent built on top of them. Its three layers separate concerns: a foundation of provider-agnostic model, message, and tool primitives; a domain-agnostic agent loop with parallel tool invocation, middleware hooks at eight lifecycle points, and human-in-the-loop approval; and a coding layer with bash, file editing, patching, and search tools plus a todo-based plan mode. Skills follow the standard agentskills.io format and are auto-discovered from global and project directories, and AGENTS.md files at the repo root serve as project guidance. The whole stack runs on Bun — chosen deliberately because Claude Code uses the same runtime — with Ink/React for the TUI and single-binary compilation for distribution. It targets developers who want a readable, modifiable agent codebase as much as a daily coding tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/helixent.md)
