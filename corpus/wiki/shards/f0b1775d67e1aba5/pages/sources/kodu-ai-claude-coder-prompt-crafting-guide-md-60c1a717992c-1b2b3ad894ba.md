---
access: public
aliases: []
claim_ids:
- clm_ac88ee7d0dc7042fe609130742d2fe14d3949f34877d8625b898209a6ec9b3f0
- clm_b742646e9127708a0cb58ac37ce9f7ab4f9b38126214ab1991b6880ee261733d
- clm_c2c7db8d6129b7d437bf1724914e0efb2f7808bf706431e505bf50c1b347d30d
- clm_f24a94be275bef03277ecc31cb1617aefb8c9a4122c1e7546a46cd4137a093ce
maturity: draft
page_id: pg_a628bf6c5a365ae791fa1b2b3ad894ba
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa07529fc8375c55a6dfda11670661b0
title: kodu-ai/claude-coder/prompt-crafting-guide.md @ 60c1a717992c
updated_at: '2026-09-14T02:09:50Z'
---

# kodu-ai/claude-coder/prompt-crafting-guide.md @ 60c1a717992c

<!-- rcw:begin owner=source:src_aa07529fc8375c55a6dfda11670661b0 block=evidence -->
- Task processing follows a Reasoning-Acting-Observing (ReAct) loop: analyze and plan, execute actions with tools, then evaluate results and adjust. [@claim:clm_ac88ee7d0dc7042fe609130742d2fe14d3949f34877d8625b898209a6ec9b3f0]
- The prompt guide recommends decomposing large tasks by spawning a SubTask agent for planning, additional SubTask agents for components, and letting the main agent coordinate. [@claim:clm_b742646e9127708a0cb58ac37ce9f7ab4f9b38126214ab1991b6880ee261733d]
- The prompt guide describes a multi-agent system with a main Kodu agent that follows a ReAct pattern and can spawn specialized sub-agents. [@claim:clm_c2c7db8d6129b7d437bf1724914e0efb2f7808bf706431e505bf50c1b347d30d]
- The guide references an add_interested_file tool used to track files relevant to the current task. [@claim:clm_f24a94be275bef03277ecc31cb1617aefb8c9a4122c1e7546a46cd4137a093ce]
<!-- rcw:end owner=source:src_aa07529fc8375c55a6dfda11670661b0 block=evidence -->

## Researcher notes

