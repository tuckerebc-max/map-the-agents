# 2389 Agent Protocol (Rust) (`2389-agent-rust`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent-sdk
- Provider/maker: 2389-research
- License: MIT
- Language: Rust
- Interface: install=cargo install
- Model providers: OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (extensible JSON-schema-validated tool system) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (agent discovery/capability matching) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/2389-agent-rust](../../repos/2389-research/2389-agent-rust.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Production-ready Rust implementation of the 2389 Agent Protocol — a standard for interoperable AI agents communicating via MQTT in distributed systems. Provides an agent runtime (deployable agent binaries), a Rust library (agent2389 on crates.io), multi-LLM support, extensible JSON-schema-validated tool system, MQTT transport with QoS 1, agent discovery/capability matching, and observability (health endpoints, metrics).

(captured site page body (agents/2389-agent-rust.md), not a verified repo-code finding)
This is the production-ready Rust implementation of the 2389 Agent Protocol, a standard for interoperable AI agents that communicate over MQTT in distributed systems. It ships an agent runtime as deployable binaries and a Rust library (agent2389 on crates.io) for embedding the protocol elsewhere. Agents advertise capabilities through discovery and capability matching, transport runs over MQTT with QoS 1, and tools are extensible and JSON-schema-validated so an agent's tool surface is describable and checkable. Multi-LLM support spans OpenAI and Anthropic, and observability comes via health endpoints and metrics. It is a framework for building interoperable agents, not a coding agent itself. The audience is developers wiring agents together across processes and machines who need a real protocol rather than ad-hoc HTTP.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/2389-agent-rust.md)
