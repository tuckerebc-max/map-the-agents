# humanstack/vibe-coding-template -- full detail

[Back to orientation](vibe-coding-template.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/humanstack/vibe-coding-template/7cec003ce14ef117e8c9a0501554bed512343ed5/e2ecbbaa1e07bb94.json](../../../wiki/dossiers/humanstack/vibe-coding-template/7cec003ce14ef117e8c9a0501554bed512343ed5/e2ecbbaa1e07bb94.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The template ships a Python FastAPI backend with Supabase integration for auth, database, realtime, storage, and migrations, plus LLM and vector-database services. -- evidence: [README.md#L35-L49](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L35-L49), [README.md#L3-L3](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L3-L3) (`clm_55039d88b7f6199ff53bd05094fc6da687beed15f61b036c7a0cfc91111a2a96`)
- [observation/documented] The frontend is a Next.js application using Tailwind CSS with a Supabase client and complete auth flows including login, signup, and password reset. -- evidence: [README.md#L52-L56](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L52-L56) (`clm_287aee8924c465f7f7b7f7bef87e62f69e59866dfebe153659e629292ecbfa43`)
- [observation/documented] The backend includes an abstracted LLM service supporting OpenAI and Claude, a vector embeddings service, and Qdrant integration with document storage and semantic search. -- evidence: [README.md#L35-L49](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L35-L49) (`clm_25ae4abfc6c9793739a041f533e38bbe5dbea58ddd02c9a078d24bfaf67e6bbe`)

## design-choices (1 claim(s))

- [observation/documented] The vector database layer falls back automatically to a local in-memory database when Qdrant is unavailable. -- evidence: [README.md#L35-L49](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L35-L49) (`clm_26899ffffbf601995b0801b92d4d3240569253ceb5d717a2c01bf2f188ace99e`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to use TypeScript for frontend files, Python type hints and async/await in the backend, and snake_case/camelCase naming conventions. -- evidence: [AGENTS.md#L16-L20](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/AGENTS.md#L16-L20) (`clm_74bb134fed878fee0dd04037ea8429f83cef4375f994ee23791b3c30129981c1`)
- [observation/documented] Repository development practice: contributors are told to follow the service layer pattern, use Pydantic models for validation, and use the generic SupabaseDatabaseService for database operations. -- evidence: [AGENTS.md#L23-L27](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/AGENTS.md#L23-L27) (`clm_039e5eba9047527a91a5127d99b36bc73b24ed56f04c2514735793253c6b9feb`)
- [observation/documented] Repository development practice: the repo includes Cursor rules under .cursor/rules/ that apply automatically based on edited files, with templates like @api-endpoint-template and @react-component-template. -- evidence: [README.md#L14-L17](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L14-L17), [README.md#L196-L198](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L196-L198) (`clm_f6e674f5040deb64a79525f1a7570968541277baa9ab46141462f23aebf9951c`)
- [observation/documented] Repository development practice: setup is via ./first-time.sh (tool checks, API key prompts, .env generation) or manually by copying .env.example files, then make dev. -- evidence: [README.md#L113-L116](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L113-L116), [README.md#L103-L106](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L103-L106), [README.md#L75-L82](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L75-L82), [README.md#L98-L101](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L98-L101) (`clm_e214456fd9a250d4bc11bc5352c910f5687496e0ecce1393e8b65f4a81418228`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Running the dev environment exposes the frontend at localhost:3000, the backend API at localhost:8000, and API docs at localhost:8000/docs. -- evidence: [README.md#L89-L92](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L89-L92) (`clm_8a2202f3089e9aa0c7d5bd0c536377bdb4631a1a215bd56952a5dd52d13a8cc1`)
- [observation/documented] A Makefile provides commands such as make dev, prod variants, clean, and database migration commands like db-migration-new, db-apply, db-list, db-status, and db-push. -- evidence: [README.md#L173-L175](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L173-L175), [README.md#L179-L179](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L179-L179), [README.md#L167-L169](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L167-L169), [README.md#L183-L187](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L183-L187) (`clm_ea0dbbe6943764224bbd0c0a94e65958c9e38ac07ac843724a62cbae00bf8f7b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites include Docker and Docker Compose, Make, Node.js 18+, Python 3.10+, and the Supabase CLI for migrations. -- evidence: [README.md#L61-L65](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L61-L65) (`clm_4947b76bfe1e4c6475b49cd09b21b62f6e86f1e6415a272e6eb1f47de2c79b14`)
- [observation/documented] Environment configuration requires Supabase URL and service key, OpenAI and/or Anthropic API keys for LLM features, and optionally Qdrant credentials. -- evidence: [AGENTS.md#L114-L117](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/AGENTS.md#L114-L117), [README.md#L108-L111](https://github.com/humanstack/vibe-coding-template/blob/7cec003ce14ef117e8c9a0501554bed512343ed5/README.md#L108-L111) (`clm_882e0ef5c44847fbbfcf2ee55d63250d4cfa5668906cdf26953d0e697807fcb1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

