---
access: public
aliases: []
claim_ids:
- clm_16714afb5d316992c28803dd85912914f8cf29f5bcecc07877471a1ddb0228de
- clm_6470e77b6e5cdfa042ff27b3fab27f6b7dad712241e284be818ee5dc57395807
- clm_742dbdd84130d4a4f72e33af5ab890b91e8f6779fa12e8982cc47695739e74c7
- clm_c2e31087356a2932e37d1ebc9c7b8083d0a4b44e83d4364ee7e4c812a6b5d7a5
- clm_e2adc14c99702f12f6f24596de61e3736c145656179f72308feb2603f287cf56
- clm_f475384775a5a00165b86df217bd062deedd4a007e6fbbfc1b27739f182932b1
maturity: draft
page_id: pg_cd581a66bc5453da85fd0567ec37a630
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4713a86dd43c576bbc52a9107b3917a4
title: landing-ai/ade-cli/docs/ade-cli-v2-proposal.md @ d1995ffef4e6
updated_at: '2026-09-14T04:04:38Z'
---

# landing-ai/ade-cli/docs/ade-cli-v2-proposal.md @ d1995ffef4e6

<!-- rcw:begin owner=source:src_4713a86dd43c576bbc52a9107b3917a4 block=evidence -->
- The proposal defines parse as an idempotent state machine (absent/pending/complete/failed/expired) over the store, blocking by default with --wait, where Ctrl-C stops waiting but never the server-side work. [@claim:clm_16714afb5d316992c28803dd85912914f8cf29f5bcecc07877471a1ddb0228de]
- A draft v2 proposal (revised 2026-07-21) re-keys the store on job item ids — a hash of verb, source path, content, and params — replacing content-derived doc ids, with a flat ~/.ade/jobs/<id>/ layout. [@claim:clm_6470e77b6e5cdfa042ff27b3fab27f6b7dad712241e284be818ee5dc57395807]
- The proposal targets the ADE v2 API: async POST /v2/parse and /v2/extract job contracts, priority/standard service tiers, parse returning markdown plus a structure tree with inline grounding {page, range, box}. [@claim:clm_742dbdd84130d4a4f72e33af5ab890b91e8f6779fa12e8982cc47695739e74c7]
- Re-running an identical command consumes no credits because results persist in the local store; parse dedup serves stored results with an explicit notice and only `--force` re-bills. [@claim:clm_c2e31087356a2932e37d1ebc9c7b8083d0a4b44e83d4364ee7e4c812a6b5d7a5]
- The proposal notes the ADE v2 backend has no job cancel — submitted work always completes and bills — and encrypted PDFs are always rejected with a 422 (encrypted_pdf_unsupported). [@claim:clm_e2adc14c99702f12f6f24596de61e3736c145656179f72308feb2603f287cf56]
- Per the proposal, extract accepts a parse job item id, a document path (reusing the latest completed parse or auto-parsing first), or bring-your-own markdown, and field-to-box evidence is computed as a local join stored as evidence.json. [@claim:clm_f475384775a5a00165b86df217bd062deedd4a007e6fbbfc1b27739f182932b1]
<!-- rcw:end owner=source:src_4713a86dd43c576bbc52a9107b3917a4 block=evidence -->

## Researcher notes

