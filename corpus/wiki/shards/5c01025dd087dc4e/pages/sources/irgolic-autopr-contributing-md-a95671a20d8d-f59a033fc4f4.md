---
access: public
aliases: []
claim_ids:
- clm_399d16008598e563f5393cf1f00baae7e37cec11739885977cfcd5d1dd0a184a
- clm_778e6a72ac56a618bb891b46e62e44b2cd49daeae71496fa3b050c9f1003a60a
- clm_b653979a20ef02eb3857e1d830d13833759dc79f1f4d1d0fba37233b746f4c0b
maturity: draft
page_id: pg_39e605ad76555b9d8b81f59a033fc4f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0dc6ce3784a15daf8cfeeab0b3bc3340
title: irgolic/AutoPR/CONTRIBUTING.md @ a95671a20d8d
updated_at: '2026-09-14T02:05:59Z'
---

# irgolic/AutoPR/CONTRIBUTING.md @ a95671a20d8d

<!-- rcw:begin owner=source:src_0dc6ce3784a15daf8cfeeab0b3bc3340 block=evidence -->
- Repository development practice: contributors extend AutoPR by subclassing Action (with an id and run method) or Agent (with handle_event), and actions share state via a ContextDict passed between actions. [@claim:clm_399d16008598e563f5393cf1f00baae7e37cec11739885977cfcd5d1dd0a184a]
- Repository development practice: only the IssueLabeledEvent event type is currently supported, with events defined in autopr/models/events.py. [@claim:clm_778e6a72ac56a618bb891b46e62e44b2cd49daeae71496fa3b050c9f1003a60a]
- Repository development practice: each rail run makes two LLM calls — a natural-language chat message, then a guardrails call serializing the response to typed JSON. [@claim:clm_b653979a20ef02eb3857e1d830d13833759dc79f1f4d1d0fba37233b746f4c0b]
<!-- rcw:end owner=source:src_0dc6ce3784a15daf8cfeeab0b3bc3340 block=evidence -->

## Researcher notes

