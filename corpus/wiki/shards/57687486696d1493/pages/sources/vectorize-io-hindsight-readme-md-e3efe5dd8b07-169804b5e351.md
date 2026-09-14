---
access: public
aliases: []
claim_ids:
- clm_21ed2cba4593d075dddb8757589e83cf5472d4450719b58abe6a52ffb5469cbc
- clm_36dadd9593f754dc35d89903a42ebdca38233f6403be6623675f8a78b3733a9f
- clm_3e4cbb355de874596d82c4ee30bd04d4d005fce008658155d2c281e715401fe4
- clm_42688d4ec4e4156ef475f01f6d4a1056b5c8d4b1d7eb03f9115afba11122d178
- clm_54fd7d6a0a9e0a4a96eb6cdc9e2a6626bc9bd5c82d3cb50bdc942b66f828f9bd
- clm_6ce50761c934b014f7de1da4bd3a3a4a0fdadf31cdd8b8014f266b6b8b755142
- clm_9241421a8ecd39b18cccf70671b5bf207ba19ef11c9e632d7b6f8d81b0bc11cc
- clm_956dc963185b967a803a9338a04721e0cf3db04aa0cb56634804fd7112d23a71
- clm_a179d096f2edb1040ba27f1b79370b451801209b47d5063606c74270db1984c2
- clm_b4f175733345b07bb0447e33cb7be1251d7d8d68fdb30f6abe0106a7fb5f6fbf
- clm_c3bec46a6430ab1fa6e0f1d320271f4f4f89a78f6fcaeced58161fdb402717e0
- clm_cc9483d8ef4e10025356da709297133ee8d402e71569d0abd6cc43a78f4cc2bd
- clm_e153d7f87219fcd4417011ce448c344ff1ae314dc8f0d528b554c214eaa88847
- clm_fd3d04ced8ef569369beb4a7b7ab4a76ec289c92df2bc034036633c23f4911a5
maturity: draft
page_id: pg_720ff911fed352b893b0169804b5e351
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bb4f92f02d1c5bafaf835c92f74d417d
title: vectorize-io/hindsight/README.md @ e3efe5dd8b07
updated_at: '2026-09-14T04:30:35Z'
---

# vectorize-io/hindsight/README.md @ e3efe5dd8b07

<!-- rcw:begin owner=source:src_bb4f92f02d1c5bafaf835c92f74d417d block=evidence -->
- An opt-in per-bank Memory Defense policy scans retains against 45 secret/PII patterns, redacting or blocking matches before storage. [@claim:clm_21ed2cba4593d075dddb8757589e83cf5472d4450719b58abe6a52ffb5469cbc]
- Recall runs four retrieval strategies in parallel (semantic vector, BM25 keyword, graph, temporal) and merges results with reciprocal rank fusion plus cross-encoder reranking. [@claim:clm_36dadd9593f754dc35d89903a42ebdca38233f6403be6623675f8a78b3733a9f]
- A coding-agents package builds a per-repo memory bank from git history and past sessions, injected into supported CLI coding agents with automatic ingestion. [@claim:clm_3e4cbb355de874596d82c4ee30bd04d4d005fce008658155d2c281e715401fe4]
- Mental models are standing answers to defined questions that are rewritten in the background and readable as a plain database read without retrieval or an LLM call. [@claim:clm_42688d4ec4e4156ef475f01f6d4a1056b5c8d4b1d7eb03f9115afba11122d178]
- Hindsight is described as an agent memory system aimed at agents that learn over time, not merely recall conversation history. [@claim:clm_54fd7d6a0a9e0a4a96eb6cdc9e2a6626bc9bd5c82d3cb50bdc942b66f828f9bd]
- Storage uses PostgreSQL with pgvector, or Oracle AI Database 23ai with claimed full feature parity for enterprise deployments. [@claim:clm_6ce50761c934b014f7de1da4bd3a3a4a0fdadf31cdd8b8014f266b6b8b755142]
- Every server ships a built-in MCP endpoint, one per bank, at /mcp/{bank_id}/, exposing retain, recall and reflect as tools to any MCP client. [@claim:clm_9241421a8ecd39b18cccf70671b5bf207ba19ef11c9e632d7b6f8d81b0bc11cc]
- Hindsight targets conversational and autonomous agents needing personalization and learning, and may be overkill for simple n8n-style workflows. [@claim:clm_956dc963185b967a803a9338a04721e0cf3db04aa0cb56634804fd7112d23a71]
- Banks carry disposition traits such as skepticism, literalism and empathy that shape how reflect reasons, and strict isolation prevents cross-bank leakage. [@claim:clm_a179d096f2edb1040ba27f1b79370b451801209b47d5063606c74270db1984c2]
- Background consolidation builds observations that keep supporting evidence with exact quotes and a proof count, and are refined rather than overwritten as new evidence arrives. [@claim:clm_b4f175733345b07bb0447e33cb7be1251d7d8d68fdb30f6abe0106a7fb5f6fbf]
- The server supports 25+ LLM providers via HINDSIGHT_API_LLM_PROVIDER, including hosted, local (ollama, lmstudio, llamacpp), OpenAI-compatible endpoints, and subscription-based options. [@claim:clm_c3bec46a6430ab1fa6e0f1d320271f4f4f89a78f6fcaeced58161fdb402717e0]
- The product exposes three core operations: retain (store), recall (search), and reflect (deeper analysis), callable via Python, Node.js, Go, CLI, and REST clients. [@claim:clm_cc9483d8ef4e10025356da709297133ee8d402e71569d0abd6cc43a78f4cc2bd]
- The README reports state-of-the-art LongMemEval benchmark results, with live per-model accuracy, latency and cost published on a benchmarks site and independent reproduction claimed by Virginia Tech and The Washington Post. [@claim:clm_e153d7f87219fcd4417011ce448c344ff1ae314dc8f0d528b554c214eaa88847]
- Memories are organized into four types: world facts, experiences, observations, and mental models, stored in isolated banks. [@claim:clm_fd3d04ced8ef569369beb4a7b7ab4a76ec289c92df2bc034036633c23f4911a5]
<!-- rcw:end owner=source:src_bb4f92f02d1c5bafaf835c92f74d417d block=evidence -->

## Researcher notes

