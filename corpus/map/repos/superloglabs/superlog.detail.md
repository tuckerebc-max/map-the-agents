# superloglabs/superlog -- full detail

[Back to orientation](superlog.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/superloglabs/superlog/feffc9fd542a75a865f94a80c72214368b690a55/804cab7eff5456ea.json](../../../wiki/dossiers/superloglabs/superlog/feffc9fd542a75a865f94a80c72214368b690a55/804cab7eff5456ea.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The community edition includes a web app and API, an OTLP ingest proxy, worker processes for incident grouping and background jobs, Postgres schema with ClickHouse-backed telemetry queries, and agent runner interfaces. -- evidence: [README.md#L59-L64](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L59-L64) (`clm_1a18d1e8e262df30c9e9c391a06522900cc72d0817a74e85d5ed06dc43fbfe0b`)

## design-choices (1 claim(s))

- [observation/documented] Onboarding follows an integration-first product principle, favoring connected no-code integrations over manual SDK wiring where possible. -- evidence: [design.md#L21-L23](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/design.md#L21-L23) (`clm_cdb6ae71d9db1aab091d25a5de920b8a3f5c9f0186101fdbdbcdb7b63b4ac27a`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local development requires Node.js 20+, pnpm 9+, and Docker; setup uses pnpm install, docker compose up -d, a db migrate command, pnpm dev, and pnpm typecheck for typechecks. -- evidence: [README.md#L72-L74](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L72-L74), [README.md#L100-L102](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L100-L102), [README.md#L84-L88](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L84-L88) (`clm_de72b291019f760760fd1e33cd7c2e3e5801f008433abf1f8f91f42af1e34b0d`)
- [observation/documented] Repository development practice: the web design system's rules live in apps/web/DESIGN.md with a live /design sheet, and contributors are told to read it before adding or restyling UI; a stated rule forbids combining monospace fonts with uppercased text for labels and chrome. -- evidence: [design.md#L3-L6](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/design.md#L3-L6), [design.md#L12-L17](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/design.md#L12-L17) (`clm_a5c90096f10653ec68db631bcf80dc27fc5a8cb8b62f3bb09864f9b6bfa40f62`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The default local stack serves a web UI at localhost:5173, an API at localhost:4100, and OTLP intake at localhost:4101. -- evidence: [README.md#L92-L94](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L92-L94) (`clm_12f97141da6ede68b624a6aaf9be9a2913c04222020297a459b2d9d6c1f13971`)
- [observation/documented] Outgoing webhooks use exactly two events, incident.created and incident.updated; resolve, reopen, merge, and agent start/finish/fail/await-input are all incident.updated distinguished by a change.kind field. -- evidence: [docs/webhooks.md#L14-L17](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L14-L17), [docs/webhooks.md#L26-L34](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L26-L34), [docs/webhooks.md#L19-L22](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L19-L22) (`clm_3d70a2711a3754162d35e5e3dbea9673fa8b3cc6361f26cde522255b6fdbe3b3`)
- [observation/documented] Webhook deliveries carry a Stripe-style Superlog-Signature header (t=<unix-ts>,v1=<hex>) where the hex is HMAC-SHA256 over '<timestamp>.<raw body>'; verification must use the raw body before JSON parsing. -- evidence: [docs/webhooks.md#L87-L87](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L87-L87), [docs/webhooks.md#L113-L114](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L113-L114), [docs/webhooks.md#L83-L85](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L83-L85), [docs/webhooks.md#L81-L81](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L81-L81) (`clm_fd6e4cbfe8bb6700351129167ddde7d053860c1add0dc82bb9d76e0d125fc569`)
- [observation/documented] Webhook delivery is a JSON POST with a 10-second timeout; failures are retried with backoff up to 8 attempts (~8h) before being marked failed, and retries reuse a stable Superlog-Delivery UUID as an idempotency key. -- evidence: [docs/webhooks.md#L118-L123](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L118-L123), [docs/webhooks.md#L57-L77](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L57-L77) (`clm_86e231bb57bc19427e07677cd6dc9f5a0346474f1398cc99dfc7e1c43b6d1fef`)
- [observation/documented] The agent integrates with GitHub via a GitHub App using two OAuth callback URLs on the API: /github/install/callback for the connect/install flow and /github/author/callback for a commit-author OAuth flow. -- evidence: [docs/github-app-setup.md#L3-L5](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/github-app-setup.md#L3-L5), [docs/github-app-setup.md#L63-L66](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/github-app-setup.md#L63-L66) (`clm_4e2eca492102310199b71e3bedb3655e5a502eef81f51c34cbf0aeb59c959348`)

## memory-state (1 claim(s))

- [observation/documented] OAuth and relay credentials are encrypted at rest using AGENT_SECRETS_KEY, which is required alongside STATE_SIGNING_SECRET. -- evidence: [docs/sentry-app-setup.md#L40-L41](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/sentry-app-setup.md#L40-L41) (`clm_ac3b2fb5577fb10dcceda5ee4be64aafea22eceff5e9fe177bd26e203b263677`)

## orchestration (2 claim(s))

- [observation/documented] Agent investigation runtimes are pluggable, with a default 'community' runner that records a local incident summary; webhook agentRun payloads show a runtime value of 'anthropic' and states including queued, running, awaiting_human, blocked_no_github, complete, and failed. -- evidence: [docs/webhooks.md#L197-L213](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L197-L213), [README.md#L59-L64](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L59-L64) (`clm_4e24f56c08597b4e5bf19e6f1e352de6b37e6807b8d4e52986189f79bdb42944`)
- [observation/documented] A completed agent investigation can produce a root cause with confidence, estimated impact, severity, an opened pull request with patch and validation status, and Linear tickets, embedded in the agent_completed webhook payload. -- evidence: [docs/webhooks.md#L311-L313](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L311-L313), [docs/webhooks.md#L315-L420](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/webhooks.md#L315-L420) (`clm_189ea82591a4c70aa5ac4d2bb98dd27bc07f2d1cbe8232699c948eb48ea40743`)

## tools-permissions (1 claim(s))

- [observation/documented] The GitHub App is configured with minimum repository permissions: Contents read/write to read files and push fix branches, Pull requests read/write to open/update/merge PRs, Issues read/write for comments, and read-only Metadata; no account or organization permissions are required. -- evidence: [docs/github-app-setup.md#L88-L90](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/github-app-setup.md#L88-L90), [docs/github-app-setup.md#L81-L86](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/github-app-setup.md#L81-L86) (`clm_1c7f0af6ae4b2123933e56ea49dacca108233d152a64b8d14229a275dbb443b6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The Sentry connector supports only Sentry Cloud via a public Sentry App; self-hosted Sentry is not supported. -- evidence: [docs/sentry-app-setup.md#L8-L8](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/sentry-app-setup.md#L8-L8), [docs/sentry-app-setup.md#L3-L6](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/docs/sentry-app-setup.md#L3-L6) (`clm_7ea4aebc839e605cdb80e566306a73e08549f51043c5c433af46fe47eb9e0344`)

## relevance (1 claim(s))

- [observation/documented] Superlog targets teams debugging production systems: it is an open-core observability workspace for OpenTelemetry data that ingests traces, logs, and metrics and groups noisy signals into incidents. -- evidence: [README.md#L38-L39](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L38-L39), [README.md#L53-L55](https://github.com/superloglabs/superlog/blob/feffc9fd542a75a865f94a80c72214368b690a55/README.md#L53-L55) (`clm_171a7fda0d77784346eba80f99b269085d46a579a3743ebf226f9d4f655375e8`)

