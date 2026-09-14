# ovh/shai -- full detail

[Back to orientation](shai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ovh/shai/f076f6128a826a96a28e47d0d674284b1552905e/77abcd8c07c0bab2.json](../../../wiki/dossiers/ovh/shai/f076f6128a826a96a28e47d0d674284b1552905e/77abcd8c07c0bab2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The workspace is split into shai-cli (CLI entry point), shai-core (agent, state machine, protocol), and shai-llm (LLM provider wrappers), plus docs, examples, and tests directories. -- evidence: [SHAI.md#L15-L23](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/SHAI.md#L15-L23) (`clm_8f6bf1b85a7ef7e3485a6ef0f7ef0f797fed24481db1e4c527fbb1a9ef64492c`)

## design-choices (1 claim(s))

- [observation/documented] Project context is loaded from a `SHAI.md` file at the project root, which the agent automatically reads as additional context. -- evidence: [README.md#L132-L132](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L132-L132), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15) (`clm_8b2ab68d870210ff235cb484e2e8612cedacee102d068334f30914f20513d08c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions must follow coding style rules, be unit-tested and documented, be DCO signed-off, and be submitted via GitHub pull requests under Apache 2.0. -- evidence: [CONTRIBUTING.md#L35-L36](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L35-L36), [CONTRIBUTING.md#L30-L31](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L30-L31), [CONTRIBUTING.md#L6-L10](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L6-L10) (`clm_79f8c66b114821cf2b88d278ae8cb2c6afada08cbba690717ec9f972b020b362`)
- [observation/documented] Repository development practice: releases require bumping versions in four crate Cargo.toml files, running `cargo check`, then tagging and pushing to trigger the release workflow. -- evidence: [CONTRIBUTING.md#L16-L19](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L16-L19), [CONTRIBUTING.md#L23-L26](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L23-L26) (`clm_1a498401b475351423595817b011178975e27f1638efeed6f0342f1d1c7bb5a4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Running `shai` starts an interactive terminal coding agent for chatting, writing code, fixing bugs, and answering questions. -- evidence: [README.md#L59-L59](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L59-L59), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15) (`clm_9d07ff204b709f04d399425f08c613df4dbc61d9fbd96e4f937cd6046dbfafd0`)
- [observation/documented] Headless mode accepts a piped prompt and streams events to stderr; shai can be told to return the whole conversation as a trace, which enables chaining shai calls. -- evidence: [README.md#L63-L63](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L63-L63), [README.md#L79-L81](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L79-L81), [README.md#L77-L77](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L77-L77), [README.md#L71-L71](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L71-L71) (`clm_e3ea0d966f27771d903ceb230a09c4abbb1636b8a608efb5b49b8bb5d1e5d038`)
- [observation/documented] `shai serve --port 3000` runs an HTTP service with SSE streaming and OpenAI-compatible endpoints including POST /v1/chat/completions and POST /v1/responses. -- evidence: [README.md#L85-L85](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L85-L85), [README.md#L87-L89](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L87-L89), [README.md#L95-L100](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L95-L100) (`clm_f2000a24957a8e4d8cb8c74d6dd098f5f2247083be63ee756873cb098a51248e`)
- [observation/documented] Server options include `--port` (default 3000), `--ephemeral` to spawn a new agent per request, and an optional agent name for a persistent session. -- evidence: [README.md#L104-L106](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L104-L106) (`clm_322c932866838250b1c026716928ebc10b193200b2978be15ba95b165d75b1d8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Custom agents can be defined in separate config files placed under ~/.config/shai/agents/, listed with `shai agent list`, and run via `shai agent <name>`; MCP and OAuth are supported. -- evidence: [README.md#L136-L136](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L136-L136), [README.md#L142-L145](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L142-L145), [README.md#L140-L140](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L140-L140), [README.md#L147-L147](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L147-L147), [README.md#L149-L151](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L149-L151), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15) (`clm_8f6a78a445246f4cfa675c9028c09718d38a2e2278561389d52c4a30a2b98379`)

## tools-permissions (1 claim(s))

- [observation/documented] A shell-assistant mode hooks the terminal via `shai on`/`shai off`, sending the last command, output, and error code to the LLM provider to suggest fixes for failed commands. -- evidence: [README.md#L110-L110](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L110-L110), [README.md#L124-L126](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L124-L126), [README.md#L114-L116](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L114-L116) (`clm_9b8adc6e473988b91de43b21e2b92eed6d602ed5627a71b9cea7aca62f2997c0`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Shai works with multiple LLM providers including OVHcloud (default, anonymous with rate limits), OpenAI, and other compatible endpoints; `shai auth` configures sign-in or provider selection. -- evidence: [README.md#L41-L43](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L41-L43), [README.md#L39-L39](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L39-L39), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15) (`clm_2997ed0ba4e96f2f5ffb4631d9acf945bb0a46a9f0b2a815b8dea17b4da4a4c2`)
- [observation/documented] For OVHcloud, function-calling models (e.g. gpt-oss-120b, gpt-oss-20b, Mistral-Small-3.2-24B) are recommended, or any model with structured output forced via the `/set so` option. -- evidence: [README.md#L157-L158](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L157-L158) (`clm_33944129e45cb908a9a37110b1a74fc440a964a49bcbb4c792db28cecf059aca`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

