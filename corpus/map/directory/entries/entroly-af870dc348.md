# Entroly (`entroly`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: juyterman1000
- License: Apache-2.0
- Language: Python, Rust, TypeScript
- Interface: platforms=IDE; install=pip install -U entroly, npm install -g entroly, cargo build --release (Rust), brew install juyterman1000/entroly/entroly, or docker pull ghcr.io/juyterman1000/entroly:latest
- Model providers: OpenAI, Anthropic, Google, NVIDIA Nemotron via Ollama, OpenAI/Anthropic-compatible endpoints
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [juyterman1000/entroly](../../repos/juyterman1000/entroly.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Drop-in context assurance / local-first Context OS for AI coding agents; content-addressed evidence with byte-exact recovery, auditable Context Receipts, local hallucination detection (WITNESS) without a second API call, cache-aware compression that preserves provider prompt-cache discounts, and panic-rescue for over-long sessions

(captured site page body (agents/entroly.md), not a verified repo-code finding)
Entroly was built on the observation that agent failures often trace to degraded context — truncated, lossy, or unverifiable — and that token cost scales with noisy context. It intercepts requests on routes it controls, selects the highest-value evidence, compresses it, and issues receipts that make every context decision auditable and recoverable byte-for-byte, with a local WITNESS detector flagging hallucination risk without cloud calls. Attachment paths include an MCP server (with a .mcpb bundle and Smithery config), a Claude Code plugin, an API-key proxy, and an SDK, so teams can adopt it incrementally across Claude Code, Codex, Cursor, Copilot, and Aider. The project is candid that savings are workload-dependent — its own benchmark shows accuracy dropping on some workloads — and \`entroly simulate\` estimates savings before adoption.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/entroly.md)
