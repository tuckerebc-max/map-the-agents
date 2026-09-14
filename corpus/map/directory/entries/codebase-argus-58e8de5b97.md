# codebase-argus (`codebase-argus`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: AaronZ345
- License: MIT
- Language: TypeScript
- Interface: install=/plugin marketplace add AaronZ345/codebase-argus then /plugin install codebase-argus@codebase-argus (Claude Code); or npm ci / npm link for local dev
- Model providers: openai-api, anthropic-api, gemini-api (API); codex-cli, claude-cli, gemini-cli (local CLI)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [aaronz345/codebase-argus](../../repos/aaronz345/codebase-argus.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent PR review + downstream fork-sync risk analysis for maintainers; combines deterministic review with multi-provider tribunal consensus, local git simulations (merge-tree, rebase, cherry, range-diff), and CI failure diagnosis.

(captured site page body (agents/codebase-argus.md), not a verified repo-code finding)
Codebase-argus targets repository maintainers who need review verdicts they can trust, combining deterministic evidence with multi-model judgment. For each pull request it assembles an evidence package — patch, check status, changed files, branch state, policy gates from .codebase-argus.yml, and prior reviews — enriched with local git simulations such as merge-tree projections, rebase simulations, and git cherry/range-diff comparisons against downstream forks. Multiple providers then review the same evidence, and tribunal mode groups findings that independent models agree on, surfacing provider failures rather than hiding them. Beyond PR review it diagnoses CI failures from logs and plans gated autofixes for mechanical changes. It ships as a CLI, a Next.js dashboard, a GitHub Action, a webhook-based GitHub App, and a Claude Code plugin installable from a marketplace.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codebase-argus.md)
