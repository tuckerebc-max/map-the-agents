---
access: public
aliases: []
claim_ids:
- clm_c3e0f3cecb7c769c587ee060ea186b6ee29890340a1e1adf613b58012535a04a
- clm_c80934970d1b411abe7318837ce23bd19b65bd4e2444b9ecc746e350818a20e4
- clm_d70d0317c3cd9762ab4916376e83f6bae00080a6381467626055aedb2db5ffdc
maturity: draft
page_id: pg_57e4d55ddcfe58b8aecee2b23573b5ca
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c9d358687d7e5041944a558ebba23e23
title: Quinnod345/context-engine/docs/architecture.md @ ff40183c8225
updated_at: '2026-09-14T04:17:15Z'
---

# Quinnod345/context-engine/docs/architecture.md @ ff40183c8225

<!-- rcw:begin owner=source:src_c9d358687d7e5041944a558ebba23e23 block=evidence -->
- Query ranking multiplies cosine similarity by relevance and an exponential half-life decay factor 0.5^(age/halfLife), with a configurable decayHours defaulting to 24 hours. [@claim:clm_c3e0f3cecb7c769c587ee060ea186b6ee29890340a1e1adf613b58012535a04a]
- Storage adapters include SQLiteStorage built on better-sqlite3 with brute-force JS cosine search suited to roughly 10,000 events, and PostgresStorage using pgvector's cosine-distance operator for production scale. [@claim:clm_c80934970d1b411abe7318837ce23bd19b65bd4e2444b9ecc746e350818a20e4]
- Ingest deduplicates events whose cosine similarity exceeds a configurable threshold (default 0.95) within a time window (default 60s), merging timestamps, boosting relevance, and tracking a _mergeCount field. [@claim:clm_d70d0317c3cd9762ab4916376e83f6bae00080a6381467626055aedb2db5ffdc]
<!-- rcw:end owner=source:src_c9d358687d7e5041944a558ebba23e23 block=evidence -->

## Researcher notes

