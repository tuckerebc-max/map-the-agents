---
access: public
aliases: []
claim_ids:
- clm_0df76e340b358da39d08cadc318614a1b41ebf0703fbb54750ca874f4ea62313
- clm_14a69fd5e9aa4cdfe323c078de6e61ff61da7e610e14ecc091c1802b026f5609
maturity: draft
page_id: pg_672b41bc0fb65b9da936d7d8186b0991
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c52f5f5c0ff05bd2b9e93bf041eecbdb
title: vocodedev/vocode-core/docs/actions.mdx @ e054c33a7278
updated_at: '2026-09-14T04:31:45Z'
---

# vocodedev/vocode-core/docs/actions.mdx @ e054c33a7278

<!-- rcw:begin owner=source:src_c52f5f5c0ff05bd2b9e93bf041eecbdb block=evidence -->
- A hosted REST API at api.vocode.dev exposes endpoints such as /v1/actions/create and /v1/numbers/update with Bearer-token authentication, shown in Python, TypeScript, and cURL examples. [@claim:clm_0df76e340b358da39d08cadc318614a1b41ebf0703fbb54750ca874f4ea62313]
- Actions fire via two trigger mechanisms: the default FunctionCallActionTrigger, where the agent decides based on prompting, or PhraseBasedActionTrigger, which fires after the bot speaks a configured phrase. [@claim:clm_14a69fd5e9aa4cdfe323c078de6e61ff61da7e610e14ecc091c1802b026f5609]
<!-- rcw:end owner=source:src_c52f5f5c0ff05bd2b9e93bf041eecbdb block=evidence -->

## Researcher notes

