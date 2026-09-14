---
access: public
aliases: []
claim_ids:
- clm_34ff02e0e76ad65e22f6596286f51db4a60142ead597023033688841c9732259
- clm_4242f15bcc11fae734b5dffb4d0fd9978645d757a2c8a17851b57de26db5dcc5
- clm_5f35a275a7f9bdbc9098083e74a7d98e90dafb82dcefafb0b4c315fa7c55c512
- clm_faac9936e43b482813be191f4051587cbf7d43e452cf683a9a33fb48caac1eb8
maturity: draft
page_id: pg_453f9218450e530c8b433bb2cb3c3ba2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8da7d3fe5da75296b1f082770dfafc72
title: Ralph-Workflow/Ralph-Workflow/AGENTS.md @ 3d9d847f41fe
updated_at: '2026-09-14T02:35:18Z'
---

# Ralph-Workflow/Ralph-Workflow/AGENTS.md @ 3d9d847f41fe

<!-- rcw:begin owner=source:src_8da7d3fe5da75296b1f082770dfafc72 block=evidence -->
- Repository development practice: all tests must fit a combined 60-second wall-clock budget enforced by import-time invariants in ralph/verify.py, with non-circumvention rules against splitting suites or raising per-suite timeouts. [@claim:clm_34ff02e0e76ad65e22f6596286f51db4a60142ead597023033688841c9732259]
- Repository development practice: contributors must run `make verify` from ralph-workflow/ before completion; it must pass in full with no unrelated-failure exemptions, and a red gate is owned by whoever next observes it. [@claim:clm_4242f15bcc11fae734b5dffb4d0fd9978645d757a2c8a17851b57de26db5dcc5]
- Repository development practice: AGENTS.md mandates trunk-based development with all work committed directly to main, forbids branch creation and pull requests, and permits commits only via `ralph --generate-commit`. [@claim:clm_5f35a275a7f9bdbc9098083e74a7d98e90dafb82dcefafb0b4c315fa7c55c512]
- Repository development practice: a three-level fabrication_guard.py checks public-facing markdown, with level 1 as a pre-commit hook and levels 2-3 verifying external repos, packages, and stats against live sources. [@claim:clm_faac9936e43b482813be191f4051587cbf7d43e452cf683a9a33fb48caac1eb8]
<!-- rcw:end owner=source:src_8da7d3fe5da75296b1f082770dfafc72 block=evidence -->

## Researcher notes

