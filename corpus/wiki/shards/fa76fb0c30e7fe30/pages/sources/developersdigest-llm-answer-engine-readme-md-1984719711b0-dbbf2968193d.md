---
access: public
aliases: []
claim_ids:
- clm_1221a415c896506eaeefdc1b471e6e2c0273c40fd4c5b0a1a00e9a16b2fad518
- clm_1604233aea01ba52075b1e01e84737b0777275dc02574e40eb5d4a6b75a68a33
- clm_235828817c9b3ebdd73e124ff865635cb6ea512ddd3fb7e79c7e449bc6124101
- clm_8f4b73645fc7e38f946b37974c3aee2c43e24aaae653d8142707c1f8c7e3ebb1
- clm_9d580b8633e18b6d7975ec18bde123584e7d0217b7c98a6e6cc96cc0f7792f3d
- clm_b6d9828e2d6ccd9061a5a9e7f349fec6e34260d578a4e495614ff689baa30f6f
- clm_c4200fd600dbd1ddfd4be299b7d757a2ec14a778813e9d9396448533329b78f0
- clm_c4ae66ff30e7292f91c00c8144ac573c4cbf5960082caa35f7dd7fabe6fd09da
- clm_cfa5d1000371f6fedf1080a1c603141703f4457be5173f5baa8702da89bcc076
- clm_df5f8b5379ec92201fb9a7a43d4dc2825774ac6f61d961e2fed6cc3458388648
- clm_f597db8c2d5e7824905540093076126c3e01863d171728478192578dcde16b7c
maturity: draft
page_id: pg_9d27e3caf73c562e8ba9dbbf2968193d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_58056baf665b5a61a462d5a60a8a4bf8
title: developersdigest/llm-answer-engine/README.md @ 1984719711b0
updated_at: '2026-09-14T03:46:25Z'
---

# developersdigest/llm-answer-engine/README.md @ 1984719711b0

<!-- rcw:begin owner=source:src_58056baf665b5a61a462d5a60a8a4bf8 block=evidence -->
- Function calling (beta) supports maps/locations and shopping via Serper APIs, TradingView stock data, and Spotify, and must be enabled by setting useFunctionCalling to true. [@claim:clm_1221a415c896506eaeefdc1b471e6e2c0273c40fd4c5b0a1a00e9a16b2fad518]
- Repository development practice: contributions are accepted via fork, changes, and pull requests, and issues may be opened for improvements or bugs. [@claim:clm_1604233aea01ba52075b1e01e84737b0777275dc02574e40eb5d4a6b75a68a33]
- With Ollama, time-to-first-token can be long when using local embedding and inference models; the README recommends lowering RAG-related config values to reduce it. [@claim:clm_235828817c9b3ebdd73e124ff865635cb6ea512ddd3fb7e79c7e449bc6124101]
- Ollama support is partial: streaming text and embeddings work, but follow-up questions are not yet supported and are skipped when useOllamaInference is true. [@claim:clm_8f4b73645fc7e38f946b37974c3aee2c43e24aaae653d8142707c1f8c7e3ebb1]
- Setup requires API keys from OpenAI, Groq, Brave Search, and Serper, provided via a .env file or docker-compose.yml, with Node.js >= 18.17.0 required by Next.js 14.1.x. [@claim:clm_9d580b8633e18b6d7975ec18bde123584e7d0217b7c98a6e6cc96cc0f7792f3d]
- Behavior is controlled via app/config.tsx flags including useOllamaInference, useOllamaEmbeddings, useFunctionCalling, useRateLimiting, useSemanticCache, and usePortkey, with defaults like mixtral-8x7b-32768 and textChunkSize 800. [@claim:clm_b6d9828e2d6ccd9061a5a9e7f349fec6e34260d578a4e495614ff689baa30f6f]
- A standalone Node.js/Express backend version exists in the express-api directory as a reference for building a similar API. [@claim:clm_c4200fd600dbd1ddfd4be299b7d757a2ec14a778813e9d9396448533329b78f0]
- The app can be run via Docker (docker compose up -d) or non-Docker (npm/bun run dev), and one-click Vercel deployment is offered with all four API keys required. [@claim:clm_c4ae66ff30e7292f91c00c8144ac573c4cbf5960082caa35f7dd7fabe6fd09da]
- The project relies on Groq, Mistral's Mixtral, Langchain.JS, Brave Search, Serper API, and OpenAI to return sources, answers, images, videos, and follow-up questions. [@claim:clm_cfa5d1000371f6fedf1080a1c603141703f4457be5173f5baa8702da89bcc076]
- The stack includes Next.js, Tailwind CSS, Vercel AI SDK, Cheerio for HTML parsing, plus optional Ollama, Upstash Redis rate limiting, and Upstash semantic cache. [@claim:clm_df5f8b5379ec92201fb9a7a43d4dc2825774ac6f61d961e2fed6cc3458388648]
- Completed roadmap items include Portkey AI Gateway for multiple model providers, semantic caching, Fal.AI SD3 image generation via @ mention, conditional UI components, and dark mode. [@claim:clm_f597db8c2d5e7824905540093076126c3e01863d171728478192578dcde16b7c]
<!-- rcw:end owner=source:src_58056baf665b5a61a462d5a60a8a4bf8 block=evidence -->

## Researcher notes

