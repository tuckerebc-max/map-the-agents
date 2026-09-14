# Mql (`mql`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: shurutech
- License: MIT
- Language: Python, Node.js
- Interface: install=Docker (make install) or local setup (./setup.sh)
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [shurutech/mql](../../repos/shurutech/mql.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): MQL (My Query Language) transforms natural language queries into executable SQL queries; users connect their database or upload schema, ask queries in natural language, and receive generated SQL.

(captured site page body (agents/mql.md), not a verified repo-code finding)
MQL, from Shuru, addressed the analyst's recurring bottleneck: querying a database requires SQL fluency that most business users lack. Users connect a PostgreSQL database or upload a schema, type questions in plain language, and receive generated SQL, with pgvector-based retrieval over schema context improving generation quality and an OpenAI API key supplying the model. A built-in accuracy harness against a sample e-learning database — 43 of 50 queries correct, about 74% executing cleanly — made the tool unusually honest about its limits, publishing its own failure rate. The web dashboard supports user login and query review, and Docker or a setup script handles deployment. The roadmap items listed in the README (query execution, MySQL support, visualizations, Slack integration) were never implemented, and the repository has seen no sustained activity since its 2023 debut, leaving it as an early NL-to-SQL prototype rather than a maintained product.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mql.md)
