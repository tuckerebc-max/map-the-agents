---
access: public
aliases: []
claim_ids:
- clm_525758f066a3868907d88ac5d23d4fc4ce4477bbc18dbd70acfdf856a9c23095
- clm_b70b2702076dc089762bdc197e643d4e093417d6d2ed28ad5e42295b64c90b97
- clm_c4d3ec1a1eff10baba78763332f400021c9f4b3d26516b39a80d40ffed4cf37f
- clm_cad58bb0f79f261bb375a9cf2b3748f801aa7ed68c4451b0a78201a56c2e41a1
- clm_d5b7cab0ede4e71c693091319690d6b5c4a003541a2e1dd4a0d40724360426a9
- clm_eddbab0b459a32ee1bbd15d57e34d03969dc32e68f2862158c49eb5082a139de
maturity: draft
page_id: pg_b5e63390d775590ba8dad88c58db1ab8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0ef6494d1cdb550fb70fc65f0a6782ba
title: qcri/codebadger/docs/architecture.md @ 857adcabe386
updated_at: '2026-09-14T04:17:42Z'
---

# qcri/codebadger/docs/architecture.md @ 857adcabe386

<!-- rcw:begin owner=source:src_0ef6494d1cdb550fb70fc65f0a6782ba block=evidence -->
- Joern runs out-of-process in Docker; a Python FastMCP server orchestrates CPG generation, a memory-aware query-server pool, caching, and a durable job queue. [@claim:clm_525758f066a3868907d88ac5d23d4fc4ce4477bbc18dbd70acfdf856a9c23095]
- Postgres stores catalog, tool cache, findings, and the durable job queue; Redis holds cross-process query locks and the pool ledger, and the server refuses to boot if either is unreachable. [@claim:clm_b70b2702076dc089762bdc197e643d4e093417d6d2ed28ad5e42295b64c90b97]
- CPGs are disk-cached by content hash; sleeping servers cost no RAM and wake by re-importing the cached .bin on the next query. [@claim:clm_c4d3ec1a1eff10baba78763332f400021c9f4b3d26516b39a80d40ffed4cf37f]
- A GET /health endpoint probes joern, postgres, redis, docker, and cpg_queue concurrently, returning up/partial/down with HTTP 200/503 for orchestrators. [@claim:clm_cad58bb0f79f261bb375a9cf2b3748f801aa7ed68c4451b0a78201a56c2e41a1]
- Admission is governed by a memory budget rather than a fixed server count: heap tiers derive from CPG size, with LRU eviction, an RSS backstop, and an idle-TTL reaper (default 600s). [@claim:clm_d5b7cab0ede4e71c693091319690d6b5c4a003541a2e1dd4a0d40724360426a9]
- Repository development practice: docs/contributing.md covers dev setup, tests, and guidelines, and tests/ contains unit and integration suites per the repository layout. [@claim:clm_eddbab0b459a32ee1bbd15d57e34d03969dc32e68f2862158c49eb5082a139de]
<!-- rcw:end owner=source:src_0ef6494d1cdb550fb70fc65f0a6782ba block=evidence -->

## Researcher notes

