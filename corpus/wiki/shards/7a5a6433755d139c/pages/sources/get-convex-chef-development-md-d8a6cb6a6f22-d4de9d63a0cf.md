---
access: public
aliases: []
claim_ids:
- clm_49f6c636c0003b5ddb6337a5f288229250be2ac13c919890a7d2954e712bb804
- clm_517774d1a3f69bda0cb73709cda6d527e69ce9cd80229dec3204f77936572398
- clm_6fb78f14f6e4d6374f81ccfe2a8d85f01ce26dd486904ae7ee12b95533315487
- clm_faed0a1823692c0b7e3e15ffe0eac06e75ae640ba2e2c733bed35dea274f712c
maturity: draft
page_id: pg_db1e5e48c449577082a8d4de9d63a0cf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_80afda3bd8a75137bc20f08253a6e4e4
title: get-convex/chef/DEVELOPMENT.md @ d8a6cb6a6f22
updated_at: '2026-09-14T01:51:03Z'
---

# get-convex/chef/DEVELOPMENT.md @ d8a6cb6a6f22

<!-- rcw:begin owner=source:src_80afda3bd8a75137bc20f08253a6e4e4 block=evidence -->
- Chef appears to use a WebContainer-style environment: a documented debug global exposes 'chefWebContainer' as the unix-ish container where tooling and generated code run. [@claim:clm_49f6c636c0003b5ddb6337a5f288229250be2ac13c919890a7d2954e712bb804]
- Repository development practice: PRs target main; a commit queue blocks on tests, formatting, lints, and typechecking via pnpm scripts, and the repo has very few tests and no e2e tests. [@claim:clm_517774d1a3f69bda0cb73709cda6d527e69ce9cd80229dec3204f77936572398]
- Repository development practice: DEVELOPMENT.md is aimed at Convex employees and is not a supported workflow for external users. [@claim:clm_6fb78f14f6e4d6374f81ccfe2a8d85f01ce26dd486904ae7ee12b95533315487]
- Repository development practice: releases push main to staging, then merge staging into release after agent evals run (~10 min) with a 100% isSuccess rate expected. [@claim:clm_faed0a1823692c0b7e3e15ffe0eac06e75ae640ba2e2c733bed35dea274f712c]
<!-- rcw:end owner=source:src_80afda3bd8a75137bc20f08253a6e4e4 block=evidence -->

## Researcher notes

