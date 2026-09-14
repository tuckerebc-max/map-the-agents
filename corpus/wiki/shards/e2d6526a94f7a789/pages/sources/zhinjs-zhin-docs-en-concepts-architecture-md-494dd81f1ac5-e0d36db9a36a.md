---
access: public
aliases: []
claim_ids:
- clm_1647a43c812099acae398b4762bd603e833ed3720643ba94cc6c17cc549caeef
- clm_55c4f9919c082483d9be940ffb4c0d445d7974be41a35028e3e1c30db73dab61
- clm_717080968ab6f9bf8e5a296089876e17ba0d4f90cac83c089c3139c00481a50a
maturity: draft
page_id: pg_3b29a9b67751504ebb58e0d36db9a36a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c20cda1dc7455daf8fff546017e92438
title: zhinjs/zhin/docs/en/concepts/architecture.md @ 494dd81f1ac5
updated_at: '2026-09-14T04:33:46Z'
---

# zhinjs/zhin/docs/en/concepts/architecture.md @ 494dd81f1ac5

<!-- rcw:begin owner=source:src_c20cda1dc7455daf8fff546017e92438 block=evidence -->
- AI is opt-in: the default install is an IM core under ~10MB, and agent capability requires adding @zhin.js/agent, zod, ai, and a provider package such as @ai-sdk/openai. [@claim:clm_1647a43c812099acae398b4762bd603e833ed3720643ba94cc6c17cc549caeef]
- Repository development practice: `pnpm check:architecture` runs in CI to block lower-layer packages importing upper-layer packages, and the layering rule is enforced by harness checks rather than convention. [@claim:clm_55c4f9919c082483d9be940ffb4c0d445d7974be41a35028e3e1c30db73dab61]
- Package dependency direction is unidirectional downward: upper layers may depend on lower ones, and lower layers never reference upper layers; @zhin.js/cli is the sole exception allowed to import across all layers. [@claim:clm_717080968ab6f9bf8e5a296089876e17ba0d4f90cac83c089c3139c00481a50a]
<!-- rcw:end owner=source:src_c20cda1dc7455daf8fff546017e92438 block=evidence -->

## Researcher notes

