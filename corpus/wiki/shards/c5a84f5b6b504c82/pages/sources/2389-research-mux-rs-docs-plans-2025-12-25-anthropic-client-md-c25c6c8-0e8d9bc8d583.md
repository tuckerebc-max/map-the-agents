---
access: public
aliases: []
claim_ids:
- clm_49d2698042b1f93fbf7983eec6f760d9b373456068bafe1748fbb0aaf2d9ab22
- clm_4d2913f676115c63175d7420003298bf0c2f4c4dcaf567f6aaaf7450faecf41b
- clm_6aa1c21faed7920792b2c1ec542a9cb66faba035de8b4ece1d73f24f1660f6aa
- clm_7dc00bede7df14b813e9673b2e68a8f05319076c6345221e4fa13bb536363452
- clm_a8a9f481a361e4db352e7be4578bbebd30f65180a428589d20b62cbd20b394a1
- clm_c5656c8867753e79d23267572efe2c7a826684f20a3351adeb58efef548705d4
- clm_e347956f0a35de2f4c6ee0019230d1b3ac57e0caa4d8c39a259bee4c959289af
- clm_e7945a56905129521cee3b8cb1d35fb791c135df55b6e20731cb0a8040c3ab4b
maturity: draft
page_id: pg_a06af4fa677a5daeb4630e8d9bc8d583
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6d32a3da1e275d7fa6d6701246ebc9d8
title: 2389-research/mux-rs/docs/plans/2025-12-25-anthropic-client.md @ c25c6c8e1acb
updated_at: '2026-09-14T01:28:13Z'
---

# 2389-research/mux-rs/docs/plans/2025-12-25-anthropic-client.md @ c25c6c8e1acb

<!-- rcw:begin owner=source:src_6d32a3da1e275d7fa6d6701246ebc9d8 block=evidence -->
- The planned client posts to https://api.anthropic.com/v1/messages with x-api-key, anthropic-version (2023-06-01), and JSON content-type headers, mapping non-success statuses to LlmError::Api. [@claim:clm_49d2698042b1f93fbf7983eec6f760d9b373456068bafe1748fbb0aaf2d9ab22]
- A plan document specifies implementing an AnthropicClient that connects to the Claude API and implements the LlmClient trait. [@claim:clm_4d2913f676115c63175d7420003298bf0c2f4c4dcaf567f6aaaf7450faecf41b]
- The plan adds streaming support via an AnthropicStreamEvent enum (message start/stop, content block events, ping, error) and an async-stream based SSE parser that buffers chunks and splits on blank lines. [@claim:clm_6aa1c21faed7920792b2c1ec542a9cb66faba035de8b4ece1d73f24f1660f6aa]
- Repository development practice: each plan task prescribes verification via cargo check or cargo test, final clippy and cargo fmt runs, and a git commit per task with conventional-commit style messages. [@claim:clm_7dc00bede7df14b813e9673b2e68a8f05319076c6345221e4fa13bb536363452]
- The planned Anthropic client architecture uses reqwest for HTTP with SSE streaming support, serializing the crate's Request type to Anthropic's format and deserializing responses back. [@claim:clm_a8a9f481a361e4db352e7be4578bbebd30f65180a428589d20b62cbd20b394a1]
- The planned AnthropicRequest type carries model, messages, max_tokens, optional system and temperature, a tools list, and an optional stream flag, with optional fields skipped during serialization. [@claim:clm_c5656c8867753e79d23267572efe2c7a826684f20a3351adeb58efef548705d4]
- Repository development practice: the plan's header instructs the implementing Claude agent to use the superpowers:executing-plans skill to implement the plan task-by-task. [@claim:clm_e347956f0a35de2f4c6ee0019230d1b3ac57e0caa4d8c39a259bee4c959289af]
- The plan defines AnthropicClient::from_env, which reads the ANTHROPIC_API_KEY environment variable and returns an LlmError::Api error when it is unset. [@claim:clm_e7945a56905129521cee3b8cb1d35fb791c135df55b6e20731cb0a8040c3ab4b]
<!-- rcw:end owner=source:src_6d32a3da1e275d7fa6d6701246ebc9d8 block=evidence -->

## Researcher notes

