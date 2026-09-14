---
access: public
aliases: []
claim_ids:
- clm_49b4294830a88a7e799db03b1cfca10fb8125e8b39b7d16e4ca0cc197593ea1f
- clm_58854593a4f7b90e4e8d135ec4f12f8c91ee5d1430d03f0cd2458dde00e77858
- clm_735f8b4431dd41abf3868175ade2230ff550082a0b768cf34718ee4c7a72bbf9
- clm_971f8ebe187e0f299ac9493069ba3952e3fefdfe66be60dabea2adca6d09f214
- clm_a6144611811556b93584874be0eeaab48dd22ab66a85be0f2c3ced79caebf852
- clm_cf33e53f213e9887267011bdd2ba5390592790b706c44b7bf456cf9bed283230
- clm_d4512348254cacf7dd13b4be2ae289228b0149c57a3e9345deb3ed1e8ce61a85
maturity: draft
page_id: pg_2ba5489ea48c5265bd3d978534a0afc1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5023c0e0b6a652be8db1d910ec85860d
title: tractorjuice/arc-kit/docs/au-federal-validation-scorecard.md @ bc6bf533811d
updated_at: '2026-09-14T04:27:55Z'
---

# tractorjuice/arc-kit/docs/au-federal-validation-scorecard.md @ bc6bf533811d

<!-- rcw:begin owner=source:src_5023c0e0b6a652be8db1d910ec85860d block=evidence -->
- The build harness schedules recipe targets via topological sort over `targets[].deps` with glob expansion; the au-federal plan computes 9 build waves with maximum parallelism of 11 in wave W2. [@claim:clm_49b4294830a88a7e799db03b1cfca10fb8125e8b39b7d16e4ca0cc197593ea1f]
- Repository development practice: regression tests live in `tests/plugin/test_au_federal_recipe.py` (run via pytest with `-k round2` or `-k ai6` filters), and the suite grew from 61 baseline tests to 191 across review rounds. [@claim:clm_58854593a4f7b90e4e8d135ec4f12f8c91ee5d1430d03f0cd2458dde00e77858]
- The `au-federal` recipe defines 35 targets including 9 optional ones, 2 post-build hooks (arckit:health, arckit:pages), schema_version 1, and an explicit top-level `flagship: AU_DISP`. [@claim:clm_735f8b4431dd41abf3868175ade2230ff550082a0b768cf34718ee4c7a72bbf9]
- A validation scorecard reports 9 evaluation runs of the 8 AU commands with a 25/25 scorecard pass rate at Run 3, zero UK framework leakage, and 220 AU framework references in the artefacts. [@claim:clm_971f8ebe187e0f299ac9493069ba3952e3fefdfe66be60dabea2adca6d09f214]
- Per the arckit-build skill's recipe-loading rules, the harness reads recipes from `.arckit/recipes/` first, so a project-level override takes precedence over plugin defaults. [@claim:clm_a6144611811556b93584874be0eeaab48dd22ab66a85be0f2c3ced79caebf852]
- Per-command validation assessed au-e8-posture against the ASD Essential Eight (8 strategies x 4 maturity levels), au-pia against all 13 Australian Privacy Principles, au-dss against all 13 Digital Service Standard criteria, and au-ism-controls against 17 ISM control domains. [@claim:clm_cf33e53f213e9887267011bdd2ba5390592790b706c44b7bf456cf9bed283230]
- Layer A validation tested the 8 community commands against a real Australian SMB engagement (DISP-track, OFFICIAL:Sensitive, pure-SaaS estate), with underlying artefacts available under NDA. [@claim:clm_d4512348254cacf7dd13b4be2ae289228b0149c57a3e9345deb3ed1e8ce61a85]
<!-- rcw:end owner=source:src_5023c0e0b6a652be8db1d910ec85860d block=evidence -->

## Researcher notes

