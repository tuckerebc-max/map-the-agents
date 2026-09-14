---
access: public
aliases: []
claim_ids:
- clm_066e542d2001fc7243fb5864bd33c099e22e6736f4e36f596d3fe680e8dab508
- clm_8f1cbf5530a23deda01537e2cedf676823793c19414529ea1dde1db0fdacd123
maturity: draft
page_id: pg_a9ca2a938e215813a85a60bc4247861e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5388956710b25682926147d6be88924f
title: NorviaLabs/forge/FORGE-DESIGN.md @ 8a1c5e85ec5c
updated_at: '2026-09-14T02:23:41Z'
---

# NorviaLabs/forge/FORGE-DESIGN.md @ 8a1c5e85ec5c

<!-- rcw:begin owner=source:src_5388956710b25682926147d6be88924f block=evidence -->
- Colours are semantic tokens defined per theme rather than fixed hex values, and the design system names ACCENT_STATUS_MIN_HUE_DISTANCE as its single hardest rule, asserted over built-in themes in tests. [@claim:clm_066e542d2001fc7243fb5864bd33c099e22e6736f4e36f596d3fe680e8dab508]
- Core UX invariants include exactly one effective keyboard owner at a time, colour never being the sole state indicator, approvals and failures outranking routine activity, and refusing to render below an enforced minimum of 80x18. [@claim:clm_8f1cbf5530a23deda01537e2cedf676823793c19414529ea1dde1db0fdacd123]
<!-- rcw:end owner=source:src_5388956710b25682926147d6be88924f block=evidence -->

## Researcher notes

