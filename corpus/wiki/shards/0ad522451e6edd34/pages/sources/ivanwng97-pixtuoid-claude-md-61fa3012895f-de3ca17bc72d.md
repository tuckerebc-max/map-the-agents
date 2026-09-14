---
access: public
aliases: []
claim_ids:
- clm_03cf0b6bfc8b07e8a53c4f9ccf4e8a33e83dddeea11ff2432251ea8f7e55a04c
- clm_2d0b20251ade98d5610c27842f56fd5668f5c06f92510d97ccceb32a35a99ebf
- clm_60d20b25f9a9f84e0723590a99a9b1fa48c0a1b33843d876f8d1edf55368d1a8
- clm_7182be8fb87e29d4635428e9d7ac5b36deab44741467ab29a05829c4a0d6d353
- clm_9f7329ff90d50b620236a161562118674fb09717c57bfc51f908024416363ea3
maturity: draft
page_id: pg_06ca94bca79a52eab737de3ca17bc72d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_08e915910d165cf3839610e565094b84
title: IvanWng97/pixtuoid/CLAUDE.md @ 61fa3012895f
updated_at: '2026-09-14T02:05:53Z'
---

# IvanWng97/pixtuoid/CLAUDE.md @ 61fa3012895f

<!-- rcw:begin owner=source:src_08e915910d165cf3839610e565094b84 block=evidence -->
- Repository development practice: conventions require TDD-first, WHY-only comments, no magic numbers, no unwrap() outside tests, and no ratatui/crossterm dependencies in pixtuoid-core or pixtuoid-scene. [@claim:clm_03cf0b6bfc8b07e8a53c4f9ccf4e8a33e83dddeea11ff2432251ea8f7e55a04c]
- Repository development practice: contributors use `just build`, `just test` (nextest), and `just preflight` as the pre-push gate running lint, clippy, hack, and test in CI order. [@claim:clm_2d0b20251ade98d5610c27842f56fd5668f5c06f92510d97ccceb32a35a99ebf]
- The project is a Rust workspace of five crates, with the core having no terminal dependencies. [@claim:clm_60d20b25f9a9f84e0723590a99a9b1fa48c0a1b33843d876f8d1edf55368d1a8]
- Repository development practice: committed repo skills include two-lens-review, beautify-decoration, add-source, add-theme, and procedural-lofi. [@claim:clm_7182be8fb87e29d4635428e9d7ac5b36deab44741467ab29a05829c4a0d6d353]
- Repository development practice: non-trivial work follows an arc (pick, design gate, spec, TDD build, self-review, merge gate) where the merge gate is a two-lens-review skill requiring 2+ differentiated lenses, green CI, and dispositioned bot findings, and a human performs the merge. [@claim:clm_9f7329ff90d50b620236a161562118674fb09717c57bfc51f908024416363ea3]
<!-- rcw:end owner=source:src_08e915910d165cf3839610e565094b84 block=evidence -->

## Researcher notes

