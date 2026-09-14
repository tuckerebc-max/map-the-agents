---
access: public
aliases: []
claim_ids:
- clm_4d8bc7825855389170daecb49ea3b693b282ab114288602de290d30e2eb73f6e
- clm_9b91732c095465e78c07c8bfc395c9576fccb738fddb1e5a0f64e9f67db71edd
maturity: draft
page_id: pg_59b9a6cdc9dc5370a812cc68f0cc91cc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f4840b9d60c7513ea0881a81a6dfcf63
title: feiskyer/koder/docs/configuration.md @ 55f553326039
updated_at: '2026-09-14T02:01:03Z'
---

# feiskyer/koder/docs/configuration.md @ 55f553326039

<!-- rcw:begin owner=source:src_f4840b9d60c7513ea0881a81a6dfcf63 block=evidence -->
- Permission rules live in settings files under permissions.allow/deny as tool_name(content) strings with deny winning over allow; KODER_ENFORCE_TOOL_APPROVAL controls approval-required tool calls, failing closed when non-interactive by default. [@claim:clm_4d8bc7825855389170daecb49ea3b693b282ab114288602de290d30e2eb73f6e]
- An optional local managed policy file ~/.koder/managed-settings.json can define high-priority hook settings and sandbox policy keys (enabled, mode, backend, autoAllowBashIfSandboxed); no hosted managed-settings service is fetched. [@claim:clm_9b91732c095465e78c07c8bfc395c9576fccb738fddb1e5a0f64e9f67db71edd]
<!-- rcw:end owner=source:src_f4840b9d60c7513ea0881a81a6dfcf63 block=evidence -->

## Researcher notes

