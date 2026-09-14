---
access: public
aliases: []
claim_ids:
- clm_1612c38b10873705cd879a8d57110042cfa21f9ec639491cb166db177fb2278f
- clm_174893598bfa0d8a6ac24e3d857bdd22542c7782ba5bc625f13d635a63afccac
- clm_1974d039e9b1fa7f25478ecb9c7428fa87fd60cd0137cde7f00f42830bae539d
- clm_3591358bdd82f847a58fcbcb18935f6e0dfc606d4025bbe0407d44f8369a719f
- clm_4e9b57bb63a41f3280ffc01130e169fa6e7ad874d294302a7aee516981a218ec
- clm_56c8f3ce8999e7883dab8ceb9e6cc47b05d3486727e7bf5f41ef6ac6d7db479e
- clm_618651a901534b876b287f0590086076e9c334194843dcda2a816ab195c31007
- clm_abb45277b201e88ee5e1fff573d7d7a2f49dc961d576effac7bc9396e83ce8ae
maturity: draft
page_id: pg_fc39b28014e05d1682f9443e67c48011
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7c8aec717c7c5567adb07a11adcdcf72
title: Junliu1066/vibe-coding-kit/README.md @ cb387af342e6
updated_at: '2026-09-14T04:02:16Z'
---

# Junliu1066/vibe-coding-kit/README.md @ cb387af342e6

<!-- rcw:begin owner=source:src_7c8aec717c7c5567adb07a11adcdcf72 block=evidence -->
- Usage paths documented: paste a SKILL.md into any chat (Claude/ChatGPT/Codex), upload a skill folder to claude.ai settings, or copy folders into ~/.claude/skills/ for Claude Code auto-triggering. [@claim:clm_1612c38b10873705cd879a8d57110042cfa21f9ec639491cb166db177fb2278f]
- The kit targets non-coders or beginners (PMs, founders, indie developers) who build products via AI, aiming to teach requirements clarity and discipline rather than coding. [@claim:clm_174893598bfa0d8a6ac24e3d857bdd22542c7782ba5bc625f13d635a63afccac]
- Repository development practice: contributions via Issue and PR are welcomed, with requested style of plain language, stating costs, and avoiding complexity. [@claim:clm_1974d039e9b1fa7f25478ecb9c7428fa87fd60cd0137cde7f00f42830bae539d]
- A three-layer governance system is described: CLAUDE.md as auto-loaded constitution, a harness skill for post-hoc artifact validation, and per-SKILL.md pre-delivery checklists, all derived from a root harness.json config. [@claim:clm_3591358bdd82f847a58fcbcb18935f6e0dfc606d4025bbe0407d44f8369a719f]
- Process state lives in docs/进度账本.md, which the AI must read at the start of each turn and update after each gate; a .dsu/progress/ card system (index, module, task files) handles development-context recovery. [@claim:clm_4e9b57bb63a41f3280ffc01130e169fa6e7ad874d294302a7aee516981a218ec]
- harness.json is the single source of truth from which CLAUDE.md, the harness skill, and SKILL.md checklists are derived, so editing one place keeps the three layers in sync. [@claim:clm_56c8f3ce8999e7883dab8ceb9e6cc47b05d3486727e7bf5f41ef6ac6d7db479e]
- The kit ships six skills (prd, requirements, architecture, production, survival, harness), each a folder with a SKILL.md in a generic skill format, intended to trigger automatically when needed. [@claim:clm_618651a901534b876b287f0590086076e9c334194843dcda2a816ab195c31007]
- The harness.json workflow block defines an ordered S1 requirements → S2 architecture → S3 launch pipeline with entry/exit gates, per-step exit conditions, and rules that skipped steps must be recorded in the ledger. [@claim:clm_abb45277b201e88ee5e1fff573d7d7a2f49dc961d576effac7bc9396e83ce8ae]
<!-- rcw:end owner=source:src_7c8aec717c7c5567adb07a11adcdcf72 block=evidence -->

## Researcher notes

