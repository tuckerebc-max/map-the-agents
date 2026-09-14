---
access: public
aliases: []
claim_ids:
- clm_04f6323a9d373ceacd037d1cb3d374f87b1e9039237a88675cc2e7092b99cd11
- clm_9d950b7126123044d15cfbbab0f6ed8c9cb1458ba273b3e49ce4c257fd086c3e
- clm_af7ff1c591f5c1fdfbf13cdef200f9519480427c2296d09e0322194db337484f
- clm_c2003f50adea8886875d8e218602a08f4d9bae63ba63996f0f93370a401e46ab
- clm_c399c6e0f7986563cb0691de293ac8e81793039852b2a9af09250d057f4d79ad
- clm_e20abae88fae20a9eb0f940d9f1adacf7409fc9d420e3f35b1b73769dbf87480
- clm_f1f3d12802ca6b66a7c0b30c4f3e4ae695990f3cf3e086089527785f3c746be6
- clm_f88084d2baff02f00726a4855dc9bbfd432e8c16aa0f26e437a3e491ec3edf9b
- clm_f9f959f77b73d54da9994773c4ad87ec37f3b90bfd414b30fe7c05d34b95717a
maturity: draft
page_id: pg_ec4b66314f1d5b47b05ea06b8754ad96
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a56d4e5f518357be9dcd744c3704c43e
title: youssefvdel/qwengate/docs/API.md @ 5220f7d3c50c
updated_at: '2026-09-14T05:10:29Z'
---

# youssefvdel/qwengate/docs/API.md @ 5220f7d3c50c

<!-- rcw:begin owner=source:src_a56d4e5f518357be9dcd744c3704c43e block=evidence -->
- A built-in dashboard serves vanilla HTML/JS pages at /dashboard, /dashboard/logs, /dashboard/accounts, /dashboard/network, and /dashboard/settings, with live SSE updates at /log/stream and JSON logs at /log/json. [@claim:clm_04f6323a9d373ceacd037d1cb3d374f87b1e9039237a88675cc2e7092b99cd11]
- The product exposes OpenAI-compatible endpoints POST /v1/chat/completions and GET /v1/models at base URL http://localhost:26405/v1, documented as working with OpenAI SDKs and HTTP clients. [@claim:clm_9d950b7126123044d15cfbbab0f6ed8c9cb1458ba273b3e49ce4c257fd086c3e]
- Multiple Qwen accounts are rotated round-robin with automatic failover, health-weighted load balancing, rate-limit tracking, and a configurable cooldown (default 2 minutes via RATE_LIMIT_COOLDOWN_MS); sessions are pooled, reused, auto-scaled, and idle-cleaned. [@claim:clm_af7ff1c591f5c1fdfbf13cdef200f9519480427c2296d09e0322194db337484f]
- Streaming responses use SSE with an initial heartbeat, OpenAI-format chunks, optional reasoning_content deltas for thinking models, and a data: [DONE] terminator; usage appears in the final chunk when requested. [@claim:clm_c2003f50adea8886875d8e218602a08f4d9bae63ba63996f0f93370a401e46ab]
- The documented stack is Bun 1.3+, TypeScript, Hono, wreq-js for HTTP with TLS fingerprinting, Playwright for login/auth only, and tsx; the frontend is vanilla HTML/CSS/JS with no framework dependencies. [@claim:clm_c399c6e0f7986563cb0691de293ac8e81793039852b2a9af09250d057f4d79ad]
- Chat completions accept model, messages, stream (default true), temperature, max_tokens, top_p, tools, tool_choice, and stream_options with include_usage for usage data in the final chunk. [@claim:clm_e20abae88fae20a9eb0f940d9f1adacf7409fc9d420e3f35b1b73769dbf87480]
- API requests authenticate with an Authorization: Bearer header carrying an API key configured in .env or config.json; leaving API_KEY empty disables authentication. [@claim:clm_f1f3d12802ca6b66a7c0b30c4f3e4ae695990f3cf3e086089527785f3c746be6]
- Tool call content is gated during streaming via a toolCallDepth counter that suppresses emission inside XML tool-call blocks, delivering the clean tool call as a finish_reason: tool_calls phase. [@claim:clm_f88084d2baff02f00726a4855dc9bbfd432e8c16aa0f26e437a3e491ec3edf9b]
- Large context payloads are auto-uploaded as Qwen file attachments, and tool results such as git diffs and JSON arrays are compressed before being sent to the model to reduce token usage. [@claim:clm_f9f959f77b73d54da9994773c4ad87ec37f3b90bfd414b30fe7c05d34b95717a]
<!-- rcw:end owner=source:src_a56d4e5f518357be9dcd744c3704c43e block=evidence -->

## Researcher notes

