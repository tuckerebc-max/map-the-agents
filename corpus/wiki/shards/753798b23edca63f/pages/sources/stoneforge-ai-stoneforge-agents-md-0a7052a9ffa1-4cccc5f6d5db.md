---
access: public
aliases: []
claim_ids:
- clm_224d3d55407bf5fc0c65faf1b780c3052e184494adc9ed038876eeead23dde96
- clm_7c56c7cf7b30f6e6c8c4677e548db929e732a690a8cee8139cde65cfd2001b01
maturity: draft
page_id: pg_ce2f2aa2d299537aa9c04cccc5f6d5db
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4b94fc2734c45bbd895d873212f34012
title: stoneforge-ai/stoneforge/AGENTS.md @ 0a7052a9ffa1
updated_at: '2026-09-14T02:43:53Z'
---

# stoneforge-ai/stoneforge/AGENTS.md @ 0a7052a9ffa1

<!-- rcw:begin owner=source:src_4b94fc2734c45bbd895d873212f34012 block=evidence -->
- Repository development practice: contributors use pnpm/bun commands (pnpm install, pnpm build, pnpm test, pnpm lint, pnpm typecheck; bun test), tests are colocated as *.test.ts files, and contributors must sign a CLA before PR merge. [@claim:clm_224d3d55407bf5fc0c65faf1b780c3052e184494adc9ed038876eeead23dde96]
- Repository development practice: AGENTS.md instructs contributing agents that 'blocked' status is computed from dependencies and must never be set directly, and that api.addDependency() does not detect cycles, so DependencyService.detectCycle() should be used. [@claim:clm_7c56c7cf7b30f6e6c8c4677e548db929e732a690a8cee8139cde65cfd2001b01]
<!-- rcw:end owner=source:src_4b94fc2734c45bbd895d873212f34012 block=evidence -->

## Researcher notes

