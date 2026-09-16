# ade-cli (`ade-cli`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: landing-ai
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI; install=binary
- Model providers: locked
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [landing-ai/ade-cli](../../repos/landing-ai/ade-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic document extraction CLI (from LandingAI) that turns documents with tables/figures/charts into grounded Markdown and schema-shaped fields with page-and-box evidence; caches results locally to avoid duplicate credit usage.

(captured site page body (agents/ade-cli.md), not a verified repo-code finding)
Coding agents asked to read contracts, claims, or financial PDFs hallucinate structure unless the extraction tool returns grounded evidence, which is the gap LandingAI's Agentic Document Extraction CLI fills. Its parse command converts documents into Markdown with per-element bounding boxes, and extract fills schema-shaped fields with page-and-box evidence linking every value to its source region. Every command supports --json and ade help --json exposes the full command surface so agents can discover the interface programmatically, guided by a bundled SKILL.md contract. Results cache in ~/.ade so repeated identical commands consume no credits — important because the underlying API is metered. Data engineers and agent builders processing documents at scale are the users.
Sources: [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json); [site page @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/agents/ade-cli.md)
