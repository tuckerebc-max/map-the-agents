---
access: public
aliases: []
claim_ids:
- clm_a8982545176872a3499638959b0012781a1268aadcceaea7be2a5b5acd031cc4
- clm_ee205600f0cee36ceb43bb435d30b7b7ab404feb16bcb0f81a5796df5306be30
maturity: draft
page_id: pg_3b5e7c8d9e295b8bb82a50587e1f5cda
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_edb2d22b86485799b0abef2c550867c1
title: Zoo-Code-Org/Zoo-Code/docs/architecture/task-lifecycle-model.md @ ba46d1f34a5b
updated_at: '2026-09-14T03:28:20Z'
---

# Zoo-Code-Org/Zoo-Code/docs/architecture/task-lifecycle-model.md @ ba46d1f34a5b

<!-- rcw:begin owner=source:src_edb2d22b86485799b0abef2c550867c1 block=evidence -->
- Repository development practice: a bounded TypeScript model-check suite (pnpm lifecycle:model-check) runs six submodels covering task delegation, shared-store concurrency, provider handoff, cleanup, parser scoping, and completion persistence, and is the model-check entry point in the compile CI job. [@claim:clm_a8982545176872a3499638959b0012781a1268aadcceaea7be2a5b5acd031cc4]
- Repository development practice: the shared-store model tracks two known-unsafe witnesses as issue-keyed ratchets (#1469 stale completion after handoff, #1021 stale live-task save after abandonment), and CI fails if witnesses or landmarks change. [@claim:clm_ee205600f0cee36ceb43bb435d30b7b7ab404feb16bcb0f81a5796df5306be30]
<!-- rcw:end owner=source:src_edb2d22b86485799b0abef2c550867c1 block=evidence -->

## Researcher notes

