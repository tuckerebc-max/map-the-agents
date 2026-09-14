# narenmanoharan/gpt-code-assistant -- full detail

[Back to orientation](gpt-code-assistant.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/narenmanoharan/gpt-code-assistant/2bd455a1699320dca85f215c05c11626d99f3539/b7f97ce5a86938fe.json](../../../wiki/dossiers/narenmanoharan/gpt-code-assistant/2bd455a1699320dca85f215c05c11626d99f3539/b7f97ce5a86938fe.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Creating a project indexes all files by generating embeddings for each file and storing them in a local database. -- evidence: [README.md#L46-L46](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L46-L46) (`clm_e6060cdccd54b12977c700a83f48032e1152b9a1074ed494e3507f84d5e57dcf`)

## design-choices (2 claim(s))

- [observation/documented] The tool is described as privacy-centric: code snippets are only sent when a question is asked and the LLM requests relevant code, though snippets are shared with OpenAI. -- evidence: [README.md#L27-L30](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L27-L30) (`clm_be5789e3606addf335ee91c9b73aaf65aea9939b23dddae369299f712a9f7ce7`)
- [observation/documented] The tool is designed to work directly on any local codebase and claims language-agnostic support for multiple programming languages. -- evidence: [README.md#L27-L30](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L27-L30) (`clm_5df5b5b5ef74aa6507e9d1454cb137621463f568fe1c2b0cba365791ebfefc09`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors fork the repo, create a descriptively named branch, install dependencies with poetry, install pre-commit hooks, and submit pull requests for maintainer review. -- evidence: [CONTRIBUTING.md#L47-L49](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L47-L49), [CONTRIBUTING.md#L37-L37](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L37-L37), [CONTRIBUTING.md#L13-L13](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L13-L13), [CONTRIBUTING.md#L17-L19](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L17-L19), [CONTRIBUTING.md#L79-L84](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L79-L84) (`clm_2175ddeeddfb53add892e6389d2bc4db2565d5b84c9702e0435c23c38b156189`)
- [observation/documented] Repository development practice: local development sets the LOCAL_DEV environment variable to true and runs the project via 'poetry run gpt-code-assistant'. -- evidence: [CONTRIBUTING.md#L51-L51](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L51-L51), [CONTRIBUTING.md#L59-L61](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L59-L61), [CONTRIBUTING.md#L53-L55](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L53-L55) (`clm_1110d6cbb6434ceee86e6da03ae30c8edb79e7995f341789c98445e709b84fcd`)
- [observation/documented] Repository development practice: pull requests should be kept in small chunks with context provided, and are merged after review and passing tests. -- evidence: [CONTRIBUTING.md#L88-L88](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L88-L88), [CONTRIBUTING.md#L79-L84](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L79-L84) (`clm_4ccfeceffcc4c62e93c11e16d4d83ff281ef4368b5d894e4353fda6d3fa495de`)

## skills-patterns (1 claim(s))

- [observation/documented] Documentation advises that mentioning a specific file name or keywords in a query improves search accuracy. -- evidence: [README.md#L64-L64](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L64-L64), [README.md#L76-L76](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L76-L76) (`clm_d73d855348374f9995046065c626215ceb29a5ebe9ec48af5c192c80170bd73e`)

## interfaces (2 claim(s))

- [observation/documented] The product is a terminal CLI named gpt-code-assistant with subcommands including create-project, query, list-projects, refresh-project, delete-project, and select-model. -- evidence: [README.md#L106-L108](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L106-L108), [README.md#L82-L84](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L82-L84), [README.md#L90-L92](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L90-L92), [README.md#L58-L60](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L58-L60), [README.md#L48-L49](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L48-L49), [README.md#L98-L100](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L98-L100) (`clm_d974dcbb7c4d1b2c1c703779076e7e9df599cf6ac3ee34675ca6fbbd68b01d13`)
- [observation/documented] The selected model is persisted in $HOME/.gpt-code-assistant/config.toml. -- evidence: [README.md#L110-L110](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L110-L110) (`clm_b0a665ddba84b0d87fd379142b2c9445a3515344894df309edf700d15d0b589f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool uses OpenAI's API; it prompts the user to configure OPENAI_API_KEY if not already set, and defaults to the gpt-3.5-turbo-16k model. -- evidence: [README.md#L110-L110](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L110-L110), [README.md#L114-L114](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L114-L114) (`clm_7d6ea39a5c50e14ed3924750d8deebb4fa199c2fb9501999c0678a699c5134b1`)
- [observation/documented] The package is installable via pip as gpt-code-assistant. -- evidence: [README.md#L38-L40](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L38-L40) (`clm_099082f07bdb315eecdcc3d50ba5b12d3152c565a801e35af738e4a9eeecd762`)

## limitations (1 claim(s))

- [observation/documented] Per the roadmap, support for additional models (Claude, Bedrock), local models (Llama2, Starcoder), code generation saved to files, and multi-codebase search are planned but not yet implemented. -- evidence: [README.md#L129-L135](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L129-L135) (`clm_96c4a780c56b7a32c8b44d7eb2e6282fb754ae1f7bf75823c3e4c8682c47b842`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

