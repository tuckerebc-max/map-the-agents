---
access: public
aliases: []
claim_ids:
- clm_05bfc9239ece7221faa52a6499b2fe51990744d78264460f0ca741d4694b6d4e
- clm_0ea5f3800ff6e23c9f990d32d8341daad2d764a386a2222e3434d84766854635
- clm_1ca8ebb1c9d7e571ec8f2e35af89854226bc179284d54dc6fbea2aa26d376025
- clm_1ebbc939ba91534a0fd62ac5add9731acdef6b241ee4c0b7a3c227360e33e3be
- clm_33199e111d6c4e88a183ba58d5071a4754007c92d61dcfb7482339392c4435b8
- clm_9c1ee8d9c661d045999cd35cbbfc3197659a4f59192b215b3f6b633172a6a21d
- clm_b66088473de904a305f758103636ac1f76a9d9b0eb21283a64551deec099d06b
- clm_ef39686d6c4f8022a4a764d4a059094abb55243f879baf4e010680abb896cdd4
- clm_f97af19ac147dbf56ad02bab2fafe752eb552bc6af47054faa4baa4680c248fd
- clm_f9ede29cd8e34e7e7a3503f70202c99527abe95a8d252991ec72f0737ede3f06
maturity: draft
page_id: pg_69d820f36c0c5c7582b56b6404f3e30f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_16a7176017e85754956c4f2782ab7f4f
title: kleneway/next-ai-starter/README.md @ 690c51ade437
updated_at: '2026-09-14T04:03:32Z'
---

# kleneway/next-ai-starter/README.md @ 690c51ade437

<!-- rcw:begin owner=source:src_16a7176017e85754956c4f2782ab7f4f block=evidence -->
- UI tooling includes Tailwind CSS, Framer Motion, Lucide Icons, dark mode, react-toastify notifications, Storybook, and the Geist font. [@claim:clm_05bfc9239ece7221faa52a6499b2fe51990744d78264460f0ca741d4694b6d4e]
- Supabase serves as the Postgres database, but the README says the Supabase client is not used directly, so it can be swapped via DATABASE_URL and DIRECT_URL environment variables. [@claim:clm_0ea5f3800ff6e23c9f990d32d8341daad2d764a386a2222e3434d84766854635]
- Repository development practice: the repo ships Cursor custom slash commands (/start, /continue, /review, /document, /refactor) defined in .cursor/commands to drive agent task workflows, with new commands addable in that folder. [@claim:clm_1ca8ebb1c9d7e571ec8f2e35af89854226bc179284d54dc6fbea2aa26d376025]
- The project structure places App Router pages and API routes in app/, UI components in src/components, tRPC routers in src/lib/api, and the database schema in prisma/. [@claim:clm_1ebbc939ba91534a0fd62ac5add9731acdef6b241ee4c0b7a3c227360e33e3be]
- Repository development practice: agent-helpers/ provides agent instructions, a task checklist, a scratchpad, and logs, and the README suggests gitignoring the logs, sample-code, and scratchpad paths to avoid conflicts. [@claim:clm_33199e111d6c4e88a183ba58d5071a4754007c92d61dcfb7482339392c4435b8]
- The stack includes Resend for transactional email, AWS S3 for file storage, and Inngest for background jobs and scheduled tasks. [@claim:clm_9c1ee8d9c661d045999cd35cbbfc3197659a4f59192b215b3f6b633172a6a21d]
- Repository development practice: getting started involves forking, npm install, copying .env.example to .env, running npx prisma migrate dev, and npm run dev, with deployment optimized for Vercel. [@claim:clm_b66088473de904a305f758103636ac1f76a9d9b0eb21283a64551deec099d06b]
- The template is explicitly designed to be optimized for AI coding assistants such as Cursor. [@claim:clm_ef39686d6c4f8022a4a764d4a059094abb55243f879baf4e010680abb896cdd4]
- The template is built on Next.js 14 with the App Router, TypeScript, tRPC for end-to-end type-safe APIs, Prisma as ORM, and NextAuth.js with a Prisma adapter. [@claim:clm_f97af19ac147dbf56ad02bab2fafe752eb552bc6af47054faa4baa4680c248fd]
- Multiple AI provider integrations are listed: OpenAI (GPT-4 and o-series), Anthropic Sonnet-3.5, Perplexity web-search models, and Groq for fast inference. [@claim:clm_f9ede29cd8e34e7e7a3503f70202c99527abe95a8d252991ec72f0737ede3f06]
<!-- rcw:end owner=source:src_16a7176017e85754956c4f2782ab7f4f block=evidence -->

## Researcher notes

