# AURA (`aura`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: mezmo
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/mezmo/aura/main/scripts/install.sh | bash (Linux/macOS, verifies checksums); docker run mezmo/aura; Helm chart for Kubernetes; embed the Rust core as a library
- Model providers: OpenAI, Anthropic, AWS Bedrock, Google Gemini, Ollama, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [mezmo/aura](../../repos/mezmo/aura.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A production-tested SRE agent platform that began as Mezmo's internal operations harness: teams of specialist agents investigate production incidents across observability and infrastructure tools, the whole agent system is defined in reviewable TOML, sensitive actions wait for human approval, and it runs self-hosted or air-gapped with OpenTelemetry traces on every decision.

(captured site page body (agents/aura.md), not a verified repo-code finding)
AURA started life as the internal harness Mezmo built to run its own SaaS, and is now the Apache-2.0 core of their operations story: a Rust agent runtime you can install on Linux or macOS in minutes and point at your own stack. The whole agent system lives in reviewable TOML — models, specialist agent teams, per-agent prompts, tools, approval policies and guardrails — so an SRE team can version its incident-response setup like code. In action, a preconfigured team of agents investigates incidents by correlating the tools you already run: PagerDuty, Datadog, Prometheus, Kubernetes, Argo CD, AWS, and more, reached through built-in integrations and MCP servers over Streamable HTTP, SSE or STDIO, with Qdrant or Bedrock knowledge bases grounding runbook lookups. Guardrails are the design center: sensitive tool calls wait for explicit human approval (webhook or in-conversation, failing closed on timeout or transport error), oversized tool results park on disk for selective retrieval, and every model, tool and orchestration decision exports as OpenTelemetry spans. It runs interactively as a terminal chat assistant, as a daemon wired to monitoring systems, as the mezmo/aura container or a Helm-charted Kubernetes workload, or embedded as a Rust library — and it serves agents through an OpenAI-compatible API, so existing chat clients work unchanged. Mezmo's engineering and SRE teams still run it in production, teams outside Mezmo run it in their own environments, and ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/aura.md)
