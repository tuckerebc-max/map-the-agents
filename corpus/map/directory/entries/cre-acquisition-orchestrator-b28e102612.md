# cre-acquisition-orchestrator (`cre-acquisition-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ahacker-1
- License: Apache-2.0
- Language: TypeScript, React, Node.js, Python
- Interface: install=git clone -\> npm install -\> npm run setup -- --skip-codex-install --skip-login -\> npm run proof
- Model providers: OpenAI Codex CLI / ChatGPT; deterministic offline simulation
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ahacker-1/cre-acquisition-orchestrator](../../repos/ahacker-1/cre-acquisition-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Most in-depth open-source CRE acquisition framework: 31-role AI deal team, source-backed extraction with provenance, human approval gates, local-first with optional live Codex web-search runtime, honest open evaluation harness reporting real weaknesses, deterministic Parkview demo requiring no API keys

(captured site page body (agents/cre-acquisition-orchestrator.md), not a verified repo-code finding)
Multifamily acquisitions run on unstructured documents - rent rolls, T12s, offering memos - and CRE software has largely missed the agent wave, so this project models the entire deal lifecycle as an agent workflow. A 31-role team (six orchestrators, twenty-one acquisition specialists, four document-ingestion agents) processes uploads through document parsing (pandas, PyMuPDF, OCR) into extraction candidates that carry source provenance, and a human approval gate is required before any field becomes an underwriting input. The default runtime is live OpenAI Codex CLI with web search enabled so agents cite real market data, while a deterministic offline simulation engine backs demos and CI without credentials. A React/TypeScript dashboard, 28 JSON Schema contracts, and an eval harness over synthetic deals make the system testable. CRE analysts and AI-in-real-estate practitioners use it as a reference architecture rather than production software.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cre-acquisition-orchestrator.md)
