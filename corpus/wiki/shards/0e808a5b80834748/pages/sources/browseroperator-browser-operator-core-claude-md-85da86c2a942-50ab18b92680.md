---
access: public
aliases: []
claim_ids:
- clm_260b9aab8b9fd25e04baa5583a17c8fa36f5189f1ec44a357580eea248080e6c
- clm_397777d17a11c7c6ec5839c577732e1bfc70033e9df97af1f3fe91daf46b6551
maturity: draft
page_id: pg_2fa556756c0557199e9850ab18b92680
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c40a356f5c8d5824a4200837928a61db
title: BrowserOperator/browser-operator-core/CLAUDE.md @ 85da86c2a942
updated_at: '2026-09-14T03:05:59Z'
---

# BrowserOperator/browser-operator-core/CLAUDE.md @ 85da86c2a942

<!-- rcw:begin owner=source:src_c40a356f5c8d5824a4200837928a61db block=evidence -->
- The product supports four LLM providers (LiteLLM, OpenAI, Groq, OpenRouter) per MODEL-CONFIGS.md, with LiteLLM enabling local models via Ollama; CLAUDE.md additionally lists cerebras and anthropic providers. [@claim:clm_260b9aab8b9fd25e04baa5583a17c8fa36f5189f1ec44a357580eea248080e6c]
- Repository development practice: contributors use gclient sync and npm install, build via npm run build, run Karma/Mocha unit tests, Puppeteer webtests, and ESLint, and must add tests and pass lint before PRs reviewed by maintainers. [@claim:clm_397777d17a11c7c6ec5839c577732e1bfc70033e9df97af1f3fe91daf46b6551]
<!-- rcw:end owner=source:src_c40a356f5c8d5824a4200837928a61db block=evidence -->

## Researcher notes

