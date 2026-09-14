# Fuxi (`fuxi`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: fuxicodex
- License: Proprietary
- Language: HTML
- Interface: platforms=CLI, IDE; install=binary
- Model providers: OpenAI-compatible, Anthropic, Gemini, Bedrock/Vertex
- Feature flags (directory-reported):
  - mcp_support: yes (stdio; both MCP client and server) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [fuxicodex/fuxi](../../repos/fuxicodex/fuxi.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-first AI coding agent with a Think → Act → Verify loop; cost-aware intelligent routing (complexity-scored model selection with automatic failover); 50+ built-in tools in a single static binary; safety guardrails (AST shell command classifier, explicit permission model); durable sessions & memory with checkpoints and idle 'dreaming' consolidation; self-updating with checksum verification.

(captured site page body (agents/fuxi.md), not a verified repo-code finding)
FuXi exists as a provider-agnostic alternative to Claude Code: one static Go binary with no runtime dependencies that reads and edits code, runs commands, and verifies its own work in a Think-Act-Verify loop. Model selection is scored by task complexity with failover across any OpenAI-compatible endpoint, Anthropic, Gemini, or Bedrock/Vertex, using either user API keys or a FuXi OAuth login. Extensibility covers hooks, skills, plugins, and slash commands, all hot-reloadable, and the binary can both consume MCP servers and run as one. Sessions checkpoint and consolidate memory during idle periods, updates are checksum-verified, and a plan permission mode gates execution; the binary itself is proprietary freeware with the repository hosting only docs and the issue tracker.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fuxi.md)
