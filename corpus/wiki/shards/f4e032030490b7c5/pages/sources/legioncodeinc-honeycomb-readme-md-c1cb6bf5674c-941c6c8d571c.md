---
access: public
aliases: []
claim_ids:
- clm_06c3553dcda7bab8ab137a0a034ca23fff1ac0c2d8d332b5e4e83eb12814956d
- clm_0d7a97f48fa79eb9b9198c73c29e71a1566bf737b6d503343957e0d4da72343b
- clm_165082757878f530c9262761bd432563d42a678a9e9014567c4753cfb4044f67
- clm_41fe9389a72614698ee314e99f5fd384a4a27a3cdfeaacd4355b1a147db58c2b
- clm_7267a6371ecfcd5c44006fff118690fb1183267cec9a7555503c19b39276a385
- clm_8bd600f44841d38325e762b3cfa68912a8e8c05c7a2ad198ece46daf02b4352f
- clm_9442bbe46aabaab82ff85d5f9afadf19f3279ed83cd3695cf3021211ca2c283d
- clm_9a3b259b09a109931c694e197051a1682108e1f4395050d7002c38e3d9436efe
- clm_9a3b97bde017f7ae99b837e55ae76336d9712899fedfda62cee4c69360cc7dd5
- clm_a8500666d1f2648bdb760f6350d8302a160c84114a33f6156cb0b68800aa0df1
- clm_ddf6cb96e3ce82a516ff68742ab020fb12e34502691ab1ada66df2a5cfafcbfb
- clm_e9c6db1674f7e632776380adbc6cd349d00b47ec659b703616330b430e14a84e
- clm_fc6f70f475ec8d1675162d04a2fce9bc9c70b2b0e2c5c68439dbb0613555e3cb
maturity: draft
page_id: pg_b18067aeab165b24bb52941c6c8d571c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_36ef18a78d73569682489ee5fe8db017
title: legioncodeinc/honeycomb/README.md @ c1cb6bf5674c
updated_at: '2026-09-14T04:05:46Z'
---

# legioncodeinc/honeycomb/README.md @ c1cb6bf5674c

<!-- rcw:begin owner=source:src_36ef18a78d73569682489ee5fe8db017 block=evidence -->
- The distillation pipeline (background summarization and graph extraction) is disabled by default to avoid surprise model spend, and running Honeycomb alongside Hivemind is unsupported, though the dashboard offers migration. [@claim:clm_06c3553dcda7bab8ab137a0a034ca23fff1ac0c2d8d332b5e4e83eb12814956d]
- Besides the CLI, Honeycomb is reachable via the Hive portal dashboard at 127.0.0.1:3853, a bundled MCP server exposing read/resolve and search/mine tools, and a TypeScript SDK with /react, /vercel, and /openai subpath entries. [@claim:clm_0d7a97f48fa79eb9b9198c73c29e71a1566bf737b6d503343957e0d4da72343b]
- The product is a long-lived local daemon plus thin clients (hooks, CLI, MCP, SDK); the daemon is the sole process talking to storage, reached over loopback HTTP on 127.0.0.1:3850. [@claim:clm_165082757878f530c9262761bd432563d42a678a9e9014567c4753cfb4044f67]
- Honeycomb provides shared, persistent memory for AI coding agents: what one harness learns is recallable by others across sessions, tools, devices, and teammates. [@claim:clm_41fe9389a72614698ee314e99f5fd384a4a27a3cdfeaacd4355b1a147db58c2b]
- A unified honeycomb CLI exposes verbs such as setup, status, login, start/stop, remember, recall, sessions, and uninstall; baseline operational verbs accept --json with exit codes 2/1/0 for malformed usage, runtime failure, and success. [@claim:clm_7267a6371ecfcd5c44006fff118690fb1183267cec9a7555503c19b39276a385]
- Storage can be self-hosted against Activeloop's pg_deeplake Postgres extension, pointed at via honeycomb login --endpoint with a postgres:// or https:// URL, without an Activeloop account. [@claim:clm_8bd600f44841d38325e762b3cfa68912a8e8c05c7a2ad198ece46daf02b4352f]
- Repository development practice: npm run ci is the quality gate every change must pass, combining typecheck, duplication detection (jscpd), vitest tests, and a SQL-safety audit. [@claim:clm_9442bbe46aabaab82ff85d5f9afadf19f3279ed83cd3695cf3021211ca2c283d]
- The daemon binds loopback only (single machine); cross-device and cross-user sharing happen through Deeplake's org/workspace scope rather than a remote daemon bind. [@claim:clm_9a3b259b09a109931c694e197051a1682108e1f4395050d7002c38e3d9436efe]
- Honeycomb is built on Activeloop Deeplake (extending the open-source Hivemind agent-memory project), using BM25 lexical plus 768-dim nomic-embed-text-v1.5 semantic search fused by Reciprocal Rank Fusion. [@claim:clm_9a3b97bde017f7ae99b837e55ae76336d9712899fedfda62cee4c69360cc7dd5]
- The README reports a measured recall@5 of approximately 0.72-0.78 for the hybrid lexical-plus-semantic retrieval, and describes a smoke:golden-path script run against live Deeplake credentials. [@claim:clm_a8500666d1f2648bdb760f6350d8302a160c84114a33f6156cb0b68800aa0df1]
- At session start a bounded index of roughly 300-800 tokens of relevant keys is pushed once, with deeper detail pulled on demand rather than injected per turn. [@claim:clm_ddf6cb96e3ce82a516ff68742ab020fb12e34502691ab1ada66df2a5cfafcbfb]
- Embeddings are opt-in: recall defaults to lexical BM25, and enabling the local embedding runtime (~600 MB fetched on first warmup) adds semantic recall; recall silently falls back and never errors when embeddings are unavailable. [@claim:clm_e9c6db1674f7e632776380adbc6cd349d00b47ec659b703616330b430e14a84e]
- Memories exist at three tiers: a one-line key, a distilled summary carrying the semantic embedding, and the full raw session dialogue; resolution is a deterministic pointer walk across three Deeplake tables. [@claim:clm_fc6f70f475ec8d1675162d04a2fce9bc9c70b2b0e2c5c68439dbb0613555e3cb]
<!-- rcw:end owner=source:src_36ef18a78d73569682489ee5fe8db017 block=evidence -->

## Researcher notes

