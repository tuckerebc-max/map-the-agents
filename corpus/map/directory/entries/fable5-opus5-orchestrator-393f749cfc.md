# fable5-opus5-orchestrator (`fable5-opus5-orchestrator`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Rylaa
- License: MIT
- Language: Python
- Interface: install=/plugin marketplace add Rylaa/fable5-opus5-orchestrator && /plugin install orchestrator@fable-orchestrator (requires python3 on PATH; macOS and Linux only)
- Model providers: Anthropic (Claude Fable 5, Sonnet 5, Opus 5)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [rylaa/fable5-opus5-orchestrator](../../repos/rylaa/fable5-opus5-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Claude Code plugin for token-frugal multi-agent orchestration keeping Claude Fable 5 as the chair while delegating volume work to Sonnet 5 and hard tasks to Opus 5; enforces a Requirements Ledger and guard hooks (spawn/task/close) with fresh-eyes verification on every close.

(captured site page body (agents/fable5-opus5-orchestrator.md), not a verified repo-code finding)
The plugin addresses a cost problem specific to frontier subscriptions: every token an expensive chair model spends on routine work is a token unavailable for thinking, so Fable 5 is confined to planning and arbitration while Sonnet 5 writes code and tests and Opus 5 handles architecture, security review, and final verification. A /fire workflow clarifies the request one question at a time, writes a requirements ledger to .workflow/LEDGER.md, delegates to sized workers, and has a fresh agent verify the result. Five hook-based gates (Clarify, Approve, Spawn, Task list, Close) block non-compliant tool calls rather than trusting instructions, and a watchdog monitors spawned agents for stalled states. Claude Code subscribers on usage-limited plans running multi-step engineering work are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fable5-opus5-orchestrator.md)
