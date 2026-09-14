---
access: public
aliases: []
claim_ids:
- clm_09ab4aa3a35d0cb5fecc7245e06c53b1bb8ec5d2837440d2e4bf4f36df77bd83
- clm_77ca1f3dff279cba57d6f65f706a95f0e2a40d76542dc37d89c2a0d576bbf3ed
- clm_975b03f08f602eac30b91a9f7d2847fd486771703376ef5a70876ff1a81783f2
maturity: draft
page_id: pg_19e56d28fc7d5849988f91b5dc04bc08
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_df0d4aa646955333877369aad9142198
title: madarco/agentbox/CLAUDE.md @ 138c1f585fdb
updated_at: '2026-09-14T02:15:17Z'
---

# madarco/agentbox/CLAUDE.md @ 138c1f585fdb

<!-- rcw:begin owner=source:src_df0d4aa646955333877369aad9142198 block=evidence -->
- Repository development practice: contributors must keep the public docs site (apps/web/content/docs) in sync in the same change whenever a CLI command, flag, config key, default, or provider behavior changes, and first-time contributors sign a one-line CLA on their first PR. [@claim:clm_09ab4aa3a35d0cb5fecc7245e06c53b1bb8ec5d2837440d2e4bf4f36df77bd83]
- Repository development practice: tests use vitest with default discovery and must stay pure (no docker, no network); integration testing is currently manual, and linting uses eslint plus prettier via `pnpm lint`/`pnpm format`. [@claim:clm_77ca1f3dff279cba57d6f65f706a95f0e2a40d76542dc37d89c2a0d576bbf3ed]
- Repository development practice: the codebase convention is strict TypeScript ESM with tsup builds, commander for the CLI, @clack/prompts for interactivity, and execa for shelling out to docker; a PTY harness (`pnpm drive`) drives interactive TUIs during verification. [@claim:clm_975b03f08f602eac30b91a9f7d2847fd486771703376ef5a70876ff1a81783f2]
<!-- rcw:end owner=source:src_df0d4aa646955333877369aad9142198 block=evidence -->

## Researcher notes

