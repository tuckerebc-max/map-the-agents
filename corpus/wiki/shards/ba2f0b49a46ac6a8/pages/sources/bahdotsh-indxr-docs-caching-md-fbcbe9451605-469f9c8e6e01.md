---
access: public
aliases: []
claim_ids:
- clm_0945cc6eeb9b42d020570081bdda5f29473d269ed19a6019a09fa8403a23166a
- clm_297f237a7776543742cc3e0a64151bb81573a75b51674ffec99bd6fd851c53df
- clm_2df115fd8555e7e06e2a2952be9bc865d465a030b49c161650f29564e752abca
- clm_88fba53b26ee6c87ae903460f0a6d8330d2367ef590cb063ef64808b92d9f1bd
- clm_a9e45fed2dc67da8d4191779770165095fb70c14b172609f7da6436b8f335ca7
- clm_df73c6644b6cb9df8ea5125c282f00c57a6c8ce52cc08e921a746a2a7738067b
- clm_f1514c1576f4a8644b5c8db9956b2a73d1a011d14cc1906b0ac4c36297c33b9a
maturity: draft
page_id: pg_84f18ca851fe533bb083469f9c8e6e01
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5b15d93ea61a50cdabc964a46f919ed5
title: bahdotsh/indxr/docs/caching.md @ fbcbe9451605
updated_at: '2026-09-14T04:42:11Z'
---

# bahdotsh/indxr/docs/caching.md @ fbcbe9451605

<!-- rcw:begin owner=source:src_5b15d93ea61a50cdabc964a46f919ed5 block=evidence -->
- The cache file carries a version marker; on a version mismatch after an upgrade the cache is discarded and rebuilt from scratch. [@claim:clm_0945cc6eeb9b42d020570081bdda5f29473d269ed19a6019a09fa8403a23166a]
- Documented cache performance numbers show warm runs roughly 3.3x-7.3x faster than cold runs across three codebase sizes, with speedup growing with codebase size. [@claim:clm_297f237a7776543742cc3e0a64151bb81573a75b51674ffec99bd6fd851c53df]
- The cache is serialized with bincode, and each entry stores relative file path, mtime, size, an xxh3_64 content hash, and the parsed FileIndex. [@claim:clm_2df115fd8555e7e06e2a2952be9bc865d465a030b49c161650f29564e752abca]
- indxr maintains an incremental binary cache at .indxr-cache/cache.bin that avoids re-parsing unchanged files, making subsequent runs faster. [@claim:clm_88fba53b26ee6c87ae903460f0a6d8330d2367ef590cb063ef64808b92d9f1bd]
- The CLI exposes cache options: --cache-dir for a custom location and --no-cache, which creates a no-op cache that never hits, useful for benchmarking or guaranteed fresh parses. [@claim:clm_a9e45fed2dc67da8d4191779770165095fb70c14b172609f7da6436b8f335ca7]
- Cache validation is two-tier: a quick mtime+size check, with an xxh3 content-hash fallback for cases like touch where metadata changed but content did not. [@claim:clm_df73c6644b6cb9df8ea5125c282f00c57a6c8ce52cc08e921a746a2a7738067b]
- The MCP server (indxr serve) indexes the project once at startup and serves from an in-memory index, with the on-disk cache accelerating that startup parse. [@claim:clm_f1514c1576f4a8644b5c8db9956b2a73d1a011d14cc1906b0ac4c36297c33b9a]
<!-- rcw:end owner=source:src_5b15d93ea61a50cdabc964a46f919ed5 block=evidence -->

## Researcher notes

