---
access: public
aliases: []
claim_ids:
- clm_9f339a154cef17c117c94f754284d95930942068fa1df8146c525fa2b1710aa4
- clm_b0b688b5223542f70b6e1affc3ef31aa9e227600fad64d59f97e4e36264da7cd
maturity: draft
page_id: pg_c64000b598f252038c5aa34fb15fc67b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_52452562738d5a239d41482ce11d2402
title: 233i/ore-code/docs/06-skill-system.md @ b36da0c05720
updated_at: '2026-09-14T01:58:37Z'
---

# 233i/ore-code/docs/06-skill-system.md @ b36da0c05720

<!-- rcw:begin owner=source:src_52452562738d5a239d41482ce11d2402 block=evidence -->
- Skills are user-level reusable workflow instructions stored at ~/.ore-code/skills/<skill-id>/SKILL.md; each skill auto-registers a slash command and its content is injected into the current prompt. [@claim:clm_9f339a154cef17c117c94f754284d95930942068fa1df8146c525fa2b1710aa4]
- Skills are documentation-like instructions, not plugin code, and do not execute arbitrary scripts; actual file, shell, and git actions still go through existing tools and the approval system. [@claim:clm_b0b688b5223542f70b6e1affc3ef31aa9e227600fad64d59f97e4e36264da7cd]
<!-- rcw:end owner=source:src_52452562738d5a239d41482ce11d2402 block=evidence -->

## Researcher notes

