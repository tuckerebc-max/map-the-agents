# kleneway/next-ai-starter

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 690c51ade437 @ 9b033758491e3b65

## Summary (orientation draft, not independently verified)

The snapshot is a Next.js 14 full-stack template (tRPC, Prisma, NextAuth, Supabase, Inngest, multiple AI providers) documented via README, plus agent-helper files and Cursor slash commands intended to guide AI coding agents working on the repo. Evidence is documentation-only; no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The template is explicitly designed to be optimized for AI coding assistants such as Cursor. -- evidence: [README.md#L15-L15](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L15-L15)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: agent instructions require files to stay small (≤500 LOC), functional typed components, updated top-of-file docs, and running npm run build after all changes, fixing errors but ignoring warnings. -- evidence: [AGENTS.md#L5-L8](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/AGENTS.md#L5-L8)
  - [observation/documented] Repository development practice: the repo ships Cursor custom slash commands (/start, /continue, /review, /document, /refactor) defined in .cursor/commands to drive agent task workflows, with new commands addable in that folder. -- evidence: [README.md#L112-L112](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L112-L112), [README.md#L91-L95](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L91-L95)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The project structure places App Router pages and API routes in app/, UI components in src/components, tRPC routers in src/lib/api, and the database schema in prisma/. -- evidence: [README.md#L140-L147](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L140-L147)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (5 claim(s)):
  - [observation/documented] The template is built on Next.js 14 with the App Router, TypeScript, tRPC for end-to-end type-safe APIs, Prisma as ORM, and NextAuth.js with a Prisma adapter. -- evidence: [README.md#L27-L32](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L27-L32)
  - [observation/documented] Supabase serves as the Postgres database, but the README says the Supabase client is not used directly, so it can be swapped via DATABASE_URL and DIRECT_URL environment variables. -- evidence: [README.md#L57-L60](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L57-L60)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(6 additional claim(s) omitted for length; see [full detail](next-ai-starter.detail.md) for every claim.)

Metadata and full claim list: [full detail](next-ai-starter.detail.md)
Human notes ([notes](next-ai-starter.notes.md), never overwritten by build)

[Back to map index](../../index.md)
