---
access: public
aliases: []
claim_ids:
- clm_3f3a4f64d4f0a7ccaa9bff3cecd8dca0e2779dbff4458be896491bff67fbb6ed
- clm_9f5e9fd48d60b947a74460202e1c4245a76bdfd9b0d27e3cff402435fc972035
maturity: draft
page_id: pg_3f3bbbb9007a57538e6b2137862ba40a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_36330e19c34e51beb867973b2745b71c
title: kleneway/next-ai-starter/AGENTS.md @ 690c51ade437
updated_at: '2026-09-14T04:03:32Z'
---

# kleneway/next-ai-starter/AGENTS.md @ 690c51ade437

<!-- rcw:begin owner=source:src_36330e19c34e51beb867973b2745b71c block=evidence -->
- Repository development practice: agent instructions require files to stay small (≤500 LOC), functional typed components, updated top-of-file docs, and running npm run build after all changes, fixing errors but ignoring warnings. [@claim:clm_3f3a4f64d4f0a7ccaa9bff3cecd8dca0e2779dbff4458be896491bff67fbb6ed]
- Repository development practice: backend conventions forbid raw SQL and prisma db push, mandate migrations via npx prisma migrate dev, and route AI calls through generateChatCompletion in src/lib/aiClient.ts, defaulting to GPT-5. [@claim:clm_9f5e9fd48d60b947a74460202e1c4245a76bdfd9b0d27e3cff402435fc972035]
<!-- rcw:end owner=source:src_36330e19c34e51beb867973b2745b71c block=evidence -->

## Researcher notes

