---
access: public
aliases: []
claim_ids:
- clm_6d9665f090b2c247f9936ab72b25265b23363cbdc18d2c9b4ad7a749efdc45c9
- clm_b66cb0c76f0df4396995fb17655289c3576156910a1254b20e646a8955b36732
maturity: draft
page_id: pg_54a8d3f0686f5ac6a706f19fa3fddfc5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_857348cfc3515ede89022d65dcb6b326
title: halfwhey/claudraband/docs/daemon-api.md @ d2b6a7d1836f
updated_at: '2026-09-14T01:53:26Z'
---

# halfwhey/claudraband/docs/daemon-api.md @ d2b6a7d1836f

<!-- rcw:begin owner=source:src_857348cfc3515ede89022d65dcb6b326 block=evidence -->
- The daemon exposes an HTTP API mirroring CLI verbs: POST /sessions, /prompt, /send, /interrupt, GET /sessions/:id/status, /last, and an SSE /watch endpoint, with JSON error bodies and 400/404/409/500 statuses. [@claim:clm_6d9665f090b2c247f9936ab72b25265b23363cbdc18d2c9b4ad7a749efdc45c9]
- The SSE watch stream sends a ready event, then JSON events with monotonically increasing seq values; kinds include user_message, assistant_text, assistant_thinking, tool_call, tool_result, turn_end, system, and error, plus permission_request events. [@claim:clm_b66cb0c76f0df4396995fb17655289c3576156910a1254b20e646a8955b36732]
<!-- rcw:end owner=source:src_857348cfc3515ede89022d65dcb6b326 block=evidence -->

## Researcher notes

