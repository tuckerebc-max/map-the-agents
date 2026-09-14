# nasiko (`nasiko`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Nasiko-Labs
- License: Apache-2.0
- Language: Rust
- Interface: install=docker
- Model providers: OpenAI-compatible (LLM Router proxy)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [nasiko-labs/nasiko](../../repos/nasiko-labs/nasiko.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Single-process developer control plane for any A2A-protocol-speaking agent. Terminates TLS, authenticates, proxies all agent-to-agent traffic (agents never publicly exposed). Built-in MCP Gateway, LLM Router (OpenAI-compatible egress with short-lived tokens), embedded OCI registry, encrypted secrets, 3-stage intelligent routing (embedding → rerank → LLM pick), full OpenTelemetry observability with token cost collection.

(captured site page body (agents/nasiko.md), not a verified repo-code finding)
Nasiko targets teams operating fleets of A2A-protocol agents who need a single enforcement point for identity, cost, and security. Agents register through a CLI and are never publicly reachable; every hop passes through the control plane, which applies allowlists, rate limits, and OpenTelemetry tracing while collecting per-call token costs. An LLM router resolves provider, model, and key server-side so agents hold only short-lived identity tokens, and the MCP gateway merges Composio toolkits and custom servers into one credential-free URL. It hardcodes A2A spec v1.0, so language choice is unconstrained — Python, Rust, Go, and TypeScript agents all work. Deployment is Docker Compose with standard Postgres, Redis, and S3 backends.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nasiko.md)
