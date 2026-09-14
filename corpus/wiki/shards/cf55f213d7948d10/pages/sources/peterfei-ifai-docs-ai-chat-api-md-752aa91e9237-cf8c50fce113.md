---
access: public
aliases: []
claim_ids:
- clm_215aab98eec72b526ae5b3d3fec391b2c022b4c8c4bde322e7d57325191385d9
- clm_7bc32c3ea497a44151884b763603da68add2fab948f35b4dbc94fe3d72b5f92c
- clm_b83b71f2247b6834b40c77f28f857db21754a836804a8a860702421f6d421df9
- clm_fa81b1ede2c86d5d68ad9635b7a313416e1653a7819c0c4b1f5863607e1c967a
maturity: draft
page_id: pg_8b6bb1c8bf4c5b9faad3cf8c50fce113
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8f7dc0129d705e15af329ac3acc0e8be
title: peterfei/ifai/docs/AI-CHAT-API.md @ 752aa91e9237
updated_at: '2026-09-14T02:30:22Z'
---

# peterfei/ifai/docs/AI-CHAT-API.md @ 752aa91e9237

<!-- rcw:begin owner=source:src_8f7dc0129d705e15af329ac3acc0e8be block=evidence -->
- An HTTP API exposes POST /api/ai/chat/stream returning SSE (text/event-stream) streaming chat responses, with request fields messages, provider_config (name, api_key, base_url), model, and optional enable_tools. [@claim:clm_215aab98eec72b526ae5b3d3fec391b2c022b4c8c4bde322e7d57325191385d9]
- Repository development practice: contributors run the app in dev mode with npm run tauri dev after npm install, and build releases with npm run build:community followed by npm run tauri:community; the HTTP API is enabled in dev via ENABLE_HTTP_API=true. [@claim:clm_7bc32c3ea497a44151884b763603da68add2fab948f35b4dbc94fe3d72b5f92c]
- Per the API documentation, tool calling via the enable_tools flag is marked as not yet implemented (待实现). [@claim:clm_b83b71f2247b6834b40c77f28f857db21754a836804a8a860702421f6d421df9]
- SSE events include content_delta, done (with finish_reason), and error types carrying error codes such as AI_SERVICE_ERROR, NETWORK_ERROR, TIMEOUT, and API_ERROR; HTTP 503 and 500 are documented error statuses. [@claim:clm_fa81b1ede2c86d5d68ad9635b7a313416e1653a7819c0c4b1f5863607e1c967a]
<!-- rcw:end owner=source:src_8f7dc0129d705e15af329ac3acc0e8be block=evidence -->

## Researcher notes

