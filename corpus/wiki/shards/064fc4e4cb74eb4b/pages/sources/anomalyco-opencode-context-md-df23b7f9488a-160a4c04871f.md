---
access: public
aliases: []
claim_ids:
- clm_645ac21eec51b4cff13e948c1f843e5af8a06e547f02ce06d3ac89ef6585cda7
- clm_76811de7c97bae5ef508e5093e34fb07476bb588abef97791352c5e1feacb3af
- clm_9cd244ecc341f8f15c68a067fe2177e5916cb3901bdcc67957c0084961560d26
- clm_d2adc8097b8bd0ef4ea7fbabdfb8bed7b1a3e2021af15b73cf1be3316352ab7c
maturity: draft
page_id: pg_88b85824ac8f5bc19d8a160a4c04871f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5ada12a6318b55cfa75484d124e1a778
title: anomalyco/opencode/CONTEXT.md @ df23b7f9488a
updated_at: '2026-09-14T01:33:42Z'
---

# anomalyco/opencode/CONTEXT.md @ df23b7f9488a

<!-- rcw:begin owner=source:src_5ada12a6318b55cfa75484d124e1a778 block=evidence -->
- The client architecture derives Promise and Effect SDK clients from a public HttpApi; an Embedded OpenCode host reuses the same router and handlers over an in-memory HTTP transport. [@claim:clm_645ac21eec51b4cff13e948c1f843e5af8a06e547f02ce06d3ac89ef6585cda7]
- CONTEXT.md flags that the legacy experimental.chat.system.transform plugin hook can arbitrarily mutate the baseline system prompt, and V2 plugins do not yet expose an equivalent hook. [@claim:clm_76811de7c97bae5ef508e5093e34fb07476bb588abef97791352c5e1feacb3af]
- Tool outputs exceeding history limits are projected into bounded Model Tool Output, with full oversized output retained in a managed temporary file under a shared tool-output directory. [@claim:clm_9cd244ecc341f8f15c68a067fe2177e5916cb3901bdcc67957c0084961560d26]
- CONTEXT.md defines a session runtime where sessions preserve durable conversation history and assemble a System Context from typed Context Sources, with changes admitted as Mid-Conversation System Messages at safe provider-turn boundaries. [@claim:clm_d2adc8097b8bd0ef4ea7fbabdfb8bed7b1a3e2021af15b73cf1be3316352ab7c]
<!-- rcw:end owner=source:src_5ada12a6318b55cfa75484d124e1a778 block=evidence -->

## Researcher notes

