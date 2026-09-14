---
access: public
aliases: []
claim_ids:
- clm_0cc22999768ecbfd8096dc73e7e316f6c60de8631a3ec21ee0dbb0ecbe600249
- clm_2486e910279353cd73e356bc0171c3705ee659602ef47d8ae019c342d30d13f3
- clm_6ffcba04acd6d33c02fac2bd5540bc52358c2e38e0f882d25de54e7cb66fdb73
- clm_70706102a347bfa0e4ec04f4243998cfaeb8d7ce272a1c4c9e448e74fe85a1b6
- clm_70f66d52fa98c4f8eff66aabc108ce0e3ff51d225ef08a83835a66b2df07e295
- clm_9307c05ca67ae3a6af1a4f98e3359c9c422b671b7fb61239a5237d2d9afde464
- clm_d67ab1f1f4238b0e7dce67e22b04b478749e1ebc935bb1b938862a2fee248ba0
- clm_ea66851a2d093998e6d8f2191322194f1958b586b62b98cb03d1ac872791ffc2
maturity: draft
page_id: pg_233873756c3853cc9708b3b8d1beda49
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f2744588dd185e139217bea443f5c02e
title: husu/loom/README.md @ 905416f838bf
updated_at: '2026-09-14T03:58:08Z'
---

# husu/loom/README.md @ 905416f838bf

<!-- rcw:begin owner=source:src_f2744588dd185e139217bea443f5c02e block=evidence -->
- Loom uses a custom JSON Schema format (draft-07) for API docs, with module title/description, an endpoints array carrying path, HTTP method, optional request schema (headers, params, query, body), and responses keyed by status code. [@claim:clm_0cc22999768ecbfd8096dc73e7e316f6c60de8631a3ec21ee0dbb0ecbe600249]
- Chat input history is persisted globally at ~/.loom/history.jsonl (capped at 100 entries) and is navigable across sessions with arrow keys; configuration lives at ~/.loom/config.json while docs/ stays per-project. [@claim:clm_2486e910279353cd73e356bc0171c3705ee659602ef47d8ae019c342d30d13f3]
- The /scan feature caches LLM output keyed by file content hash in <outDir>/.loom-scan-cache.json, skipping unchanged files on incremental rescans; cache invalidation is driven by source-hash plus per-entry shape checks rather than a global version wipe. [@claim:clm_6ffcba04acd6d33c02fac2bd5540bc52358c2e38e0f882d25de54e7cb66fdb73]
- Inside `loom chat`, slash commands include /help, /reset, /list, /mock, /view, /scan <dir> (with resume/reset), /abort, and /exit; Tab autocompletes commands and arrow keys navigate persisted history. [@claim:clm_70706102a347bfa0e4ec04f4243998cfaeb8d7ce272a1c4c9e448e74fe85a1b6]
- The mock and web-viewer services can be started, stopped, and restarted from within the TUI via /mock and /view commands, or run together on one port via `loom serve`. [@claim:clm_70f66d52fa98c4f8eff66aabc108ce0e3ff51d225ef08a83835a66b2df07e295]
- Reusable entity schemas live in docs/entities/*.entity.schema.json and are referenced from endpoint schemas via an x-entity-ref keyword, in either string form or object form with an entity name and a pick list of properties. [@claim:clm_9307c05ca67ae3a6af1a4f98e3359c9c422b671b7fb61239a5237d2d9afde464]
- The project requires Node.js >= 18 and a DeepSeek API key, and credits Fastify, React, mock-json-schema, and Ink as key libraries; the mock server reportedly uses mock-json-schema for data generation. [@claim:clm_d67ab1f1f4238b0e7dce67e22b04b478749e1ebc935bb1b938862a2fee248ba0]
- The combined `loom serve` mode serves the web viewer at /, documentation APIs at /api/docs, /api/schemas, /api/entities, and mock routes under /mock/... on one port. [@claim:clm_ea66851a2d093998e6d8f2191322194f1958b586b62b98cb03d1ac872791ffc2]
<!-- rcw:end owner=source:src_f2744588dd185e139217bea443f5c02e block=evidence -->

## Researcher notes

