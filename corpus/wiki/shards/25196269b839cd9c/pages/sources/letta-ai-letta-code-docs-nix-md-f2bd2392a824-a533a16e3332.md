---
access: public
aliases: []
claim_ids:
- clm_1ba4043fccbf2bdf6d064a5540ce7a058466779ebd05a22fef6a4318d49c4156
- clm_af2163f126c36bc2be5d465fe8af34f4edb0309259661cdc66ca2d5ac18b6c25
maturity: draft
page_id: pg_885b0016b32b594bb088a533a16e3332
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1e266e03bae95ddcbacada3142726014
title: letta-ai/letta-code/docs/nix.md @ f2bd2392a824
updated_at: '2026-09-14T02:12:21Z'
---

# letta-ai/letta-code/docs/nix.md @ f2bd2392a824

<!-- rcw:begin owner=source:src_1e266e03bae95ddcbacada3142726014 block=evidence -->
- Repository development practice: when bun.lock changes, contributors should regenerate the Nix dependency expression with `bunx bun2nix -o bun.nix` before opening a PR. [@claim:clm_1ba4043fccbf2bdf6d064a5540ce7a058466779ebd05a22fef6a4318d49c4156]
- The Nix flake builds the CLI with Bun; dependency resolution is driven by the checked-in bun.lock, with a generated bun.nix enabling reproducible offline Nix builds. [@claim:clm_af2163f126c36bc2be5d465fe8af34f4edb0309259661cdc66ca2d5ac18b6c25]
<!-- rcw:end owner=source:src_1e266e03bae95ddcbacada3142726014 block=evidence -->

## Researcher notes

