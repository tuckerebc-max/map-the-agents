# wrtnlabs/autobe -- full detail

[Back to orientation](autobe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/wrtnlabs/autobe/f5de9927c8eee6805afa3aeafd204f4c45037e49/4ec75f7d61738f6c.json](../../../wiki/dossiers/wrtnlabs/autobe/f5de9927c8eee6805afa3aeafd204f4c45037e49/4ec75f7d61738f6c.json)

## specifications (1 claim(s))

- [observation/documented] AutoBE generates requirements analysis reports, database/ERD and Prisma schema design, API specifications, e2e test functions, and implementations, and users can stop at any phase rather than running the full pipeline. -- evidence: [README.md#L47-L51](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L47-L51), [README.md#L16-L16](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L16-L16), [README.md#L174-L174](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L174-L174) (`clm_f240908f74b15bf1f29f0cb73b98d7e5c891f0e1fe932f022a570d82b8ed03f7`)

## components (1 claim(s))

- [observation/documented] Compiler feedback loops include a Database compiler, an OpenAPI compiler, a Test compiler, and a hybrid compiler for the Realize phase, connected to their respective agents in the architecture diagram. -- evidence: [README.md#L99-L117](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L99-L117) (`clm_6865ceb921d7c3f2a713628a7b67bf114c5222954137a8ca4066b69054c0a674`)

## design-choices (2 claim(s))

- [observation/documented] Rather than emitting code directly, agents build language-neutral ASTs from predefined schemas; each node is validated against type rules before code generation, and each waterfall stage has AI-friendly compilers that guarantee type safety. -- evidence: [README.md#L121-L121](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L121-L121) (`clm_bb96774733d8644d310f26a9730db8dec6aaf70d48c385c714699e1af8a2df00`)
- [inference/documented] The system appears to rely heavily on function calling: the job description states the whole system, from AST generation to orchestration, operates through function calling, and the roadmap lists dynamic function calling schemas as completed work. -- evidence: [JOB-DESCRIPTION-KR.md#L101-L101](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/JOB-DESCRIPTION-KR.md#L101-L101), [README.md#L228-L234](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L228-L234) (`clm_0242d94aa3b2bc67e40930453c9ec352ceae9c55a03e13c3e955c40284b9f878`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] AutoBE documents a WebSocket protocol with RPC support for NestJS servers, NodeJS servers, and client applications, plus an agent library covering facade controller, configuration, event handling, and prompt histories. -- evidence: [README.md#L72-L85](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L72-L85) (`clm_71d01aaa46fabdb5bc80a671df79d17ef3fdf55f98ed760b2cdc884499fd5072`)
- [observation/documented] Every generated backend automatically includes a type-safe TypeScript client SDK with no manual setup, usable from React, Vue, Angular, or other TS/JS projects; the same SDK is used internally to generate e2e test suites. -- evidence: [README.md#L182-L185](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L182-L185), [README.md#L213-L213](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L213-L213), [README.md#L180-L180](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L180-L180) (`clm_311c099c3a2ce52f0c41a2f9c01ea5986773a9be817dc4d060c03f0b6ed4864f`)

## memory-state (2 claim(s))

- [observation/documented] PLAN.md states the current playground server is completely stateless (no database, memory only) and proposes re-implementing persistence on SQLite with vendor management including encrypted API keys and per-session vendor tracking. -- evidence: [PLAN.md#L5-L5](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L5-L5), [PLAN.md#L76-L80](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L76-L80), [PLAN.md#L88-L96](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L88-L96) (`clm_265bad583043e2cc644a546d9b0b47ce6d211fbcaad7924edd9c82d2f79afed9`)
- [observation/documented] The planned Prisma schema defines models for vendors, sessions, session connections, session histories, session events, and session aggregates (with phase and token usage fields), with a unique constraint on the aggregate's session id. -- evidence: [PLAN.md#L134-L140](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L134-L140), [PLAN.md#L164-L169](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L164-L169), [PLAN.md#L88-L96](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L88-L96), [PLAN.md#L149-L155](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L149-L155), [PLAN.md#L102-L110](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L102-L110) (`clm_10d2fe9f6615c4259f37f730f5d7c8734f7689fb2023b4a27f8e3d8a76eaaf98`)

## orchestration (1 claim(s))

- [observation/documented] A Facade Controller coordinates specialized functional agents (Analyze, Database, Interface, Test, Realize) in a waterfall flow, with 40+ agents working in coordinated teams across phases. -- evidence: [README.md#L99-L117](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L99-L117), [README.md#L119-L119](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L119-L119) (`clm_d8acaee374c8a5db4a23ac2b2f5a87ef600bc748d73ba571ed11eb2fd751d58f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] An automated benchmark pipeline scores generated backends across 13+ LLM models and 4 project types on compilation correctness, documentation, requirements/test/API coverage, logic completeness, and AI-agent analysis, with 0-100 scores and A-F grades published at autobe.dev/benchmark. -- evidence: [README.md#L137-L137](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L137-L137), [README.md#L135-L135](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L135-L135) (`clm_9744588fb217a69c955584a1f69d386b52a97bbf206bd0082a85dd9935286f33`)

## dependencies (1 claim(s))

- [observation/documented] AutoBE itself is built with TypeScript and AI function calling, and generates backends on a TypeScript + NestJS + Prisma stack; the repo uses pnpm (via corepack) for setup and benchmark commands. -- evidence: [README.md#L153-L153](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L153-L153), [JOB-DESCRIPTION-KR.md#L64-L64](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/JOB-DESCRIPTION-KR.md#L64-L64), [README.md#L34-L39](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L34-L39) (`clm_62c2d0699878340f883647ce86c0d419d97cbd72ae343e8f4d856c61555bad31`)

## limitations (1 claim(s))

- [observation/documented] Generated apps compile but runtime behavior may still need refinement (e.g. database connection issues or endpoint failures), designs may differ from user expectations, complex projects consume 30M-250M+ tokens, and AutoBE does not provide ongoing maintenance after generation. -- evidence: [README.md#L290-L290](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L290-L290), [README.md#L292-L292](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L292-L292), [README.md#L288-L288](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L288-L288), [README.md#L294-L294](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L294-L294) (`clm_100d2f393c153c445fe49fc97d243dfc21e05d4946789faf9557448d099b3d14`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

