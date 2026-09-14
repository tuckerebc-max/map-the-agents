---
access: public
aliases: []
claim_ids:
- clm_0cb635a690c92d397dfb9447e8e4d96937d86c8ffaa8500a5684cb44d40a9864
- clm_33d1f7d42d10d23d0ee7ab7dd06a7c41055de93b3c857fd8cc2e34277083a46f
- clm_d5711a0312ab356d119a9d610212c77b2824bbffd49a9f75ccc48da68e50cc01
- clm_ff9ba47623d7dd3751177d295a7962f6593f4acf8f4c1b7add564eb754cfa22f
maturity: draft
page_id: pg_5d4b87d478e650c29fbf302934bc59b3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a09b09dc2bbc5c62841f2ff42ee6b9df
title: r1n7aro/Locus/docs/sessions/permissions.mdx @ 52e714341f53
updated_at: '2026-09-14T02:33:39Z'
---

# r1n7aro/Locus/docs/sessions/permissions.mdx @ 52e714341f53

<!-- rcw:begin owner=source:src_a09b09dc2bbc5c62841f2ff42ee6b9df block=evidence -->
- Approval cards support single and batch confirmation with diff previews, and a feedback field lets the agent revise and re-request a rejected proposal. [@claim:clm_0cb635a690c92d397dfb9447e8e4d96937d86c8ffaa8500a5684cb44d40a9864]
- Behavior approvals are independent of global mode: even in Auto, switching Unity Editor/Play Mode state or editing protected knowledge folders can be set to require confirmation. [@claim:clm_33d1f7d42d10d23d0ee7ab7dd06a7c41055de93b3c857fd8cc2e34277083a46f]
- Tool execution has two modes: Auto runs all tools without approval, while Ask requires per-tool confirmation; read tools default to auto-run and modifying tools (write, edit, bash, web_fetch, unity_execute, unity_run_states, subagent) default to confirmation. [@claim:clm_d5711a0312ab356d119a9d610212c77b2824bbffd49a9f75ccc48da68e50cc01]
- A File Tool Boundary setting can restrict file tools to the current project directory; by default (All) paths outside the workspace are allowed. [@claim:clm_ff9ba47623d7dd3751177d295a7962f6593f4acf8f4c1b7add564eb754cfa22f]
<!-- rcw:end owner=source:src_a09b09dc2bbc5c62841f2ff42ee6b9df block=evidence -->

## Researcher notes

