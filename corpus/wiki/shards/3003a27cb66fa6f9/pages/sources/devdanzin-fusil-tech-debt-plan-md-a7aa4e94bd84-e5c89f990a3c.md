---
access: public
aliases: []
claim_ids:
- clm_587c3096b2ca3b931c2af98fc7ee5650290eadd2b82b1fd0f197eb8ea7092126
- clm_dec7f2c48fba5db8049b41a98bc03c6b1bafcf7f72c2fc80a199cf92358425b0
maturity: draft
page_id: pg_e18ea3a087a954bfadfce5c89f990a3c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9c2b474ba6a454a294b9cb10c829ae5d
title: devdanzin/fusil/TECH_DEBT_PLAN.md @ a7aa4e94bd84
updated_at: '2026-09-14T03:46:53Z'
---

# devdanzin/fusil/TECH_DEBT_PLAN.md @ a7aa4e94bd84

<!-- rcw:begin owner=source:src_9c2b474ba6a454a294b9cb10c829ae5d block=evidence -->
- The memory cap was made ASan-safe: RLIMIT_AS is skipped when an ASan target is auto-detected or --no-memory-limit is set (since ASan reserves ~20 TB of virtual address space), relying on an external cgroup cap, while core-dump/nproc/nice limits are kept in all cases. [@claim:clm_587c3096b2ca3b931c2af98fc7ee5650290eadd2b82b1fd0f197eb8ea7092126]
- Repository development practice: a tech-debt plan records that CI (GitHub Actions running unittest and ruff check) was added after phases 0-7, with the suite green on Python 3.13 and 3.14 and grown to 308 tests. [@claim:clm_dec7f2c48fba5db8049b41a98bc03c6b1bafcf7f72c2fc80a199cf92358425b0]
<!-- rcw:end owner=source:src_9c2b474ba6a454a294b9cb10c829ae5d block=evidence -->

## Researcher notes

