# sfarpak/alifullstack

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c34f5cfea36d @ 95607c8a121f3d47

## Summary (orientation draft, not independently verified)

Evidence consists of README, an AI rules file, an architecture doc, and a Selenium test plan for AliFullStack, an Electron-based local AI app builder. Claims cover its Electron architecture, XML-like tool simulation, context strategy, and contributor workflows. Evidence coverage: 181 of 333 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] AliFullStack is an Electron desktop app with a sandboxed renderer process for the React UI and a privileged Node.js main process, communicating via IPC. -- evidence: [docs/architecture.md#L11-L11](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L11-L11), [docs/architecture.md#L7-L7](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L7-L7)
- design-choices (2 claim(s)):
  - [observation/documented] The project deliberately simulates tool calling with XML-like tags instead of native function calling, citing support for many simultaneous calls and evidence that JSON-embedded code degrades quality. -- evidence: [docs/architecture.md#L31-L32](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L31-L32), [docs/architecture.md#L27-L27](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L27-L27)
  - [observation/documented] By default each LLM request includes the entire codebase as context; a Smart Context feature uses smaller models to filter important files, and agentic codebase search is avoided for cost reasons. -- evidence: [docs/architecture.md#L50-L50](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L50-L50), [docs/architecture.md#L48-L48](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L48-L48), [docs/architecture.md#L52-L52](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L52-L52)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to set up pre-commit hooks (recommended), run unit tests with npm test, run E2E tests after npm run pre:e2e, and submit PRs from feature branches. -- evidence: [README.md#L214-L214](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L214-L214), [README.md#L233-L233](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L233-L233), [README.md#L198-L198](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L198-L198), [README.md#L202-L204](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L202-L204), [README.md#L192-L192](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L192-L192), [README.md#L177-L177](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L177-L177)
  - [observation/documented] Repository development practice: a functional Selenium test plan (Java/TestNG, WireMock, H2) is outlined covering app creation, chat, integrations, data persistence, errors, and performance suites. -- evidence: [functional_selenium_test_plan.md#L106-L106](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L106-L106), [functional_selenium_test_plan.md#L96-L96](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L96-L96), [functional_selenium_test_plan.md#L124-L124](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L124-L124), [functional_selenium_test_plan.md#L133-L133](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L133-L133), [functional_selenium_test_plan.md#L5-L5](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L5-L5), [functional_selenium_test_plan.md#L87-L87](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L87-L87), [functional_selenium_test_plan.md#L11-L19](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L11-L19), [functional_selenium_test_plan.md#L115-L115](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L115-L115)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The system prompt instructs the LLM to respond using XML-like tags such as <alifullstack-write>, which a specialized Markdown parser renders in the UI and a response processor executes. -- evidence: [docs/architecture.md#L17-L19](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L17-L19), [docs/architecture.md#L21-L21](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/docs/architecture.md#L21-L21)
  - [inference/documented] The product appears to integrate with external services including Supabase, GitHub, Vercel, and Neon, based on the integration test cases described in the test plan. -- evidence: [functional_selenium_test_plan.md#L331-L331](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L331-L331), [functional_selenium_test_plan.md#L106-L106](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L106-L106), [functional_selenium_test_plan.md#L108-L111](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L108-L111), [functional_selenium_test_plan.md#L314-L314](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L314-L314), [functional_selenium_test_plan.md#L297-L297](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/functional_selenium_test_plan.md#L297-L297)
- memory-state (1 claim(s)):
  - [observation/documented] Setup requires creating a userData directory for the database and applying Drizzle migrations via npm run db:generate and db:push; Drizzle Studio can inspect the database. -- evidence: [README.md#L147-L147](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L147-L147), [README.md#L162-L165](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L162-L165), [README.md#L185-L188](https://github.com/SFARPak/AliFullStack/blob/c34f5cfea36db008b7c3e29c0d451b60758a30f4/README.md#L185-L188)
- orchestration (1 claim(s)):
More evidence: [full detail](alifullstack.detail.md)

Metadata and full claim list: [full detail](alifullstack.detail.md)
Human notes ([notes](alifullstack.notes.md), never overwritten by build)

[Back to map index](../../index.md)
