# sammwyy/singulary -- full detail

[Back to orientation](singulary.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sammwyy/singulary/5b51298504a410ecfaf483318814a57d73e05b42/27be8bccf199f5ab.json](../../../wiki/dossiers/sammwyy/singulary/5b51298504a410ecfaf483318814a57d73e05b42/27be8bccf199f5ab.json)

## specifications (2 claim(s))

- [observation/documented] The project specification targets a self-hostable alternative to tools like v0, Lovable, Bolt, Replit Agent, or Cursor-style agents, emphasizing local-first development, BYOK access, Docker-based execution, multi-project workspaces, and auditable AI-driven changes. -- evidence: [PROJECT.md#L5-L5](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L5-L5) (`clm_5bdfb26ef1e354f8cbbe5e8baa9786fcfc96754272cc7bd00ca44506ff399ed3`)
- [observation/documented] The spec calls for both single-user mode (first user becomes instance admin owning everything) and multi-user organization mode with teams, roles, groups, permissions, shared keys, quotas, and scoped environments. -- evidence: [PROJECT.md#L99-L99](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L99-L99), [PROJECT.md#L116-L116](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L116-L116), [PROJECT.md#L15-L16](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L15-L16) (`clm_35065921992e004b63afc5b65fdd405026d2a867d0eca8cd5d0ee2338084c472`)

## components (3 claim(s))

- [observation/documented] Singulary is a monorepo with a React frontend and an Express backend; in production the frontend is built to static assets and served by the same Express process that exposes the API under /api. -- evidence: [ARCHITECTURE.md#L3-L3](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L3-L3), [ARCHITECTURE.md#L35-L39](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L35-L39) (`clm_e007aa779d0827cb75d9e77a4d5dffc2eb2ad237cee1d1197e549223957fe770`)
- [observation/documented] The backend (apps/server) is an Express application on Node.js using TypeScript, responsible for API routing, an agent loop with SSE-streamed LLM responses, Docker orchestration, and SQLite metadata storage. -- evidence: [ARCHITECTURE.md#L43-L48](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L43-L48) (`clm_5d9100d5c44897ec2ac9e389f8ba0a6907932f67d63eeae6232aad31ff52363a`)
- [observation/documented] The frontend (apps/web) is a React app powered by Vite and styled with Tailwind CSS, organized into components, hooks, services, Zustand stores, utils, and views directories. -- evidence: [ARCHITECTURE.md#L52-L52](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L52-L52), [ARCHITECTURE.md#L54-L69](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L54-L69) (`clm_fd3cdf004ae18f452e19063e3fef75fafd7efe0110999b0fcf7c5c29408993d6`)

## design-choices (3 claim(s))

- [observation/documented] Frontend data flow follows View -> hook -> service -> API, with hooks writing results into Zustand stores that cache fetched data; mutations update stores and hooks may expose refetch() to bypass the cache. -- evidence: [ARCHITECTURE.md#L81-L81](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L81-L81), [ARCHITECTURE.md#L73-L73](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L73-L73), [ARCHITECTURE.md#L75-L79](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L75-L79) (`clm_e6be9196497b053573dee7d3a6fdcd15fb7ec8ac364a14c07270e61f8c58fa76`)
- [observation/documented] The product is BYOK: it does not force a specific AI provider, and documentation lists supported keys including OpenAI, Anthropic, OpenRouter, Google Gemini, Mistral, Groq, xAI, DeepSeek, and Ollama/LM Studio or custom OpenAI-compatible endpoints. -- evidence: [docs/byok.md#L6-L15](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/docs/byok.md#L6-L15), [docs/byok.md#L3-L3](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/docs/byok.md#L3-L3) (`clm_1e2f175ef1c4747f7b1aa4e44fc2f010bb5954e1300de34d9e33e7c8373b4158`)
- [observation/documented] Provider and service credentials can be configured at personal-user, workspace, organization, and global admin-managed levels, and all keys are AES-GCM encrypted at rest. -- evidence: [docs/byok.md#L24-L24](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/docs/byok.md#L24-L24), [docs/byok.md#L18-L22](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/docs/byok.md#L18-L22) (`clm_b612a2d4c7c9abb771f957328717229e629414a48adcb5bc701ef21252950550`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The browser client communicates with the Express API over REST, SSE, and WebSocket, and the backend manages interactive shells via WebSocket. -- evidence: [ARCHITECTURE.md#L43-L48](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L43-L48), [ARCHITECTURE.md#L7-L31](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L7-L31) (`clm_c29a242e29d2aaa2b2e09f37629326a9db8e9ad257196324124698b97d2d5f17`)

## memory-state (1 claim(s))

- [inference/documented] The spec describes a snapshot-based filesystem where every AI change should be reversible, using content-addressed blobs, tree objects, diffs, branching, and restore operations similar to Git internally; this is stated as a design target rather than confirmed implemented behavior. -- evidence: [PROJECT.md#L397-L404](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L397-L404), [PROJECT.md#L767-L767](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L767-L767), [PROJECT.md#L760-L765](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L760-L765), [PROJECT.md#L62-L62](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L62-L62), [PROJECT.md#L64-L64](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L64-L64) (`clm_f239b708e01d83ee9c63082dc710844c3f8cf8c799b35469ad4ed159f7cd1b57`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [inference/documented] The specification envisions a permissioned tool system (filesystem, shell, docker, env, database, network tools) with risk levels and approval requirements, and states the agent should never have raw unrestricted access; this is a design goal, not verified runtime behavior. -- evidence: [PROJECT.md#L565-L565](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L565-L565), [PROJECT.md#L591-L599](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L591-L599), [PROJECT.md#L567-L587](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L567-L587), [PROJECT.md#L603-L608](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L603-L608), [PROJECT.md#L563-L563](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/PROJECT.md#L563-L563) (`clm_5c1bcd742bb9dad38d3646a731a70163d67878a6e7d4c1fd23eaa9adf832ed1e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] SQLite stores instance metadata by default at storage/singulary.sqlite, tracking user accounts, token limits, rules, and workspace topology. -- evidence: [ARCHITECTURE.md#L43-L48](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L43-L48), [ARCHITECTURE.md#L35-L39](https://github.com/sammwyy/singulary/blob/5b51298504a410ecfaf483318814a57d73e05b42/ARCHITECTURE.md#L35-L39) (`clm_f0aa1e354583391d27e16712a01167dbf73da0dd39532d9279fc33f1294d4288`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

