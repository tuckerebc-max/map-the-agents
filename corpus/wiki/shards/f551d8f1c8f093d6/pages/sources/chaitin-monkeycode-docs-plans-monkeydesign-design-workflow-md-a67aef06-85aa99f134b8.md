---
access: public
aliases: []
claim_ids:
- clm_16217d9acbcbc15cb19c14496e29cddb8589dab2e0b9ebd5a2823bc10ea93135
- clm_2babaa4f99befd1e281460e2df19a1ad90982116b00736448176f48a9a48e494
- clm_9c3a5f1370a4fd338e36f3b39026d555ec610090021541e41fd60c25542c6532
- clm_bab0f642bd4682e07151be6145be1d06974dfbd81a29c020aa8737539c19000e
- clm_bb0c595ad37cead759be14608f5c310a64d9f8337ff3bd0a0b22ccef951e4cf2
maturity: draft
page_id: pg_19b2000897f9599f95c885aa99f134b8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5d714be338465d1bb615a87deb8aeaa1
title: chaitin/MonkeyCode/docs/plans/monkeydesign-design-workflow.md @ a67aef068778
updated_at: '2026-09-14T01:39:55Z'
---

# chaitin/MonkeyCode/docs/plans/monkeydesign-design-workflow.md @ a67aef068778

<!-- rcw:begin owner=source:src_5d714be338465d1bb615a87deb8aeaa1 block=evidence -->
- A DesignFlowState state machine is proposed so the design flow persists explicit stage state rather than relying on model memory; it appears to be a design proposal, not verified shipped code. [@claim:clm_16217d9acbcbc15cb19c14496e29cddb8589dab2e0b9ebd5a2823bc10ea93135]
- The plan lists non-goals including Figma two-way sync, a public design-pattern marketplace, multi-user collaboration and org-level permissions, and automatic production deployment. [@claim:clm_2babaa4f99befd1e281460e2df19a1ad90982116b00736448176f48a9a48e494]
- The plan notes the image generation provider is not yet integrated into the current MonkeyDesign runtime, and Open Design code/assets licensing needs confirmation. [@claim:clm_9c3a5f1370a4fd338e36f3b39026d555ec610090021541e41fd60c25542c6532]
- A design-workflow plan proposes extracting design patterns via Skills/Atoms (code-import, design-extract, token-map, rewrite-plan), saved as Design System Packages with revisions so re-extraction creates a new revision rather than overwriting. [@claim:clm_bab0f642bd4682e07151be6145be1d06974dfbd81a29c020aa8737539c19000e]
- The plan proposes new agent-client protocol messages (design/start-choice, template/reference/pattern selection, redesign-level) because plain AskUserQuestion cannot carry images; these appear to be proposals, not shipped behavior. [@claim:clm_bb0c595ad37cead759be14608f5c310a64d9f8337ff3bd0a0b22ccef951e4cf2]
<!-- rcw:end owner=source:src_5d714be338465d1bb615a87deb8aeaa1 block=evidence -->

## Researcher notes

