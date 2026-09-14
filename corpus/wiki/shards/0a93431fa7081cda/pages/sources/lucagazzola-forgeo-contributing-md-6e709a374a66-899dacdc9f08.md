---
access: public
aliases: []
claim_ids:
- clm_09bdd8288a200c68a853e249deb1c2ec784dd7964a94fb7410d6d4b1d57f1eb5
- clm_eba71376f94ccc43fdcd8122179470d2c36a8d98dcb3d0f5e06f1aef70882334
maturity: draft
page_id: pg_d93ed93d857953c2be78899dacdc9f08
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b2c2c07470425edb9255d90e162e2559
title: lucaGazzola/forgeo/CONTRIBUTING.md @ 6e709a374a66
updated_at: '2026-09-14T02:15:16Z'
---

# lucaGazzola/forgeo/CONTRIBUTING.md @ 6e709a374a66

<!-- rcw:begin owner=source:src_b2c2c07470425edb9255d90e162e2559 block=evidence -->
- Repository development practice: contributors must run pytest, ruff check, and mypy src/forgeo before opening a PR, and CI enforces the same quality gates on pull requests. [@claim:clm_09bdd8288a200c68a853e249deb1c2ec784dd7964a94fb7410d6d4b1d57f1eb5]
- The agent contract is agent-agnostic: any CLI that reads the FORGEO_TASK environment variable can be used, and the backlog task's acceptance criteria are rendered into that instruction. [@claim:clm_eba71376f94ccc43fdcd8122179470d2c36a8d98dcb3d0f5e06f1aef70882334]
<!-- rcw:end owner=source:src_b2c2c07470425edb9255d90e162e2559 block=evidence -->

## Researcher notes

