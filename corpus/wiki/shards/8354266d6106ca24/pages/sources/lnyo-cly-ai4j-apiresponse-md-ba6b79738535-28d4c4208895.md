---
access: public
aliases: []
claim_ids:
- clm_060790fa73c3100b806c41c281d3bb198d3bd188552f8eb7c78aeb7c861024b7
- clm_3f44cddc2217087654c456e7aae24a3c4d2aed998e00751b5c57c125b1d35272
- clm_599285ba2a501176851a2d026b93ac9a935e92d3c18b9fb5b12a562e24ec09a0
- clm_ea91459b1cab32bd760589d68b637d652dc0cbf82650cdc5d50138f1edf6d45c
- clm_ebe75ac29d72bd2d2e16c6354077482d665bd0bf24bd0daa67438f280d30e459
maturity: draft
page_id: pg_98288a3b21fc5dfb89d928d4c4208895
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_21b0b230c0485880b30ff8e550a6b4f3
title: LnYo-Cly/ai4j/APIResponse.md @ ba6b79738535
updated_at: '2026-09-14T02:13:49Z'
---

# LnYo-Cly/ai4j/APIResponse.md @ ba6b79738535

<!-- rcw:begin owner=source:src_21b0b230c0485880b30ff8e550a6b4f3 block=evidence -->
- Documented Ollama qwen3 streaming shows tool_calls arriving complete within a single data chunk, including function name and arguments, requiring no extra concatenation. [@claim:clm_060790fa73c3100b806c41c281d3bb198d3bd188552f8eb7c78aeb7c861024b7]
- Documented DeepSeek-R1 streaming separates reasoning into a reasoning_content delta field (with reasoning_tokens counted in usage) before regular content deltas begin. [@claim:clm_3f44cddc2217087654c456e7aae24a3c4d2aed998e00751b5c57c125b1d35272]
- APIResponse.md documents that Ollama's deepseek-r1 streams thinking and answer content together in the content field, with thinking wrapped in <think> tags, unlike qwen3 which places reasoning in a separate thinking field. [@claim:clm_599285ba2a501176851a2d026b93ac9a935e92d3c18b9fb5b12a562e24ec09a0]
- Documented OpenAI streaming tool calls arrive incrementally: each delta carries a tool_calls fragment with index, id, function name, and argument string split across chunks, finishing with finish_reason 'tool_calls'. [@claim:clm_ea91459b1cab32bd760589d68b637d652dc0cbf82650cdc5d50138f1edf6d45c]
- Documented OpenAI streaming responses use SSE 'data:' chunks of chat.completion.chunk objects; the finish_reason stop chunk is followed by a separate chunk with empty choices that carries usage, then a 'data: [DONE]' sentinel. [@claim:clm_ebe75ac29d72bd2d2e16c6354077482d665bd0bf24bd0daa67438f280d30e459]
<!-- rcw:end owner=source:src_21b0b230c0485880b30ff8e550a6b4f3 block=evidence -->

## Researcher notes

