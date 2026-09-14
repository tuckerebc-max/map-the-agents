# humanstack/vibe-coding-template

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7cec003ce14e @ e2ecbbaa1e07bb94

## Summary (orientation draft, not independently verified)

The repository is a full-stack starter template pairing a Next.js frontend with a Python FastAPI backend, Supabase auth/database/storage, LLM services (OpenAI/Anthropic), and Qdrant vector search, plus Cursor rules and AGENTS.md guidance for AI-assisted development. Evidence is documentation-only; no source code slices are present.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The template ships a Python FastAPI backend with Supabase integration for auth, database, realtime, storage, and migrations, plus LLM and vector-database services. -- evidence: [README.md#L35-L49](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L35-L49), [README.md#L3-L3](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L3-L3)
  - [observation/documented] The frontend is a Next.js application using Tailwind CSS with a Supabase client and complete auth flows including login, signup, and password reset. -- evidence: [README.md#L52-L56](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L52-L56)
- design-choices (1 claim(s)):
  - [observation/documented] The vector database layer falls back automatically to a local in-memory database when Qdrant is unavailable. -- evidence: [README.md#L35-L49](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L35-L49)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to use TypeScript for frontend files, Python type hints and async/await in the backend, and snake_case/camelCase naming conventions. -- evidence: [AGENTS.md#L16-L20](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/AGENTS.md#L16-L20)
  - [observation/documented] Repository development practice: contributors are told to follow the service layer pattern, use Pydantic models for validation, and use the generic SupabaseDatabaseService for database operations. -- evidence: [AGENTS.md#L23-L27](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/AGENTS.md#L23-L27)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Running the dev environment exposes the frontend at localhost:3000, the backend API at localhost:8000, and API docs at localhost:8000/docs. -- evidence: [README.md#L89-L92](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L89-L92)
  - [observation/documented] A Makefile provides commands such as make dev, prod variants, clean, and database migration commands like db-migration-new, db-apply, db-list, db-status, and db-push. -- evidence: [README.md#L173-L175](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L173-L175), [README.md#L179-L179](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L179-L179), [README.md#L167-L169](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L167-L169), [README.md#L183-L187](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L183-L187)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Prerequisites include Docker and Docker Compose, Make, Node.js 18+, Python 3.10+, and the Supabase CLI for migrations. -- evidence: [README.md#L61-L65](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L61-L65)
  - [observation/documented] Environment configuration requires Supabase URL and service key, OpenAI and/or Anthropic API keys for LLM features, and optionally Qdrant credentials. -- evidence: [AGENTS.md#L114-L117](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/AGENTS.md#L114-L117), [README.md#L108-L111](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L108-L111)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](vibe-coding-template.detail.md) for every claim.)

Metadata and full claim list: [full detail](vibe-coding-template.detail.md)
Human notes ([notes](vibe-coding-template.notes.md), never overwritten by build)

[Back to map index](../../index.md)
