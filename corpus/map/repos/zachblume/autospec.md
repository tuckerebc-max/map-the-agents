# zachblume/autospec

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e379edd427fc @ 7239b7163f559e68

## Summary (orientation draft, not independently verified)

README-only evidence for autospec, an AI agent that explores web apps and generates/executes Playwright e2e tests via a CLI. Product behavior, CLI options, architecture, and requirements are documented; no code or dev-workflow evidence beyond contributing pointers.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Autospec is described as an AI agent that autonomously explores a web app, generates commonsense test specs, and executes them, producing reusable Playwright test files. -- evidence: [README.md#L5-L10](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L5-L10)
- components (1 claim(s)):
  - [observation/documented] The src/ tree includes cli.ts, index.ts, ai.ts (Vercel AI SDK provider setup), planner.ts, executor.ts, reporter.ts, browser.ts, and schemas.ts (Zod schemas). -- evidence: [README.md#L92-L102](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L92-L102)
- design-choices (1 claim(s)):
  - [observation/documented] It uses vision and language models to judge the whole UI after each interaction, deciding correctness rather than checking regressions against rigid prior behavior. -- evidence: [README.md#L5-L10](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L5-L10)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are invited to open an issue or pull request on the GitHub repository to get started. -- evidence: [README.md#L111-L113](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L111-L113)
- skills-patterns (1 claim(s)):
  - [observation/documented] The executor uses semantic actions like click by role, fill by label, press keys, scroll, and navigate, re-reading the accessibility snapshot after each step. -- evidence: [README.md#L80-L88](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L80-L88)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is invoked as npx autospecai with a required --url flag and optional --model, --spec_limit, --apikey, --specFile, --help and --version flags. -- evidence: [README.md#L60-L76](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L60-L76), [README.md#L52-L55](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L52-L55), [README.md#L57-L58](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L57-L58)
  - [observation/documented] --spec_limit defaults to 10; --model supports claude-opus-4-6 (default), gpt-5.4, and gemini-2.5-flash; --specFile accepts a JSON file of predefined specs or stdin via '-'. -- evidence: [README.md#L60-L76](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L60-L76)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The workflow has three phases: plan (crawl up to 3 pages, capture accessibility snapshots, generate specs), execute (specs run in parallel in isolated browser contexts), and report. -- evidence: [README.md#L80-L88](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L80-L88)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] If --apikey is omitted, the tool falls back on ANTHROPIC_API_KEY, OPENAI_API_KEY, or GOOGLE_GENERATIVE_AI_API_KEY environment variables; keys can also be configured via a .env file. -- evidence: [README.md#L60-L76](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L60-L76), [README.md#L44-L48](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L44-L48), [README.md#L42-L42](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L42-L42)
  - [observation/documented] Requirements are Node.js >= 22 and an API key for one of the supported models; the first run may download dependencies such as browser binaries. -- evidence: [README.md#L106-L107](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L106-L107), [README.md#L25-L26](https://github.com/zachblume/autospec/blob/e379edd427fc5ee2056be3bb2008f1fc26620b7f/README.md#L25-L26)
- limitations (1 claim(s)):
More evidence: [full detail](autospec.detail.md)

Metadata and full claim list: [full detail](autospec.detail.md)
Human notes ([notes](autospec.notes.md), never overwritten by build)

[Back to map index](../../index.md)
