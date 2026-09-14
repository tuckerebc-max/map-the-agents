# zachblume/autospec -- full detail

[Back to orientation](autospec.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zachblume/autospec/e379edd427fc5ee2056be3bb2008f1fc26620b7f/7239b7163f559e68.json](../../../wiki/dossiers/zachblume/autospec/e379edd427fc5ee2056be3bb2008f1fc26620b7f/7239b7163f559e68.json)

## specifications (1 claim(s))

- [observation/documented] Autospec is described as an AI agent that autonomously explores a web app, generates commonsense test specs, and executes them, producing reusable Playwright test files. -- evidence: [README.md#L5-L10](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L5-L10) (`clm_b85652e8945459d9dbc519e2c1251ac705450bcbded1f67c7b2422a71ce9a523`)

## components (1 claim(s))

- [observation/documented] The src/ tree includes cli.ts, index.ts, ai.ts (Vercel AI SDK provider setup), planner.ts, executor.ts, reporter.ts, browser.ts, and schemas.ts (Zod schemas). -- evidence: [README.md#L92-L102](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L92-L102) (`clm_a827647b82b191892e38dd675073fcdd5721979b6b77db0f7bbb6fdd1f3e3634`)

## design-choices (1 claim(s))

- [observation/documented] It uses vision and language models to judge the whole UI after each interaction, deciding correctness rather than checking regressions against rigid prior behavior. -- evidence: [README.md#L5-L10](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L5-L10) (`clm_423afbe7c3e8e5e16b5c63dfd6ae774cbc021b5bd6c4a0ed80035309168e2a1d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are invited to open an issue or pull request on the GitHub repository to get started. -- evidence: [README.md#L111-L113](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L111-L113) (`clm_205e168a6fa373dac480f7accdf107e80d89c58b002fdff8f236bc59af31f150`)

## skills-patterns (1 claim(s))

- [observation/documented] The executor uses semantic actions like click by role, fill by label, press keys, scroll, and navigate, re-reading the accessibility snapshot after each step. -- evidence: [README.md#L80-L88](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L80-L88) (`clm_95976a5ba630166f47980f48dc5729bc7ea87df999e5c26f73d1790d5524f4b4`)

## interfaces (3 claim(s))

- [observation/documented] The CLI is invoked as npx autospecai with a required --url flag and optional --model, --spec_limit, --apikey, --specFile, --help and --version flags. -- evidence: [README.md#L60-L76](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L60-L76), [README.md#L52-L55](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L52-L55), [README.md#L57-L58](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L57-L58) (`clm_566616b10adf49f998fbf9722229c1e25689fc8022ebb876d0d34a6b95770c4a`)
- [observation/documented] --spec_limit defaults to 10; --model supports claude-opus-4-6 (default), gpt-5.4, and gemini-2.5-flash; --specFile accepts a JSON file of predefined specs or stdin via '-'. -- evidence: [README.md#L60-L76](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L60-L76) (`clm_1b261a2d1db8a4c7668be240d00e7e358ce10f79394335d813f08abc9e3eb0eb`)
- [observation/documented] Passing specs are saved as Playwright .spec.js files in a trajectories/ folder with video recordings and screenshots, re-runnable via npx playwright test. -- evidence: [README.md#L28-L30](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L28-L30), [README.md#L32-L35](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L32-L35) (`clm_8b75534c775e0b8fd202133b834340c5be803ffdf3fe0d5c56235885840933db`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The workflow has three phases: plan (crawl up to 3 pages, capture accessibility snapshots, generate specs), execute (specs run in parallel in isolated browser contexts), and report. -- evidence: [README.md#L80-L88](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L80-L88) (`clm_51a6020f9f0bd713804dbbcc5f90d1eb6764bf03293e95db5132f4e8324061b1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] If --apikey is omitted, the tool falls back on ANTHROPIC_API_KEY, OPENAI_API_KEY, or GOOGLE_GENERATIVE_AI_API_KEY environment variables; keys can also be configured via a .env file. -- evidence: [README.md#L60-L76](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L60-L76), [README.md#L44-L48](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L44-L48), [README.md#L42-L42](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L42-L42) (`clm_3ed797636c8b423a01c2e66f82816baa927a25e84da905db15946b2984d357da`)
- [observation/documented] Requirements are Node.js >= 22 and an API key for one of the supported models; the first run may download dependencies such as browser binaries. -- evidence: [README.md#L106-L107](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L106-L107), [README.md#L25-L26](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L25-L26) (`clm_599f5945655dc2e0369f40139de3a6cbd872712ec1ab7398ce8ddd3d103276c1`)

## limitations (1 claim(s))

- [inference/documented] Planning appears limited to crawling up to 3 pages from the target URL, suggesting a bounded exploration scope per run. -- evidence: [README.md#L80-L88](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L80-L88) (`clm_15e9c9abe3b96da231e523a698409a265f13400c8d2ed21ca67c37d540dfc169`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

