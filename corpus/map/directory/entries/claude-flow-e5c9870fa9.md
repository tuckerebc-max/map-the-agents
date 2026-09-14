# claude-flow (`claude-flow`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: ruvnet
- License: MIT
- Language: TypeScript
- Interface: platforms=Autonomous; install=npm
- Model providers: Claude, OpenAI (GPT), Google (Gemini), Cohere, Ollama, OpenRouter, ruvLLM (local)
- Feature flags (directory-reported):
  - mcp_support: yes (MCP server via stdio, ~210 MCP tools) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry (renamed): original lead [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) (source: backing, field: `source_code_url`) now resolves to [ruvnet/ruflo](../../repos/ruvnet/ruflo.md) (github id 995029641, verified [https://github.com/ruvnet/ruflo](https://github.com/ruvnet/ruflo)).

## Description

Highlight (site page `what_makes_it_special`): An agent meta-harness providing the execution layer around Claude Code and Codex with a GOAP A* planner, self-learning architecture (SONA neural patterns, ReasoningBank), and zero-trust Agent Federation ('Slack for Agents').

(captured site page body (agents/claude-flow.md), not a verified repo-code finding)
Claude Flow treats the model-plus-harness split literally: Claude Code or Codex remains the coding surface, while Ruflo supplies swarm coordination (hierarchical, mesh, adaptive topologies with consensus mechanisms), 27 hooks for task routing, persistent learning memory (ReasoningBank, trajectory learning), and a GOAP planner that re-plans adaptively rather than restarting on failure. It installs as a Claude Code plugin or npx scaffold, an MCP server exposes its toolset, and a zero-trust federation layer lets agent clusters collaborate across machines with mTLS and PII stripping. The project is among the most-starred in this census (roughly 70k stars), is MIT-licensed, and was renamed Ruflo with active v3 development.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-flow.md)
