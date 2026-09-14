# martian56/lumnicode -- full detail

[Back to orientation](lumnicode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/martian56/lumnicode/b18933aa526d345bb2262548db7947e93820144e/9e65f50aca588f87.json](../../../wiki/dossiers/martian56/lumnicode/b18933aa526d345bb2262548db7947e93820144e/9e65f50aca588f87.json)

## specifications (1 claim(s))

- [observation/documented] Lumnicode is described as an online code editor with built-in AI assistance where users supply their own API keys from supported providers, with no subscriptions or per-seat pricing. -- evidence: [README.md#L22-L22](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L22-L22), [README.md#L5-L5](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L5-L5) (`clm_51b109ad3d2a14ac7739e99547240f3e1f8bed3ac2737586fde91bd3a74e640d`)

## components (1 claim(s))

- [observation/documented] The architecture pairs a React SPA (Vite + TypeScript) frontend with a FastAPI Python backend, backed by PostgreSQL for metadata, MinIO/S3 for file content, and LangChain-based AI providers, connected via REST, SSE, and WebSocket. -- evidence: [README.md#L91-L110](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L91-L110), [README.md#L114-L122](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L114-L122), [README.md#L126-L134](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L126-L134) (`clm_9734362a804a2ceeafe797c8eb969ea197fb4afc25a35bb086c62b417d221fdf`)

## design-choices (1 claim(s))

- [observation/documented] File content is stored in S3-compatible storage (MinIO in development) rather than the database, with the database holding project and file metadata. -- evidence: [README.md#L91-L110](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L91-L110), [README.md#L26-L33](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L26-L33) (`clm_2ddf70d3d94108b05b1b5f63507ebc6189aaa31f51ed2cf30c101f63587a8c0e`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: local setup starts Postgres and MinIO via docker-compose.dev.yml, then runs the backend with uv (uv sync, alembic upgrade head, uvicorn) and the frontend with npm install and npm run dev. -- evidence: [README.md#L78-L83](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L78-L83), [README.md#L68-L74](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L68-L74), [README.md#L58-L62](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L58-L62), [README.md#L64-L64](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L64-L64) (`clm_5af34905b21cbe916f3053470488a912f8e6467994ef234623ab3c5a8b83cf96`)
- [observation/documented] Repository development practice: contributors run Black and Ruff plus pytest for the backend and ESLint plus a typed build for the frontend before committing; Python style is Black at line length 88 with PEP 8 and type hints. -- evidence: [CONTRIBUTING.md#L74-L78](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L74-L78), [README.md#L220-L223](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L220-L223), [CONTRIBUTING.md#L91-L95](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L91-L95), [CONTRIBUTING.md#L66-L72](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L66-L72), [README.md#L226-L229](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L226-L229) (`clm_874515dc6ce26f9afe32b48d759d5fe1d1bd7721732a81456e45bf1dfd0ca6e9`)
- [observation/documented] Repository development practice: feature branches are cut from develop using feature/, hotfix/, and release/ prefixes, and pull requests against develop should pass checks, get maintainer review, and squash commits when possible. -- evidence: [CONTRIBUTING.md#L51-L53](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L51-L53), [CONTRIBUTING.md#L57-L62](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L57-L62), [CONTRIBUTING.md#L85-L85](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L85-L85), [CONTRIBUTING.md#L161-L164](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L161-L164) (`clm_a6d57640042f6747e356c12ef028740b788837cdf5f1503e1ab423292ff4dc6d`)
- [observation/documented] Repository development practice: security vulnerabilities must not be filed as public GitHub issues; they are reported by email with a stated 48-hour acknowledgment and 30-day fix timeline for critical issues. -- evidence: [SECURITY.md#L16-L16](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/SECURITY.md#L16-L16), [SECURITY.md#L27-L29](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/SECURITY.md#L27-L29), [SECURITY.md#L14-L14](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/SECURITY.md#L14-L14) (`clm_b14889c714be84e4e33443b5d4839999c8f57936494ffd20339df24622312365`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The backend exposes REST endpoints such as POST /assist, POST /assist/stream (SSE), project and file CRUD, POST /ai/generate/{id}, and a WebSocket /ws/ai-progress/{id}; interactive docs are served at /docs and /redoc. -- evidence: [README.md#L205-L214](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L205-L214), [README.md#L200-L201](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L200-L201) (`clm_f6a44308eedd03e83ed8ea22e202a97a67a1f1af2adf66fe52e3e10f5f96ff1d`)

## memory-state (1 claim(s))

- [observation/documented] Users add their own AI API keys through the app's Settings > API Keys page after signing in with Clerk. -- evidence: [README.md#L87-L87](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L87-L87) (`clm_bfedbfe2367693ecefbb462627e829f3364d2316c7fe190467f219dd285bf14d`)

## orchestration (1 claim(s))

- [observation/documented] AI project generation is orchestrated by a LangGraph state machine with four nodes — plan, config, generate, finalize — streaming progress to the frontend over WebSocket. -- evidence: [README.md#L138-L158](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L138-L158), [README.md#L26-L33](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L26-L33) (`clm_9386153183ad98e986b3886604f13356f352797543f0fef468a569f7f49bb057`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Supported AI providers include OpenAI, Anthropic, Google Gemini, Groq, Together, Fireworks, and Cohere, with several accessed via OpenAI-compatible APIs; the backend uses LangChain/LangGraph and uv for dependency management. -- evidence: [README.md#L114-L122](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L114-L122), [README.md#L162-L170](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L162-L170), [README.md#L26-L33](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L26-L33) (`clm_e83aaafb8e7cc6e488ebf6b95193a6979569d9e9eb8f5ae3df62fea7feef59c1`)

## limitations (1 claim(s))

- [observation/documented] The README roadmap lists real-time collaboration, Git integration, a terminal emulator, a plugin system, a self-hosted deployment guide, and a mobile responsive editor as unchecked, i.e., planned but not yet delivered. -- evidence: [README.md#L263-L268](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L263-L268) (`clm_65ace3a972a28f67ebf1a34640a935a320838b36c5e5d084ae23f6b4c028edef`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

