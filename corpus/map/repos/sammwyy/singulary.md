# sammwyy/singulary

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5b51298504a4 @ 27be8bccf199f5ab

## Summary (orientation draft, not independently verified)

The snapshot consists of design/architecture documentation (ARCHITECTURE.md, PROJECT.md, docs/byok.md) describing Singulary as a self-hostable, Docker-based AI app-builder monorepo with a React/Vite frontend and Express/TypeScript backend. Most PROJECT.md content is aspirational ('should') specification rather than verified runtime behavior. Evidence coverage: 212 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project specification targets a self-hostable alternative to tools like v0, Lovable, Bolt, Replit Agent, or Cursor-style agents, emphasizing local-first development, BYOK access, Docker-based execution, multi-project workspaces, and auditable AI-driven changes. -- evidence: [PROJECT.md#L5-L5](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L5-L5)
  - [observation/documented] The spec calls for both single-user mode (first user becomes instance admin owning everything) and multi-user organization mode with teams, roles, groups, permissions, shared keys, quotas, and scoped environments. -- evidence: [PROJECT.md#L99-L99](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L99-L99), [PROJECT.md#L116-L116](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L116-L116), [PROJECT.md#L15-L16](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L15-L16)
- components (3 claim(s)):
  - [observation/documented] Singulary is a monorepo with a React frontend and an Express backend; in production the frontend is built to static assets and served by the same Express process that exposes the API under /api. -- evidence: [ARCHITECTURE.md#L3-L3](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L3-L3), [ARCHITECTURE.md#L35-L39](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L35-L39)
  - [observation/documented] The backend (apps/server) is an Express application on Node.js using TypeScript, responsible for API routing, an agent loop with SSE-streamed LLM responses, Docker orchestration, and SQLite metadata storage. -- evidence: [ARCHITECTURE.md#L43-L48](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L43-L48)
- design-choices (3 claim(s)):
  - [observation/documented] Frontend data flow follows View -> hook -> service -> API, with hooks writing results into Zustand stores that cache fetched data; mutations update stores and hooks may expose refetch() to bypass the cache. -- evidence: [ARCHITECTURE.md#L81-L81](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L81-L81), [ARCHITECTURE.md#L73-L73](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L73-L73), [ARCHITECTURE.md#L75-L79](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L75-L79)
  - [observation/documented] The product is BYOK: it does not force a specific AI provider, and documentation lists supported keys including OpenAI, Anthropic, OpenRouter, Google Gemini, Mistral, Groq, xAI, DeepSeek, and Ollama/LM Studio or custom OpenAI-compatible endpoints. -- evidence: [docs/byok.md#L6-L15](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/docs/byok.md#L6-L15), [docs/byok.md#L3-L3](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/docs/byok.md#L3-L3)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The browser client communicates with the Express API over REST, SSE, and WebSocket, and the backend manages interactive shells via WebSocket. -- evidence: [ARCHITECTURE.md#L43-L48](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L43-L48), [ARCHITECTURE.md#L7-L31](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L7-L31)
- memory-state (1 claim(s)):
  - [inference/documented] The spec describes a snapshot-based filesystem where every AI change should be reversible, using content-addressed blobs, tree objects, diffs, branching, and restore operations similar to Git internally; this is stated as a design target rather than confirmed implemented behavior. -- evidence: [PROJECT.md#L397-L404](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L397-L404), [PROJECT.md#L767-L767](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L767-L767), [PROJECT.md#L760-L765](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L760-L765), [PROJECT.md#L62-L62](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L62-L62), [PROJECT.md#L64-L64](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L64-L64)
More evidence: [full detail](singulary.detail.md)

Metadata and full claim list: [full detail](singulary.detail.md)
Human notes ([notes](singulary.notes.md), never overwritten by build)

[Back to map index](../../index.md)
