# SIFT (`sift`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: unknown
- Interface: platforms=IDE; install=npx skills add 2389-research/sift
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Agent Skill format, npx skills add) (yes)
  - claude_code_plugin: yes (runs inside Claude Code and similar agents) (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/sift](../../repos/2389-research/sift.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Structural Inspection for Technical Simplification — a read-only Agent Skill that audits a whole codebase for material simplifications (data structures, state, algorithms, control flow, schemas, lifecycle/concurrency, ownership). Produces a coverage contract, partitions the repo into subsystem reviews, validates findings, and outputs a prioritized report. Does not edit code or run tests.

(captured site page body (agents/sift.md), not a verified repo-code finding)
SIFT — Structural Inspection for Technical Simplification — is a read-only Agent Skill that runs inside host agents such as Claude Code rather than as a standalone tool. It audits an entire codebase for material simplifications across data structures, state, algorithms, control flow, schemas, lifecycle and concurrency, and ownership. The skill first produces a coverage contract so the audit's scope is explicit, partitions the repository into subsystem reviews, validates each finding, and emits a prioritized report. It does not edit code or run tests; its output is a map of where the codebase can be made simpler and why. The audience is engineers who want a structured, repeatable simplification pass driven by the host agent they already use, without the skill touching anything.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sift.md)
