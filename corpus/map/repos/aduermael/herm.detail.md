# aduermael/herm -- full detail

[Back to orientation](herm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aduermael/herm/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/de79735aea23feee.json](../../../wiki/dossiers/aduermael/herm/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/de79735aea23feee.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The CLI is a terminal TUI with an event loop selecting on stdin, agent events, and async results; agent events include Thinking, ToolCall, Approval, and Done, and sub-agent events continue to be drained after the main agent stops. -- evidence: [ARCHITECTURE.md#L381-L383](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L381-L383), [ARCHITECTURE.md#L98-L124](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L98-L124), [ARCHITECTURE.md#L276-L281](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L276-L281) (`clm_51aa9be651617cb21e2f3882bff59532613a07a06d17d3e04efc7f2631d31630`)
- [observation/documented] The repository also contains a SwiftUI iOS/macOS app that uses an in-process Unix-like sandbox and a Luau-scriptable runtime for on-device tasks; it is not usable as a coding agent in that context and is not yet on the App Store. -- evidence: [README.md#L55-L55](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L55-L55), [README.md#L53-L53](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L53-L53) (`clm_8f807df959a3eb7fd4db477965219320e493f8917fc87958dafd653ae9f6ac59`)

## design-choices (2 claim(s))

- [observation/documented] Herm is described as a model-agnostic, general-purpose AI agent built for safe, flexible execution, natively supporting multiple isolation methods including containers, in-process Unix-like sandboxes, and host sandboxes such as sandbox_exec on macOS or bubblewrap on Linux. -- evidence: [README.md#L7-L7](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L7-L7) (`clm_6c25410aa4145661b46467d1e9135cf0aec4e4d2d82efaca0f242da2c8c57173`)
- [observation/documented] Herm extends container environments by writing Dockerfiles dynamically, with environments scoped per project (the current working directory). -- evidence: [README.md#L21-L21](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L21-L21) (`clm_22e53c0df0dbc699689299f26bb9bfa8ee848755b0fbb7f7092597f9a362ffb7`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README points contributors to CONTRIBUTING.md for setup, tests, CI checks, coding standards, and pull request expectations, and CI badges cover test, prompt-length, and ci-checks GitHub Actions workflows. -- evidence: [README.md#L92-L92](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L92-L92), [README.md#L3-L5](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L3-L5) (`clm_3745db136312b68cb39333b6f9539ad8882c82a20a2d1ad0bf7b757e9a07c9ea`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports multiple providers (Anthropic, OpenAI, Gemini, Grok, OpenRouter, Ollama, Azure OpenAI, Vertex AI, Bedrock) and models can be mixed, e.g. a different model for the main agent, exploration, or vision. -- evidence: [README.md#L19-L19](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L19-L19) (`clm_46f2b966e1746f8d27133217200ad2398e2a57f4088e6650b3caf89747da31fc`)
- [observation/documented] Documented CLI flags include --version, --debug, --prompt for headless mode, --cpsl to run with a CPSL local sandbox library, and --naked to run without Docker or CPSL. -- evidence: [CLI_QUICK_START.md#L12-L14](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L12-L14), [CLI_QUICK_START.md#L45-L52](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L45-L52), [CLI_DOCS_INDEX.md#L382-L382](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_DOCS_INDEX.md#L382-L382), [CLI_DOCS_INDEX.md#L81-L98](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_DOCS_INDEX.md#L81-L98) (`clm_2fb5ad3688435dde152798d2ce208987413799752bd45cc5d99b5f00e0f7128d`)

## memory-state (1 claim(s))

- [observation/documented] Configuration merges a global config (~/.herm/config.json, holding API keys, model, exploration, tool config, UI preferences) with a project-level .herm/config.json that can override model and tools. -- evidence: [ARCHITECTURE.md#L311-L314](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L311-L314), [ARCHITECTURE.md#L229-L232](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L229-L232), [ARCHITECTURE.md#L219-L225](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L219-L225) (`clm_460bc4a7c85cc5208096c198c47fa9c8b388d8da580cc30c8842d7c8b7ea5b72`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] By default the CLI runs the agent inside Docker containers that can only access files from the current working directory, with no permission prompts. -- evidence: [README.md#L9-L9](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L9-L9), [README.md#L17-L17](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L17-L17) (`clm_a75511beb25b34f32b212d997afee17d4c6dc290d70d1abe5580445c5012d57e`)
- [observation/documented] In --naked host mode, commands run through a workspace-scoped sandbox requiring sandbox-exec (macOS) or bwrap (Linux); new command segments and outside-workspace paths prompt for approval, and approved permissions persist in .herm/permissions.json with user-editable command_regexes and path_regexes. -- evidence: [CLI_QUICK_START.md#L45-L52](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L45-L52) (`clm_f9b26289654df7b531464da0042f0bdc5515e4be9583255bc60dea59a9746a5f`)

## evaluation (1 claim(s))

- [observation/documented] Benchmarking Herm against coding agents such as Claude Code, Codex, and Grok Build is listed as the top roadmap item, i.e. planned rather than an existing evaluation harness. -- evidence: [README.md#L61-L63](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L61-L63), [README.md#L59-L59](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L59-L59) (`clm_fc16f955102927f6a6e2cac42dc5e1cb985819da37a53d146ef028066536bcef`)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Go 1.24+ and, for the default container backend, Docker; the repo uses git submodules (langdag for LLM client/orchestration and cpsl for the native sandbox backend) that must be initialized before building. -- evidence: [CLI_QUICK_START.md#L12-L14](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L12-L14), [CLI_QUICK_START.md#L5-L10](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L5-L10), [README.md#L67-L88](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L67-L88), [CLI_QUICK_START.md#L16-L16](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L16-L16) (`clm_980fd1e6782178c00af303b83b33d0c86f9200650be8081bf8168062765eecd0`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

