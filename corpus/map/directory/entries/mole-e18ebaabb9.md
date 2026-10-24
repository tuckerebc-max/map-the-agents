# Mole (`mole`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: lajosdeme
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI; install=Static binaries (mole + mole-mcp) from the repo releases
- Model providers: configurable
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [lajosdeme/mole](../../repos/lajosdeme/mole.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A deep-research agent with an enforced budget: every model call is reserved and settled against a ledger so --usd 0.50 hard-stops the run at fifty cents, and every claim must carry a verbatim quote from its source or be discarded. Ships with a toolkit mode where a coding agent's model does the reasoning and mole supplies deterministic quote verification, SQL ...

(captured site page body (agents/mole.md), not a verified repo-code finding)
Mole is a Go deep-research agent, not a coding agent: it takes a research question, decomposes it into sub-questions, searches the web and academic sources (Crossref, OpenAlex, arXiv, PubMed), reads sources, extracts claims, and writes a cited answer. Its two signature constraints are an enforced budget — every model call is reserved and settled against a ledger so a --usd 0.50 flag hard-stops the run at fifty cents with measured zero overshoot — and verified quotes, where every claim must carry a verbatim quote from its source and unverified claims are discarded or flagged. A privacy boundary lets it analyze local CSV/JSON data with only aggregates leaving the machine, and mole crossings shows exactly what crossed. It ships as two static binaries, mole and mole-mcp, the latter exposing it over MCP so a coding agent like Claude Code can drive it — either with mole owning the model, or in toolkit mode where the agent's model reasons while mole supplies the deterministic parts. It is included here as tooling that complements coding agents rather than a harness.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/mole.md)
