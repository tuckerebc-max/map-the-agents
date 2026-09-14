# electric (`electric`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: electric-sql
- License: Apache-2.0
- Language: Elixir, TypeScript
- Interface: install=docker
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [electric-sql/electric](../../repos/electric-sql/electric.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Real-time sync engine for Postgres (not a coding agent). Uses 'Shapes' for partial replication, fan-out, and data delivery from Postgres to clients. Core protocol is a low-level HTTP API integrating with CDNs for scalable delivery. CRDT-based sync. Positioned as 'the agent platform built on sync' -- enables apps and AI agents to work with live local data.

(captured site page body (agents/electric.md), not a verified repo-code finding)
Electric grew out of the observation that most applications need only a slice of a Postgres database, delivered live, and that no existing tool handled partial replication plus massive fan-out. The sync service streams shape logs (rows matching a shape definition, with position tracking for resume) over an HTTP API designed to be cached by CDNs, so a single Postgres primary can serve read-path sync to very large client counts without exposing Postgres itself. Clients consume shapes directly over HTTP or through TypeScript packages with framework bindings like the React useShape hook. Its users are web and mobile application teams building local-first or collaborative products, and the project has more recently positioned the same sync machinery as a data layer for AI agents that need live application data.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/electric.md)
