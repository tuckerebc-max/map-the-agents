---
access: public
aliases: []
claim_ids:
- clm_019a6d1b9241994c986dbbcc918fea4e0ec992c4ef898a4938edf78e9aafa185
- clm_4e4d1d0f957eabf056848f842ee69da2d9a1060de36538c50b9379a62b37c164
- clm_dd1571767c47fb08c21ec0b4c007f6a644525053b30c9e4e428bc7c5a24118c4
maturity: draft
page_id: pg_68c0e4c5b305563db750d0b506b6dab3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d3c3442a2cb35f4b92143775a9f91ccb
title: editor-code-assistant/eca/docs/config/skills.md @ e30026331ad6
updated_at: '2026-09-14T01:47:30Z'
---

# editor-code-assistant/eca/docs/config/skills.md @ e30026331ad6

<!-- rcw:begin owner=source:src_d3c3442a2cb35f4b92143775a9f91ccb block=evidence -->
- Skills are SKILL.md folders following the agentskills standard, searched in ~/.config/eca/skills, .eca/skills, and .agents/skills; only name and description are sent to the LLM, which loads a skill via the `eca__skill` tool. [@claim:clm_019a6d1b9241994c986dbbcc918fea4e0ec992c4ef898a4938edf78e9aafa185]
- Skills can be parameterized as slash commands using $ARGS, $ARGUMENTS, and positional variables; when arguments are given, ECA substitutes them into the skill body instead of using the eca__skill tool. [@claim:clm_4e4d1d0f957eabf056848f842ee69da2d9a1060de36538c50b9379a62b37c164]
- Tool-call approval is configurable globally or per agent with allow/deny rules and argsMatchers, e.g. denying `eca__skill` globally while allowing a specific skill name for one agent. [@claim:clm_dd1571767c47fb08c21ec0b4c007f6a644525053b30c9e4e428bc7c5a24118c4]
<!-- rcw:end owner=source:src_d3c3442a2cb35f4b92143775a9f91ccb block=evidence -->

## Researcher notes

