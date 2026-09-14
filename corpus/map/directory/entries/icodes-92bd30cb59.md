# Icodes (`icodes`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: a115
- License: CC0-1.0
- Language: Python
- Interface: install=pip install icodes; or clone repo and use Poetry: git clone https://github.com/a115/iCODES.git then poetry install
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [a115/icodes](../../repos/a115/icodes.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM-powered Git archeology tool (Intelligent Commit Ontology Distiller and Enhanced Search) that analyzes and indexes Git commit histories in context, summarizing commit intents and enabling semantic search. Suggests commit messages from staged changes and extracts insights/trends from code evolution history.

(captured site page body (agents/icodes.md), not a verified repo-code finding)
iCODES addresses a narrow problem: Git histories record what changed but rarely why. The tool walks a repository's commit history, sends each commit to an LLM for intent summarization, and stores the results in an index that supports filtered and semantic search over authors, paths, dates, and meanings. Secondary commands suggest commit messages from staged changes and surface trends across code evolution. There is no agentic loop — the LLM performs one-shot analysis per commit — and the project is single-maintainer hobby code on OpenAI's API, last touched in May 2024.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/icodes.md)
