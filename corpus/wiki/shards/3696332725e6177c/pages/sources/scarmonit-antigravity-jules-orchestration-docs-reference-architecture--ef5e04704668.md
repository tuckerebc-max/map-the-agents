---
access: public
aliases: []
claim_ids:
- clm_08d8af258fbc47bf85888001c6f96ee1446098cf5d645570565aaab3617343a8
- clm_7074de051b24963c255c3e73041ed8c2243e5ca0e879859df1bfb57daf50e46e
- clm_d31a662b07743d128b3f4709ee535c3cc08d52fe44c3d8ea5b7a4d815125b4a2
maturity: draft
page_id: pg_1d334d82817f56bab515ef5e04704668
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7262c466551b5dd2b6ddd0b3b2fa2f74
title: Scarmonit/antigravity-jules-orchestration/docs/reference/ARCHITECTURE.md @
  49d26f81817c
updated_at: '2026-09-14T04:19:55Z'
---

# Scarmonit/antigravity-jules-orchestration/docs/reference/ARCHITECTURE.md @ 49d26f81817c

<!-- rcw:begin owner=source:src_7262c466551b5dd2b6ddd0b3b2fa2f74 block=evidence -->
- The architecture positions Jules API as the inner-loop coding executor (clone, plan, edit, create PRs) with agent.scarmonit.com as an orchestration layer translating events into tasks and managing approval flows. [@claim:clm_08d8af258fbc47bf85888001c6f96ee1446098cf5d645570565aaab3617343a8]
- The system is event-driven, reacting to GitHub labels (jules-auto), comments (@jules plan this), PR review comments, monitoring webhooks, and CI build failures. [@claim:clm_7074de051b24963c255c3e73041ed8c2243e5ca0e879859df1bfb57daf50e46e]
- Safety design includes approval gates requiring a 'Plan Approved' state before code modification, stricter approval for high-risk infra/auth tasks, and all Jules output delivered via pull requests for human review. [@claim:clm_d31a662b07743d128b3f4709ee535c3cc08d52fe44c3d8ea5b7a4d815125b4a2]
<!-- rcw:end owner=source:src_7262c466551b5dd2b6ddd0b3b2fa2f74 block=evidence -->

## Researcher notes

