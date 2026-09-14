# conch (`conch`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
Chat platforms want coding agents their users can summon without running infrastructure, and Conch is Crustocean's reference implementation of that pattern. The Node.js worker joins Crustocean over We
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
