---
access: public
aliases: []
claim_ids:
- clm_05c519830705cc1537f1c7ef1328998a617ceca753bdafdff6ee153c1d73e80c
- clm_3eb6d4ca2a8badd2957a211516b4279498f93740e4854e1d062cd6c256a282c6
- clm_762b2dc5bb00d8cb6235e4464529486c76f8f8eb703b56ce2fe3d147ece003e7
- clm_766a90d31c7c12b46c3081a71ad7831352cb5f6c10049cf9e9da8ee46705e65d
- clm_7af6d6a0c7b90cf27841ff612ab7cd533dbcf9333b9ff0eb2aae92d9437168dc
maturity: draft
page_id: pg_387a968520b158c9944c01f2da1e5981
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b442bd2e961b5a77aec5fdde1cc7cf3f
title: TrafficGuard/typedai/docs/docs/agent-concepts.md @ 34139aec65bb
updated_at: '2026-09-14T04:27:59Z'
---

# TrafficGuard/typedai/docs/docs/agent-concepts.md @ 34139aec65bb

<!-- rcw:begin owner=source:src_b442bd2e961b5a77aec5fdde1cc7cf3f block=evidence -->
- Each agent is configured with three LLMs for easy, medium, and hard tasks, making it simple to swap in different models at a given capability level. [@claim:clm_05c519830705cc1537f1c7ef1328998a617ceca753bdafdff6ee153c1d73e80c]
- Agent state, current user, tool configuration, and default LLMs are looked up through Node's AsyncLocalStorage, requiring agent code to run within an AsyncLocalStorage context. [@claim:clm_3eb6d4ca2a8badd2957a211516b4279498f93740e4854e1d062cd6c256a282c6]
- Workflows run with a persisted agent context whose state is saved as 'completed' or 'error', so agent actions can be reviewed and resumed in the UI. [@claim:clm_762b2dc5bb00d8cb6235e4464529486c76f8f8eb703b56ce2fe3d147ece003e7]
- TypedAI includes two autonomous agent types, XML and CodeGen, which apply reasoning to break a user request into a plan executed via available function calls. [@claim:clm_766a90d31c7c12b46c3081a71ad7831352cb5f6c10049cf9e9da8ee46705e65d]
- The project distinguishes workflow agents, whose control flow is defined in code with LLM results driving conditionals, from autonomous agents where the LLM directs its own process and tool usage. [@claim:clm_7af6d6a0c7b90cf27841ff612ab7cd533dbcf9333b9ff0eb2aae92d9437168dc]
<!-- rcw:end owner=source:src_b442bd2e961b5a77aec5fdde1cc7cf3f block=evidence -->

## Researcher notes

