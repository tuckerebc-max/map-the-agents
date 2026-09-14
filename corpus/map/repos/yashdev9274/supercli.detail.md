# yashdev9274/supercli -- full detail

[Back to orientation](supercli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yashdev9274/supercli/fbc5af2801270d5f35de71daf345223881d6d578/cf220776536a8161.json](../../../wiki/dossiers/yashdev9274/supercli/fbc5af2801270d5f35de71daf345223881d6d578/cf220776536a8161.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The monorepo includes a Next.js dashboard (apps/web), MDX docs site, terminal web client, an AI coding agent CLI published to npm as `supercode`, a scaffolded API server, and an open-model fine-tuning project. -- evidence: [README.md#L82-L88](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L82-L88), [README.md#L69-L74](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L69-L74), [README.md#L67-L67](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L67-L67) (`clm_29f51eb8fb37e8ea11f5733cc9601a4dbc977204db1df25d0f38b80c275beacd`)
- [observation/documented] Shared packages include @super/db (Prisma dashboard schema), @super/auth (Better-Auth), @super/claude-sdk, @super/embeddings-sdk, and @super/skills for reusable agent skills. -- evidence: [README.md#L93-L104](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L93-L104) (`clm_17d6d0d4818fb8d9c73cd739870ff180f0e54864794a808f18374759f3402871`)

## design-choices (1 claim(s))

- [observation/documented] The repository is managed as a Turborepo monorepo with Bun workspaces defined in package.json as apps/*, apps/supercode-cli/*, and packages/*. -- evidence: [README.md#L78-L78](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L78-L78) (`clm_fc5859b294be88381eb3bc07254ae70ddcb8a33de1495a375988b0a6317cebab`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local setup requires cloning, `bun install`, copying apps/web/.env.example, starting PostgreSQL via Docker Compose, running `bun run db:migrate`, then `bun run dev:web`; Prisma generation skips gracefully when DATABASE_URL is unset. -- evidence: [README.md#L50-L57](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L50-L57), [README.md#L270-L277](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L270-L277), [README.md#L289-L293](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L289-L293), [README.md#L259-L263](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L259-L263), [README.md#L279-L282](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L279-L282), [README.md#L61-L61](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L61-L61), [README.md#L284-L287](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L284-L287) (`clm_a400a5943036161dfc6ebbd9c099ffd5d3efca133b10bd088f574fedc265ea5c`)
- [observation/documented] Repository development practice: quality scripts include `bun run test`, `bun run lint` (ESLint), and `bun run typecheck`; database migrations are created from packages/db or packages/db-terminal via `bunx prisma migrate dev`. -- evidence: [README.md#L423-L428](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L423-L428), [README.md#L440-L444](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L440-L444), [README.md#L448-L452](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L448-L452), [README.md#L432-L436](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L432-L436) (`clm_996d2651b59617c21ef818e0a80f4d1b74bd04f4fc9234616b1cd2ddf68c0c46`)

## skills-patterns (1 claim(s))

- [observation/documented] The CLI added an @-picker with fuzzy file search, scroll-windowed slash commands and model selector, and a code review analysis prompt, per the changelog. -- evidence: [CHANGELOG.md#L51-L67](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L51-L67), [CHANGELOG.md#L34-L37](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L34-L37), [CHANGELOG.md#L41-L43](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L41-L43) (`clm_f25a73ac69b2902099a814e73b422d937572f3341d3da8ffe3931669cf7af91a`)

## interfaces (4 claim(s))

- [observation/documented] The supercode CLI server supports multiple model providers (OpenRouter, Anthropic, Google) and ships a tool system covering file read/write, command execution, and search. -- evidence: [README.md#L116-L117](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L116-L117) (`clm_d4511f5006d5892bb41ff475694320856dbaf27dd1e691a83f8027810f6e17c3`)
- [observation/documented] cortex-sdk exposes createGateway() returning a Vercel AI SDK LanguageModel with listModels() discovery, supporting eight gateway providers including ConcentrateAI, OpenRouter, Gemini, MiniMax, NVIDIA NIM, and a server-proxied Supercode Cloud. -- evidence: [cortex-sdk.md#L213-L213](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L213-L213), [cortex-sdk.md#L22-L44](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L22-L44), [cortex-sdk.md#L11-L16](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L11-L16), [cortex-sdk.md#L50-L58](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L50-L58) (`clm_8141ac0b14231c34891f04b36e5d88977d6b87daaf4c3a01491b032603aa6c72`)
- [observation/documented] cortex-sdk provides tool modules: createAgentHandler() (MergeDev MCP tool packs), createWebSearch() (Exa, Firecrawl, Context.dev), createComposio() (local SDK or server-proxied modes), createMcpManager() (GitHub/Linear/Slack/custom), and voice STT/TTS, all returning AI SDK Tool records. -- evidence: [cortex-sdk.md#L325-L327](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L325-L327), [cortex-sdk.md#L246-L246](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L246-L246), [cortex-sdk.md#L366-L366](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L366-L366), [cortex-sdk.md#L22-L44](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L22-L44), [cortex-sdk.md#L50-L58](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L50-L58), [cortex-sdk.md#L285-L285](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L285-L285) (`clm_ced59a7192c83745f8472f380955637039c2e38d8ff74f098112075da7924777`)
- [observation/documented] A SupercodeAgent class combines gateway, agent-handler, composio, web search, MCP servers, and voice configuration in a single constructor object. -- evidence: [cortex-sdk.md#L373-L402](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L373-L402), [cortex-sdk.md#L22-L44](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L22-L44) (`clm_d047a4e819a9404006cb9dcd01b8ab54e6ed2c63f46b08f437e0b5c53b6e97a8`)

## memory-state (1 claim(s))

- [observation/documented] The terminal CLI has its own separate database and Prisma schema under packages/db-terminal (the @super/db-terminal package), distinct from the dashboard database. -- evidence: [README.md#L93-L104](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L93-L104), [README.md#L438-L438](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L438-L438) (`clm_4371a1471f6c4e3b80c0d834c851154d3756306bddfbd5c339966d9129f7f5c0`)

## orchestration (1 claim(s))

- [observation/documented] The CLI's Composio integration uses a fallback chain: server-side session proxy via a bearer-authenticated POST /api/composio endpoint, then local SDK, then user prompt; init and /mcp flows try the server session before prompting for an API key. -- evidence: [CHANGELOG.md#L12-L15](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L12-L15), [CHANGELOG.md#L19-L22](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L19-L22), [CHANGELOG.md#L26-L26](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L26-L26) (`clm_01915cabdfbdc69f6b779903d1df0bdbe581303facfc8e995c4968aa10bfe7ae`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The open-model project includes an evaluation directory of model evaluation scripts, and the best-performing fine-tuned model is intended for deployment to the Supercode CLI; training uses Qwen3-8B via Tinker and GLM-4-9B via Modal+Axolotl with LoRA/QLoRA. -- evidence: [README.md#L191-L191](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L191-L191), [README.md#L150-L159](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L150-L159), [README.md#L143-L146](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L143-L146) (`clm_3077ad75ac581cd19753bd0cad8a88d1b0fe579e5ee0a83e816ad04c64c5a92d`)

## dependencies (3 claim(s))

- [observation/documented] The stack uses Next.js 16, React 19, TypeScript 5, Bun 1.2+ (pinned 1.2.21), Turborepo 2, PostgreSQL with Prisma 7, Pinecone, Better Auth with GitHub OAuth, and Inngest for background jobs. -- evidence: [README.md#L212-L213](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L212-L213), [README.md#L207-L209](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L207-L209), [README.md#L246-L249](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L246-L249), [README.md#L216-L216](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L216-L216), [README.md#L204-L204](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L204-L204), [README.md#L198-L201](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L198-L201) (`clm_fee97c9d9b1c22ec77bb1f689bd0d2b6955c043593586f4a0c65401f6139876c`)
- [observation/documented] AI/ML dependencies include AI SDK v6, OpenRouter, Anthropic Claude as default model, Google Gemini for embeddings, and a Vercel Minimax provider; the CLI uses Commander, Clack, Chalk, and marked-terminal. -- evidence: [README.md#L238-L240](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L238-L240), [README.md#L231-L235](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L231-L235) (`clm_7881d42cf45b1ce385322bc18c2352b7886f3c8158b551099e3f32cadeb8612e`)
- [observation/documented] Fine-tuning datasets listed are CodeAlpaca (20K), OpenCodeReasoning (100K+), and CodeFeedback (156K). -- evidence: [README.md#L165-L169](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L165-L169) (`clm_25de1d30b28060678dd6c83ec0dafde3e7d604f9e8b74e4b883cfd0119dbc805`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

