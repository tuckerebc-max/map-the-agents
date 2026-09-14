---
access: public
aliases: []
claim_ids:
- clm_99f38ef03d95427a3ef5cbefaf52bf96b869e3dbe35dea01b1159a008c70eab8
maturity: draft
page_id: pg_14088ec4837e56618f9563c483e23cd9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3987d8bc94a15f189c12bede1626f7e0
title: QwenLM/qwen-code/docs/design/daemon-sidechannel-coordination/design.md @ 7e0beb9d1823
updated_at: '2026-09-14T02:34:00Z'
---

# QwenLM/qwen-code/docs/design/daemon-sidechannel-coordination/design.md @ 7e0beb9d1823

<!-- rcw:begin owner=source:src_3987d8bc94a15f189c12bede1626f7e0 block=evidence -->
- A daemon side-channel coordination design doc specifies that in-session model changes are demuxed from `extNotification()` while approval-mode changes use the ACP `current_mode_update` sessionUpdate, since no `current_model_update` ACP type exists. [@claim:clm_99f38ef03d95427a3ef5cbefaf52bf96b869e3dbe35dea01b1159a008c70eab8]
<!-- rcw:end owner=source:src_3987d8bc94a15f189c12bede1626f7e0 block=evidence -->

## Researcher notes

