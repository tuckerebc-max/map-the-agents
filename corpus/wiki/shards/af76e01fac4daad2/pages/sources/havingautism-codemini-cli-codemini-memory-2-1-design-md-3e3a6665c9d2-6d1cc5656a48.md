---
access: public
aliases: []
claim_ids:
- clm_588a7c859133f273b0cff80a2f3b1b70077d50aa75b2336ddd8293c4e71296c6
- clm_63567129734f146b1d51efb17811a6838506f397b13556fbf09fe84b80287d2f
- clm_67591fa88eca82da71e254d7e0fb5bb48276b96048f06b2f4cf036026b608808
- clm_76471ab999d41388d8657f3b86b3fb872196e9360c2388a86c66024f301d69c8
- clm_7c7be0fa0a0792cb48537eeb61fdb4224e7ac1b347035b9a1b4aa002baf387c9
- clm_7fe49ddae134949dea32796528999879ef0ec76ae331200b8be06432dbb0f21f
- clm_80a9555406e787020f7d5065dd8b3a09326de0c0abb2a297f3e31a804fe99ae3
- clm_981fd41c2f871b8eeca1d771e0087c16c838d49219bab39635015a7dcfd6921c
- clm_b6f242e1b03985c0a39ef933636482c724b96dd542bc2462c075b9f52430973d
- clm_e9238398b75f82ae956eb6a9d096302ea36cc6e1699b19aa0bf939d3d08031f6
- clm_ede699310232f10c3cb894f289da582653ff1ef7bfee6ecb1efb7e2d44a732ef
- clm_fd80a5674ec93833de497ea6bd01db01080cacdeb4f0bf6c10c9741159f6aace
maturity: draft
page_id: pg_97ecab269ddf588ba2d56d1cc5656a48
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3fbdf62866815843a69214e39c9f8001
title: havingautism/Codemini-CLI/codemini-memory-2.1-design.md @ 3e3a6665c9d2
updated_at: '2026-09-14T02:03:15Z'
---

# havingautism/Codemini-CLI/codemini-memory-2.1-design.md @ 3e3a6665c9d2

<!-- rcw:begin owner=source:src_3fbdf62866815843a69214e39c9f8001 block=evidence -->
- The design mandates graceful degradation so memory is never a single point of failure: FTS failure leads to rebuild then substring fallback, writeback failure is skipped, and a disabled memory subsystem leaves the normal agent loop intact. [@claim:clm_588a7c859133f273b0cff80a2f3b1b70077d50aa75b2336ddd8293c4e71296c6]
- Chinese-text retrieval is handled by pre-segmenting with Node's native Intl.Segmenter (zh, word granularity) into the FTS search_text, while canonical content keeps the original text; if segmentation is unavailable, unicode61 plus substring fallback is used. [@claim:clm_63567129734f146b1d51efb17811a6838506f397b13556fbf09fe84b80287d2f]
- The repository contains a design RFC (status: Design RFC) scoped to Codemini CLI / WebUI / Agent Runtime, proposing a memory subsystem with SQLite FTS5 + BM25 as default retrieval and embeddings explicitly optional. [@claim:clm_67591fa88eca82da71e254d7e0fb5bb48276b96048f06b2f4cf036026b608808]
- A unified MemoryRetrievalAdapter interface is specified with search, upsert, remove, and rebuild methods; the default implementation is FTS5RetrievalAdapter, with a HybridRetrievalAdapter mentioned as a possible future extension. [@claim:clm_76471ab999d41388d8657f3b86b3fb872196e9360c2388a86c66024f301d69c8]
- Three recall paths are specified: bootstrap recall injecting a small stable profile at session start, per-turn recall of top 3-5 repo/coding/procedure memories, and failure-triggered recall of 1-3 coding memories after a tool failure; retrieval before every tool call is explicitly discouraged. [@claim:clm_7c7be0fa0a0792cb48537eeb61fdb4224e7ac1b347035b9a1b4aa002baf387c9]
- Canonical memory is the single source of truth; the FTS retrieval index is derived data that must be rebuildable when corrupted, without affecting the memory itself. [@claim:clm_7fe49ddae134949dea32796528999879ef0ec76ae331200b8be06432dbb0f21f]
- The architecture separates understanding from retrieval: the LLM judges what is worth remembering, extracts atomic facts, classifies scope/family/kind, and detects conflicts, while FTS5/BM25 handles retrieval, filtering, ranking, and top-K recall; embeddings are not relied on by default. [@claim:clm_80a9555406e787020f7d5065dd8b3a09326de0c0abb2a297f3e31a804fe99ae3]
- The design targets four goals: cross-session memory, task-relevant recall rather than stuffing all memory into the prompt, learning reusable engineering experience from failure-to-verification cycles, and long-term governance (dedup, expiry, conflict handling, eviction). [@claim:clm_981fd41c2f871b8eeca1d771e0087c16c838d49219bab39635015a7dcfd6921c]
- Storage is local-first: user/global memories go in codemini.sqlite, while project memories live in <repo>/.codemini/index.sqlite alongside the repository, avoiding global absolute-path mapping. [@claim:clm_b6f242e1b03985c0a39ef933636482c724b96dd542bc2462c075b9f52430973d]
- Memory records are typed along three orthogonal dimensions: scope (user/global/project), family (personal/repo/coding/procedure), and kind (preference/convention/lesson/note). [@claim:clm_e9238398b75f82ae956eb6a9d096302ea36cc6e1699b19aa0bf939d3d08031f6]
- A proposed MemoryRecord interface includes lifecycle (operational/longterm/archived), confidence, source/session/branch metadata, counters for confirmations, accesses, successes and failures, expected validity days, pinned flag, and revision number. [@claim:clm_ede699310232f10c3cb894f289da582653ff1ef7bfee6ecb1efb7e2d44a732ef]
- First-version retrieval ranking is a weighted blend: BM25 relevance 70%, confidence 15%, verification 10%, recency 5%, with project exact-scope applied as a filter rather than a soft weight; retrieval score and long-term retention score are kept as separate concepts. [@claim:clm_fd80a5674ec93833de497ea6bd01db01080cacdeb4f0bf6c10c9741159f6aace]
<!-- rcw:end owner=source:src_3fbdf62866815843a69214e39c9f8001 block=evidence -->

## Researcher notes

