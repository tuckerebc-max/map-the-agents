---
access: public
aliases: []
claim_ids:
- clm_10ec3ced1b0716cebbcbd2a2c3d7862b2d8fcb258afb359b76c7612a6414e80e
- clm_270696d65805383ec97ef3c7814e31ec64b6b883df3b13e64def131e237f870e
- clm_91ac23d2434e7ee7770189d0be48da5f1878558cfb6ba0ee877e442f96305f56
- clm_b073d68618295e2f8c1f250d99780f2a392de26d6043f2bd702bafa0c830bf56
- clm_d8073d6887fd543270ac5fc17e391f6154679e4a3bb9390a7be34bc512635444
- clm_f170c7f8620d525fa3b69b90323ac4653aa4e10ee719e0d73995ee1b1e7814fe
maturity: draft
page_id: pg_ec614d6e152b50c6b07dea23974a9df5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6559d3ef6e4d5fb5b8414d9e38d4fe96
title: cactus-compute/needle/doc/apis.md @ 956840ff176b
updated_at: '2026-09-14T03:40:37Z'
---

# cactus-compute/needle/doc/apis.md @ 956840ff176b

<!-- rcw:begin owner=source:src_6559d3ef6e4d5fb5b8414d9e38d4fe96 block=evidence -->
- The Python API exposes needle.Needle(tools, system, weights, tool_index_path, buffer_size), agent.run/complete/embed/reset, needle.tool, needle.Field, and needle.extract; tools can be decorated functions, Pydantic models, raw JSON schemas, or a JSON string. [@claim:clm_10ec3ced1b0716cebbcbd2a2c3d7862b2d8fcb258afb359b76c7612a6414e80e]
- Every response carries a calibrated confidence score from a learned head, defined as the minimum of a post-hoc head score and the decoding probability of the call tokens; users set a threshold and escalate below it. [@claim:clm_270696d65805383ec97ef3c7814e31ec64b6b883df3b13e64def131e237f870e]
- agent.run() drives a full agentic loop (max_steps=8 default): the model picks calls, Needle executes the user's Python functions, feeds results back, and returns final results; ungrounded fields are refused unless strict=False. [@claim:clm_91ac23d2434e7ee7770189d0be48da5f1878558cfb6ba0ee877e442f96305f56]
- Each turn returns one JSON object with fields including type, success, error, function_calls, reasoning, confidence, prefill_tps, decode_tps, and peak_ram_mb; empty function_calls is the off-topic refusal. [@claim:clm_b073d68618295e2f8c1f250d99780f2a392de26d6043f2bd702bafa0c830bf56]
- Tool calls are constrained by a byte-level grammar compiled from the declared schemas, so output is structured JSON and cannot be malformed; the reasoning field is generated unconstrained. [@claim:clm_d8073d6887fd543270ac5fc17e391f6154679e4a3bb9390a7be34bc512635444]
- For catalogues above five tools, a built-in contrastive retrieval head embeds schemas at init and renders only the top five tools per turn, rebuilding the grammar over that subset. [@claim:clm_f170c7f8620d525fa3b69b90323ac4653aa4e10ee719e0d73995ee1b1e7814fe]
<!-- rcw:end owner=source:src_6559d3ef6e4d5fb5b8414d9e38d4fe96 block=evidence -->

## Researcher notes

