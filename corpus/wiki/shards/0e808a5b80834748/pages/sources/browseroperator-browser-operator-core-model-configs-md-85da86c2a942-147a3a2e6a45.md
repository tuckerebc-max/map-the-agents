---
access: public
aliases: []
claim_ids:
- clm_260b9aab8b9fd25e04baa5583a17c8fa36f5189f1ec44a357580eea248080e6c
- clm_877e56586ffe66be75a509e9c3016bd12078f04190a0d376e6d7603becd1bd52
- clm_97dd9429faaef74c1a78553c2dfde848594b6653837284b225455e37193d79e5
- clm_c1ba1e5c03074ff33b7e3b526c2b83d60f5242e6b3baa6e00e82816b2f0a7dad
- clm_e76fda5ac983280fa6a052d8e40fae6757e011a5f1bb41a4952752a234db0aca
maturity: draft
page_id: pg_5ba032633b2f52b0bb37147a3a2e6a45
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_38ad4e075add52718a2ce786bcd4d979
title: BrowserOperator/browser-operator-core/MODEL-CONFIGS.md @ 85da86c2a942
updated_at: '2026-09-14T03:05:59Z'
---

# BrowserOperator/browser-operator-core/MODEL-CONFIGS.md @ 85da86c2a942

<!-- rcw:begin owner=source:src_38ad4e075add52718a2ce786bcd4d979 block=evidence -->
- The product supports four LLM providers (LiteLLM, OpenAI, Groq, OpenRouter) per MODEL-CONFIGS.md, with LiteLLM enabling local models via Ollama; CLAUDE.md additionally lists cerebras and anthropic providers. [@claim:clm_260b9aab8b9fd25e04baa5583a17c8fa36f5189f1ec44a357580eea248080e6c]
- Provider, model, and API-key settings are persisted in localStorage under keys such as ai_chat_provider, ai_chat_model_selection, ai_chat_mini_model, ai_chat_nano_model, and per-provider API key/endpoint keys. [@claim:clm_877e56586ffe66be75a509e9c3016bd12078f04190a0d376e6d7603becd1bd52]
- An evaluation protocol defines JSON-RPC methods including 'configure_llm' for persistent LLM configuration and 'evaluate' requests that can carry per-request model, provider, API key, and endpoint overrides. [@claim:clm_97dd9429faaef74c1a78553c2dfde848594b6653837284b225455e37193d79e5]
- The configuration rollout notes agent-server support for persistent configuration and comprehensive tests/performance testing as still pending (marked in-progress), while earlier phases are marked completed. [@claim:clm_c1ba1e5c03074ff33b7e3b526c2b83d60f5242e6b3baa6e00e82816b2f0a7dad]
- LLM configuration uses a three-tier model scheme (Main for agent execution, Mini for lightweight operations, Nano for simple tasks) with configuration precedence of override first, then localStorage fallback. [@claim:clm_e76fda5ac983280fa6a052d8e40fae6757e011a5f1bb41a4952752a234db0aca]
<!-- rcw:end owner=source:src_38ad4e075add52718a2ce786bcd4d979 block=evidence -->

## Researcher notes

