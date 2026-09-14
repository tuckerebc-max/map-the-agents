# bahdotsh/indxr

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fbcbe9451605 @ 0ad631914a9cdd40

## Summary (orientation draft, not independently verified)

Evidence documents indxr, a Rust codebase-indexing CLI with an incremental binary cache, dependency-graph generation, filtering, an MCP server, and a benchmark harness comparing LLM answer quality with indxr context versus full-file context. Evidence coverage: 159 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] indxr maintains an incremental binary cache at .indxr-cache/cache.bin that avoids re-parsing unchanged files, making subsequent runs faster. -- evidence: [docs/caching.md#L9-L15](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L9-L15), [docs/caching.md#L3-L3](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L3-L3), [docs/caching.md#L19-L19](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L19-L19)
  - [observation/documented] The MCP server (indxr serve) indexes the project once at startup and serves from an in-memory index, with the on-disk cache accelerating that startup parse. -- evidence: [docs/caching.md#L87-L87](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L87-L87)
- design-choices (2 claim(s)):
  - [observation/documented] Cache validation is two-tier: a quick mtime+size check, with an xxh3 content-hash fallback for cases like touch where metadata changed but content did not. -- evidence: [docs/caching.md#L9-L15](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L9-L15)
  - [observation/documented] The cache file carries a version marker; on a version mismatch after an upgrade the cache is discarded and rebuilt from scratch. -- evidence: [docs/caching.md#L62-L62](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L62-L62)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI exposes cache options: --cache-dir for a custom location and --no-cache, which creates a no-op cache that never hits, useful for benchmarking or guaranteed fresh parses. -- evidence: [docs/caching.md#L31-L34](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L31-L34), [docs/caching.md#L46-L48](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L46-L48), [docs/caching.md#L50-L50](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L50-L50)
  - [observation/documented] indxr --graph generates dependency graphs in DOT, Mermaid, or JSON, with --graph-level choosing file or symbol granularity and --graph-depth limiting hops. -- evidence: [docs/dep-graph.md#L47-L47](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L47-L47), [docs/dep-graph.md#L11-L11](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L11-L11), [docs/dep-graph.md#L7-L9](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L7-L9), [docs/dep-graph.md#L3-L3](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L3-L3), [docs/dep-graph.md#L28-L31](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L28-L31)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The repo includes an accuracy benchmark (accuracy_bench.py, accuracy_questions.json) measuring LLM answer quality with full-file context versus indxr structural context, scoring answers and writing JSON results. -- evidence: [INDEX.md#L143-L158](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L143-L158), [INDEX.md#L160-L163](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L160-L163)
  - [observation/documented] Documented cache performance numbers show warm runs roughly 3.3x-7.3x faster than cold runs across three codebase sizes, with speedup growing with codebase size. -- evidence: [docs/caching.md#L66-L70](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L66-L70), [docs/caching.md#L72-L72](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L72-L72)
- dependencies (1 claim(s)):
  - [observation/documented] The cache is serialized with bincode, and each entry stores relative file path, mtime, size, an xxh3_64 content hash, and the parsed FileIndex. -- evidence: [docs/caching.md#L56-L60](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L56-L60), [docs/caching.md#L54-L54](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L54-L54)
More evidence: [full detail](indxr.detail.md)

Metadata and full claim list: [full detail](indxr.detail.md)
Human notes ([notes](indxr.notes.md), never overwritten by build)

[Back to map index](../../index.md)
