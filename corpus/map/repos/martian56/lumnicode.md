# martian56/lumnicode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b18933aa526d @ 9e65f50aca588f87

## Summary (orientation draft, not independently verified)

README-documented snapshot of Lumnicode, a BYOK AI-powered online code editor with a FastAPI/React architecture, LangGraph-based AI generation, and S3 file storage; contributor guides cover setup, style, and PR workflow. No agent-performance evaluation evidence is present.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Lumnicode is described as an online code editor with built-in AI assistance where users supply their own API keys from supported providers, with no subscriptions or per-seat pricing. -- evidence: [README.md#L22-L22](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L22-L22), [README.md#L5-L5](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The architecture pairs a React SPA (Vite + TypeScript) frontend with a FastAPI Python backend, backed by PostgreSQL for metadata, MinIO/S3 for file content, and LangChain-based AI providers, connected via REST, SSE, and WebSocket. -- evidence: [README.md#L91-L110](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L91-L110), [README.md#L114-L122](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L114-L122), [README.md#L126-L134](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L126-L134)
- design-choices (1 claim(s)):
  - [observation/documented] File content is stored in S3-compatible storage (MinIO in development) rather than the database, with the database holding project and file metadata. -- evidence: [README.md#L91-L110](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L91-L110), [README.md#L26-L33](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L26-L33)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: local setup starts Postgres and MinIO via docker-compose.dev.yml, then runs the backend with uv (uv sync, alembic upgrade head, uvicorn) and the frontend with npm install and npm run dev. -- evidence: [README.md#L78-L83](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L78-L83), [README.md#L68-L74](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L68-L74), [README.md#L58-L62](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L58-L62), [README.md#L64-L64](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L64-L64)
  - [observation/documented] Repository development practice: contributors run Black and Ruff plus pytest for the backend and ESLint plus a typed build for the frontend before committing; Python style is Black at line length 88 with PEP 8 and type hints. -- evidence: [CONTRIBUTING.md#L74-L78](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L74-L78), [README.md#L220-L223](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L220-L223), [CONTRIBUTING.md#L91-L95](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L91-L95), [CONTRIBUTING.md#L66-L72](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/CONTRIBUTING.md#L66-L72), [README.md#L226-L229](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L226-L229)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The backend exposes REST endpoints such as POST /assist, POST /assist/stream (SSE), project and file CRUD, POST /ai/generate/{id}, and a WebSocket /ws/ai-progress/{id}; interactive docs are served at /docs and /redoc. -- evidence: [README.md#L205-L214](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L205-L214), [README.md#L200-L201](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L200-L201)
- memory-state (1 claim(s)):
  - [observation/documented] Users add their own AI API keys through the app's Settings > API Keys page after signing in with Clerk. -- evidence: [README.md#L87-L87](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L87-L87)
- orchestration (1 claim(s)):
  - [observation/documented] AI project generation is orchestrated by a LangGraph state machine with four nodes — plan, config, generate, finalize — streaming progress to the frontend over WebSocket. -- evidence: [README.md#L138-L158](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L138-L158), [README.md#L26-L33](https://github.com/martian56/lumnicode/blob/b18933aa526d345bb2262548db7947e93820144e/README.md#L26-L33)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](lumnicode.detail.md)

Metadata and full claim list: [full detail](lumnicode.detail.md)
Human notes ([notes](lumnicode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
