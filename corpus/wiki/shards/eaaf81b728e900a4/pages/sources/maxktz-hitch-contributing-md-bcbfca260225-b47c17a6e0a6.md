---
access: public
aliases: []
claim_ids:
- clm_8da2f6f795818f6575b7ae57a7877b48524e00fc9ebcf436419b60b05208b7d4
- clm_ba1c5f2217655bdacc2ef49bd6ab15bda6303007ae37d5d7f8e601acb69d685d
maturity: draft
page_id: pg_91b30ddfd2ff57a896b5b47c17a6e0a6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ccdd2b54c3ea5a3db4becd00281f4a13
title: maxktz/hitch/CONTRIBUTING.md @ bcbfca260225
updated_at: '2026-09-14T04:09:11Z'
---

# maxktz/hitch/CONTRIBUTING.md @ bcbfca260225

<!-- rcw:begin owner=source:src_ccdd2b54c3ea5a3db4becd00281f4a13 block=evidence -->
- Repository development practice: contributors run `cargo fmt -- --check` and `cargo test` before committing, and build locally with `cargo build --release`. [@claim:clm_8da2f6f795818f6575b7ae57a7877b48524e00fc9ebcf436419b60b05208b7d4]
- Repository development practice: releases use `npm run release -- <version>` and a tag push; GitHub Actions then builds native binaries, publishes hitch-cli to npm, and creates a GitHub release. [@claim:clm_ba1c5f2217655bdacc2ef49bd6ab15bda6303007ae37d5d7f8e601acb69d685d]
<!-- rcw:end owner=source:src_ccdd2b54c3ea5a3db4becd00281f4a13 block=evidence -->

## Researcher notes

