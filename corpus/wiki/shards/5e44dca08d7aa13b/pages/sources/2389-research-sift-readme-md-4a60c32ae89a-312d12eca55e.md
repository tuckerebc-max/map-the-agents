---
access: public
aliases: []
claim_ids:
- clm_3e93a5aa17ce412315ceb87fb8403230e7ee0e5d56afaa28cc23d507c0b4bcab
- clm_3eeceb75514ba434b698440fe9745a1bce7c9f928d34ea4a98de9ff910718e33
- clm_58fe49f5e6b2ce8e3728643410765c088cf902fb9dcc5a6ea57b468e63e2f22b
- clm_a0140567ca2eaabdcdf25255aae7847d5de9846bf54257921eb1d92dff066bca
- clm_ed66d103026e27e1efaf48ad2d1f9e71e1417dbe10e4e3cf72297cc0d4ee5fc9
maturity: draft
page_id: pg_4ea476e76511505d9f72312d12eca55e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7984529ed5875551b7e722c707063c56
title: 2389-research/sift/README.md @ 4a60c32ae89a
updated_at: '2026-09-14T03:29:36Z'
---

# 2389-research/sift/README.md @ 4a60c32ae89a

<!-- rcw:begin owner=source:src_7984529ed5875551b7e722c707063c56 block=evidence -->
- The package contains SKILL.md, README.md, LICENSE, and three reference files: finding-schema.md, report-template.md, and worker-brief.md. [@claim:clm_3e93a5aa17ce412315ceb87fb8403230e7ee0e5d56afaa28cc23d507c0b4bcab]
- The audit is read-only by design: the sole repository write is the final report, defaulting to docs/sift-audit-<date>.md, honoring a user-named path, or writing nothing when the user declines or the environment cannot write files. [@claim:clm_3eeceb75514ba434b698440fe9745a1bce7c9f928d34ea4a98de9ff910718e33]
- Installation is via 'npx skills add 2389-research/sift' (project-local by default, -g for user-wide), or manually by cloning and copying the directory, which must be named sift-codebase-audit to match the skill's name field. [@claim:clm_58fe49f5e6b2ce8e3728643410765c088cf902fb9dcc5a6ea57b468e63e2f22b]
- The audit targets material simplifications in data structures, schemas, state representation, control flow, algorithms, lifecycle/concurrency, and module ownership boundaries. [@claim:clm_a0140567ca2eaabdcdf25255aae7847d5de9846bf54257921eb1d92dff066bca]
- The skill is invoked via the slash command /sift-codebase-audit or a natural-language request, and defaults to the current repository with whole-application coverage unless a narrower scope is stated. [@claim:clm_ed66d103026e27e1efaf48ad2d1f9e71e1417dbe10e4e3cf72297cc0d4ee5fc9]
<!-- rcw:end owner=source:src_7984529ed5875551b7e722c707063c56 block=evidence -->

## Researcher notes

