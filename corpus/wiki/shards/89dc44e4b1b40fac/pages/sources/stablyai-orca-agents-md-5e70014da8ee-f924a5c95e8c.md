---
access: public
aliases: []
claim_ids:
- clm_357df3b7ab4931c8a2305858f58799e08c2338ae484e71c57b43bf92be6d27db
- clm_57b460e4b5b660c40632f715be93c0532145751a6642d555a7b00da8370c08a6
- clm_ac0c2ba60dfafe95f8372893349d29d0a6e090be07db5d2227fa0f09048577e4
- clm_ca9c5340e6ecf263a0e20d5af8ce199e01b53448d272ddc5c24161d3a657ff12
- clm_dd495ee73575222164a5465aa69fb5d62f5cbc00444ef1bb2ec538a6b1c62b82
maturity: draft
page_id: pg_af8d2b50e9e25be9ba83f924a5c95e8c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9053ff77ab835a9ea830ff05978b6400
title: stablyai/orca/AGENTS.md @ 5e70014da8ee
updated_at: '2026-09-14T02:42:29Z'
---

# stablyai/orca/AGENTS.md @ 5e70014da8ee

<!-- rcw:begin owner=source:src_9053ff77ab835a9ea830ff05978b6400 block=evidence -->
- Repository development practice: platform-dependent behavior must stay behind runtime checks, and Windows child processes must go through the shared runProcess/spawnProcess helpers instead of child_process directly. [@claim:clm_357df3b7ab4931c8a2305858f58799e08c2338ae484e71c57b43bf92be6d27db]
- Repository development practice: Git 2.25 is treated as the core-workflow compatibility baseline, with capability caching scoped per executing host (native, WSL, SSH, or relay). [@claim:clm_57b460e4b5b660c40632f715be93c0532145751a6642d555a7b00da8370c08a6]
- Repository development practice: Electron UI validation must run in the background with `ORCA_BACKGROUND_LAUNCH=1`, never stealing focus, using Playwright CDP screenshots of hidden renderers. [@claim:clm_ac0c2ba60dfafe95f8372893349d29d0a6e090be07db5d2227fa0f09048577e4]
- Repository development practice: UI work must follow docs/STYLEGUIDE.md and use design tokens from main.css and shadcn primitives rather than inventing new values. [@claim:clm_ca9c5340e6ecf263a0e20d5af8ce199e01b53448d272ddc5c24161d3a657ff12]
- Repository development practice: contributors verify changes with `pnpm tc` for typecheck, `pnpm test` for tests, and `oxlint`/`pnpm format` for linting and formatting. [@claim:clm_dd495ee73575222164a5465aa69fb5d62f5cbc00444ef1bb2ec538a6b1c62b82]
<!-- rcw:end owner=source:src_9053ff77ab835a9ea830ff05978b6400 block=evidence -->

## Researcher notes

