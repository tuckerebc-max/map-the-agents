# sfarpak/alifullstack -- full detail

[Back to orientation](alifullstack.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sfarpak/alifullstack/c34f5cfea36db008b7c3e29c0d451b60758a30f4/95607c8a121f3d47.json](../../../wiki/dossiers/sfarpak/alifullstack/c34f5cfea36db008b7c3e29c0d451b60758a30f4/95607c8a121f3d47.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] AliFullStack is an Electron desktop app with a sandboxed renderer process for the React UI and a privileged Node.js main process, communicating via IPC. -- evidence: [docs/architecture.md#L11-L11](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L11-L11), [docs/architecture.md#L7-L7](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L7-L7) (`clm_dbc9c924f27f4bea7ee61cfecf0978cba724dc9d2b9fe2f474a8200c0be24ef1`)

## design-choices (2 claim(s))

- [observation/documented] The project deliberately simulates tool calling with XML-like tags instead of native function calling, citing support for many simultaneous calls and evidence that JSON-embedded code degrades quality. -- evidence: [docs/architecture.md#L31-L32](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L31-L32), [docs/architecture.md#L27-L27](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L27-L27) (`clm_ca9f5f9f2c87b2eb058e09776795403a329eec0ba07805a5d6d3d36977116a0f`)
- [observation/documented] By default each LLM request includes the entire codebase as context; a Smart Context feature uses smaller models to filter important files, and agentic codebase search is avoided for cost reasons. -- evidence: [docs/architecture.md#L50-L50](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L50-L50), [docs/architecture.md#L48-L48](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L48-L48), [docs/architecture.md#L52-L52](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L52-L52) (`clm_49a0589fea1c5337f79148f7c5f3bac3fc0f43cbcfd76179ea3c05b4f73437c8`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are told to set up pre-commit hooks (recommended), run unit tests with npm test, run E2E tests after npm run pre:e2e, and submit PRs from feature branches. -- evidence: [README.md#L214-L214](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L214-L214), [README.md#L233-L233](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L233-L233), [README.md#L198-L198](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L198-L198), [README.md#L202-L204](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L202-L204), [README.md#L192-L192](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L192-L192), [README.md#L177-L177](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L177-L177) (`clm_5297982905ed3de5de6e4276ff9dea54727f562eb26e775371e98ed0e6074eb9`)
- [observation/documented] Repository development practice: a functional Selenium test plan (Java/TestNG, WireMock, H2) is outlined covering app creation, chat, integrations, data persistence, errors, and performance suites. -- evidence: [functional_selenium_test_plan.md#L106-L106](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L106-L106), [functional_selenium_test_plan.md#L96-L96](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L96-L96), [functional_selenium_test_plan.md#L124-L124](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L124-L124), [functional_selenium_test_plan.md#L133-L133](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L133-L133), [functional_selenium_test_plan.md#L5-L5](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L5-L5), [functional_selenium_test_plan.md#L87-L87](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L87-L87), [functional_selenium_test_plan.md#L11-L19](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L11-L19), [functional_selenium_test_plan.md#L115-L115](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L115-L115) (`clm_709458d070e718dcacc711daced80098b9d75218aa290c5b6cd94c34dd348aa4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The system prompt instructs the LLM to respond using XML-like tags such as <alifullstack-write>, which a specialized Markdown parser renders in the UI and a response processor executes. -- evidence: [docs/architecture.md#L17-L19](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L17-L19), [docs/architecture.md#L21-L21](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L21-L21) (`clm_abd49e09e6341098acb9293f5aa4af67e54811ca7eb79a95dc4e2e80e7614579`)
- [inference/documented] The product appears to integrate with external services including Supabase, GitHub, Vercel, and Neon, based on the integration test cases described in the test plan. -- evidence: [functional_selenium_test_plan.md#L331-L331](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L331-L331), [functional_selenium_test_plan.md#L106-L106](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L106-L106), [functional_selenium_test_plan.md#L108-L111](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L108-L111), [functional_selenium_test_plan.md#L314-L314](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L314-L314), [functional_selenium_test_plan.md#L297-L297](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L297-L297) (`clm_4fd33eb8dd77e4f614721f403745f83d1a9074b319b69f27651606b391ca72aa`)

## memory-state (1 claim(s))

- [observation/documented] Setup requires creating a userData directory for the database and applying Drizzle migrations via npm run db:generate and db:push; Drizzle Studio can inspect the database. -- evidence: [README.md#L147-L147](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L147-L147), [README.md#L162-L165](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L162-L165), [README.md#L185-L188](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L185-L188) (`clm_4ffb3e9ca4010e6a905e2af3b7379c50fa9545ce38b76f1836ee799dcf2d398d`)

## orchestration (1 claim(s))

- [observation/documented] The agentic loop is intentionally simple: typically a single LLM request per user prompt, with optional TypeScript auto-fix, avoiding complex multi-step agent workflows to control cost. -- evidence: [docs/architecture.md#L40-L40](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L40-L40), [docs/architecture.md#L42-L42](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L42-L42) (`clm_eea60684e3ef061c2f2b2f4e4dc2ee6cf431226acdc5b21ab9d5cc3e29a67920`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Node.js >=20 with npm or pnpm (pnpm recommended); the app runs in development mode via npm start as an Electron app. -- evidence: [README.md#L127-L128](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L127-L128), [README.md#L169-L171](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L169-L171), [README.md#L173-L173](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L173-L173) (`clm_9ea742a2514684521e227cc6151ccfc2b0759477f4959c7e83c2ba1c1aaf3b0e`)

## limitations (1 claim(s))

- [observation/documented] The architecture doc acknowledges AliFullStack is less agentic than tools like Cursor, which plan, search codebases, run linters/tests, and auto-fix code. -- evidence: [docs/architecture.md#L38-L38](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L38-L38), [docs/architecture.md#L40-L40](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L40-L40) (`clm_c20989b80e2b6f41b85e74cd7411d5620889402f272d8349028797a08938afbc`)

## relevance (1 claim(s))

- [observation/documented] The roadmap marks React, Next.js, Vue 3, Django, FastAPI, Flask, Node.js, and multiple LLM providers (OpenAI, Gemini, Claude, Bedrock, etc.) as supported, with Angular, Rails, Mistral and others planned. -- evidence: [README.md#L65-L71](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L65-L71), [README.md#L55-L61](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L55-L61), [README.md#L75-L86](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L75-L86) (`clm_b9b930f752094d0d97aedbd9ade491c93274c3ddfbc5879e0c45d40553825703`)

