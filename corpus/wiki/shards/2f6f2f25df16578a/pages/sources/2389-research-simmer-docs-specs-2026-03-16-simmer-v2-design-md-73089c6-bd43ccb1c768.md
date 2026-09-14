---
access: public
aliases: []
claim_ids:
- clm_15a63447d967a606bc5c76e6ef7b41bea5d357a74ec95e612d05a22addcd95d7
- clm_29e63738ba42a86cb835c97cc85c5529d371a68cb4e91697ee630f49eac035dc
- clm_ac0e3569366ae30daaae55e550182ccc2f80b45025667969eca53471c260cc92
- clm_f293ce370837c3c5494befae45ffd49835a60461c28f0d1c9134fff2e0662213
maturity: draft
page_id: pg_ea80ad4e85b258a29d0abd43ccb1c768
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0a68d8eb30225280b1845adee6cad635
title: 2389-research/simmer/docs/specs/2026-03-16-simmer-v2-design.md @ 73089c6f2224
updated_at: '2026-09-14T03:29:51Z'
---

# 2389-research/simmer/docs/specs/2026-03-16-simmer-v2-design.md @ 73089c6f2224

<!-- rcw:begin owner=source:src_0a68d8eb30225280b1845adee6cad635 block=evidence -->
- In workspace mode, each iteration is snapshotted as a git commit, enabling diffing and rollback via git checkout to the best iteration's commit; single-file mode instead writes iteration-N-candidate.md files. [@claim:clm_15a63447d967a606bc5c76e6ef7b41bea5d357a74ec95e612d05a22addcd95d7]
- Each iteration targets one direction via ASI (Actionable Side Information), the single highest-leverage fix; for workspace targets this becomes one coherent multi-file direction rather than unrelated changes. [@claim:clm_29e63738ba42a86cb835c97cc85c5529d371a68cb4e91697ee630f49eac035dc]
- Three evaluation modes are supported: judge-only (default, for text artifacts), runnable (judge interprets a script's output), and hybrid (both). There is no format contract on evaluator output; the judge reads whatever the script produces. [@claim:clm_ac0e3569366ae30daaae55e550182ccc2f80b45025667969eca53471c260cc92]
- The v2 design spec extends the refinement loop with pluggable evaluation, multi-file workspace targets, expanded ASI, and background constraints; all additions are opt-in and default behavior matches v1. [@claim:clm_f293ce370837c3c5494befae45ffd49835a60461c28f0d1c9134fff2e0662213]
<!-- rcw:end owner=source:src_0a68d8eb30225280b1845adee6cad635 block=evidence -->

## Researcher notes

