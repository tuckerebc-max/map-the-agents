---
access: public
aliases: []
claim_ids:
- clm_32c61942c7b7f9ce407e4dcf7e70eaace648d1b5e102959a0cb29f3ac42d4dcc
- clm_be4597f148decf72d8985d6558fd5d6db5587ad04311d5689ae930338e431b85
- clm_d432652a1b14bd4230a5a565b52defd13a0541554e6a6719f0a9c39ee8b42012
maturity: draft
page_id: pg_19b8ed3e7dfe50d0ba7297eb72afb552
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d000dcd323425da69ae15569a54bc444
title: yushui2022/easy-coding-agents/docs/BENCHMARKS.md @ 72fad500ec1e
updated_at: '2026-09-14T03:26:07Z'
---

# yushui2022/easy-coding-agents/docs/BENCHMARKS.md @ 72fad500ec1e

<!-- rcw:begin owner=source:src_d000dcd323425da69ae15569a54bc444 block=evidence -->
- A SWE-bench-format memory probe checks whether issue context, failing-test evidence, task state, and false-DONE prevention survive memory reconstruction; it explicitly does not measure patch correctness, which requires the official SWE-bench Docker harness. [@claim:clm_32c61942c7b7f9ce407e4dcf7e70eaace648d1b5e102959a0cb29f3ac42d4dcc]
- A benchmark harness compares six memory baselines (no_memory, summary, long-context, keyword FTS, vector RAG, evidence-gated) on LongMemEval-S, LoCoMo10, and BEAM-lite, scoring retrieval/term recall, evidence source coverage, tokens, latency, and false-fact rate after a context wipe. [@claim:clm_be4597f148decf72d8985d6558fd5d6db5587ad04311d5689ae930338e431b85]
- The README reports evidence-gated memory at 0.40 retrieval recall and 0.87 evidence coverage on LongMemEval-S (100 cases), and the docs note LoCoMo10 answer-term recall remains low and is described as a current weakness. [@claim:clm_d432652a1b14bd4230a5a565b52defd13a0541554e6a6719f0a9c39ee8b42012]
<!-- rcw:end owner=source:src_d000dcd323425da69ae15569a54bc444 block=evidence -->

## Researcher notes

