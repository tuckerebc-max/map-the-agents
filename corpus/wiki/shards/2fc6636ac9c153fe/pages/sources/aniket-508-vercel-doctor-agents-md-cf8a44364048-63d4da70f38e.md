---
access: public
aliases: []
claim_ids:
- clm_112e7983845734b8ffc5e374c75b1ae0ff50869ffd60a243c7c7ae63c4e76513
- clm_33009d60afaa1faf9a8b51e4e008b417c6b02962228f5cb6a61d70092d6f523a
- clm_6d4b8c66e049785f8b7f46dbc60a8305a4fcb42b9e35711917b467fd825d7429
- clm_76d81581bcae7add04c447f2c42e01f7a78769db6474a90cb49059e5a339949e
maturity: draft
page_id: pg_29eebc21fe4c51058ab763d4da70f38e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_219d0e4be4dd5f4688e342a382853772
title: Aniket-508/vercel-doctor/AGENTS.md @ cf8a44364048
updated_at: '2026-09-14T03:35:15Z'
---

# Aniket-508/vercel-doctor/AGENTS.md @ cf8a44364048

<!-- rcw:begin owner=source:src_219d0e4be4dd5f4688e342a382853772 block=evidence -->
- Repository development practice: contributors must follow TypeScript conventions including interfaces over types, arrow functions, kebab-case file names, descriptive variable names, and avoiding type casts. [@claim:clm_112e7983845734b8ffc5e374c75b1ae0ff50869ffd60a243c7c7ae63c4e76513]
- Repository development practice: agents are told to minimize token usage by batching edits, not re-reading files they just wrote, skipping confirmations, and not echoing large code blocks. [@claim:clm_33009d60afaa1faf9a8b51e4e008b417c6b02962228f5cb6a61d70092d6f523a]
- Repository development practice: checks should always be run before committing, using pnpm test (e2e tests), pnpm lint, pnpm typecheck, and pnpm format. [@claim:clm_6d4b8c66e049785f8b7f46dbc60a8305a4fcb42b9e35711917b467fd825d7429]
- Repository development practice: magic numbers belong in constants.ts using SCREAMING_SNAKE_CASE with unit suffixes, and small focused utilities go in utils/ with one utility per file. [@claim:clm_76d81581bcae7add04c447f2c42e01f7a78769db6474a90cb49059e5a339949e]
<!-- rcw:end owner=source:src_219d0e4be4dd5f4688e342a382853772 block=evidence -->

## Researcher notes

