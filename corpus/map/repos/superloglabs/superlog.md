# superloglabs/superlog

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit feffc9fd542a @ 804cab7eff5456ea

## Summary (orientation draft, not independently verified)

Superlog is an open-source, open-core observability workspace for OpenTelemetry data that ingests traces/logs/metrics, groups them into incidents, and runs pluggable agent investigations that can open PRs; docs describe GitHub App and Sentry integrations and an outgoing webhook interface.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The community edition includes a web app and API, an OTLP ingest proxy, worker processes for incident grouping and background jobs, Postgres schema with ClickHouse-backed telemetry queries, and agent runner interfaces. -- evidence: [README.md#L59-L64](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L59-L64)
- design-choices (1 claim(s)):
  - [observation/documented] Onboarding follows an integration-first product principle, favoring connected no-code integrations over manual SDK wiring where possible. -- evidence: [design.md#L21-L23](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/design.md#L21-L23)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local development requires Node.js 20+, pnpm 9+, and Docker; setup uses pnpm install, docker compose up -d, a db migrate command, pnpm dev, and pnpm typecheck for typechecks. -- evidence: [README.md#L72-L74](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L72-L74), [README.md#L100-L102](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L100-L102), [README.md#L84-L88](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L84-L88)
  - [observation/documented] Repository development practice: the web design system's rules live in apps/web/DESIGN.md with a live /design sheet, and contributors are told to read it before adding or restyling UI; a stated rule forbids combining monospace fonts with uppercased text for labels and chrome. -- evidence: [design.md#L3-L6](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/design.md#L3-L6), [design.md#L12-L17](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/design.md#L12-L17)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The default local stack serves a web UI at localhost:5173, an API at localhost:4100, and OTLP intake at localhost:4101. -- evidence: [README.md#L92-L94](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L92-L94)
  - [observation/documented] Outgoing webhooks use exactly two events, incident.created and incident.updated; resolve, reopen, merge, and agent start/finish/fail/await-input are all incident.updated distinguished by a change.kind field. -- evidence: [docs/webhooks.md#L14-L17](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L14-L17), [docs/webhooks.md#L26-L34](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L26-L34), [docs/webhooks.md#L19-L22](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L19-L22)
- memory-state (1 claim(s)):
  - [observation/documented] OAuth and relay credentials are encrypted at rest using AGENT_SECRETS_KEY, which is required alongside STATE_SIGNING_SECRET. -- evidence: [docs/sentry-app-setup.md#L40-L41](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/sentry-app-setup.md#L40-L41)
- orchestration (2 claim(s)):
  - [observation/documented] Agent investigation runtimes are pluggable, with a default 'community' runner that records a local incident summary; webhook agentRun payloads show a runtime value of 'anthropic' and states including queued, running, awaiting_human, blocked_no_github, complete, and failed. -- evidence: [docs/webhooks.md#L197-L213](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L197-L213), [README.md#L59-L64](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L59-L64)
  - [observation/documented] A completed agent investigation can produce a root cause with confidence, estimated impact, severity, an opened pull request with patch and validation status, and Linear tickets, embedded in the agent_completed webhook payload. -- evidence: [docs/webhooks.md#L311-L313](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L311-L313), [docs/webhooks.md#L315-L420](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L315-L420)
- tools-permissions (1 claim(s)):
More evidence: [full detail](superlog.detail.md)

Metadata and full claim list: [full detail](superlog.detail.md)
Human notes ([notes](superlog.notes.md), never overwritten by build)

[Back to map index](../../index.md)
