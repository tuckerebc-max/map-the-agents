# divar-ir/ai-doc-gen -- full detail

[Back to orientation](ai-doc-gen.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/divar-ir/ai-doc-gen/bd3aba71a0c57aa43aef4020917989efc4507db3/8234197f8a7e2c0e.json](../../../wiki/dossiers/divar-ir/ai-doc-gen/bd3aba71a0c57aa43aef4020917989efc4507db3/8234197f8a7e2c0e.json)

## specifications (1 claim(s))

- [observation/documented] The tool analyzes repositories with five specialized analysis agents (code structure, dependencies, data flow, request flow, APIs) and generates a README plus AI assistant configuration files such as CLAUDE.md, AGENTS.md, and Cursor rules. -- evidence: [README.md#L3-L3](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L3-L3), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32) (`clm_a8eef703a36a5bbaffa6690914f0844482e9e81e09f9bbf6ca329e377edae4cf`)

## components (1 claim(s))

- [observation/documented] The architecture is layered: an argparse CLI entry point, command-specific handlers implementing an AbstractHandler interface, pydantic-ai agents with YAML/Jinja2 prompts, and a tool layer with file-reading and file-listing tools registered with every agent. -- evidence: [README.md#L184-L190](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L184-L190) (`clm_dd7ef5b37d6ae51caed3095a6949899a0517d7d127502e5eebef58a2276624c7`)

## design-choices (1 claim(s))

- [observation/documented] Configuration is layered with precedence from Pydantic defaults, then a .ai/config.yaml (or .yml) file in the target repository, then CLI flags. -- evidence: [README.md#L168-L168](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L168-L168) (`clm_c60e4526a9c72ce521f467097df97c2cc51edb3606afb95c91f01975c7dd0428`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must run ruff format and ruff check on src/ before submitting, follow a branch and commit-message convention (e.g. [Feature], [Fix]), and squash-merge feature branches into main. -- evidence: [AGENTS.md#L62-L64](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/AGENTS.md#L62-L64), [AGENTS.md#L24-L26](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/AGENTS.md#L24-L26) (`clm_6f5d01c3b023025ac8ec1151fa7058e9a2b39c1450735951d1ff2f96e62b3eb8`)
- [observation/documented] Repository development practice: the project has no automated tests; changes are verified manually by running the analyze, generate readme, and generate ai-rules commands against a test repository. -- evidence: [AGENTS.md#L52-L58](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/AGENTS.md#L52-L58) (`clm_f2cdd1cc6b487526c531553c5aae3ff466fa7c6a7a048d6bc6a69011fe0f48ff`)

## skills-patterns (1 claim(s))

- [observation/documented] The repository ships as an installable Claude Code plugin providing three skills: analyze-codebase, generate-readme, and generate-ai-rules, installable via the plugin marketplace commands. -- evidence: [README.md#L47-L49](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L47-L49), [README.md#L40-L43](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L40-L43), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32) (`clm_af120992b96e69e10cb8562b03d9ccfb2d8c48f61dccea6c6def3e9ded1ab4d4`)

## interfaces (1 claim(s))

- [observation/documented] The CLI exposes analyze, generate readme, and generate ai-rules commands taking a --repo-path argument, plus a cronjob analyze command; an ai-doc-gen console script exposes the same CLI. -- evidence: [README.md#L114-L114](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L114-L114), [README.md#L117-L118](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L117-L118), [README.md#L111-L111](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L111-L111), [README.md#L120-L120](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L120-L120), [README.md#L108-L108](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L108-L108) (`clm_d70e50f0438c6198cce0898e29e13a356539b7faf98ff4a2c8410095e8f4eb9e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Analyzer agents run in parallel through a configurable worker pool controlled by ANALYZER_MAX_WORKERS, where 0 means auto-detecting the CPU count; a --max-workers flag can cap concurrency. -- evidence: [README.md#L130-L130](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L130-L130), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32) (`clm_8a61315b01ddc5298e4b601e8ab6042b77b3a7780f7011adb8aaab3775921913`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents access the codebase through registered tools: FileReadTool for ranged file reading and ListFilesTool for filtered recursive listing, both registered with every agent. -- evidence: [README.md#L184-L190](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L184-L190) (`clm_bc9bc372df5b644b1a5e2000ecdf50c40aa50ff2d10d21aec70e87fc3c37f4d8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The stack is Python 3.13 with pydantic-ai for agent orchestration, OpenAI-compatible APIs for LLM access, GitPython and python-gitlab for Git/GitLab operations, and logfire/OpenTelemetry plus optional Langfuse for observability. -- evidence: [README.md#L194-L198](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L194-L198) (`clm_0d67e716fde8c277f703c18068b426a5beea4b7e80e95030f1e679a8f42e7fa3`)
- [observation/documented] Installation is documented via uv (recommended) or pip, and a Dockerfile plus a Helm chart under k8s/helm support containerized and Kubernetes CronJob deployments. -- evidence: [README.md#L63-L67](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L63-L67), [README.md#L69-L72](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L69-L72), [README.md#L74-L74](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L74-L74) (`clm_3fa7fe2bc667035fce1f33e22972e1cde467fae7e1c04f3d11ee34b8e1772cec`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [inference/documented] The tool appears most relevant to teams using GitLab and AI coding assistants (Claude Code, Cursor) who want automated, recurring documentation updates via merge requests. -- evidence: [README.md#L3-L3](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L3-L3), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32) (`clm_a16d06e3346b1fec9bd79f9a09dad95bf041044219cd5358567091d54cf10adf`)

