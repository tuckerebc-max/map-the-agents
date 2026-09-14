---
access: public
aliases: []
claim_ids:
- clm_15e9c9abe3b96da231e523a698409a265f13400c8d2ed21ca67c37d540dfc169
- clm_1b261a2d1db8a4c7668be240d00e7e358ce10f79394335d813f08abc9e3eb0eb
- clm_205e168a6fa373dac480f7accdf107e80d89c58b002fdff8f236bc59af31f150
- clm_3ed797636c8b423a01c2e66f82816baa927a25e84da905db15946b2984d357da
- clm_423afbe7c3e8e5e16b5c63dfd6ae774cbc021b5bd6c4a0ed80035309168e2a1d
- clm_51a6020f9f0bd713804dbbcc5f90d1eb6764bf03293e95db5132f4e8324061b1
- clm_566616b10adf49f998fbf9722229c1e25689fc8022ebb876d0d34a6b95770c4a
- clm_599f5945655dc2e0369f40139de3a6cbd872712ec1ab7398ce8ddd3d103276c1
- clm_8b75534c775e0b8fd202133b834340c5be803ffdf3fe0d5c56235885840933db
- clm_95976a5ba630166f47980f48dc5729bc7ea87df999e5c26f73d1790d5524f4b4
- clm_a827647b82b191892e38dd675073fcdd5721979b6b77db0f7bbb6fdd1f3e3634
- clm_b85652e8945459d9dbc519e2c1251ac705450bcbded1f67c7b2422a71ce9a523
maturity: draft
page_id: pg_8fa7ee3b8a0c5e8399ac20521ec4f357
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0ea1f3d67f1959c184d32da0ebffc190
title: zachblume/autospec/README.md @ e379edd427fc
updated_at: '2026-09-14T03:27:01Z'
---

# zachblume/autospec/README.md @ e379edd427fc

<!-- rcw:begin owner=source:src_0ea1f3d67f1959c184d32da0ebffc190 block=evidence -->
- Planning appears limited to crawling up to 3 pages from the target URL, suggesting a bounded exploration scope per run. [@claim:clm_15e9c9abe3b96da231e523a698409a265f13400c8d2ed21ca67c37d540dfc169]
- --spec_limit defaults to 10; --model supports claude-opus-4-6 (default), gpt-5.4, and gemini-2.5-flash; --specFile accepts a JSON file of predefined specs or stdin via '-'. [@claim:clm_1b261a2d1db8a4c7668be240d00e7e358ce10f79394335d813f08abc9e3eb0eb]
- Repository development practice: contributors are invited to open an issue or pull request on the GitHub repository to get started. [@claim:clm_205e168a6fa373dac480f7accdf107e80d89c58b002fdff8f236bc59af31f150]
- If --apikey is omitted, the tool falls back on ANTHROPIC_API_KEY, OPENAI_API_KEY, or GOOGLE_GENERATIVE_AI_API_KEY environment variables; keys can also be configured via a .env file. [@claim:clm_3ed797636c8b423a01c2e66f82816baa927a25e84da905db15946b2984d357da]
- It uses vision and language models to judge the whole UI after each interaction, deciding correctness rather than checking regressions against rigid prior behavior. [@claim:clm_423afbe7c3e8e5e16b5c63dfd6ae774cbc021b5bd6c4a0ed80035309168e2a1d]
- The workflow has three phases: plan (crawl up to 3 pages, capture accessibility snapshots, generate specs), execute (specs run in parallel in isolated browser contexts), and report. [@claim:clm_51a6020f9f0bd713804dbbcc5f90d1eb6764bf03293e95db5132f4e8324061b1]
- The CLI is invoked as npx autospecai with a required --url flag and optional --model, --spec_limit, --apikey, --specFile, --help and --version flags. [@claim:clm_566616b10adf49f998fbf9722229c1e25689fc8022ebb876d0d34a6b95770c4a]
- Requirements are Node.js >= 22 and an API key for one of the supported models; the first run may download dependencies such as browser binaries. [@claim:clm_599f5945655dc2e0369f40139de3a6cbd872712ec1ab7398ce8ddd3d103276c1]
- Passing specs are saved as Playwright .spec.js files in a trajectories/ folder with video recordings and screenshots, re-runnable via npx playwright test. [@claim:clm_8b75534c775e0b8fd202133b834340c5be803ffdf3fe0d5c56235885840933db]
- The executor uses semantic actions like click by role, fill by label, press keys, scroll, and navigate, re-reading the accessibility snapshot after each step. [@claim:clm_95976a5ba630166f47980f48dc5729bc7ea87df999e5c26f73d1790d5524f4b4]
- The src/ tree includes cli.ts, index.ts, ai.ts (Vercel AI SDK provider setup), planner.ts, executor.ts, reporter.ts, browser.ts, and schemas.ts (Zod schemas). [@claim:clm_a827647b82b191892e38dd675073fcdd5721979b6b77db0f7bbb6fdd1f3e3634]
- Autospec is described as an AI agent that autonomously explores a web app, generates commonsense test specs, and executes them, producing reusable Playwright test files. [@claim:clm_b85652e8945459d9dbc519e2c1251ac705450bcbded1f67c7b2422a71ce9a523]
<!-- rcw:end owner=source:src_0ea1f3d67f1959c184d32da0ebffc190 block=evidence -->

## Researcher notes

