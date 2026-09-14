---
access: public
aliases: []
claim_ids:
- clm_12f97141da6ede68b624a6aaf9be9a2913c04222020297a459b2d9d6c1f13971
- clm_171a7fda0d77784346eba80f99b269085d46a579a3743ebf226f9d4f655375e8
- clm_1a18d1e8e262df30c9e9c391a06522900cc72d0817a74e85d5ed06dc43fbfe0b
- clm_4e24f56c08597b4e5bf19e6f1e352de6b37e6807b8d4e52986189f79bdb42944
- clm_de72b291019f760760fd1e33cd7c2e3e5801f008433abf1f8f91f42af1e34b0d
maturity: draft
page_id: pg_036263aaba6f5e4f98af63015b917744
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d7843c2227ba54a695830c610cd93521
title: superloglabs/superlog/README.md @ feffc9fd542a
updated_at: '2026-09-14T03:17:02Z'
---

# superloglabs/superlog/README.md @ feffc9fd542a

<!-- rcw:begin owner=source:src_d7843c2227ba54a695830c610cd93521 block=evidence -->
- The default local stack serves a web UI at localhost:5173, an API at localhost:4100, and OTLP intake at localhost:4101. [@claim:clm_12f97141da6ede68b624a6aaf9be9a2913c04222020297a459b2d9d6c1f13971]
- Superlog targets teams debugging production systems: it is an open-core observability workspace for OpenTelemetry data that ingests traces, logs, and metrics and groups noisy signals into incidents. [@claim:clm_171a7fda0d77784346eba80f99b269085d46a579a3743ebf226f9d4f655375e8]
- The community edition includes a web app and API, an OTLP ingest proxy, worker processes for incident grouping and background jobs, Postgres schema with ClickHouse-backed telemetry queries, and agent runner interfaces. [@claim:clm_1a18d1e8e262df30c9e9c391a06522900cc72d0817a74e85d5ed06dc43fbfe0b]
- Agent investigation runtimes are pluggable, with a default 'community' runner that records a local incident summary; webhook agentRun payloads show a runtime value of 'anthropic' and states including queued, running, awaiting_human, blocked_no_github, complete, and failed. [@claim:clm_4e24f56c08597b4e5bf19e6f1e352de6b37e6807b8d4e52986189f79bdb42944]
- Repository development practice: local development requires Node.js 20+, pnpm 9+, and Docker; setup uses pnpm install, docker compose up -d, a db migrate command, pnpm dev, and pnpm typecheck for typechecks. [@claim:clm_de72b291019f760760fd1e33cd7c2e3e5801f008433abf1f8f91f42af1e34b0d]
<!-- rcw:end owner=source:src_d7843c2227ba54a695830c610cd93521 block=evidence -->

## Researcher notes

