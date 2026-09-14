---
access: public
aliases: []
claim_ids:
- clm_5fef9a8fea1659b3d876687b845697d7f5e46eb84f2a1504eeb69e00b56aaf41
- clm_96bd7115dc93855d6278f8d28a63ef4e070d216aca3855267bfdbb6ac49988b1
- clm_af7ff1c591f5c1fdfbf13cdef200f9519480427c2296d09e0322194db337484f
- clm_c199f8554a6ff4bd1589619f34c8632abc1f85a7bc196b00729667f1d267ba59
- clm_c399c6e0f7986563cb0691de293ac8e81793039852b2a9af09250d057f4d79ad
- clm_d781ab921c1f10a9b1ef5d1962f2e8cc901d9cb3dfad0dc24d3e6b0c9bd5c575
- clm_f88084d2baff02f00726a4855dc9bbfd432e8c16aa0f26e437a3e491ec3edf9b
- clm_f9f959f77b73d54da9994773c4ad87ec37f3b90bfd414b30fe7c05d34b95717a
maturity: draft
page_id: pg_31d2c73bf5fa538ba66df6ce05a5412e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eafbf75854c659f28d24f863e771642b
title: youssefvdel/qwengate/docs/ARCHITECTURE.md @ 5220f7d3c50c
updated_at: '2026-09-14T05:10:29Z'
---

# youssefvdel/qwengate/docs/ARCHITECTURE.md @ 5220f7d3c50c

<!-- rcw:begin owner=source:src_eafbf75854c659f28d24f863e771642b block=evidence -->
- A dual-transport design uses Node.js fetch via wreq-js (with TLS fingerprinting) for API calls and reserves Playwright browser automation only for login/auth and initial header extraction. [@claim:clm_5fef9a8fea1659b3d876687b845697d7f5e46eb84f2a1504eeb69e00b56aaf41]
- A content-filter pipeline (cleanTextOfXmlArtifacts, filterContent, cleanThinkTags) strips thinking tags and XML artifacts from streamed output, with per-chunk and flush paths plus an amplification guard. [@claim:clm_96bd7115dc93855d6278f8d28a63ef4e070d216aca3855267bfdbb6ac49988b1]
- Multiple Qwen accounts are rotated round-robin with automatic failover, health-weighted load balancing, rate-limit tracking, and a configurable cooldown (default 2 minutes via RATE_LIMIT_COOLDOWN_MS); sessions are pooled, reused, auto-scaled, and idle-cleaned. [@claim:clm_af7ff1c591f5c1fdfbf13cdef200f9519480427c2296d09e0322194db337484f]
- Configuration follows a three-tier priority: environment variables highest, then config.json, then defaults, with runtime updates and hot reload supported via a centralized config service. [@claim:clm_c199f8554a6ff4bd1589619f34c8632abc1f85a7bc196b00729667f1d267ba59]
- The documented stack is Bun 1.3+, TypeScript, Hono, wreq-js for HTTP with TLS fingerprinting, Playwright for login/auth only, and tsx; the frontend is vanilla HTML/CSS/JS with no framework dependencies. [@claim:clm_c399c6e0f7986563cb0691de293ac8e81793039852b2a9af09250d057f4d79ad]
- The architecture comprises an API layer (Hono, src/routes/), a Session Pool Manager (src/services/sessionPool.ts with SessionPool, Session, and AccountManager classes), a Qwen API transport layer, a configuration service, and a dashboard frontend. [@claim:clm_d781ab921c1f10a9b1ef5d1962f2e8cc901d9cb3dfad0dc24d3e6b0c9bd5c575]
- Tool call content is gated during streaming via a toolCallDepth counter that suppresses emission inside XML tool-call blocks, delivering the clean tool call as a finish_reason: tool_calls phase. [@claim:clm_f88084d2baff02f00726a4855dc9bbfd432e8c16aa0f26e437a3e491ec3edf9b]
- Large context payloads are auto-uploaded as Qwen file attachments, and tool results such as git diffs and JSON arrays are compressed before being sent to the model to reduce token usage. [@claim:clm_f9f959f77b73d54da9994773c4ad87ec37f3b90bfd414b30fe7c05d34b95717a]
<!-- rcw:end owner=source:src_eafbf75854c659f28d24f863e771642b block=evidence -->

## Researcher notes

