---
access: public
aliases: []
claim_ids:
- clm_881a28a14118ccf21bf2a78a50051e5082029de9df9b01caef85f464821a67e0
- clm_baa66fccea9d68de322450999c9097e9c192d1d498482975d0cdfa70da90cf11
maturity: draft
page_id: pg_ae7282a7d2845e7ea6f510c0c98b60c4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_23c2fe436d9c599ebf86b93060c36740
title: CodebuffAI/freebuff/docs/testing.md @ 654a906e6758
updated_at: '2026-09-14T03:40:43Z'
---

# CodebuffAI/freebuff/docs/testing.md @ 654a906e6758

<!-- rcw:begin owner=source:src_23c2fe436d9c599ebf86b93060c36740 block=evidence -->
- Repository development practice: every package must have a bunfig.toml preloading sdk/test/setup-env.ts so package-local 'bun test' gets placeholder env values instead of the developer's .env. [@claim:clm_881a28a14118ccf21bf2a78a50051e5082029de9df9b01caef85f464821a67e0]
- Repository development practice: CI runs tests through scripts/ci/test-with-guard.ts, which fails the build on errors outside test bodies or on test/file counts below a recorded baseline in .github/test-baselines.json. [@claim:clm_baa66fccea9d68de322450999c9097e9c192d1d498482975d0cdfa70da90cf11]
<!-- rcw:end owner=source:src_23c2fe436d9c599ebf86b93060c36740 block=evidence -->

## Researcher notes

