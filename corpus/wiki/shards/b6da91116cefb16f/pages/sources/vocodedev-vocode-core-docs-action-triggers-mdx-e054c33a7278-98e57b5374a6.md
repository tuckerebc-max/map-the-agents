---
access: public
aliases: []
claim_ids:
- clm_14a69fd5e9aa4cdfe323c078de6e61ff61da7e610e14ecc091c1802b026f5609
- clm_cf11b136c8a82144e1ff2886eb3c9d6bc424ece6fa771e12d775b2f509b03dce
maturity: draft
page_id: pg_6a97bc34f0be57bdb5a798e57b5374a6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dc8e0c85b3e351dda300287389d89846
title: vocodedev/vocode-core/docs/action-triggers.mdx @ e054c33a7278
updated_at: '2026-09-14T04:31:45Z'
---

# vocodedev/vocode-core/docs/action-triggers.mdx @ e054c33a7278

<!-- rcw:begin owner=source:src_dc8e0c85b3e351dda300287389d89846 block=evidence -->
- Actions fire via two trigger mechanisms: the default FunctionCallActionTrigger, where the agent decides based on prompting, or PhraseBasedActionTrigger, which fires after the bot speaks a configured phrase. [@claim:clm_14a69fd5e9aa4cdfe323c078de6e61ff61da7e610e14ecc091c1802b026f5609]
- The only supported phrase-trigger condition type is 'phrase_condition_type_contains', which matches case-insensitively against the bot's spoken turn. [@claim:clm_cf11b136c8a82144e1ff2886eb3c9d6bc424ece6fa771e12d775b2f509b03dce]
<!-- rcw:end owner=source:src_dc8e0c85b3e351dda300287389d89846 block=evidence -->

## Researcher notes

