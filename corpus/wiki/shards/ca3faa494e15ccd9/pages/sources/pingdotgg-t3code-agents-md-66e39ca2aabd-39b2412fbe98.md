---
access: public
aliases: []
claim_ids:
- clm_21c6581f38a29aa5ddaa97430425b0326517ea7485a8c3e357aaa150b2dc2583
- clm_434357f4a42766d3350f3bc159773965380f148534972aebbff6fd38da314547
- clm_d5b2b4134a6b5dd9ec3222f3cc9fe8550bc87ad39ddf5c511a70c21578b55ab7
maturity: draft
page_id: pg_8278d151c611553395da39b2412fbe98
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4635faf0c15555d78eb91106fedfb397
title: pingdotgg/t3code/AGENTS.md @ 66e39ca2aabd
updated_at: '2026-09-14T03:12:02Z'
---

# pingdotgg/t3code/AGENTS.md @ 66e39ca2aabd

<!-- rcw:begin owner=source:src_4635faf0c15555d78eb91106fedfb397 block=evidence -->
- Repository development practice: AGENTS.md forbids killing processes by name/path matching, forbids starting servers against or writing to the live ~/.t3/userdata database, and forbids setting VITE_HTTP_URL/VITE_WS_URL in dev because Vite proxies /api, /ws, /oauth, and /.well-known. [@claim:clm_21c6581f38a29aa5ddaa97430425b0326517ea7485a8c3e357aaa150b2dc2583]
- Repository development practice: verification uses targeted `vp test run` on touched files plus scoped lint/typecheck; repo-wide checks like `vp check` are reserved for CI, and tests must wait on typed receipts rather than sleeps or timeouts. [@claim:clm_434357f4a42766d3350f3bc159773965380f148534972aebbff6fd38da314547]
- Repository development practice: agents must never open a PR unless the developer explicitly asks; PRs use conventional-commit titles, one concern per PR, before/after images for UI changes, and evidence uploaded to GitHub rather than committed. [@claim:clm_d5b2b4134a6b5dd9ec3222f3cc9fe8550bc87ad39ddf5c511a70c21578b55ab7]
<!-- rcw:end owner=source:src_4635faf0c15555d78eb91106fedfb397 block=evidence -->

## Researcher notes

