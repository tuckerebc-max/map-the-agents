---
access: public
aliases: []
claim_ids:
- clm_0eb800c631bb8da8a7928657e91b904d909cb79eedc055b8e81156e27d36c661
- clm_13eac932e03bc0b4a45f76d866857f9b93f74dd2ec338d1c6a7506def136106d
- clm_1ed30322967d4329468a1c105881cad3218132d2e7533bcd647ef60ede5d5083
maturity: draft
page_id: pg_07c477719c425d6baaf2901cf7a0584a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e5f411f9998c513198c4073d1fc8bd46
title: stravu/crystal/AGENTS.md @ 1e18e0bc9812
updated_at: '2026-09-14T03:15:51Z'
---

# stravu/crystal/AGENTS.md @ 1e18e0bc9812

<!-- rcw:begin owner=source:src_e5f411f9998c513198c4073d1fc8bd46 block=evidence -->
- Repository development practice: contributors must use TypeScript with ESLint configs, 2-space indentation, camelCase/PascalCase/kebab-case naming, run lint and typecheck before PRs, and include descriptions, linked issues, and testing notes in PRs. [@claim:clm_0eb800c631bb8da8a7928657e91b904d909cb79eedc055b8e81156e27d36c661]
- Repository development practice: AGENTS.md requires Node >= 22.14 and pnpm >= 8, secrets kept in .env and never committed, and instructs automation agents to review the root CLAUDE.md and every folder's CLAUDE.md before working there. [@claim:clm_13eac932e03bc0b4a45f76d866857f9b93f74dd2ec338d1c6a7506def136106d]
- Repository development practice: AGENTS.md specifies a pnpm workspace (main, frontend, shared, tests packages) with commands like pnpm dev, pnpm build, pnpm lint, pnpm typecheck, and Playwright E2E tests via pnpm test. [@claim:clm_1ed30322967d4329468a1c105881cad3218132d2e7533bcd647ef60ede5d5083]
<!-- rcw:end owner=source:src_e5f411f9998c513198c4073d1fc8bd46 block=evidence -->

## Researcher notes

