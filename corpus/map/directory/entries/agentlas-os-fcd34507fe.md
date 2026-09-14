# Agentlas OS (`agentlas-os`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: agentlas-ai
- License: Apache-2.0
- Language: Shell, Python
- Interface: platforms=Web; install=binary
- Model providers: Anthropic (Claude Code), OpenAI (Codex), Google (Gemini CLI), Antigravity, Cursor, OpenCode, OpenClaw, Hermes, Grok, local/API models (BYOM)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [agentlas-ai/agentlas-os](../../repos/agentlas-ai/agentlas-os.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Engine-neutral agent standard: agents are portable, owner-scoped packages (not trapped in one vendor workspace). Separates Build/Borrow/Own. Package contract is a 'method document' with routing cards, memory boundaries, verification gates. Local-first execution; works across multiple LLM hosts with the same agent package. Per-runtime plugin drivers for Claude Code, Codex, etc. Multi-agent teams with PM Orchestrator, Memory Curator, Policy Gate, QA.

(captured site page body (agents/agentlas-os.md), not a verified repo-code finding)
Agent definitions are usually trapped inside a single vendor's workspace, so Agentlas OS specifies a package format that separates the LLM (the worker), the runtime (files, shell, browser facilities), and the agent package (procedures, judgement rules, I/O contracts, stop conditions). A package-contract.json plus a verification script enforce that every build emits required artifacts such as intake and output schemas, and provenance markers (extracted, read, graded, absent) keep package claims auditable. Runtime drivers adapt the same package to Claude Code, Codex, Gemini CLI/Antigravity, Cursor, OpenCode, OpenClaw, Hermes, Grok, Kimi, Goose, Ollama, and API hosts through slash commands like /agentlas build or Codex $hephaestus-* skills. Supporting subsystems include a meta-agent factory, a briefing interview engine that freezes work briefs after ambiguity gates, Stormbreaker verification-gated execution, and a local SQLite/FTS5 ontology runtime. Developers who want agent assets to outlive any one vendor workspace are the target audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentlas-os.md)
