# withastro/flue -- full detail

[Back to orientation](flue.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/withastro/flue/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/e9dc4791c6cf7883.json](../../../wiki/dossiers/withastro/flue/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/e9dc4791c6cf7883.json)

## specifications (1 claim(s))

- [observation/documented] Agents are exported TypeScript functions marked with a 'use agent' directive; hooks like useModel, useSandbox, useSkill, and useTool compose capabilities, and the function's returned string is its instruction. -- evidence: [README.md#L30-L32](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L30-L32), [README.md#L14-L22](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L14-L22), [README.md#L5-L12](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L5-L12), [README.md#L24-L28](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L24-L28) (`clm_8f4dd52f2e57e4405b71f542ad1c7ff7f0d2f534a5c10f105819d6700621cec8`)

## components (1 claim(s))

- [observation/documented] The repository ships @flue/runtime (harness, sessions, tools, sandbox), @flue/vite (build plugin), @flue/cli (flue binary), @flue/sdk (client for deployed agent conversations), @flue/opentelemetry, and @flue/postgres. -- evidence: [README.md#L67-L74](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L67-L74) (`clm_14f1267daeb9aba6d0d8d7c3057ab2b2c5453a70b8fa71beb8df5e33dbbfe526`)

## design-choices (1 claim(s))

- [observation/documented] The built-in TypeScript harness gives models sessions, tools, skills, instructions, filesystem access, and a secure sandbox; agents run locally via CLI or deploy to a hosted runtime. -- evidence: [README.md#L40-L40](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L40-L40) (`clm_cb4ba6a79e752df37187c870718302fc4d1e612ded6898a23aae7c647ca70db2`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: pull requests are not accepted and are automatically closed and converted into bug reports (GitHub issues) or feature requests (discussions), with agent-oriented templates also provided. -- evidence: [CONTRIBUTING.md#L11-L16](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L11-L16), [CONTRIBUTING.md#L20-L20](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L20-L20), [AGENTS.md#L9-L11](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/AGENTS.md#L9-L11) (`clm_dae1b42c4423fa67c9b2c31f2ee4b4b9406e7fd791d3139da85ba56f531c1274`)
- [observation/documented] Repository development practice: development uses pnpm in a turbo workspace, with commands for install, build, typechecking (excluding apps-www), and formatting. -- evidence: [AGENTS.md#L48-L53](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/AGENTS.md#L48-L53) (`clm_99c495ad58d3e96f6363cb7b9519e8978b5ca003306d58725b36de290406b4fc`)
- [observation/documented] Repository development practice: the project states no tests exist in the repo, and its contributing philosophy is an experiment applying the Surgical Team model, with agents handling design, research, implementation, and review under a lead maintainer. -- evidence: [CONTRIBUTING.md#L63-L63](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L63-L63), [CONTRIBUTING.md#L39-L39](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L39-L39), [AGENTS.md#L44-L44](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/AGENTS.md#L44-L44), [CONTRIBUTING.md#L28-L32](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L28-L32) (`clm_f048794a5dae11a68df7a0b598360962742a7813ae75fb08bcacc9d22ae7ab18`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes a `flue` binary for local runs, blueprints, and offline docs; @flue/sdk is a client SDK for consuming deployed agent conversations. -- evidence: [README.md#L67-L74](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L67-L74) (`clm_0d85643aa9a1e57c9eacfcdf428c0105778f73da45c25a8f5884689154bca12d`)
- [observation/documented] Documented deployment targets include Node.js, Cloudflare Workers, GitHub Actions, GitLab CI/CD, and Render; Daytona appears as a sandbox option rather than a deployment target. -- evidence: [README.md#L58-L63](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L58-L63) (`clm_16f2f5b82b5dd0c8ab65d06e539aa52ec5ea23410909087dbe525fb665cf459e`)

## memory-state (1 claim(s))

- [observation/documented] Agents keep context across conversations and events, and preserve progress through failures and restarts via durable recovery for accepted work. -- evidence: [README.md#L46-L54](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L46-L54) (`clm_4d8456a7bdea1e471b1eca58cea45863d16ee1800d51f7ab710dad780818adba`)

## orchestration (1 claim(s))

- [observation/documented] The framework supports subagents: specialized roles can be defined for different tasks, and the agent can delegate work to the appropriate expert. -- evidence: [README.md#L46-L54](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L46-L54) (`clm_22ba5b0dab1a2e4cfe42b86a03446c8b1391c2b0866153642af31951c89754b6`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Agents can connect to authenticated tools and services through MCP servers, and telemetry can be exported via OpenTelemetry and Braintrust. -- evidence: [README.md#L46-L54](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L46-L54) (`clm_2233b28f31493d43a446a1e3d3f441fd4bb6ce6be439a17d0f365e8bdf855917`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Flue positions itself as a framework for autonomous agents that receive a task rather than pre-defined steps, contrasting with agents built from raw LLM API calls. -- evidence: [README.md#L40-L40](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L40-L40), [README.md#L38-L38](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L38-L38), [README.md#L36-L36](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L36-L36) (`clm_74a2d79d27f90e8ae497a0c9b7b46bddf0a6411c3d1c794edb77d5c2f6605623`)

