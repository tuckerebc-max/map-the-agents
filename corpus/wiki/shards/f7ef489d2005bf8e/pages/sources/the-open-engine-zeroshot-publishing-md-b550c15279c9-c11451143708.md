---
access: public
aliases: []
claim_ids:
- clm_1e78f5ad236b981937399a0a2c600ce61826b2de844ff2aa0c9369a95b00ea6e
- clm_5e8d6d2cd50de0453cfb951f727b93071589e7c5f0dbcc7b3e2ab91ab8bd7145
- clm_de70252ddfbb707f3760df8955f60a739f681e71e19939772634fdbc98dafdb1
maturity: draft
page_id: pg_e84cbaa0ca9252a98d18c11451143708
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7f9af73b820450c1915da1e829aee56b
title: the-open-engine/zeroshot/PUBLISHING.md @ b550c15279c9
updated_at: '2026-09-14T03:18:50Z'
---

# the-open-engine/zeroshot/PUBLISHING.md @ b550c15279c9

<!-- rcw:begin owner=source:src_7f9af73b820450c1915da1e829aee56b block=evidence -->
- Repository development practice: releases publish one canonical version across GitHub tag, native archives, checksum manifest, npm package, target image, Python wheels, and versioned docs via a release workflow using GitHub OIDC trusted publishing, with no long-lived npm or PyPI tokens. [@claim:clm_1e78f5ad236b981937399a0a2c600ce61826b2de844ff2aa0c9369a95b00ea6e]
- The npm package installs a verified native binary for Linux x64/arm64, macOS x64/arm64, and Windows x64; native archives and SHA256 checksums are attached to each canonical vX.Y.Z GitHub Release. [@claim:clm_5e8d6d2cd50de0453cfb951f727b93071589e7c5f0dbcc7b3e2ab91ab8bd7145]
- Repository development practice: release jobs verify already-published immutable artifacts before completing missing steps, and recovery must use the same version, tag, and source commit without overwriting different artifacts. [@claim:clm_de70252ddfbb707f3760df8955f60a739f681e71e19939772634fdbc98dafdb1]
<!-- rcw:end owner=source:src_7f9af73b820450c1915da1e829aee56b block=evidence -->

## Researcher notes

