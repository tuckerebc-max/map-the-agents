---
access: public
aliases: []
claim_ids:
- clm_013a3f8279ff373dcb11380aec2e34177fa85e2549f4eb332d01df0a1d9e0d18
- clm_5b38afd1914c676952be91764ea64851ae7693bea9834474eec087cd811b4f69
- clm_aa8798664e9e195f27cea640766fa7e619a757dad7fe42235c95e03d0625f5f7
- clm_d64f17b06380857569dd0a31fe7e29f29e780a75ed2975a799d0475fc58754b6
maturity: draft
page_id: pg_e068cfca009b5d53913ccb3db4aa84fb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_38e0cf7f05635b2bb0b2d4f393eab2db
title: friuns2/codex-mobile/AGENTS.md @ fac2291b0e60
updated_at: '2026-09-14T01:49:12Z'
---

# friuns2/codex-mobile/AGENTS.md @ fac2291b0e60

<!-- rcw:begin owner=source:src_38e0cf7f05635b2bb0b2d4f393eab2db block=evidence -->
- Repository development practice: every feature/behavior change needs a measurement-grounded performance audit before completion, with profiler helpers (`pnpm run profile:browser`, `profile:thread`) writing reports under output/playwright/. [@claim:clm_013a3f8279ff373dcb11380aec2e34177fa85e2549f4eb332d01df0a1d9e0d18]
- Repository development practice: Qodo/CodeRabbit review comments are advisory; security-hardening suggestions assuming a hostile remote caller should be rejected because the app server is intended for local-user use, not public internet exposure. [@claim:clm_5b38afd1914c676952be91764ea64851ae7693bea9834474eec087cd811b4f69]
- Repository development practice: changes should be tested before completion, manual test docs under tests/<domain>/ updated with setup/actions/expected results, and a CJS smoke test is required for package/runtime/module-loading changes. [@claim:clm_aa8798664e9e195f27cea640766fa7e619a757dad7fe42235c95e03d0625f5f7]
- Repository development practice: AGENTS.md requires checking live git state before merges/rebases, committing after each discrete task, preferring PR-based merges, and inspecting conflicts intentionally rather than using automatic conflict-bias flags. [@claim:clm_d64f17b06380857569dd0a31fe7e29f29e780a75ed2975a799d0475fc58754b6]
<!-- rcw:end owner=source:src_38e0cf7f05635b2bb0b2d4f393eab2db block=evidence -->

## Researcher notes

