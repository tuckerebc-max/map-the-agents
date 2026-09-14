# bahdotsh/indxr -- full detail

[Back to orientation](indxr.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bahdotsh/indxr/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/0ad631914a9cdd40.json](../../../wiki/dossiers/bahdotsh/indxr/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/0ad631914a9cdd40.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] indxr maintains an incremental binary cache at .indxr-cache/cache.bin that avoids re-parsing unchanged files, making subsequent runs faster. -- evidence: [docs/caching.md#L9-L15](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L9-L15), [docs/caching.md#L3-L3](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L3-L3), [docs/caching.md#L19-L19](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L19-L19) (`clm_88fba53b26ee6c87ae903460f0a6d8330d2367ef590cb063ef64808b92d9f1bd`)
- [observation/documented] The MCP server (indxr serve) indexes the project once at startup and serves from an in-memory index, with the on-disk cache accelerating that startup parse. -- evidence: [docs/caching.md#L87-L87](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L87-L87) (`clm_f1514c1576f4a8644b5c8db9956b2a73d1a011d14cc1906b0ac4c36297c33b9a`)
- [observation/documented] The source tree includes tree-sitter query-based extractors for C, C++, Go, Java, JavaScript, Python, Rust, and TypeScript, plus a regex parser and a ParserRegistry. -- evidence: [INDEX.md#L8-L100](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L8-L100), [INDEX.md#L656-L662](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L656-L662), [INDEX.md#L679-L689](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L679-L689) (`clm_ec39bf530a20abbe49557c6d9e2dcdc7a1d2c2c849754a3c68460f39e6b1b6df`)

## design-choices (2 claim(s))

- [observation/documented] Cache validation is two-tier: a quick mtime+size check, with an xxh3 content-hash fallback for cases like touch where metadata changed but content did not. -- evidence: [docs/caching.md#L9-L15](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L9-L15) (`clm_df73c6644b6cb9df8ea5125c282f00c57a6c8ce52cc08e921a746a2a7738067b`)
- [observation/documented] The cache file carries a version marker; on a version mismatch after an upgrade the cache is discarded and rebuilt from scratch. -- evidence: [docs/caching.md#L62-L62](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L62-L62) (`clm_0945cc6eeb9b42d020570081bdda5f29473d269ed19a6019a09fa8403a23166a`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI exposes cache options: --cache-dir for a custom location and --no-cache, which creates a no-op cache that never hits, useful for benchmarking or guaranteed fresh parses. -- evidence: [docs/caching.md#L31-L34](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L31-L34), [docs/caching.md#L46-L48](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L46-L48), [docs/caching.md#L50-L50](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L50-L50) (`clm_a9e45fed2dc67da8d4191779770165095fb70c14b172609f7da6436b8f335ca7`)
- [observation/documented] indxr --graph generates dependency graphs in DOT, Mermaid, or JSON, with --graph-level choosing file or symbol granularity and --graph-depth limiting hops. -- evidence: [docs/dep-graph.md#L47-L47](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L47-L47), [docs/dep-graph.md#L11-L11](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L11-L11), [docs/dep-graph.md#L7-L9](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L7-L9), [docs/dep-graph.md#L3-L3](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L3-L3), [docs/dep-graph.md#L28-L31](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L28-L31) (`clm_1f3c19690890f47eff21452a5e31c924ba8c72201bfe21c9c474f283df8ae326`)
- [observation/documented] The MCP tool get_dependency_graph exposes graph generation to live agent queries with parameters path, level, format, and depth. -- evidence: [docs/dep-graph.md#L121-L128](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L121-L128), [docs/dep-graph.md#L130-L130](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L130-L130), [docs/dep-graph.md#L119-L119](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/dep-graph.md#L119-L119) (`clm_5d2f28b52e659da80fcf9714be090d7a4ed3c65e6a50f175044c7fc7d6f142a7`)
- [observation/documented] Filtering options include --filter-path (prefix match on relative paths), -l for case-insensitive language selection, --kind for declaration kind, --symbol for case-insensitive substring search, and --public-only. -- evidence: [docs/filtering.md#L23-L23](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L23-L23), [docs/filtering.md#L9-L13](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L9-L13), [docs/filtering.md#L32-L32](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L32-L32), [docs/filtering.md#L15-L15](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L15-L15), [docs/filtering.md#L62-L62](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L62-L62), [docs/filtering.md#L79-L81](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L79-L81), [docs/filtering.md#L38-L56](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/filtering.md#L38-L56) (`clm_3023e70f7f07e0cfd78df2e957b6459d6ea2a6b88e1736ed42593fb095bc2b75`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The repo includes an accuracy benchmark (accuracy_bench.py, accuracy_questions.json) measuring LLM answer quality with full-file context versus indxr structural context, scoring answers and writing JSON results. -- evidence: [INDEX.md#L143-L158](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L143-L158), [INDEX.md#L160-L163](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/INDEX.md#L160-L163) (`clm_d4df344e5bb4e82a9936f620cc4bbc9c086415d3a77b444169e175c21854d7eb`)
- [observation/documented] Documented cache performance numbers show warm runs roughly 3.3x-7.3x faster than cold runs across three codebase sizes, with speedup growing with codebase size. -- evidence: [docs/caching.md#L66-L70](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L66-L70), [docs/caching.md#L72-L72](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L72-L72) (`clm_297f237a7776543742cc3e0a64151bb81573a75b51674ffec99bd6fd851c53df`)

## dependencies (1 claim(s))

- [observation/documented] The cache is serialized with bincode, and each entry stores relative file path, mtime, size, an xxh3_64 content hash, and the parsed FileIndex. -- evidence: [docs/caching.md#L56-L60](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L56-L60), [docs/caching.md#L54-L54](https://github.com/bahdotsh/indxr/blob/fbcbe9451605c4f2f8c9ee320b5cf80d69ce05bc/docs/caching.md#L54-L54) (`clm_2df115fd8555e7e06e2a2952be9bc865d465a030b49c161650f29564e752abca`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

