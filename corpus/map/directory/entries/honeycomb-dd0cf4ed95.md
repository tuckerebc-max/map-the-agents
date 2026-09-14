# honeycomb (`honeycomb`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: legioncodeinc
- License: AGPL-3.0-or-later
- Language: TypeScript
- Interface: install=curl -fsSL https://get.theapiary.sh | sh (macOS/Linux) or irm https://get.theapiary.sh/install.ps1 | iex (Windows); or npm install -g @legioncodeinc/honeycomb; or build from source
- Model providers: nomic-embed-text-v1.5 (opt-in)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [legioncodeinc/honeycomb](../../repos/legioncodeinc/honeycomb.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Shared, persistent memory for AI coding agents; local daemon captures every agent turn and distills into three-tier memory (key -\> summary -\> raw) with deterministic SQL joins; session priming injects bounded ~300-800 token index at session start; Skillify & propagation mines reusable skills and auto-pulls team skills; pollinating loop merges duplicates/prunes junk/supersedes stale facts; knowledge graph + multi-language AST codebase ...

(captured site page body (agents/honeycomb.md), not a verified repo-code finding)
honeycomb gives coding agents a shared, durable memory across sessions, tools, and machines. A local daemon captures each agent turn through harness hooks, distills it into a three-tier structure — a one-line keyword key, a distilled summary, and the raw dialogue — and serves recall to any connected client, so a decision made in Claude Code is available to Cursor or a teammate's session later. Session priming injects a bounded keyword index at the start of each session rather than re-reading raw transcripts, keeping context overhead low, while a pollinating maintenance loop merges duplicates and retires stale facts. Beyond raw memory it mines recurring patterns into skills that propagate across a team, and it maintains both an entity knowledge graph and a multi-language AST graph of the codebase. Retrieval combines BM25 with optional local embeddings through reciprocal rank fusion, with deterministic SQL joins guaranteeing exact recall of stored records.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/honeycomb.md)
