# rgr (`rgr`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: kingbootoshi
- License: unknown
- Language: TypeScript
- Interface: platforms=CLI; install=git clone, cd rgr, bun run rgr (optionally bun link); or claude plugin marketplace add kingbootoshi/rgr
- Model providers: none (LLM-free discipline gate; all checks are deterministic CLI operations)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [kingbootoshi/rgr](../../repos/kingbootoshi/rgr.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): No-dependency Red-Green-Refactor gate for coding agents enabling 'trustless engineering' — freezes failing tests with SHA-256 hashes and snapshots, and refuses to mark Green or Refactor if the Red test was edited. The .rgr/ directory is evidence, not authority — CI verifies against a trusted lock the agent cannot control.

(captured site page body (agents/rgr.md), not a verified repo-code finding)
The premise is that an agent with write access cannot be trusted to report its own test results — it can weaken a failing test, delete the evidence, or replace real assertions with mock-echo tests. rgr makes the discipline mechanical: the agent must first record a genuinely failing test (Red), which the tool freezes with hashes and snapshots; subsequent Green and Refactor steps fail if the protected evidence changed. Because local enforcement can be bypassed by an agent that deletes .rgr, the authoritative mode replays the Red proof from recorded base commits inside CI, outside the agent's reach. It ships as Claude Code and Codex plugins with a prompt block that discourages shallow tests, and it is aimed at engineers who want CI to verify agent work without trusting the agent's report.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rgr.md)
