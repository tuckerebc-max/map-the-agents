# wrtnlabs/autobe

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f5de9927c8ee @ 4ec75f7d61738f6c

## Summary (orientation draft, not independently verified)

AutoBE is an open-source AI backend builder that generates TypeScript/NestJS/Prisma backends from natural-language chat via a waterfall of 40+ specialized agents with compiler feedback loops, includes a benchmark pipeline and type-safe client SDK, and documents limitations around runtime behavior, token consumption, and maintenance. PLAN.md describes a currently stateless playground server with a proposed SQLite-based persistence design. Evidence coverage: 137 of 218 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AutoBE generates requirements analysis reports, database/ERD and Prisma schema design, API specifications, e2e test functions, and implementations, and users can stop at any phase rather than running the full pipeline. -- evidence: [README.md#L47-L51](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L47-L51), [README.md#L16-L16](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L16-L16), [README.md#L174-L174](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L174-L174)
- components (1 claim(s)):
  - [observation/documented] Compiler feedback loops include a Database compiler, an OpenAPI compiler, a Test compiler, and a hybrid compiler for the Realize phase, connected to their respective agents in the architecture diagram. -- evidence: [README.md#L99-L117](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L99-L117)
- design-choices (2 claim(s)):
  - [observation/documented] Rather than emitting code directly, agents build language-neutral ASTs from predefined schemas; each node is validated against type rules before code generation, and each waterfall stage has AI-friendly compilers that guarantee type safety. -- evidence: [README.md#L121-L121](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L121-L121)
  - [inference/documented] The system appears to rely heavily on function calling: the job description states the whole system, from AST generation to orchestration, operates through function calling, and the roadmap lists dynamic function calling schemas as completed work. -- evidence: [JOB-DESCRIPTION-KR.md#L101-L101](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/JOB-DESCRIPTION-KR.md#L101-L101), [README.md#L228-L234](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L228-L234)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] AutoBE documents a WebSocket protocol with RPC support for NestJS servers, NodeJS servers, and client applications, plus an agent library covering facade controller, configuration, event handling, and prompt histories. -- evidence: [README.md#L72-L85](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L72-L85)
  - [observation/documented] Every generated backend automatically includes a type-safe TypeScript client SDK with no manual setup, usable from React, Vue, Angular, or other TS/JS projects; the same SDK is used internally to generate e2e test suites. -- evidence: [README.md#L182-L185](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L182-L185), [README.md#L213-L213](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L213-L213), [README.md#L180-L180](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/README.md#L180-L180)
- memory-state (2 claim(s)):
  - [observation/documented] PLAN.md states the current playground server is completely stateless (no database, memory only) and proposes re-implementing persistence on SQLite with vendor management including encrypted API keys and per-session vendor tracking. -- evidence: [PLAN.md#L5-L5](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L5-L5), [PLAN.md#L76-L80](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L76-L80), [PLAN.md#L88-L96](https://github.com/wrtnlabs/autobe/blob/f5de9927c8eee6805afa3aeafd204f4c45037e49/PLAN.md#L88-L96)
More evidence: [full detail](autobe.detail.md)

Metadata and full claim list: [full detail](autobe.detail.md)
Human notes ([notes](autobe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
