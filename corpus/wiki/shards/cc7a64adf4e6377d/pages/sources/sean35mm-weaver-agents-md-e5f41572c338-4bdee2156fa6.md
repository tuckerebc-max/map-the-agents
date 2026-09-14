---
access: public
aliases: []
claim_ids:
- clm_c942ed358ecbf9eae68ee3ea5904c196f4269e1d945b9346186cb49dbf973bea
- clm_f684634f85579c3dce135998a0672517376d5c6341e7ce0cea1775366be85623
- clm_fdae64f4fe72ba2fca9a00ff7f238827f62f72e697e6e5aa745fd85f50b9a0e0
maturity: draft
page_id: pg_d156896f7d72542188804bdee2156fa6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_01def46fb45d53969c69b2fa33529280
title: sean35mm/weaver/AGENTS.md @ e5f41572c338
updated_at: '2026-09-14T02:39:04Z'
---

# sean35mm/weaver/AGENTS.md @ e5f41572c338

<!-- rcw:begin owner=source:src_01def46fb45d53969c69b2fa33529280 block=evidence -->
- Repository development practice: tests use node:test with node:assert/strict, relative imports use explicit .ts extensions, pure logic is clock-injectable, and the core stays zero-runtime-dependency except picomatch. [@claim:clm_c942ed358ecbf9eae68ee3ea5904c196f4269e1d945b9346186cb49dbf973bea]
- Repository development practice: contributors run tests with npm test (node --test) and npm run test:bun (bun test), both of which must pass, plus npm run typecheck and npm run build. [@claim:clm_f684634f85579c3dce135998a0672517376d5c6341e7ce0cea1775366be85623]
- Repository development practice: Conventional Commits are mandatory and drive versioning via release-please; releases are cut by merging the release-please PR rather than hand-creating releases. [@claim:clm_fdae64f4fe72ba2fca9a00ff7f238827f62f72e697e6e5aa745fd85f50b9a0e0]
<!-- rcw:end owner=source:src_01def46fb45d53969c69b2fa33529280 block=evidence -->

## Researcher notes

