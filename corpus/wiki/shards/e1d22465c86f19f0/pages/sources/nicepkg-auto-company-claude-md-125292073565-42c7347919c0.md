---
access: public
aliases: []
claim_ids:
- clm_081ef3c5eb9b1353da916b373f3648a5b174b903adc88474ae04ad6062cb7ae6
- clm_12aab05b3b2550f770c5cc2bdf91244b629d5986ddf2e8eee126c5f57285f87f
- clm_80d97e2f431a312847f8eea4efa9a659b7c2964a4ad53fba526284b96386bba7
- clm_bf1dea5425fa0402ae0d898bce0423797394e7b2d18b8d4d6f92998194082f44
- clm_c823a96cae53118e686fd8a8e57cab5c4377e9707e5e7788223aee602bc2da8c
maturity: draft
page_id: pg_81ba49de9b4d510994da42c7347919c0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0b45e1fb262953889a5a3f5d9086e7a4
title: nicepkg/auto-company/CLAUDE.md @ 125292073565
updated_at: '2026-09-14T04:11:44Z'
---

# nicepkg/auto-company/CLAUDE.md @ 125292073565

<!-- rcw:begin owner=source:src_0b45e1fb262953889a5a3f5d9086e7a4 block=evidence -->
- The runtime charter grants agents all terminal tools (gh, wrangler, git, node/npm, uv/python, curl/jq listed as available) with hard safety red lines: no repo deletion, no wrangler delete, no deleting system files, no credential leaks, no force-push to main/master, and new projects must live under projects/. [@claim:clm_081ef3c5eb9b1353da916b373f3648a5b174b903adc88474ae04ad6062cb7ae6]
- Six standard collaboration chains are defined (new product evaluation, feature development, launch, pricing, weekly review, opportunity discovery), and convergence rules force concrete output: cycle 1 brainstorm, cycle 2 GO/NO-GO pre-mortem, and from cycle 3 onward pure discussion is forbidden. [@claim:clm_12aab05b3b2550f770c5cc2bdf91244b629d5986ddf2e8eee126c5f57285f87f]
- The repo ships 14 agent persona definitions under .claude/agents (e.g. ceo-bezos, cto-vogels, critic-munger, fullstack-dhh, qa-bach, devops-hightower, cfo-campbell, research-thompson) plus 30+ skills under .claude/skills. [@claim:clm_80d97e2f431a312847f8eea4efa9a659b7c2964a4ad53fba526284b96386bba7]
- Human steering appears to be intentionally limited to editing the 'Next Action' in memories/consensus.md (plus pause/resume), since the charter says humans guide direction only through that file while everything else stays autonomous. [@claim:clm_bf1dea5425fa0402ae0d898bce0423797394e7b2d18b8d4d6f92998194082f44]
- Agents are prompted as real-world luminaries (e.g. 'you are DHH' rather than 'you are a developer') to activate the LLM's deep domain knowledge, and the charter sets decision principles like Ship > Plan > Discuss and monolith-first boring technology. [@claim:clm_c823a96cae53118e686fd8a8e57cab5c4377e9707e5e7788223aee602bc2da8c]
<!-- rcw:end owner=source:src_0b45e1fb262953889a5a3f5d9086e7a4 block=evidence -->

## Researcher notes

