# contextvc (`contextvc`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: HaochengLu
- License: Apache-2.0
- Language: Rust
- Interface: install=cargo install --locked --git https://github.com/HaochengLu/contextvc.git --tag v0.1.0 (requires Rust stable toolchain)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [haochenglu/contextvc](../../repos/haochenglu/contextvc.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Git-native context control plane: treats agent memory as repo-level infrastructure (versioned, reviewed, merged, CI-checked, enforced). Single source of truth in .context/ compiles to multiple agent-native files (Claude Code, Cursor, Codex, Copilot, Gemini, Cline). Enforces constraints before risky actions via precheck gates. Human review queue for runtime-learned proposals. RepeatBench for failure-prevention benchmarking.

(captured site page body (agents/contextvc.md), not a verified repo-code finding)
Agent instruction files - CLAUDE.md, AGENTS.md, Cursor rules - multiply across tools, drift out of sync, and receive none of the review discipline applied to code. ContextVC makes that memory a git-native control plane: typed Markdown objects (constraints, decisions, failures, how-tos, code maps, preferences) live in a .context/ directory, and a render command compiles them into each tool's native format while preserving human-written text outside managed blocks. Enforcement goes beyond documentation - precheck hooks return warn, ask, or block before risky actions, CI health checks fail on drift or stale bindings, and runtime failures feed a review workflow where a human accepts proposals before they become formal memory. A local stdio MCP server exposes search and status tools to any MCP client, and context objects support log, blame, diff, and revert through normal Git semantics. Teams running multiple agents over one repository use it to keep context consistent and reviewed.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/contextvc.md)
