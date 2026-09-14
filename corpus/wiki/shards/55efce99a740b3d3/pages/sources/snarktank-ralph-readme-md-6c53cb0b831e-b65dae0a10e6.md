---
access: public
aliases: []
claim_ids:
- clm_31d1ad6ebb0ad4e089bf2979226464e68b3a5f0d67edf8f811e74a9951c6193d
- clm_4412202e98be0eb0f48be3c6cf6b8e5c85a79d03521ae77972a26e0ec3eb67d1
- clm_4456223d7175bb2ae9491440dee1bedabe78226ebae884a9882ebb095a7911b4
- clm_47b5afd707d9cc986839d139be55dbfbcc73b24ae3b0cb0f0a93e083f74c254c
- clm_54a1a0f5098ee00a2e3990252799d74d4bb67491bccd573b68936b6dec47101c
- clm_57f12a42be43f6b3e1b258a72291259eaf9ad55766b65f8c964fa999e4191098
- clm_8f58b84e7fbc4706fa22097cb989b448fad63a8691342c2d6f7c16125910eb4c
- clm_924725008f8e5bf781aa2703f913c55af8ca337ae3a13f763bc365c534cab01e
- clm_9a7896f2edf35bc19945f1729418be774036f20f093564a57f0b34383ae9bdd7
- clm_b0970ae2289f347e3b740d6edfbef7738e057d1b2e0e8e5d8e9ae6be44cc5ae6
- clm_d9a0a1184b1fdee9bb9995fea7c7bef8b13ba613e9fac7b34c39458be7537488
- clm_f7d31f86b5f5fdba0b3543e9ddc5bffb9fc17e7209f6d85eed4a9deed025747b
maturity: draft
page_id: pg_113ea417ee3853cd93cdb65dae0a10e6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_66f1076290e15f17885d25439df8c72a
title: snarktank/ralph/README.md @ 6c53cb0b831e
updated_at: '2026-09-14T02:41:10Z'
---

# snarktank/ralph/README.md @ 6c53cb0b831e

<!-- rcw:begin owner=source:src_66f1076290e15f17885d25439df8c72a block=evidence -->
- Two skills are provided: /prd for generating Product Requirements Documents and /ralph for converting PRDs to prd.json, installable via Amp config, the Claude skills directory, or a Claude Code marketplace plugin. [@claim:clm_31d1ad6ebb0ad4e089bf2979226464e68b3a5f0d67edf8f811e74a9951c6193d]
- Key files include ralph.sh (the bash loop), prompt.md and CLAUDE.md prompt templates, prd.json task list, progress.txt, skills/prd and skills/ralph, and a .claude-plugin manifest. [@claim:clm_4412202e98be0eb0f48be3c6cf6b8e5c85a79d03521ae77972a26e0ec3eb67d1]
- When all stories have passes:true, Ralph outputs <promise>COMPLETE</promise> and the loop exits. [@claim:clm_4456223d7175bb2ae9491440dee1bedabe78226ebae884a9882ebb095a7911b4]
- A recommended Amp auto-handoff setting (context 90) enables automatic handoff when context fills, letting Ralph handle stories larger than one context window. [@claim:clm_47b5afd707d9cc986839d139be55dbfbcc73b24ae3b0cb0f0a93e083f74c254c]
- Each loop iteration creates a feature branch from the PRD branchName, picks the highest-priority story with passes:false, implements it, runs quality checks, commits, marks it passes:true, and repeats until done or max iterations. [@claim:clm_54a1a0f5098ee00a2e3990252799d74d4bb67491bccd573b68936b6dec47101c]
- Frontend stories' acceptance criteria must include browser verification via the dev-browser skill, which Ralph uses to navigate and confirm UI changes. [@claim:clm_57f12a42be43f6b3e1b258a72291259eaf9ad55766b65f8c964fa999e4191098]
- Prerequisites are one installed and authenticated AI coding tool (Amp CLI default or Claude Code), jq, and a git repository for the project. [@claim:clm_8f58b84e7fbc4706fa22097cb989b448fad63a8691342c2d6f7c16125910eb4c]
- The only memory between iterations is git history, the append-only progress.txt learnings file, and prd.json story status. [@claim:clm_924725008f8e5bf781aa2703f913c55af8ca337ae3a13f763bc365c534cab01e]
- Ralph runs AI coding tools (Amp or Claude Code) repeatedly until all PRD items are complete; each iteration is a fresh instance with clean context. [@claim:clm_9a7896f2edf35bc19945f1729418be774036f20f093564a57f0b34383ae9bdd7]
- PRD items are intentionally kept small enough to finish in one context window, since oversized tasks exhaust context and yield poor code. [@claim:clm_b0970ae2289f347e3b740d6edfbef7738e057d1b2e0e8e5d8e9ae6be44cc5ae6]
- ralph.sh accepts an optional max_iterations argument and a --tool flag selecting amp (the default) or claude; the default iteration count is 10. [@claim:clm_d9a0a1184b1fdee9bb9995fea7c7bef8b13ba613e9fac7b34c39458be7537488]
- Ralph automatically archives previous runs when a new feature with a different branchName starts, saving them under archive/YYYY-MM-DD-feature-name/. [@claim:clm_f7d31f86b5f5fdba0b3543e9ddc5bffb9fc17e7209f6d85eed4a9deed025747b]
<!-- rcw:end owner=source:src_66f1076290e15f17885d25439df8c72a block=evidence -->

## Researcher notes

