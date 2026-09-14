---
access: public
aliases: []
claim_ids:
- clm_4eb01200602bd0e1f31189d1da89bd20e620773886f1a0a20ca864cefea21175
- clm_6df9278939c44de68587a51f6d4f3e1e51da591d07473526e15f3d36075116b8
- clm_8eade8d12226e253020c6117624af82638cf535978585b125b1f0afac9857104
- clm_c374efadca4a55f60dd11be885721d7ab3de18810307d689ba084426a5ea9374
- clm_eef3808ac163ac4403de73bf68064633c76426344aeb8884abd6190b40ae485e
maturity: draft
page_id: pg_7fce6234f5da54c28e29b50261b9bd2e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1ec7a16ac2d155e3a775d206dc587601
title: griddynamics/rosetta/README.md @ 785054e925aa
updated_at: '2026-09-14T03:54:35Z'
---

# griddynamics/rosetta/README.md @ 785054e925aa

<!-- rcw:begin owner=source:src_1ec7a16ac2d155e3a775d206dc587601 block=evidence -->
- Rosetta instructs agents to maintain agents/MEMORY.md with root causes, actions tried, and lessons learned, and to write execution state (plans, specs, phase progress) to disk so failed sessions resume from checkpoints. [@claim:clm_4eb01200602bd0e1f31189d1da89bd20e620773886f1a0a20ca864cefea21175]
- Repository development practice: contributors are directed to CONTRIBUTING.md for workflow and expectations, and the README notes Rosetta plugins are used to develop Rosetta itself. [@claim:clm_6df9278939c44de68587a51f6d4f3e1e51da591d07473526e15f3d36075116b8]
- Rosetta layers instructions at runtime — core, then organization, then project — with higher layers propagating to every project automatically, all authored in markdown and versioned in Git. [@claim:clm_8eade8d12226e253020c6117624af82638cf535978585b125b1f0afac9857104]
- Rosetta ships named workflows including coding-flow, requirements-authoring-flow, security-flow, testgen/api-aqa/ui-aqa flows, and code-analysis-flow, each with defined phases, subagents, and HITL gates. [@claim:clm_c374efadca4a55f60dd11be885721d7ab3de18810307d689ba084426a5ea9374]
- Rosetta workflows instruct the agent to delegate review to a separate subagent with a fresh context window that inspects the implementation against original specs, and to use a validator subagent with real execution evidence. [@claim:clm_eef3808ac163ac4403de73bf68064633c76426344aeb8884abd6190b40ae485e]
<!-- rcw:end owner=source:src_1ec7a16ac2d155e3a775d206dc587601 block=evidence -->

## Researcher notes

