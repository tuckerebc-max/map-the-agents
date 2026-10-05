# conch (`conch`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Crustocean
- License: MIT
- Language: JavaScript, Node.js (\>= 18)
- Interface: platforms=Web; install=Create agent on Crustocean via /agency create, /boot conch, /agent verify conch; cp .env.example .env and set CRUSTOCEAN_API_URL, CONCH_AGENT_TOKEN, ANTHROPIC_API_KEY; ensure @crustocean/sdk available; npm install && npm start; connect a repo with !conch connect owner/repo; deploy via Railway (railway up), Docker, or any Node.js host
- Model providers: Anthropic (Claude) - any Anthropic model with tool-use support, configurable via CONCH_MODEL
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [crustocean/conch](../../repos/crustocean/conch.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Cloud coding agent steered from the Crustocean chat platform that reads GitHub repos, writes patches, and opens PRs; stateless worker with no database, filesystem, or ports - connects via WebSocket to Crustocean and REST API to GitHub; in-memory staged writes via a Map (nothing touches GitHub until commit()) for ephemeral per-run changes; atomic commits via the Git Data API (blobs, ...

(captured site page body (agents/conch.md), not a verified repo-code finding)
Chat platforms want coding agents their users can summon without running infrastructure, and Conch is Crustocean's reference implementation of that pattern. The Node.js worker joins Crustocean over WebSocket, reads a connected GitHub repository through the REST API, and drives Claude's tool-calling loop to explore code and build patches; every write stays in memory until an explicit commit step assembles blobs, a tree, and a ref update atomically at PR creation. Permission gates require explicit approval before pull requests are created or merged, default branches are hard-blocked from deletion, and file writes are path-validated and size-capped. Runs appear in Crustocean as timelines of tool cards and status banners. Users deploy it on Railway, Docker, or any Node host and extend it by editing a single tool-definitions file.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/conch.md)
