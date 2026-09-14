---
access: public
aliases: []
claim_ids:
- clm_ea76b3cd23d31bb7c1bd2f03431942a813d45aae3a2ed963f18ed0290a1ef2fb
- clm_f0ead2dfe1eb6f65a6454b29a6307f741f7cd1533a730aa3dea386e76c6535bc
- clm_f91685431e1d62c25b8b3b80a97ba9903b98796c4b53200736b3eeef2492cb50
maturity: draft
page_id: pg_3f521fc86fa2552f84e35943f595da27
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6760d0311ba75608abc669476b6bc308
title: respeak-io/episko/RELEASE.md @ 974192b540db
updated_at: '2026-09-14T02:36:30Z'
---

# respeak-io/episko/RELEASE.md @ 974192b540db

<!-- rcw:begin owner=source:src_6760d0311ba75608abc669476b6bc308 block=evidence -->
- Repository development practice: CI runs on every push and PR to dev/main on both macOS and Windows, covering strict tsc typecheck, vitest suites (~1,535 it blocks), cargo check/test --locked (~270 #[test] functions) and clippy with -D warnings. [@claim:clm_ea76b3cd23d31bb7c1bd2f03431942a813d45aae3a2ed963f18ed0290a1ef2fb]
- The app detects external Claude sessions started outside Episko and shows them as read-only mirrors in the sidebar, and can jump to the terminal tab or window hosting such a session. [@claim:clm_f0ead2dfe1eb6f65a6454b29a6307f741f7cd1533a730aa3dea386e76c6535bc]
- Repository development practice: ignored cargo contract tests against real Claude Code (instrumentation, permission modes, temp-dir layout) are run manually via cargo test -- --ignored because CI lacks claude on PATH; one of them spends tokens and needs authentication. [@claim:clm_f91685431e1d62c25b8b3b80a97ba9903b98796c4b53200736b3eeef2492cb50]
<!-- rcw:end owner=source:src_6760d0311ba75608abc669476b6bc308 block=evidence -->

## Researcher notes

