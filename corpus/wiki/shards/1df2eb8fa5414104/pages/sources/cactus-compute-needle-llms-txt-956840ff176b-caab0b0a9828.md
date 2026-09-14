---
access: public
aliases: []
claim_ids:
- clm_10ec3ced1b0716cebbcbd2a2c3d7862b2d8fcb258afb359b76c7612a6414e80e
- clm_6dc5efe24d6c7f87c67060a7435ab98d951335969ae7f7e09b193b4d8c77b5ee
- clm_b073d68618295e2f8c1f250d99780f2a392de26d6043f2bd702bafa0c830bf56
maturity: draft
page_id: pg_a26bf5e5992152a3bfe5caab0b0a9828
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_76c380e9f3915540bfc83d876ba7e8f5
title: cactus-compute/needle/llms.txt @ 956840ff176b
updated_at: '2026-09-14T03:40:37Z'
---

# cactus-compute/needle/llms.txt @ 956840ff176b

<!-- rcw:begin owner=source:src_76c380e9f3915540bfc83d876ba7e8f5 block=evidence -->
- The Python API exposes needle.Needle(tools, system, weights, tool_index_path, buffer_size), agent.run/complete/embed/reset, needle.tool, needle.Field, and needle.extract; tools can be decorated functions, Pydantic models, raw JSON schemas, or a JSON string. [@claim:clm_10ec3ced1b0716cebbcbd2a2c3d7862b2d8fcb258afb359b76c7612a6414e80e]
- The runtime install excludes training; fine-tuning and export need the [train] extra (JAX, imported lazily), with [train,gpu] for CUDA and [train,metal] for Apple Silicon; Pydantic is used for typed extraction. [@claim:clm_6dc5efe24d6c7f87c67060a7435ab98d951335969ae7f7e09b193b4d8c77b5ee]
- Each turn returns one JSON object with fields including type, success, error, function_calls, reasoning, confidence, prefill_tps, decode_tps, and peak_ram_mb; empty function_calls is the off-topic refusal. [@claim:clm_b073d68618295e2f8c1f250d99780f2a392de26d6043f2bd702bafa0c830bf56]
<!-- rcw:end owner=source:src_76c380e9f3915540bfc83d876ba7e8f5 block=evidence -->

## Researcher notes

