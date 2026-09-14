# clio (`clio`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: icebear0828
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=git clone, npm install, npm run build, npm link (global); or npm run dev for development
- Model providers: Anthropic, OpenAI-compatible (via --api-format openai), custom gateways/proxies
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [icebear0828/clio](../../repos/icebear0828/clio.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Feature-rich Claude Code clone in TypeScript (~9200 lines, 46 source files) with prompt caching (~90% input token savings), 21 built-in tools, zero external runtime dependencies, MCP support (JSON-RPC 2.0 over stdio), manifest-driven plugins, custom subagents with git worktree isolation, agent teams with inter-agent messaging, checkpoint rollback, LSP integration, extended thinking mode, and 4-level settings hierarchy.

(captured site page body (agents/clio.md), not a verified repo-code finding)
Clio's value is architectural: it demonstrates that a complete agentic coding assistant - 21 tools, three permission modes, subagents, hooks, sessions, and MCP discovery - fits in roughly 9,200 lines of TypeScript with essentially no runtime dependencies beyond fast-glob. Prompt caching is applied at section level across system prompt, tools, and message history, cutting input token cost around 90 percent, with model-aware context limits and auto-compaction at 85 percent. Tools are tiered safe/write/dangerous and gated by default, auto, and plan modes with glob rules. It targets the Anthropic API and OpenAI-compatible endpoints, and remains a young project with a small commit history and no packaged releases.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/clio.md)
