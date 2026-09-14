---
access: public
aliases: []
claim_ids:
- clm_55c4f9919c082483d9be940ffb4c0d445d7974be41a35028e3e1c30db73dab61
- clm_717080968ab6f9bf8e5a296089876e17ba0d4f90cac83c089c3139c00481a50a
- clm_abff7469470d5505d35a9932eb59730bf18bcb730b97cc91ad6f5666ce616958
- clm_b9c24ac9810c1ff33a5dff9b6032c1d6c69af2f6e0693b34d31d121a5a5d135f
maturity: draft
page_id: pg_1b958d13bfdd5494a8d317cc4ce32d8c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bb5515fe266e5fcfa2b7d89eba8d8a0b
title: zhinjs/zhin/docs/concepts/architecture.md @ 494dd81f1ac5
updated_at: '2026-09-14T04:33:46Z'
---

# zhinjs/zhin/docs/concepts/architecture.md @ 494dd81f1ac5

<!-- rcw:begin owner=source:src_bb5515fe266e5fcfa2b7d89eba8d8a0b block=evidence -->
- Repository development practice: `pnpm check:architecture` runs in CI to block lower-layer packages importing upper-layer packages, and the layering rule is enforced by harness checks rather than convention. [@claim:clm_55c4f9919c082483d9be940ffb4c0d445d7974be41a35028e3e1c30db73dab61]
- Package dependency direction is unidirectional downward: upper layers may depend on lower ones, and lower layers never reference upper layers; @zhin.js/cli is the sole exception allowed to import across all layers. [@claim:clm_717080968ab6f9bf8e5a296089876e17ba0d4f90cac83c089c3139c00481a50a]
- The repo is a pnpm workspace monorepo whose packages include @zhin.js/core (IM layer), @zhin.js/ai, @zhin.js/agent, @zhin.js/cli (composition root), and the zhin.js facade package. [@claim:clm_abff7469470d5505d35a9932eb59730bf18bcb730b97cc91ad6f5666ce616958]
- The CLI exposes commands including `zhin runtime start`, `zhin setup`, `zhin doctor`, `zhin new my-plugin`, and `zhin search <kw>`. [@claim:clm_b9c24ac9810c1ff33a5dff9b6032c1d6c69af2f6e0693b34d31d121a5a5d135f]
<!-- rcw:end owner=source:src_bb5515fe266e5fcfa2b7d89eba8d8a0b block=evidence -->

## Researcher notes

