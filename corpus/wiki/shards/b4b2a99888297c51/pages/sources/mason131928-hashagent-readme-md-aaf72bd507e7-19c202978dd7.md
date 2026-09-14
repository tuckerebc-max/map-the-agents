---
access: public
aliases: []
claim_ids:
- clm_0ccedb14b88d48f49fa0fd99e71e61562f0912d03cb26d411ccd4089237a0ed1
- clm_1cbb673dd2f4bfa167d9b00ca453dd006a0b3078cd9cdf862c23734e15072ce2
- clm_2b47c72a8a24253b5ce5552664f2d207096035a736cbfa38c9e04b30d28450ef
- clm_33df9c2c7e1e72f55a5df2b10ab233a2748f7ce8e8534baa817f1add81197344
- clm_4f5beab5755d70b85fa92427bd886c70e1511a7dfc9d49e5fda7c428cde03fab
- clm_5cdf7357d2b5fbbc681b755a1c1ecbd83f28e4622e72c7e083e77aa7e3174744
- clm_607bd7c8262823f12e33d4f8e72974a92906f74b21111f71d5d494d234b3e21f
- clm_6a09bed3a98aac8a304fd8f79d3f0f5969aef0a287b0d73f262e0519d54f1365
- clm_9b601423c1f292644093aa5913d2e0bf6c0586260702699835b42bac5ba87293
- clm_c11a1bc7432ed5d70836261b69b156ed3fafa8a5e29d8fbcf62313553346a244
- clm_db1c9dbf300296ce7ed8f91197919f81595ef3440a9864d5cde4ea9d1680a48a
- clm_de429f46b7652a26d4ae043f1b37d3a5cba9e612207d147b5e7f7d1974ac4f2d
- clm_f028fee0862c6241e0774fb6322525cf66588b783160ab9a50d1d4f26a871622
maturity: draft
page_id: pg_e6f89ddd52e85ade95d319c202978dd7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_38c5c5530d0e536b9988e3568395ea95
title: mason131928/hashagent/README.md @ aaf72bd507e7
updated_at: '2026-09-14T04:08:09Z'
---

# mason131928/hashagent/README.md @ aaf72bd507e7

<!-- rcw:begin owner=source:src_38c5c5530d0e536b9988e3568395ea95 block=evidence -->
- Chat is ephemeral by default; if the user explicitly opts in, up to 50 recent messages are stored in device-local IndexedDB and never synced. [@claim:clm_0ccedb14b88d48f49fa0fd99e71e61562f0912d03cb26d411ccd4089237a0ed1]
- The README states local 360M-8B models are not comparable to GPT-4-class hosted models and should not be relied on for medical, legal, financial, or safety-critical decisions. [@claim:clm_1cbb673dd2f4bfa167d9b00ca453dd006a0b3078cd9cdf862c23734e15072ce2]
- Auto profile picks SmolLM2 360M on phones and Qwen2.5 3B on desktop; iOS stays on WebLLM because ONNX Runtime Web marks its WebGPU execution provider unsupported on iOS browsers. [@claim:clm_2b47c72a8a24253b5ce5552664f2d207096035a736cbfa38c9e04b30d28450ef]
- Protocol v2 agent definitions include fields v, name, emoji, sys, hello, temp (default 0.7), profile (auto|mobile|balanced|quality|vision), and an optional modelHint that is a preference, not a requirement. [@claim:clm_33df9c2c7e1e72f55a5df2b10ab233a2748f7ce8e8534baa817f1add81197344]
- Repository development practice: local development uses npm install/npm run dev for UI and inference, npm run dev:cloudflare for Pages Functions with a mock KV binding, plus npm test, build, and preview checks. [@claim:clm_4f5beab5755d70b85fa92427bd886c70e1511a7dfc9d49e5fda7c428cde03fab]
- Architecture routes agent decoding and inference through a model registry into a WebLLM Worker or a Transformers.js Worker, both targeting WebGPU on the user's device. [@claim:clm_5cdf7357d2b5fbbc681b755a1c1ecbd83f28e4622e72c7e083e77aa7e3174744]
- Models come from WebLLM's prebuiltAppConfig plus verified ONNX Community exports for Transformers.js 4.2, spanning SmolLM2 360M through Llama 3.1 8B, sourced from Meta, Microsoft, Mistral, Hugging Face, Google, Liquid AI, and Alibaba. [@claim:clm_607bd7c8262823f12e33d4f8e72974a92906f74b21111f71d5d494d234b3e21f]
- Optional stateless Cloudflare Pages Functions provide /api/search and /api/read because search providers and arbitrary pages do not reliably allow browser CORS; they can be disabled in Agent settings. [@claim:clm_6a09bed3a98aac8a304fd8f79d3f0f5969aef0a287b0d73f262e0519d54f1365]
- Each turn runs a temperature-zero planning pass restricted to 'answer', 'clarify', or one schema-validated allowlisted tool call; tool names and arguments are validated before execution and the calculator never evaluates JavaScript. [@claim:clm_9b601423c1f292644093aa5913d2e0bf6c0586260702699835b42bac5ba87293]
- The decoder supports fallbacks: '2u.' for uncompressed v2 payloads when deflate-raw is unavailable, and legacy '2.' v2 and plain-base64url v1 links remain readable with v1 upgraded in memory. [@claim:clm_c11a1bc7432ed5d70836261b69b156ed3fafa8a5e29d8fbcf62313553346a244]
- Agents are shared via a URL protocol: a self-contained '#agent=' hash carrying base64url-encoded deflate-raw compressed JSON, or an optional KV-backed '/s/<id>' short link. [@claim:clm_db1c9dbf300296ce7ed8f91197919f81595ef3440a9864d5cde4ea9d1680a48a]
- Every agent gets the same six audited tools (web search, web reader, Wikipedia, weather, calculator, local time); permissions are application capabilities, not data embedded in the shared URL. [@claim:clm_de429f46b7652a26d4ae043f1b37d3a5cba9e612207d147b5e7f7d1974ac4f2d]
- Web search parses public HTML/RSS rather than a supported search API, so upstream markup or anti-automation changes can temporarily break it; migration to an official API is the medium-term plan. [@claim:clm_f028fee0862c6241e0774fb6322525cf66588b783160ab9a50d1d4f26a871622]
<!-- rcw:end owner=source:src_38c5c5530d0e536b9988e3568395ea95 block=evidence -->

## Researcher notes

