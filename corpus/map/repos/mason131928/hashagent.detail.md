# mason131928/hashagent -- full detail

[Back to orientation](hashagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mason131928/hashagent/aaf72bd507e796b791712f13fa21512f6a4cc497/c140ae9412f930bb.json](../../../wiki/dossiers/mason131928/hashagent/aaf72bd507e796b791712f13fa21512f6a4cc497/c140ae9412f930bb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Architecture routes agent decoding and inference through a model registry into a WebLLM Worker or a Transformers.js Worker, both targeting WebGPU on the user's device. -- evidence: [README.md#L58-L58](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L58-L58), [README.md#L27-L41](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L27-L41) (`clm_5cdf7357d2b5fbbc681b755a1c1ecbd83f28e4622e72c7e083e77aa7e3174744`)
- [observation/documented] Optional stateless Cloudflare Pages Functions provide /api/search and /api/read because search providers and arbitrary pages do not reliably allow browser CORS; they can be disabled in Agent settings. -- evidence: [README.md#L45-L45](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L45-L45) (`clm_6a09bed3a98aac8a304fd8f79d3f0f5969aef0a287b0d73f262e0519d54f1365`)

## design-choices (1 claim(s))

- [observation/documented] Auto profile picks SmolLM2 360M on phones and Qwen2.5 3B on desktop; iOS stays on WebLLM because ONNX Runtime Web marks its WebGPU execution provider unsupported on iOS browsers. -- evidence: [README.md#L114-L114](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L114-L114), [README.md#L23-L23](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L23-L23) (`clm_2b47c72a8a24253b5ce5552664f2d207096035a736cbfa38c9e04b30d28450ef`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributor guidance says to treat tracked files as public, use neutral fixtures, keep tests deterministic and portable, and run npm run check, npm run build, and git diff --check before handing off changes. -- evidence: [AGENTS.md#L5-L9](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/AGENTS.md#L5-L9) (`clm_63dbc8903a3018a656ca5f5b94b5565813806c06c843b15b79e3fa716ff6d5b3`)
- [observation/documented] Repository development practice: local development uses npm install/npm run dev for UI and inference, npm run dev:cloudflare for Pages Functions with a mock KV binding, plus npm test, build, and preview checks. -- evidence: [README.md#L175-L177](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L175-L177), [README.md#L181-L185](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L181-L185), [README.md#L168-L171](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L168-L171), [README.md#L173-L173](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L173-L173) (`clm_4f5beab5755d70b85fa92427bd886c70e1511a7dfc9d49e5fda7c428cde03fab`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Agents are shared via a URL protocol: a self-contained '#agent=' hash carrying base64url-encoded deflate-raw compressed JSON, or an optional KV-backed '/s/<id>' short link. -- evidence: [README.md#L86-L89](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L86-L89), [README.md#L64-L67](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L64-L67) (`clm_db1c9dbf300296ce7ed8f91197919f81595ef3440a9864d5cde4ea9d1680a48a`)
- [observation/documented] Protocol v2 agent definitions include fields v, name, emoji, sys, hello, temp (default 0.7), profile (auto|mobile|balanced|quality|vision), and an optional modelHint that is a preference, not a requirement. -- evidence: [README.md#L82-L82](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L82-L82), [README.md#L69-L80](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L69-L80) (`clm_33df9c2c7e1e72f55a5df2b10ab233a2748f7ce8e8534baa817f1add81197344`)
- [observation/documented] The decoder supports fallbacks: '2u.' for uncompressed v2 payloads when deflate-raw is unavailable, and legacy '2.' v2 and plain-base64url v1 links remain readable with v1 upgraded in memory. -- evidence: [README.md#L91-L91](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L91-L91) (`clm_c11a1bc7432ed5d70836261b69b156ed3fafa8a5e29d8fbcf62313553346a244`)

## memory-state (1 claim(s))

- [observation/documented] Chat is ephemeral by default; if the user explicitly opts in, up to 50 recent messages are stored in device-local IndexedDB and never synced. -- evidence: [README.md#L229-L229](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L229-L229), [README.md#L5-L5](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L5-L5) (`clm_0ccedb14b88d48f49fa0fd99e71e61562f0912d03cb26d411ccd4089237a0ed1`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Every agent gets the same six audited tools (web search, web reader, Wikipedia, weather, calculator, local time); permissions are application capabilities, not data embedded in the shared URL. -- evidence: [README.md#L124-L124](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L124-L124), [README.md#L126-L133](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L126-L133) (`clm_de429f46b7652a26d4ae043f1b37d3a5cba9e612207d147b5e7f7d1974ac4f2d`)
- [observation/documented] Each turn runs a temperature-zero planning pass restricted to 'answer', 'clarify', or one schema-validated allowlisted tool call; tool names and arguments are validated before execution and the calculator never evaluates JavaScript. -- evidence: [README.md#L135-L135](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L135-L135) (`clm_9b601423c1f292644093aa5913d2e0bf6c0586260702699835b42bac5ba87293`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Models come from WebLLM's prebuiltAppConfig plus verified ONNX Community exports for Transformers.js 4.2, spanning SmolLM2 360M through Llama 3.1 8B, sourced from Meta, Microsoft, Mistral, Hugging Face, Google, Liquid AI, and Alibaba. -- evidence: [README.md#L114-L114](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L114-L114), [README.md#L97-L112](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L97-L112), [README.md#L95-L95](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L95-L95) (`clm_607bd7c8262823f12e33d4f8e72974a92906f74b21111f71d5d494d234b3e21f`)

## limitations (2 claim(s))

- [observation/documented] Web search parses public HTML/RSS rather than a supported search API, so upstream markup or anti-automation changes can temporarily break it; migration to an official API is the medium-term plan. -- evidence: [README.md#L145-L145](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L145-L145) (`clm_f028fee0862c6241e0774fb6322525cf66588b783160ab9a50d1d4f26a871622`)
- [observation/documented] The README states local 360M-8B models are not comparable to GPT-4-class hosted models and should not be relied on for medical, legal, financial, or safety-critical decisions. -- evidence: [README.md#L245-L245](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L245-L245) (`clm_1cbb673dd2f4bfa167d9b00ca453dd006a0b3078cd9cdf862c23734e15072ce2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

