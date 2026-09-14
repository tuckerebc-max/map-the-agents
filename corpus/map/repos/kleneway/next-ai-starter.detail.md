# kleneway/next-ai-starter -- full detail

[Back to orientation](next-ai-starter.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kleneway/next-ai-starter/690c51ade437c0ccba79d852749a026ba31472c4/9b033758491e3b65.json](../../../wiki/dossiers/kleneway/next-ai-starter/690c51ade437c0ccba79d852749a026ba31472c4/9b033758491e3b65.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The template is explicitly designed to be optimized for AI coding assistants such as Cursor. -- evidence: [README.md#L15-L15](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L15-L15) (`clm_ef39686d6c4f8022a4a764d4a059094abb55243f879baf4e010680abb896cdd4`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: agent instructions require files to stay small (≤500 LOC), functional typed components, updated top-of-file docs, and running npm run build after all changes, fixing errors but ignoring warnings. -- evidence: [AGENTS.md#L5-L8](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/AGENTS.md#L5-L8) (`clm_3f3a4f64d4f0a7ccaa9bff3cecd8dca0e2779dbff4458be896491bff67fbb6ed`)
- [observation/documented] Repository development practice: the repo ships Cursor custom slash commands (/start, /continue, /review, /document, /refactor) defined in .cursor/commands to drive agent task workflows, with new commands addable in that folder. -- evidence: [README.md#L112-L112](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L112-L112), [README.md#L91-L95](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L91-L95) (`clm_1ca8ebb1c9d7e571ec8f2e35af89854226bc179284d54dc6fbea2aa26d376025`)
- [observation/documented] Repository development practice: agent-helpers/ provides agent instructions, a task checklist, a scratchpad, and logs, and the README suggests gitignoring the logs, sample-code, and scratchpad paths to avoid conflicts. -- evidence: [README.md#L70-L74](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L70-L74), [README.md#L80-L83](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L80-L83) (`clm_33199e111d6c4e88a183ba58d5071a4754007c92d61dcfb7482339392c4435b8`)
- [observation/documented] Repository development practice: backend conventions forbid raw SQL and prisma db push, mandate migrations via npx prisma migrate dev, and route AI calls through generateChatCompletion in src/lib/aiClient.ts, defaulting to GPT-5. -- evidence: [AGENTS.md#L20-L22](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/AGENTS.md#L20-L22), [AGENTS.md#L33-L34](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/AGENTS.md#L33-L34) (`clm_9f5e9fd48d60b947a74460202e1c4245a76bdfd9b0d27e3cff402435fc972035`)
- [observation/documented] Repository development practice: getting started involves forking, npm install, copying .env.example to .env, running npx prisma migrate dev, and npm run dev, with deployment optimized for Vercel. -- evidence: [README.md#L126-L128](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L126-L128), [README.md#L116-L117](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L116-L117), [README.md#L123-L124](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L123-L124), [README.md#L151-L151](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L151-L151), [README.md#L119-L121](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L119-L121), [README.md#L132-L134](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L132-L134) (`clm_b66088473de904a305f758103636ac1f76a9d9b0eb21283a64551deec099d06b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The project structure places App Router pages and API routes in app/, UI components in src/components, tRPC routers in src/lib/api, and the database schema in prisma/. -- evidence: [README.md#L140-L147](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L140-L147) (`clm_1ebbc939ba91534a0fd62ac5add9731acdef6b241ee4c0b7a3c227360e33e3be`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (5 claim(s))

- [observation/documented] The template is built on Next.js 14 with the App Router, TypeScript, tRPC for end-to-end type-safe APIs, Prisma as ORM, and NextAuth.js with a Prisma adapter. -- evidence: [README.md#L27-L32](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L27-L32) (`clm_f97af19ac147dbf56ad02bab2fafe752eb552bc6af47054faa4baa4680c248fd`)
- [observation/documented] Supabase serves as the Postgres database, but the README says the Supabase client is not used directly, so it can be swapped via DATABASE_URL and DIRECT_URL environment variables. -- evidence: [README.md#L57-L60](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L57-L60) (`clm_0ea5f3800ff6e23c9f990d32d8341daad2d764a386a2222e3434d84766854635`)
- [observation/documented] The stack includes Resend for transactional email, AWS S3 for file storage, and Inngest for background jobs and scheduled tasks. -- evidence: [README.md#L19-L19](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L19-L19), [README.md#L48-L53](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L48-L53) (`clm_9c1ee8d9c661d045999cd35cbbfc3197659a4f59192b215b3f6b633172a6a21d`)
- [observation/documented] Multiple AI provider integrations are listed: OpenAI (GPT-4 and o-series), Anthropic Sonnet-3.5, Perplexity web-search models, and Groq for fast inference. -- evidence: [README.md#L48-L53](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L48-L53) (`clm_f9ede29cd8e34e7e7a3503f70202c99527abe95a8d252991ec72f0737ede3f06`)
- [observation/documented] UI tooling includes Tailwind CSS, Framer Motion, Lucide Icons, dark mode, react-toastify notifications, Storybook, and the Geist font. -- evidence: [README.md#L36-L39](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L36-L39), [README.md#L43-L44](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L43-L44), [README.md#L64-L66](https://github.com/kleneway/next-ai-starter/blob/690c51ade437c0ccba79d852749a026ba31472c4/README.md#L64-L66) (`clm_05bfc9239ece7221faa52a6499b2fe51990744d78264460f0ca741d4694b6d4e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

