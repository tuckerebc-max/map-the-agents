# joshpxyne/gpt-migrate -- full detail

[Back to orientation](gpt-migrate.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/joshpxyne/gpt-migrate/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/ee5798d35a63a1da.json](../../../wiki/dossiers/joshpxyne/gpt-migrate/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/ee5798d35a63a1da.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Default model is gpt-4-32k with temperature 0; the default run executes a flask-to-nodejs benchmark migration. -- evidence: [README.md#L52-L52](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L52-L52), [README.md#L60-L60](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L60-L60), [README.md#L58-L58](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L58-L58) (`clm_6b76fe8ee8efbc01ee45e59161801fb6db31d0e2f70fd090c41293136ad71e6f`)
- [observation/documented] Prompts are composed from tagged subprompts in four preference levels (HIERARCHY, p1-p4) via a prompt_constructor() function that yields a formattable string. -- evidence: [README.md#L113-L117](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L113-L117), [README.md#L121-L121](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L121-L121), [README.md#L111-L111](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L111-L111), [README.md#L123-L125](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L123-L125) (`clm_4c88d4ea5db2a52a6869de38e8fb33ee3d6929a5597f75137779d5c8fc31c95e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are governed by a Contributor-Covenant-based Code of Conduct covering issues, PRs, and code reviews, with violations reportable to maintainers. -- evidence: [CODE_OF_CONDUCT.md#L9-L9](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L9-L9), [CODE_OF_CONDUCT.md#L5-L5](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L5-L5), [CODE_OF_CONDUCT.md#L29-L29](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L29-L29), [CODE_OF_CONDUCT.md#L35-L35](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/CODE_OF_CONDUCT.md#L35-L35) (`clm_5364096ee916bfcf8782082548ae9a0d1aa1ac37cd8ba32f0167ac808772acb1`)
- [observation/documented] Repository development practice: the roadmap invites PRs for improvements such as model input size limiting, project-wide unit tests with CI/CD, more benchmarks, and support for other LLMs. -- evidence: [README.md#L145-L148](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L145-L148), [README.md#L152-L153](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L152-L153), [README.md#L137-L137](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L137-L137), [README.md#L141-L141](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L141-L141) (`clm_5d1170d8496eda62d56066010b0ae0d7c218596663688ab215ff2e0485e7a463`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The tool is invoked via a main.py CLI with options such as --model, --sourcedir, --sourcelang, --targetdir, --targetlang, --step, and --sourceport. -- evidence: [README.md#L82-L82](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L82-L82), [README.md#L68-L68](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L68-L68), [README.md#L70-L70](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L70-L70), [README.md#L64-L64](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L64-L64), [README.md#L58-L58](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L58-L58), [README.md#L62-L62](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L62-L62), [README.md#L56-L56](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L56-L56) (`clm_d24ed14641295eb070664321cded4fd8d939cdefad886571ffc6408f72f30129`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The migration pipeline runs steps: setup a Docker environment for the target language, map third-party dependencies, rebuild code recursively from the source entrypoint, then test and debug iteratively. -- evidence: [README.md#L100-L107](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L100-L107) (`clm_5b00c974eda846503cb539b5bdad18d76cc864e7038c512f8ef47772727d3e0c`)
- [observation/documented] During debugging the agent chooses actions like moving, creating, or editing files, and asks for user clearance before executing shell scripts. -- evidence: [README.md#L100-L107](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L100-L107) (`clm_decb6af9d933176906475763e6deb85be27eaa0f6396403408cc10f32cb5d984`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The tool generates unit tests with Python's unittest framework, optionally validating them against the original app on --sourceport before testing the migrated app on --targetport. -- evidence: [README.md#L100-L107](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L100-L107), [README.md#L78-L78](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L78-L78), [README.md#L76-L76](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L76-L76), [README.md#L50-L50](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L50-L50) (`clm_4b72322cf5da3162144752c19c451904b16cef6f2f030daadd634d3fdc5198b5`)
- [observation/documented] The project reports benchmark performance: simple benchmarks pass for easy languages like Python or JavaScript about 50% of the time, while complex languages like C++ or Rust need human assistance. -- evidence: [README.md#L129-L129](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L129-L129) (`clm_22ab54ddc70729b5958a0d402500a801ac8363db033cd328757e5852fc8ae4cf`)

## dependencies (1 claim(s))

- [observation/documented] Installation uses Poetry (poetry install) or pip with requirements.txt, and requires Docker to be installed and running; API keys for OpenRouter (default) and/or OpenAI are set via environment variables. -- evidence: [README.md#L42-L44](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L42-L44), [README.md#L26-L26](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L26-L26), [README.md#L30-L30](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L30-L30), [README.md#L40-L40](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L40-L40), [README.md#L34-L36](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L34-L36) (`clm_2b9e98de084412fc15ea66d03ddd4ad20697cf5f650520212c4429d963be34ac`)

## limitations (1 claim(s))

- [observation/documented] The project is described as a development alpha not ready for production, and users are warned not to trust output blindly since it may rewrite an entire codebase at significant token cost. -- evidence: [TERMS.md#L9-L9](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/TERMS.md#L9-L9), [TERMS.md#L5-L5](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/TERMS.md#L5-L5), [README.md#L129-L129](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L129-L129), [README.md#L20-L20](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L20-L20) (`clm_c0fd6ac9b00475fb1ae8241d3000c8a8f3d461bc65a6ef3421ba8b1e0426df7f`)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers facing costly framework or language migrations, and an expert-assisted migration service is offered at gpt-migrate.com. -- evidence: [README.md#L5-L5](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L5-L5), [README.md#L161-L161](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L161-L161), [README.md#L16-L16](https://github.com/joshpxyne/gpt-migrate/blob/262cabb5e8dae57f03e80a7c06cf0edfbc67d410/README.md#L16-L16) (`clm_0ba3936cace82b81a7f2a469aee2b1a2ffe6e44b3930e663d7dc524f6f05c41b`)

