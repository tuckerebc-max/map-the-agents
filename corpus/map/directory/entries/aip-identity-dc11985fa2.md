# Aip-Identity (`aip-identity`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: The-Nexus-Guard
- License: MIT
- Language: Python
- Interface: platforms=CLI, IDE, Web; install=pip install aip-identity (or clone and pip install -e .)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [the-nexus-guard/aip](../../repos/the-nexus-guard/aip.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent Identity Protocol (AIP) — decentralized cryptographic identity (Ed25519 keypairs), verifiable trust chains (vouching), and E2E encrypted messaging for AI agents. Enables secure, verifiable agent-to-agent communication without a central authority. Integrates with MCP to sign MCP requests and fill the 'agent identity gap.'

(captured site page body (agents/aip-identity.md), not a verified repo-code finding)
Multi-agent systems lack a way to prove who an agent is or whether to trust its output; AIP addresses this with three layers: cryptographic identity (Ed25519 keypairs, did:aip DIDs, challenge-response verification), trust chains built from signed vouches with scopes and decaying trust scores, and relay-based E2E encrypted messaging where the relay only ever sees ciphertext. A Python SDK (pip install aip-identity), CLI, MCP server, GitHub Action for trust-gated deployments, and integrations with LangChain, CrewAI, AutoGen, and A2A make it consumable from existing frameworks. It is MIT-licensed, actively versioned (v0.5.46, 325 commits), and early — 15 stars — with vouch lookup and messaging still depending on a hosted Fly.io relay.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/aip-identity.md)
