---
access: public
aliases: []
claim_ids:
- clm_a300f5fd1363645572eea38b580d4b0bd9250988789b7871958eb2084425f620
- clm_e945837735089e88937ef932609953ab14369972fbc0007997233238b0602dc1
maturity: draft
page_id: pg_5562599be660540db223bc6871f36255
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_79dec0bc4a935c9ab5f2970829598daa
title: ascorbic/am-i-vibing/CONTRIBUTING.md @ 39a2d1383d33
updated_at: '2026-09-14T03:36:01Z'
---

# ascorbic/am-i-vibing/CONTRIBUTING.md @ 39a2d1383d33

<!-- rcw:begin owner=source:src_79dec0bc4a935c9ab5f2970829598daa block=evidence -->
- Repository development practice: new providers must use verified environment variables (not guessed ones), follow a detection-method priority order, and pass a checklist including unit tests, real-environment and false-positive testing, and a changeset. [@claim:clm_a300f5fd1363645572eea38b580d4b0bd9250988789b7871958eb2084425f620]
- Repository development practice: provider unit tests go in test/detector.test.ts using a mock environment passed to detectAgenticEnvironment, and the CLI can be exercised with pnpm run cli (optionally --debug). [@claim:clm_e945837735089e88937ef932609953ab14369972fbc0007997233238b0602dc1]
<!-- rcw:end owner=source:src_79dec0bc4a935c9ab5f2970829598daa block=evidence -->

## Researcher notes

