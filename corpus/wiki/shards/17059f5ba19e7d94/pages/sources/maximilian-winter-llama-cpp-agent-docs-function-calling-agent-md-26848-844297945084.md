---
access: public
aliases: []
claim_ids:
- clm_5c8752a20aebcb66515d13b664ebffc71c25602f5648d9dc36369b88aa7bef1d
- clm_8aab6b6a87225a7b86eba49c7381aede3b034b56deb1a080e274e1a2bb6ede7f
maturity: draft
page_id: pg_372503fb47725d3889fc844297945084
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4679c4ab3d165d47ae263f99cfa3ed19
title: Maximilian-Winter/llama-cpp-agent/docs/function-calling-agent.md @ 26848efd4f35
updated_at: '2026-09-14T02:17:51Z'
---

# Maximilian-Winter/llama-cpp-agent/docs/function-calling-agent.md @ 26848efd4f35

<!-- rcw:begin owner=source:src_4679c4ab3d165d47ae263f99cfa3ed19 block=evidence -->
- Tools can be defined as Python functions, pydantic models, llama-index tools, or OpenAI tool schemas; LlamaCppFunctionTool.from_openai_tool converts an OpenAI tool schema plus a callable into a tool. [@claim:clm_5c8752a20aebcb66515d13b664ebffc71c25602f5648d9dc36369b88aa7bef1d]
- FunctionCallingAgent is constructed with a provider, a list of function tools, a send-message-to-user callback, a message formatter type, and an allow_parallel_function_calling flag. [@claim:clm_8aab6b6a87225a7b86eba49c7381aede3b034b56deb1a080e274e1a2bb6ede7f]
<!-- rcw:end owner=source:src_4679c4ab3d165d47ae263f99cfa3ed19 block=evidence -->

## Researcher notes

