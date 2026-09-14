---
access: public
aliases: []
claim_ids:
- clm_2ddf70d3d94108b05b1b5f63507ebc6189aaa31f51ed2cf30c101f63587a8c0e
- clm_51b109ad3d2a14ac7739e99547240f3e1f8bed3ac2737586fde91bd3a74e640d
- clm_5af34905b21cbe916f3053470488a912f8e6467994ef234623ab3c5a8b83cf96
- clm_65ace3a972a28f67ebf1a34640a935a320838b36c5e5d084ae23f6b4c028edef
- clm_874515dc6ce26f9afe32b48d759d5fe1d1bd7721732a81456e45bf1dfd0ca6e9
- clm_9386153183ad98e986b3886604f13356f352797543f0fef468a569f7f49bb057
- clm_9734362a804a2ceeafe797c8eb969ea197fb4afc25a35bb086c62b417d221fdf
- clm_bfedbfe2367693ecefbb462627e829f3364d2316c7fe190467f219dd285bf14d
- clm_e83aaafb8e7cc6e488ebf6b95193a6979569d9e9eb8f5ae3df62fea7feef59c1
- clm_f6a44308eedd03e83ed8ea22e202a97a67a1f1af2adf66fe52e3e10f5f96ff1d
maturity: draft
page_id: pg_f98c4d1149685888beaacf0ef846ce82
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bfcbe37df9b851d5b8601f09176ac730
title: martian56/lumnicode/README.md @ b18933aa526d
updated_at: '2026-09-14T02:16:20Z'
---

# martian56/lumnicode/README.md @ b18933aa526d

<!-- rcw:begin owner=source:src_bfcbe37df9b851d5b8601f09176ac730 block=evidence -->
- File content is stored in S3-compatible storage (MinIO in development) rather than the database, with the database holding project and file metadata. [@claim:clm_2ddf70d3d94108b05b1b5f63507ebc6189aaa31f51ed2cf30c101f63587a8c0e]
- Lumnicode is described as an online code editor with built-in AI assistance where users supply their own API keys from supported providers, with no subscriptions or per-seat pricing. [@claim:clm_51b109ad3d2a14ac7739e99547240f3e1f8bed3ac2737586fde91bd3a74e640d]
- Repository development practice: local setup starts Postgres and MinIO via docker-compose.dev.yml, then runs the backend with uv (uv sync, alembic upgrade head, uvicorn) and the frontend with npm install and npm run dev. [@claim:clm_5af34905b21cbe916f3053470488a912f8e6467994ef234623ab3c5a8b83cf96]
- The README roadmap lists real-time collaboration, Git integration, a terminal emulator, a plugin system, a self-hosted deployment guide, and a mobile responsive editor as unchecked, i.e., planned but not yet delivered. [@claim:clm_65ace3a972a28f67ebf1a34640a935a320838b36c5e5d084ae23f6b4c028edef]
- Repository development practice: contributors run Black and Ruff plus pytest for the backend and ESLint plus a typed build for the frontend before committing; Python style is Black at line length 88 with PEP 8 and type hints. [@claim:clm_874515dc6ce26f9afe32b48d759d5fe1d1bd7721732a81456e45bf1dfd0ca6e9]
- AI project generation is orchestrated by a LangGraph state machine with four nodes — plan, config, generate, finalize — streaming progress to the frontend over WebSocket. [@claim:clm_9386153183ad98e986b3886604f13356f352797543f0fef468a569f7f49bb057]
- The architecture pairs a React SPA (Vite + TypeScript) frontend with a FastAPI Python backend, backed by PostgreSQL for metadata, MinIO/S3 for file content, and LangChain-based AI providers, connected via REST, SSE, and WebSocket. [@claim:clm_9734362a804a2ceeafe797c8eb969ea197fb4afc25a35bb086c62b417d221fdf]
- Users add their own AI API keys through the app's Settings > API Keys page after signing in with Clerk. [@claim:clm_bfedbfe2367693ecefbb462627e829f3364d2316c7fe190467f219dd285bf14d]
- Supported AI providers include OpenAI, Anthropic, Google Gemini, Groq, Together, Fireworks, and Cohere, with several accessed via OpenAI-compatible APIs; the backend uses LangChain/LangGraph and uv for dependency management. [@claim:clm_e83aaafb8e7cc6e488ebf6b95193a6979569d9e9eb8f5ae3df62fea7feef59c1]
- The backend exposes REST endpoints such as POST /assist, POST /assist/stream (SSE), project and file CRUD, POST /ai/generate/{id}, and a WebSocket /ws/ai-progress/{id}; interactive docs are served at /docs and /redoc. [@claim:clm_f6a44308eedd03e83ed8ea22e202a97a67a1f1af2adf66fe52e3e10f5f96ff1d]
<!-- rcw:end owner=source:src_bfcbe37df9b851d5b8601f09176ac730 block=evidence -->

## Researcher notes

