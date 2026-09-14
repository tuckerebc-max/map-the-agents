# Twing (`twing`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: twing
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @twing/cli (Node \>= 20); twing init installs the twing-hook Go binary and wires it into Claude Code hooks
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [twing-dev/twing-cli](../../repos/twing-dev/twing-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A coordination layer for fleets of coding agents: twing align advisory-checks critical files, active work, and design overlap, while the one blocking gate requires a registered design before an agent's first Edit or Write, with conflicts bucketed into constraint violations, file overlap, Tree-sitter symbol conflicts, and LLM-judged semantic divergence. Fails closed if the coordinator is unreachable.

(captured site page body (agents/twing.md), not a verified repo-code finding)
Twing is aimed at engineering leaders running fleets of AI coding agents, on the observation that agents write whole features in parallel on the same codebase and duplicate work, contradict each other, and land conflict-prone PRs faster than humans can review. The live piece is a CLI plus a hook installed into your coding agent (Claude Code today, others planned) plus a small coordination server — hosted free at coordination-server.twing.dev or self-hosted — where a background daemon syncs the hook's stateless observations. twing align is advisory only, flagging critical files, concurrent work, and overlap with registered designs, while the design-conflict gate is the one blocking mechanism: before an agent's first edit in a session it must have a registered design, and conflicts sort into admin-gated constraint violations, advisory file overlaps, self-justifiable Tree-sitter symbol conflicts, and LLM-judged semantic divergence. It does not write code itself — it is the coordination tooling around agents — and the roadmap adds a review artifact beyond line diffs and compounding organizational context.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/twing.md)
