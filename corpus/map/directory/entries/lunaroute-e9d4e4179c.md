# lunaroute (`lunaroute`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: erans
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=Download prebuilt binary from GitHub Releases, or build from source with cargo build --release
- Model providers: OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [erans/lunaroute](../../repos/erans/lunaroute.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): High-performance local proxy for AI coding assistants (Claude Code, OpenAI Codex CLI, OpenCode) with zero-overhead passthrough, sub-millisecond latency, dual-dialect passthrough (OpenAI + Anthropic formats simultaneously), comprehensive session recording (SQLite + JSONL), automatic PII redaction, built-in Web UI, and Prometheus metrics. One-command setup via eval $(lunaroute-server env).

(captured site page body (agents/lunaroute.md), not a verified repo-code finding)
Teams adopting coding CLIs need visibility into what those agents send to model APIs without adding a cloud hop. LunaRoute sits locally in front of the assistants: one shell command starts the proxy and points ANTHROPIC_BASE_URL and OPENAI_BASE_URL at it, after which traffic passes through with sub-millisecond latency and full API fidelity, including WebSocket transport for Codex CLI. Every request and response is recorded with token counts, tool calls, and cost estimates, searchable through a built-in web UI, and PII is redacted pre-persistence under a local-first, zero-trust storage model. Prometheus metrics expose 24 metric types for operations dashboards. Individual developers and small teams with compliance constraints are the natural users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/lunaroute.md)
