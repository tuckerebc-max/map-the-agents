---
access: public
aliases: []
claim_ids:
- clm_287d7a6bdf205125f9a6aebb9a620f644db55db6c308a7ac2a3f10a5cb69631a
- clm_38b3b614dd6b2158cdac338005f9ced0ecc5692948609452d83720acd17ceea6
- clm_fc38c0b95d1f3b738f6983995e6d5826619227dd4b46394b29a6442b274dc80b
maturity: draft
page_id: pg_51eb060291ae5e5aaa3cf7b081f51690
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_abf0d85fbb36593aa2b315e287eb9f3e
title: jcz2020/par/docs/explanation/architecture.md @ 4b593db4465d
updated_at: '2026-09-14T02:07:13Z'
---

# jcz2020/par/docs/explanation/architecture.md @ 4b593db4465d

<!-- rcw:begin owner=source:src_abf0d85fbb36593aa2b315e287eb9f3e block=evidence -->
- The bash tool uses a command ADT with no raw-shell constructor, so shell injection is claimed to be unrepresentable at the type level; duplicate tool names return an error rather than overwriting. [@claim:clm_287d7a6bdf205125f9a6aebb9a620f644db55db6c308a7ac2a3f10a5cb69631a]
- The codebase is layered into core (types, runtime, ReAct engine, workflow engine, cancellation, persistence writer), providers (OpenAI, Anthropic, mock), tools, persistence, event bus, and middleware modules. [@claim:clm_38b3b614dd6b2158cdac338005f9ced0ecc5692948609452d83720acd17ceea6]
- PAR runs its stack on Eio structured concurrency: each Runtime has an Eio switch as cancellation root, and Runtime.close cancels all fibers including tool handlers and LLM streams. [@claim:clm_fc38c0b95d1f3b738f6983995e6d5826619227dd4b46394b29a6442b274dc80b]
<!-- rcw:end owner=source:src_abf0d85fbb36593aa2b315e287eb9f3e block=evidence -->

## Researcher notes

