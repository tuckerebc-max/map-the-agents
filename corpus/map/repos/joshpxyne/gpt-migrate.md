# joshpxyne/gpt-migrate

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: 0xpayne/gpt-migrate (github id 658136967).
Latest snapshot: commit 262cabb5e8da @ ee5798d35a63a1da

## Summary (orientation draft, not independently verified)

GPT-Migrate is an LLM-driven tool that migrates codebases between languages/frameworks using Docker environments, iterative debugging, and generated unit tests. Evidence is limited to README, CODE_OF_CONDUCT, and TERMS files; no source code slices are present.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Default model is gpt-4-32k with temperature 0; the default run executes a flask-to-nodejs benchmark migration. -- evidence: [README.md#L52-L52](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L52-L52), [README.md#L60-L60](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L60-L60), [README.md#L58-L58](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L58-L58)
  - [observation/documented] Prompts are composed from tagged subprompts in four preference levels (HIERARCHY, p1-p4) via a prompt_constructor() function that yields a formattable string. -- evidence: [README.md#L113-L117](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L113-L117), [README.md#L121-L121](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L121-L121), [README.md#L111-L111](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L111-L111), [README.md#L123-L125](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L123-L125)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are governed by a Contributor-Covenant-based Code of Conduct covering issues, PRs, and code reviews, with violations reportable to maintainers. -- evidence: [CODE_OF_CONDUCT.md#L9-L9](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L9-L9), [CODE_OF_CONDUCT.md#L5-L5](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L5-L5), [CODE_OF_CONDUCT.md#L29-L29](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L29-L29), [CODE_OF_CONDUCT.md#L35-L35](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L35-L35)
  - [observation/documented] Repository development practice: the roadmap invites PRs for improvements such as model input size limiting, project-wide unit tests with CI/CD, more benchmarks, and support for other LLMs. -- evidence: [README.md#L145-L148](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L145-L148), [README.md#L152-L153](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L152-L153), [README.md#L137-L137](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L137-L137), [README.md#L141-L141](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L141-L141)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The tool is invoked via a main.py CLI with options such as --model, --sourcedir, --sourcelang, --targetdir, --targetlang, --step, and --sourceport. -- evidence: [README.md#L82-L82](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L82-L82), [README.md#L68-L68](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L68-L68), [README.md#L70-L70](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L70-L70), [README.md#L64-L64](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L64-L64), [README.md#L58-L58](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L58-L58), [README.md#L62-L62](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L62-L62), [README.md#L56-L56](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L56-L56)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The migration pipeline runs steps: setup a Docker environment for the target language, map third-party dependencies, rebuild code recursively from the source entrypoint, then test and debug iteratively. -- evidence: [README.md#L100-L107](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L100-L107)
  - [observation/documented] During debugging the agent chooses actions like moving, creating, or editing files, and asks for user clearance before executing shell scripts. -- evidence: [README.md#L100-L107](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L100-L107)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The tool generates unit tests with Python's unittest framework, optionally validating them against the original app on --sourceport before testing the migrated app on --targetport. -- evidence: [README.md#L100-L107](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L100-L107), [README.md#L78-L78](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L78-L78), [README.md#L76-L76](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L76-L76), [README.md#L50-L50](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L50-L50)
  - [observation/documented] The project reports benchmark performance: simple benchmarks pass for easy languages like Python or JavaScript about 50% of the time, while complex languages like C++ or Rust need human assistance. -- evidence: [README.md#L129-L129](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L129-L129)
- dependencies (1 claim(s)):
More evidence: [full detail](gpt-migrate.detail.md)

Metadata and full claim list: [full detail](gpt-migrate.detail.md)
Human notes ([notes](gpt-migrate.notes.md), never overwritten by build)

[Back to map index](../../index.md)
