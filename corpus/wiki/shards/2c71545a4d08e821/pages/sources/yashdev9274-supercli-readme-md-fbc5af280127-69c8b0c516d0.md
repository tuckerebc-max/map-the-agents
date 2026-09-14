---
access: public
aliases: []
claim_ids:
- clm_17d6d0d4818fb8d9c73cd739870ff180f0e54864794a808f18374759f3402871
- clm_25de1d30b28060678dd6c83ec0dafde3e7d604f9e8b74e4b883cfd0119dbc805
- clm_29f51eb8fb37e8ea11f5733cc9601a4dbc977204db1df25d0f38b80c275beacd
- clm_3077ad75ac581cd19753bd0cad8a88d1b0fe579e5ee0a83e816ad04c64c5a92d
- clm_4371a1471f6c4e3b80c0d834c851154d3756306bddfbd5c339966d9129f7f5c0
- clm_7881d42cf45b1ce385322bc18c2352b7886f3c8158b551099e3f32cadeb8612e
- clm_996d2651b59617c21ef818e0a80f4d1b74bd04f4fc9234616b1cd2ddf68c0c46
- clm_a400a5943036161dfc6ebbd9c099ffd5d3efca133b10bd088f574fedc265ea5c
- clm_d4511f5006d5892bb41ff475694320856dbaf27dd1e691a83f8027810f6e17c3
- clm_fc5859b294be88381eb3bc07254ae70ddcb8a33de1495a375988b0a6317cebab
- clm_fee97c9d9b1c22ec77bb1f689bd0d2b6955c043593586f4a0c65401f6139876c
maturity: draft
page_id: pg_8b2acfb952ff5b37920869c8b0c516d0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b750329286ce5198bd093d141b52150d
title: yashdev9274/supercli/README.md @ fbc5af280127
updated_at: '2026-09-14T03:24:55Z'
---

# yashdev9274/supercli/README.md @ fbc5af280127

<!-- rcw:begin owner=source:src_b750329286ce5198bd093d141b52150d block=evidence -->
- Shared packages include @super/db (Prisma dashboard schema), @super/auth (Better-Auth), @super/claude-sdk, @super/embeddings-sdk, and @super/skills for reusable agent skills. [@claim:clm_17d6d0d4818fb8d9c73cd739870ff180f0e54864794a808f18374759f3402871]
- Fine-tuning datasets listed are CodeAlpaca (20K), OpenCodeReasoning (100K+), and CodeFeedback (156K). [@claim:clm_25de1d30b28060678dd6c83ec0dafde3e7d604f9e8b74e4b883cfd0119dbc805]
- The monorepo includes a Next.js dashboard (apps/web), MDX docs site, terminal web client, an AI coding agent CLI published to npm as `supercode`, a scaffolded API server, and an open-model fine-tuning project. [@claim:clm_29f51eb8fb37e8ea11f5733cc9601a4dbc977204db1df25d0f38b80c275beacd]
- The open-model project includes an evaluation directory of model evaluation scripts, and the best-performing fine-tuned model is intended for deployment to the Supercode CLI; training uses Qwen3-8B via Tinker and GLM-4-9B via Modal+Axolotl with LoRA/QLoRA. [@claim:clm_3077ad75ac581cd19753bd0cad8a88d1b0fe579e5ee0a83e816ad04c64c5a92d]
- The terminal CLI has its own separate database and Prisma schema under packages/db-terminal (the @super/db-terminal package), distinct from the dashboard database. [@claim:clm_4371a1471f6c4e3b80c0d834c851154d3756306bddfbd5c339966d9129f7f5c0]
- AI/ML dependencies include AI SDK v6, OpenRouter, Anthropic Claude as default model, Google Gemini for embeddings, and a Vercel Minimax provider; the CLI uses Commander, Clack, Chalk, and marked-terminal. [@claim:clm_7881d42cf45b1ce385322bc18c2352b7886f3c8158b551099e3f32cadeb8612e]
- Repository development practice: quality scripts include `bun run test`, `bun run lint` (ESLint), and `bun run typecheck`; database migrations are created from packages/db or packages/db-terminal via `bunx prisma migrate dev`. [@claim:clm_996d2651b59617c21ef818e0a80f4d1b74bd04f4fc9234616b1cd2ddf68c0c46]
- Repository development practice: local setup requires cloning, `bun install`, copying apps/web/.env.example, starting PostgreSQL via Docker Compose, running `bun run db:migrate`, then `bun run dev:web`; Prisma generation skips gracefully when DATABASE_URL is unset. [@claim:clm_a400a5943036161dfc6ebbd9c099ffd5d3efca133b10bd088f574fedc265ea5c]
- The supercode CLI server supports multiple model providers (OpenRouter, Anthropic, Google) and ships a tool system covering file read/write, command execution, and search. [@claim:clm_d4511f5006d5892bb41ff475694320856dbaf27dd1e691a83f8027810f6e17c3]
- The repository is managed as a Turborepo monorepo with Bun workspaces defined in package.json as apps/*, apps/supercode-cli/*, and packages/*. [@claim:clm_fc5859b294be88381eb3bc07254ae70ddcb8a33de1495a375988b0a6317cebab]
- The stack uses Next.js 16, React 19, TypeScript 5, Bun 1.2+ (pinned 1.2.21), Turborepo 2, PostgreSQL with Prisma 7, Pinecone, Better Auth with GitHub OAuth, and Inngest for background jobs. [@claim:clm_fee97c9d9b1c22ec77bb1f689bd0d2b6955c043593586f4a0c65401f6139876c]
<!-- rcw:end owner=source:src_b750329286ce5198bd093d141b52150d block=evidence -->

## Researcher notes

