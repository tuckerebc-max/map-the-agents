# fireproof (`fireproof`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: fireproof-storage
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Web; install=npm
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [fireproof-storage/fireproof](../../repos/fireproof-storage/fireproof.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight embedded document database with encrypted live sync and git-like versioning via hash history (cryptographic causal consistency). Encrypted content-addressed blob replication, CRDT-based multi-writer safe real-time collaboration. Runs anywhere (browser, Node, Deno, Bun, edge), offline-first with no loading/error states, small package with no WASM. Designed to fit in LLM context windows for AI code generation.

(captured site page body (agents/fireproof.md), not a verified repo-code finding)
Fireproof addresses the persistence gap in AI-built applications: an LLM can generate a React app in seconds, but wiring up a real database, sync, and conflict handling traditionally breaks the flow. As an embedded library (@fireproof/core, use-fireproof), it runs in the browser, Node, Deno, and Bun with live queries through React hooks, CRDT-based multi-writer collaboration, and a hash-chain version history that gives git-like rollback without a server. Content-addressed encrypted blob replication means data syncs between devices without a trusted server, which suits local-first and collaborative apps. Its growth tracks the vibe-coding ecosystem — it is frequently the database an AI app builder reaches for — while remaining a general-purpose embedded database for any JavaScript application.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fireproof.md)
