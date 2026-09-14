---
access: public
aliases: []
claim_ids:
- clm_1276ffb54e4b6331b803d996ab074d2565f301e8cbf03d0f3c2592d4fc0abd83
- clm_5ffeacd238e9e66ec3ac2078cc8f66e39d8f483f8ea73120274975deb9275860
- clm_9afb7575a6f2604fac857d102c0d280dd985a9605f32b3feaca1c1ecae041022
- clm_c2083a220943671988732b903870f908fc87a3a9ca3faeb6e857176ad30bbb22
- clm_cbad277d11aa5beb31b33f70cedd99d942b51f055853150bf9894e34b7e5c41c
- clm_d4e0b0b632a3adb7cc9c1085183f87f44e2bea3ea8f7506840d0b3eb4d5b9d09
- clm_f93c4b67dac4fbe0eb8cd8f9c8d4bf5c1d0d7c42b988e07a7fdad30c40b83110
maturity: draft
page_id: pg_864d11fb808b5a35b8880ebeff89e727
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_51aa2609c6805ea88a967845b632fa2f
title: 2389-research/claude-plugins/docs/DEVELOPMENT.md @ 017d34612ebf
updated_at: '2026-09-14T03:28:23Z'
---

# 2389-research/claude-plugins/docs/DEVELOPMENT.md @ 017d34612ebf

<!-- rcw:begin owner=source:src_51aa2609c6805ea88a967845b632fa2f block=evidence -->
- Repository development practice: a manual testing checklist covers auto-detection, sub-skill routing, TodoWrite checklists, correct tool use (Read, Edit, Write, Grep), and output format. [@claim:clm_1276ffb54e4b6331b803d996ab074d2565f301e8cbf03d0f3c2592d4fc0abd83]
- Skills are defined in SKILL.md markdown files with YAML frontmatter containing a name and a description used for auto-detection. [@claim:clm_5ffeacd238e9e66ec3ac2078cc8f66e39d8f483f8ea73120274975deb9275860]
- Repository development practice: skill authoring guidance requires granular TodoWrite items (2-5 minutes each), complete runnable code examples, and exact file paths rather than vague references. [@claim:clm_9afb7575a6f2604fac857d102c0d280dd985a9605f32b3feaca1c1ecae041022]
- The css-development and firebase-development plugins use a main orchestrator SKILL.md plus sub-skill directories (e.g., create-component, validate, refactor; project-setup, add-feature, debug). [@claim:clm_c2083a220943671988732b903870f908fc87a3a9ca3faeb6e857176ad30bbb22]
- Repository development practice: after modifying a skill, contributors copy it into ~/.claude/skills/, test manually against tests/integration scenarios, and verify auto-detection, TodoWrite checklists, and step ordering. [@claim:clm_cbad277d11aa5beb31b33f70cedd99d942b51f055853150bf9894e34b7e5c41c]
- All Firebase patterns are centralized in the main firebase-development SKILL.md (1323 lines), and sub-skills reference them via '@firebase-development/pattern-name' syntax. [@claim:clm_d4e0b0b632a3adb7cc9c1085183f87f44e2bea3ea8f7506840d0b3eb4d5b9d09]
- Key CSS patterns include semantic class naming, Tailwind composition with @apply, dark mode by default, and static plus component-rendering test coverage. [@claim:clm_f93c4b67dac4fbe0eb8cd8f9c8d4bf5c1d0d7c42b988e07a7fdad30c40b83110]
<!-- rcw:end owner=source:src_51aa2609c6805ea88a967845b632fa2f block=evidence -->

## Researcher notes

