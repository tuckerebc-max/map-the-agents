---
access: public
aliases: []
claim_ids:
- clm_0242d94aa3b2bc67e40930453c9ec352ceae9c55a03e13c3e955c40284b9f878
- clm_100d2f393c153c445fe49fc97d243dfc21e05d4946789faf9557448d099b3d14
- clm_311c099c3a2ce52f0c41a2f9c01ea5986773a9be817dc4d060c03f0b6ed4864f
- clm_62c2d0699878340f883647ce86c0d419d97cbd72ae343e8f4d856c61555bad31
- clm_6865ceb921d7c3f2a713628a7b67bf114c5222954137a8ca4066b69054c0a674
- clm_71d01aaa46fabdb5bc80a671df79d17ef3fdf55f98ed760b2cdc884499fd5072
- clm_9744588fb217a69c955584a1f69d386b52a97bbf206bd0082a85dd9935286f33
- clm_bb96774733d8644d310f26a9730db8dec6aaf70d48c385c714699e1af8a2df00
- clm_d8acaee374c8a5db4a23ac2b2f5a87ef600bc748d73ba571ed11eb2fd751d58f
- clm_f240908f74b15bf1f29f0cb73b98d7e5c891f0e1fe932f022a570d82b8ed03f7
maturity: draft
page_id: pg_3d0af01949055e8fb6e0bb8f40d0bd90
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_252be3d301c359b297e4e0191ca94192
title: wrtnlabs/autobe/README.md @ f5de9927c8ee
updated_at: '2026-09-14T03:23:57Z'
---

# wrtnlabs/autobe/README.md @ f5de9927c8ee

<!-- rcw:begin owner=source:src_252be3d301c359b297e4e0191ca94192 block=evidence -->
- The system appears to rely heavily on function calling: the job description states the whole system, from AST generation to orchestration, operates through function calling, and the roadmap lists dynamic function calling schemas as completed work. [@claim:clm_0242d94aa3b2bc67e40930453c9ec352ceae9c55a03e13c3e955c40284b9f878]
- Generated apps compile but runtime behavior may still need refinement (e.g. database connection issues or endpoint failures), designs may differ from user expectations, complex projects consume 30M-250M+ tokens, and AutoBE does not provide ongoing maintenance after generation. [@claim:clm_100d2f393c153c445fe49fc97d243dfc21e05d4946789faf9557448d099b3d14]
- Every generated backend automatically includes a type-safe TypeScript client SDK with no manual setup, usable from React, Vue, Angular, or other TS/JS projects; the same SDK is used internally to generate e2e test suites. [@claim:clm_311c099c3a2ce52f0c41a2f9c01ea5986773a9be817dc4d060c03f0b6ed4864f]
- AutoBE itself is built with TypeScript and AI function calling, and generates backends on a TypeScript + NestJS + Prisma stack; the repo uses pnpm (via corepack) for setup and benchmark commands. [@claim:clm_62c2d0699878340f883647ce86c0d419d97cbd72ae343e8f4d856c61555bad31]
- Compiler feedback loops include a Database compiler, an OpenAPI compiler, a Test compiler, and a hybrid compiler for the Realize phase, connected to their respective agents in the architecture diagram. [@claim:clm_6865ceb921d7c3f2a713628a7b67bf114c5222954137a8ca4066b69054c0a674]
- AutoBE documents a WebSocket protocol with RPC support for NestJS servers, NodeJS servers, and client applications, plus an agent library covering facade controller, configuration, event handling, and prompt histories. [@claim:clm_71d01aaa46fabdb5bc80a671df79d17ef3fdf55f98ed760b2cdc884499fd5072]
- An automated benchmark pipeline scores generated backends across 13+ LLM models and 4 project types on compilation correctness, documentation, requirements/test/API coverage, logic completeness, and AI-agent analysis, with 0-100 scores and A-F grades published at autobe.dev/benchmark. [@claim:clm_9744588fb217a69c955584a1f69d386b52a97bbf206bd0082a85dd9935286f33]
- Rather than emitting code directly, agents build language-neutral ASTs from predefined schemas; each node is validated against type rules before code generation, and each waterfall stage has AI-friendly compilers that guarantee type safety. [@claim:clm_bb96774733d8644d310f26a9730db8dec6aaf70d48c385c714699e1af8a2df00]
- A Facade Controller coordinates specialized functional agents (Analyze, Database, Interface, Test, Realize) in a waterfall flow, with 40+ agents working in coordinated teams across phases. [@claim:clm_d8acaee374c8a5db4a23ac2b2f5a87ef600bc748d73ba571ed11eb2fd751d58f]
- AutoBE generates requirements analysis reports, database/ERD and Prisma schema design, API specifications, e2e test functions, and implementations, and users can stop at any phase rather than running the full pipeline. [@claim:clm_f240908f74b15bf1f29f0cb73b98d7e5c891f0e1fe932f022a570d82b8ed03f7]
<!-- rcw:end owner=source:src_252be3d301c359b297e4e0191ca94192 block=evidence -->

## Researcher notes

