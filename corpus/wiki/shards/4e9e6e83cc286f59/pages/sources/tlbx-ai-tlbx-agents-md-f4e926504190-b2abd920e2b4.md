---
access: public
aliases: []
claim_ids:
- clm_32719d1269b5bf2ecbc28fd410d5461f0438046c0ff1d7b24976ffc53870ab12
- clm_4a040a0d43c9e8b0ae23ab2a35ce15d44df1c8742f22fd40fb3879c1724256c4
- clm_eff3b16b10d6ca0d9429af5368981f80b23ed47d4dbb275e241e339cd48e4a9e
maturity: draft
page_id: pg_7f509974aaa85a6883d8b2abd920e2b4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b8696a810e455077bf1025570c1fe844
title: tlbx-ai/tlbx/AGENTS.md @ f4e926504190
updated_at: '2026-09-14T03:19:50Z'
---

# tlbx-ai/tlbx/AGENTS.md @ f4e926504190

<!-- rcw:begin owner=source:src_b8696a810e455077bf1025570c1fe844 block=evidence -->
- Repository development practice: contributors are told to keep major data-processing, protocol and business logic in C# while keeping the TypeScript frontend lean, to remove superseded dead code in the same change, and to use domReconcile.ts for keyed UI lists so content-only updates preserve DOM node identity. [@claim:clm_32719d1269b5bf2ecbc28fd410d5461f0438046c0ff1d7b24976ffc53870ab12]
- Repository development practice: every release invocation must explicitly pass -TestCategories from a fixed set (assets, frontend, server, runtime, installers, dependencies, build, or all), and stable releases require all. [@claim:clm_4a040a0d43c9e8b0ae23ab2a35ce15d44df1c8742f22fd40fb3879c1724256c4]
- Repository development practice: AGENTS.md and CLAUDE.md instruct contributors that development happens on the dev branch, with main reserved for stable integration, and that release scripts (release-dev.ps1, promote.ps1, release.ps1) may only be run for the explicitly requested release path. [@claim:clm_eff3b16b10d6ca0d9429af5368981f80b23ed47d4dbb275e241e339cd48e4a9e]
<!-- rcw:end owner=source:src_b8696a810e455077bf1025570c1fe844 block=evidence -->

## Researcher notes

