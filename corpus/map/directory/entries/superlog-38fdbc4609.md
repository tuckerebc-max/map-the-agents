# Superlog (`superlog`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: superloglabs
- License: Apache-2.0
- Language: TypeScript
- Interface: install=pnpm install, docker compose up -d, pnpm --filter @superlog/db db:migrate, pnpm dev (requires Node.js 20+, pnpm 9+, Docker); or npx skills add superloglabs/skills --all
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [superloglabs/superlog](../../repos/superloglabs/superlog.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source agentic telemetry system that ingests traces, logs, and metrics, groups noisy signals into incidents, and uses AI agents to self-heal software. Local-first observability workspace for OpenTelemetry data with OTLP ingest proxy, ClickHouse-backed queries, and pluggable investigation runtimes. Y Combinator P26 company. MCP server listed (sh.superlog/superlog).

(captured site page body (agents/superlog.md), not a verified repo-code finding)
Superlog collapses the path from production signal to code change. Telemetry flows in via OpenTelemetry or imports from Datadog, Sentry, AWS, GCP, Cloudflare, Vercel, Render, and Railway, where errors are fingerprinted into incidents with severity scoring and impact assessment instead of raw alert noise. For each incident, the Responder agent investigates using codebase context (including AGENTS.md/CLAUDE.md and connected Notion or Linear docs), prepares a resolution PR when its confidence gate passes, and otherwise posts findings to the responsible engineers; a memory system feeds PR comments and review outcomes back into future fixes. All telemetry — logs, traces, metrics, dashboards — is exposed over MCP so external agents can query it. The core is Apache-2.0 and local-first with a hosted cloud tier, and the company (Pulsent Labs) is Y Combinator-backed.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/superlog.md)
