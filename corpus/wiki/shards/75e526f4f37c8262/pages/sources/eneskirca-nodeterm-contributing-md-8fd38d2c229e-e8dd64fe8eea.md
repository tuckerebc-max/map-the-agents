---
access: public
aliases: []
claim_ids:
- clm_36c34b27f25898c9ea153d3d4bc65b66f48916b9dff2036ebc70a7fdd2f1a3d7
- clm_3f898eaa8d37498fe04c0500d3acb5e9bd1268b603d1a4ea416ada4bc7a7d947
- clm_897141901f4d7d443af844eafbad34eac0a0b294dcf626b3cb507b0b77601353
maturity: draft
page_id: pg_4b32ce1f27e55134b2efe8dd64fe8eea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7382c6b6bb4d5184bdbd1e5c4761ecb1
title: eneskirca/nodeterm/CONTRIBUTING.md @ 8fd38d2c229e
updated_at: '2026-09-14T01:48:25Z'
---

# eneskirca/nodeterm/CONTRIBUTING.md @ 8fd38d2c229e

<!-- rcw:begin owner=source:src_7382c6b6bb4d5184bdbd1e5c4761ecb1 block=evidence -->
- Repository development practice: the process-boundary split is enforced by guard tests that fail if src/core or src/server import electron or ../main/*, and new service logic must go in src/core behind CorePlatform. [@claim:clm_36c34b27f25898c9ea153d3d4bc65b66f48916b9dff2036ebc70a7fdd2f1a3d7]
- Repository development practice: contributors run npm install, npm run dev, npm run typecheck (described as the fastest correctness gate), and npm test (vitest unit + integration); Windows uses bootstrap-windows.bat instead of npm install. [@claim:clm_3f898eaa8d37498fe04c0500d3acb5e9bd1268b603d1a4ea416ada4bc7a7d947]
- Repository development practice: house rules require atomic file writes via renameAtomic/writeFileAtomic, an 'error' listener on child stdin before the first write, and credentials never passed on argv, each backed by guard tests that fail PRs. [@claim:clm_897141901f4d7d443af844eafbad34eac0a0b294dcf626b3cb507b0b77601353]
<!-- rcw:end owner=source:src_7382c6b6bb4d5184bdbd1e5c4761ecb1 block=evidence -->

## Researcher notes

