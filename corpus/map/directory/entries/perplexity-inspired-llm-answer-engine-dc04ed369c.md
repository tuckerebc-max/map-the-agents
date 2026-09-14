# Perplexity-Inspired LLM Answer Engine (`perplexity-inspired-llm-answer-engine`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: developersdigest
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: Groq, OpenAI, Ollama, Portkey AI Gateway (Azure, Anyscale, Google, Anthropic, Cohere, Together, Perplexity, Mistral, Nomic, AI21, Stability, DeepInfra)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [developersdigest/llm-answer-engine](../../repos/developersdigest/llm-answer-engine.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Perplexity-like answer engine returning sources, answers, images, videos, and follow-up questions. Combines web search (Brave/Serper) with LLMs (Groq/OpenAI/Ollama), function calling (maps, shopping, stocks, Spotify), semantic caching via Upstash, rate limiting, AI gateway support for 15+ providers, dynamic UI rendering, and dual deployment (Next.js or Express-only).

(captured site page body (agents/perplexity-inspired-llm-answer-engine.md), not a verified repo-code finding)
This repository emerged from the early-2024 wave of Perplexity clones as a teachable, single-repo implementation of an answer engine: Brave and Serper supply search results, the content gets scraped and embedded, and a hosted LLM synthesizes answers with sources, images, videos, and suggested follow-ups. Function calling extends it to maps, shopping, stock data, and Spotify, while a Portkey gateway route adds a dozen additional inference providers and an Upstash layer adds semantic caching and rate limits. Deployment paths cover Vercel, Docker, and a standalone Express API. The project's value is educational — it has 5,000+ stars and an accompanying YouTube walkthrough — but development stalled on a Next.js 14 stack with Groq's deprecated Mixtral model ID, and its issues and pull requests have gone unanswered. It is studied rather than operated.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/perplexity-inspired-llm-answer-engine.md)
