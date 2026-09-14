# yashdev9274/supercli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fbc5af280127 @ cf220776536a8161

## Summary (orientation draft, not independently verified)

Supercode is a Bun/Turborepo monorepo containing a Next.js dashboard, MDX docs site, terminal web client, an npm-published AI coding agent CLI (`supercode`), and a parallel open-model fine-tuning effort; a cortex-sdk package wraps AI gateways, web search, MCP tool platforms, and voice providers. Evidence coverage: 148 of 337 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The monorepo includes a Next.js dashboard (apps/web), MDX docs site, terminal web client, an AI coding agent CLI published to npm as `supercode`, a scaffolded API server, and an open-model fine-tuning project. -- evidence: [README.md#L82-L88](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L82-L88), [README.md#L69-L74](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L69-L74), [README.md#L67-L67](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L67-L67)
  - [observation/documented] Shared packages include @super/db (Prisma dashboard schema), @super/auth (Better-Auth), @super/claude-sdk, @super/embeddings-sdk, and @super/skills for reusable agent skills. -- evidence: [README.md#L93-L104](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L93-L104)
- design-choices (1 claim(s)):
  - [observation/documented] The repository is managed as a Turborepo monorepo with Bun workspaces defined in package.json as apps/*, apps/supercode-cli/*, and packages/*. -- evidence: [README.md#L78-L78](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L78-L78)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local setup requires cloning, `bun install`, copying apps/web/.env.example, starting PostgreSQL via Docker Compose, running `bun run db:migrate`, then `bun run dev:web`; Prisma generation skips gracefully when DATABASE_URL is unset. -- evidence: [README.md#L50-L57](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L50-L57), [README.md#L270-L277](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L270-L277), [README.md#L289-L293](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L289-L293), [README.md#L259-L263](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L259-L263), [README.md#L279-L282](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L279-L282), [README.md#L61-L61](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L61-L61), [README.md#L284-L287](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L284-L287)
  - [observation/documented] Repository development practice: quality scripts include `bun run test`, `bun run lint` (ESLint), and `bun run typecheck`; database migrations are created from packages/db or packages/db-terminal via `bunx prisma migrate dev`. -- evidence: [README.md#L423-L428](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L423-L428), [README.md#L440-L444](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L440-L444), [README.md#L448-L452](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L448-L452), [README.md#L432-L436](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L432-L436)
- skills-patterns (1 claim(s)):
  - [observation/documented] The CLI added an @-picker with fuzzy file search, scroll-windowed slash commands and model selector, and a code review analysis prompt, per the changelog. -- evidence: [CHANGELOG.md#L51-L67](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L51-L67), [CHANGELOG.md#L34-L37](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L34-L37), [CHANGELOG.md#L41-L43](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/CHANGELOG.md#L41-L43)
- interfaces (4 claim(s)):
  - [observation/documented] The supercode CLI server supports multiple model providers (OpenRouter, Anthropic, Google) and ships a tool system covering file read/write, command execution, and search. -- evidence: [README.md#L116-L117](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L116-L117)
  - [observation/documented] cortex-sdk exposes createGateway() returning a Vercel AI SDK LanguageModel with listModels() discovery, supporting eight gateway providers including ConcentrateAI, OpenRouter, Gemini, MiniMax, NVIDIA NIM, and a server-proxied Supercode Cloud. -- evidence: [cortex-sdk.md#L213-L213](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L213-L213), [cortex-sdk.md#L22-L44](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L22-L44), [cortex-sdk.md#L11-L16](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L11-L16), [cortex-sdk.md#L50-L58](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/cortex-sdk.md#L50-L58)
- memory-state (1 claim(s)):
  - [observation/documented] The terminal CLI has its own separate database and Prisma schema under packages/db-terminal (the @super/db-terminal package), distinct from the dashboard database. -- evidence: [README.md#L93-L104](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L93-L104), [README.md#L438-L438](https://github.com/yashdev9274/supercli/blob/fbc5af2801270d5f35de71daf345223881d6d578/README.md#L438-L438)
- orchestration (1 claim(s)):
More evidence: [full detail](supercli.detail.md)

Metadata and full claim list: [full detail](supercli.detail.md)
Human notes ([notes](supercli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
