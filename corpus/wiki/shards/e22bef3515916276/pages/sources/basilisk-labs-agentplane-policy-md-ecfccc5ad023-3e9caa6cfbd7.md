---
access: public
aliases: []
claim_ids:
- clm_3bd92d6dbb61ff9b84997bcdf5104c2279e7afcf031f2b1b5c693308014fbb7a
- clm_54af9e8c2880354076c646a752754a6a987ca8ec3694c995b3ee6a52e8417d8a
maturity: draft
page_id: pg_bb5a560c1ef555568d363e9caa6cfbd7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a763efb8a3b55f80a573851f45a444cb
title: basilisk-labs/agentplane/POLICY.md @ ecfccc5ad023
updated_at: '2026-09-14T01:36:43Z'
---

# basilisk-labs/agentplane/POLICY.md @ ecfccc5ad023

<!-- rcw:begin owner=source:src_a763efb8a3b55f80a573851f45a444cb block=evidence -->
- Repository development practice: contributors work through the agentplane task lifecycle (task new, plan approve, verify, finish), open issues first for architectural or CLI-surface changes, and must keep src/cli, usecases, ports, and adapters layering with OS/git/network access confined to adapters. [@claim:clm_3bd92d6dbb61ff9b84997bcdf5104c2279e7afcf031f2b1b5c693308014fbb7a]
- Repository development practice: POLICY.md requires lint and full tests to pass before merging to main, tests for behavior changes, English-only user-facing strings, no accidental npm releases, and no uncommitted code changes under packages/**. [@claim:clm_54af9e8c2880354076c646a752754a6a987ca8ec3694c995b3ee6a52e8417d8a]
<!-- rcw:end owner=source:src_a763efb8a3b55f80a573851f45a444cb block=evidence -->

## Researcher notes

