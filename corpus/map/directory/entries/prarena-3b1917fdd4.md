# PRarena (`prarena`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: aavetis
- License: unknown
- Language: Python
- Interface: unknown
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [aavetis/prarena](../../repos/aavetis/prarena.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Tracks opened and merged pull requests created by top SWE coding agents (Copilot, Codex, Cursor, Devin, Codegen, Jules) to provide analytics on PR volume versus success (merge) rates.

(captured site page body (agents/prarena.md), not a verified repo-code finding)
PRarena answers a question benchmarks avoid: when real coding agents open pull requests against real GitHub repositories, how often do those PRs get merged? It runs GitHub search queries keyed on agent-specific identifiers — branch prefixes like head:codex/ or bot accounts such as devin-ai-integration\[bot\] — and tracks opened versus merged PRs per agent, updating a public dashboard and chart automatically. Comparisons use ready PRs only, since agents like Codex iterate privately before opening while Copilot and Codegen open drafts first, which would otherwise skew merge rates. The distinction between draft, ready, and merged states makes the comparison more honest than raw PR counts. Researchers and buyers of coding agents use it as one of the few population-scale measures of whether agent-authored work actually survives review.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/prarena.md)
