# Claudexor (`claudexor`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: razzant
- License: MIT
- Language: TypeScript, Swift
- Interface: platforms=CLI, Desktop; install=CLI via npm install -g claudexor; macOS app via signed DMG from GitHub Releases; or build from source using pnpm
- Model providers: Codex CLI, Claude Code, Cursor CLI, OpenCode, Antigravity CLI (agy), OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [razzant/claudexor](../../repos/razzant/claudexor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-harness control plane for AI coding agents that runs them behind one typed interface with quota-aware rotation, shared thread context, and cross-model review; best-of-N races with independent reviewers/arbitration, honest budget/quota accounting (never reports unknown cost as $0), deterministic gates, multi-account credential profiles with live quota tracking, no telemetry

(captured site page body (agents/claudexor.md), not a verified repo-code finding)
Claudexor targets the practitioner holding several paid agent subscriptions who wants them as interchangeable capacity rather than separate tools. A local daemon routes turns to a chosen harness, resumes native sessions for continuity, and turns write requests into inspectable patches; quota rotation switches accounts only on typed vendor-limit signals, and best-of-N races select winners through independent, ideally cross-family, review rather than self-grading. A --council mode has multiple harnesses draft competing plans that a primary merges. Everything runs locally with file-based artifacts, and the v3.8.0 release's missing signing documents were the one notable supply-chain stumble. Solo power users running multi-agent setups are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claudexor.md)
