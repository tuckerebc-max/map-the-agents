---
access: public
aliases: []
claim_ids:
- clm_0cc22999768ecbfd8096dc73e7e316f6c60de8631a3ec21ee0dbb0ecbe600249
- clm_2486e910279353cd73e356bc0171c3705ee659602ef47d8ae019c342d30d13f3
- clm_4e50f0c47ca654055650cbfbfb6f58e4f13b932b748d9e67d8a5b48f54567291
- clm_6ffcba04acd6d33c02fac2bd5540bc52358c2e38e0f882d25de54e7cb66fdb73
- clm_70f66d52fa98c4f8eff66aabc108ce0e3ff51d225ef08a83835a66b2df07e295
- clm_76bea33e5d443d9237b0b1c0c9aadde6be76fa7d5e167da3c769e71aa5f50d64
- clm_9307c05ca67ae3a6af1a4f98e3359c9c422b671b7fb61239a5237d2d9afde464
- clm_d67ab1f1f4238b0e7dce67e22b04b478749e1ebc935bb1b938862a2fee248ba0
maturity: draft
page_id: pg_b8eec3b86cb45322abee6f64b68d86de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_658fc31717905270958174ce96a3334f
title: husu/loom/README.en.md @ 905416f838bf
updated_at: '2026-09-14T03:58:08Z'
---

# husu/loom/README.en.md @ 905416f838bf

<!-- rcw:begin owner=source:src_658fc31717905270958174ce96a3334f block=evidence -->
- Loom uses a custom JSON Schema format (draft-07) for API docs, with module title/description, an endpoints array carrying path, HTTP method, optional request schema (headers, params, query, body), and responses keyed by status code. [@claim:clm_0cc22999768ecbfd8096dc73e7e316f6c60de8631a3ec21ee0dbb0ecbe600249]
- Chat input history is persisted globally at ~/.loom/history.jsonl (capped at 100 entries) and is navigable across sessions with arrow keys; configuration lives at ~/.loom/config.json while docs/ stays per-project. [@claim:clm_2486e910279353cd73e356bc0171c3705ee659602ef47d8ae019c342d30d13f3]
- The documented project structure includes an agents system with tool calling and conversation memory, an LLM client for DeepSeek/OpenAI, agent tools for schema generation/validation and file operations, an Ink-based TUI, a Fastify web viewer with React SPA frontend, and a mock server with dynamic route registration. [@claim:clm_4e50f0c47ca654055650cbfbfb6f58e4f13b932b748d9e67d8a5b48f54567291]
- The /scan feature caches LLM output keyed by file content hash in <outDir>/.loom-scan-cache.json, skipping unchanged files on incremental rescans; cache invalidation is driven by source-hash plus per-entry shape checks rather than a global version wipe. [@claim:clm_6ffcba04acd6d33c02fac2bd5540bc52358c2e38e0f882d25de54e7cb66fdb73]
- The mock and web-viewer services can be started, stopped, and restarted from within the TUI via /mock and /view commands, or run together on one port via `loom serve`. [@claim:clm_70f66d52fa98c4f8eff66aabc108ce0e3ff51d225ef08a83835a66b2df07e295]
- Repository development practice: contributors are asked to fork, create a feature branch, commit, push, and open a PR; development guidelines say to use strict-mode TypeScript, follow existing code style, add tests for new functionality, and update documentation. [@claim:clm_76bea33e5d443d9237b0b1c0c9aadde6be76fa7d5e167da3c769e71aa5f50d64]
- Reusable entity schemas live in docs/entities/*.entity.schema.json and are referenced from endpoint schemas via an x-entity-ref keyword, in either string form or object form with an entity name and a pick list of properties. [@claim:clm_9307c05ca67ae3a6af1a4f98e3359c9c422b671b7fb61239a5237d2d9afde464]
- The project requires Node.js >= 18 and a DeepSeek API key, and credits Fastify, React, mock-json-schema, and Ink as key libraries; the mock server reportedly uses mock-json-schema for data generation. [@claim:clm_d67ab1f1f4238b0e7dce67e22b04b478749e1ebc935bb1b938862a2fee248ba0]
<!-- rcw:end owner=source:src_658fc31717905270958174ce96a3334f block=evidence -->

## Researcher notes

