---
access: public
aliases: []
claim_ids:
- clm_0021cf51c63bd3e36b565e6987acf9faddc9d7814c113f8c4c95e0ebbeb952c0
- clm_1b63d0f83240485fa164f987a9fa4d1fadac8469dd1500f42e2c2317a222e4da
- clm_3df0c98e0533218c819df3ddc92e8f3d89a964db4f3f9b9546fd63c0e3f9683a
- clm_c7ec9f7aee411fe82f84ae67049157813defb12b06b4478849a051a175ca4285
maturity: draft
page_id: pg_ebb6c72569a05f0aa52eedf35efdd4aa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9002e17cd985507394a8f1977ab77890
title: cfal/garcon/AGENTS.md @ 42a5322794a9
updated_at: '2026-09-14T01:39:41Z'
---

# cfal/garcon/AGENTS.md @ 42a5322794a9

<!-- rcw:begin owner=source:src_9002e17cd985507394a8f1977ab77890 block=evidence -->
- Repository development practice: the frontend must follow canonical Svelte 5 patterns, including $state/$derived/$effect rune usage, callback props instead of createEventDispatcher, and typed context helpers rather than string-keyed context. [@claim:clm_0021cf51c63bd3e36b565e6987acf9faddc9d7814c113f8c4c95e0ebbeb952c0]
- Repository development practice: every WebSocket/API contract change requires updated type definitions, sender and receiver logic, tests, and a migration note in the PR description when behavior changes. [@claim:clm_1b63d0f83240485fa164f987a9fa4d1fadac8469dd1500f42e2c2317a222e4da]
- Repository development practice: integration coverage is mandatory when correctness crosses server, transport, persistence, provider, or SPA boundaries, with black-box server tests under integration-tests/tests/server and live-agent suites kept under test:live:* gated by PR CI. [@claim:clm_3df0c98e0533218c819df3ddc92e8f3d89a964db4f3f9b9546fd63c0e3f9683a]
- Repository development practice: AGENTS.md directs contributors to use bun instead of npm, run `bun run test` to validate changes, start new servers on different ports rather than killing running ones, and treat the git tree as read-only unless instructed. [@claim:clm_c7ec9f7aee411fe82f84ae67049157813defb12b06b4478849a051a175ca4285]
<!-- rcw:end owner=source:src_9002e17cd985507394a8f1977ab77890 block=evidence -->

## Researcher notes

