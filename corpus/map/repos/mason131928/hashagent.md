# mason131928/hashagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit aaf72bd507e7 @ c140ae9412f930bb

## Summary (orientation draft, not independently verified)

HashAgent is a local-first web app that encodes AI agent definitions into self-contained URLs and runs models in-browser via WebLLM/Transformers.js on WebGPU, with optional Cloudflare Pages Function gateways for search and page reading. Evidence is README documentation plus contributor hygiene rules; no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Architecture routes agent decoding and inference through a model registry into a WebLLM Worker or a Transformers.js Worker, both targeting WebGPU on the user's device. -- evidence: [README.md#L58-L58](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L58-L58), [README.md#L27-L41](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L27-L41)
  - [observation/documented] Optional stateless Cloudflare Pages Functions provide /api/search and /api/read because search providers and arbitrary pages do not reliably allow browser CORS; they can be disabled in Agent settings. -- evidence: [README.md#L45-L45](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L45-L45)
- design-choices (1 claim(s)):
  - [observation/documented] Auto profile picks SmolLM2 360M on phones and Qwen2.5 3B on desktop; iOS stays on WebLLM because ONNX Runtime Web marks its WebGPU execution provider unsupported on iOS browsers. -- evidence: [README.md#L114-L114](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L114-L114), [README.md#L23-L23](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L23-L23)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributor guidance says to treat tracked files as public, use neutral fixtures, keep tests deterministic and portable, and run npm run check, npm run build, and git diff --check before handing off changes. -- evidence: [AGENTS.md#L5-L9](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/AGENTS.md#L5-L9)
  - [observation/documented] Repository development practice: local development uses npm install/npm run dev for UI and inference, npm run dev:cloudflare for Pages Functions with a mock KV binding, plus npm test, build, and preview checks. -- evidence: [README.md#L175-L177](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L175-L177), [README.md#L181-L185](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L181-L185), [README.md#L168-L171](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L168-L171), [README.md#L173-L173](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L173-L173)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Agents are shared via a URL protocol: a self-contained '#agent=' hash carrying base64url-encoded deflate-raw compressed JSON, or an optional KV-backed '/s/<id>' short link. -- evidence: [README.md#L86-L89](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L86-L89), [README.md#L64-L67](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L64-L67)
  - [observation/documented] Protocol v2 agent definitions include fields v, name, emoji, sys, hello, temp (default 0.7), profile (auto|mobile|balanced|quality|vision), and an optional modelHint that is a preference, not a requirement. -- evidence: [README.md#L82-L82](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L82-L82), [README.md#L69-L80](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L69-L80)
- memory-state (1 claim(s)):
  - [observation/documented] Chat is ephemeral by default; if the user explicitly opts in, up to 50 recent messages are stored in device-local IndexedDB and never synced. -- evidence: [README.md#L229-L229](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L229-L229), [README.md#L5-L5](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L5-L5)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Every agent gets the same six audited tools (web search, web reader, Wikipedia, weather, calculator, local time); permissions are application capabilities, not data embedded in the shared URL. -- evidence: [README.md#L124-L124](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L124-L124), [README.md#L126-L133](https://github.com/mason131928/hashagent/blob/aaf72bd507e796b791712f13fa21512f6a4cc497/README.md#L126-L133)
More evidence: [full detail](hashagent.detail.md)

Metadata and full claim list: [full detail](hashagent.detail.md)
Human notes ([notes](hashagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
