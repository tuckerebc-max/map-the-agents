---
access: public
aliases: []
claim_ids:
- clm_515482ce6a93ea180337fa684440ba60602dadf797d1ddf47dd3c4ddb3de00f5
- clm_6e6093a7e4607f3112db51914fce343730c6de76e3481b7287ef80b388d44e37
maturity: draft
page_id: pg_5f122036c26b5824bc2ce61ddea8ceec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7a8e0b7114ad561b9d24a0b262e4ef8d
title: Grik-ai/ricochet/SECURITY.md @ 706fceac6a3e
updated_at: '2026-09-14T01:52:28Z'
---

# Grik-ai/ricochet/SECURITY.md @ 706fceac6a3e

<!-- rcw:begin owner=source:src_7a8e0b7114ad561b9d24a0b262e4ef8d block=evidence -->
- SECURITY.md's 'Not A Security Boundary' section lists model output text, markdown rendering alone, checkpoint existence, UI permission labels, and local config files holding secrets. [@claim:clm_515482ce6a93ea180337fa684440ba60602dadf797d1ddf47dd3c4ddb3de00f5]
- The agent can read files, propose edits, and run commands in the workspace; permissions, approvals, checkpoints, and pending-change review are described as safety controls but explicitly not a complete sandbox. [@claim:clm_6e6093a7e4607f3112db51914fce343730c6de76e3481b7287ef80b388d44e37]
<!-- rcw:end owner=source:src_7a8e0b7114ad561b9d24a0b262e4ef8d block=evidence -->

## Researcher notes

