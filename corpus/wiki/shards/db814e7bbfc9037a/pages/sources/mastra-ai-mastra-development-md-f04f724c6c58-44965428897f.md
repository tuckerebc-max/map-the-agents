---
access: public
aliases: []
claim_ids:
- clm_93816dff1c7a4a0dad4c9622f94c5f5aab4828c642ece3cc6caeb880da61b1de
- clm_c3eeeda604e6165440d2b77504966437332ee5982c721648c815c82540582abf
- clm_cfbf1c9e310f12bd94bba745795457633bb28dbd75dc734c0528308d601e379c
maturity: draft
page_id: pg_60984fa49b9b5a2e8df344965428897f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c0bf6bb2883e5b71b972e40dd6096e57
title: mastra-ai/mastra/DEVELOPMENT.md @ f04f724c6c58
updated_at: '2026-09-14T02:16:42Z'
---

# mastra-ai/mastra/DEVELOPMENT.md @ f04f724c6c58

<!-- rcw:begin owner=source:src_c0bf6bb2883e5b71b972e40dd6096e57 block=evidence -->
- Repository development practice: contributors need Node.js v22.13.0+, pnpm v10.18.0+ (enabled via corepack), and optionally Docker for a subset of tests; setup uses pnpm run setup to install dependencies and build the CLI package. [@claim:clm_93816dff1c7a4a0dad4c9622f94c5f5aab4828c642ece3cc6caeb880da61b1de]
- Repository development practice: PRs must link a relevant issue (e.g., Fixes #1234) or be closed; Coderabbit and Mastra Platform automatically comment on PRs, and contributors are asked to address all review comments. [@claim:clm_c3eeeda604e6165440d2b77504966437332ee5982c721648c815c82540582abf]
- Repository development practice: testing uses Vitest with pnpm test and per-package scripts; some tests require environment variables such as OPENAI_API_KEY and a local PostgreSQL DB_URL, with services started via pnpm run dev:services:up. [@claim:clm_cfbf1c9e310f12bd94bba745795457633bb28dbd75dc734c0528308d601e379c]
<!-- rcw:end owner=source:src_c0bf6bb2883e5b71b972e40dd6096e57 block=evidence -->

## Researcher notes

