---
access: public
aliases: []
claim_ids:
- clm_4e9b57bb63a41f3280ffc01130e169fa6e7ad874d294302a7aee516981a218ec
- clm_56c8f3ce8999e7883dab8ceb9e6cc47b05d3486727e7bf5f41ef6ac6d7db479e
- clm_abb45277b201e88ee5e1fff573d7d7a2f49dc961d576effac7bc9396e83ce8ae
- clm_bff7687b8f21c5b6d86497a1b103a393cbf564ec2d77c8e137df75b1b1b8ebde
- clm_cba5d1cb47488cb1f9d11d498dfaab322b6fd6a3e4783ff57c08040333bbf20b
maturity: draft
page_id: pg_9c02f0d67bfb5dffb617c212a90ab203
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b62eccb51bdc50dbbe514da4c647e0c0
title: Junliu1066/vibe-coding-kit/docs/Harness-v2-重设计方案.md @ cb387af342e6
updated_at: '2026-09-14T04:02:16Z'
---

# Junliu1066/vibe-coding-kit/docs/Harness-v2-重设计方案.md @ cb387af342e6

<!-- rcw:begin owner=source:src_b62eccb51bdc50dbbe514da4c647e0c0 block=evidence -->
- Process state lives in docs/进度账本.md, which the AI must read at the start of each turn and update after each gate; a .dsu/progress/ card system (index, module, task files) handles development-context recovery. [@claim:clm_4e9b57bb63a41f3280ffc01130e169fa6e7ad874d294302a7aee516981a218ec]
- harness.json is the single source of truth from which CLAUDE.md, the harness skill, and SKILL.md checklists are derived, so editing one place keeps the three layers in sync. [@claim:clm_56c8f3ce8999e7883dab8ceb9e6cc47b05d3486727e7bf5f41ef6ac6d7db479e]
- The harness.json workflow block defines an ordered S1 requirements → S2 architecture → S3 launch pipeline with entry/exit gates, per-step exit conditions, and rules that skipped steps must be recorded in the ledger. [@claim:clm_abb45277b201e88ee5e1fff573d7d7a2f49dc961d576effac7bc9396e83ce8ae]
- A triage step (S1.1) classifies needs as light or heavy: light/demo mode merges gate confirmations into groups and skips optional steps with a ledger note, while exit gates always apply; heavy mode confirms each step individually. [@claim:clm_bff7687b8f21c5b6d86497a1b103a393cbf564ec2d77c8e137df75b1b1b8ebde]
- The v2 redesign doc records that only batches 1-2 are done (workflow block, ledger template, prd skill pilot); extending to the other four skills, harness process audit, and end-to-end validation remain unchecked. [@claim:clm_cba5d1cb47488cb1f9d11d498dfaab322b6fd6a3e4783ff57c08040333bbf20b]
<!-- rcw:end owner=source:src_b62eccb51bdc50dbbe514da4c647e0c0 block=evidence -->

## Researcher notes

