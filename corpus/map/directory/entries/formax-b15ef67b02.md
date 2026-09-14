# formax (`formax`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: yusifeng
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm i -g @yusifeng/formax@beta
- Model providers: Anthropic, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [yusifeng/formax](../../repos/yusifeng/formax.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source implementation of a Claude Code-style AI assistant built 100% with Codex (AI-assisted development traces intentionally kept in repo); implements Claude Code behavior by reverse-engineering/observation; offers both terminal (TUI) and web (GUI) interfaces modeled after the Codex UI. Beta stage, suited for learning/experimentation.

(captured site page body (agents/formax.md), not a verified repo-code finding)
Claude Code is closed source, and formax exists to answer the question of what a Claude Code-style harness looks like on the inside. The author reconstructed its behavior from network traces and observation, then rebuilt it in a TypeScript/Node monorepo with an Ink-based TUI, a web GUI, and a JSON-RPC app-server with a WebSocket bridge mode. It supports Anthropic and OpenAI-compatible endpoints, mirrors Claude Code workflows such as /init CLAUDE.md generation, plan mode, and sub-agent code review, and documents MCP and hooks as known gaps. The repository deliberately preserves the Codex build artifacts, plans, and docs, which makes it a reference for developers studying how agentic coding harnesses are constructed.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/formax.md)
