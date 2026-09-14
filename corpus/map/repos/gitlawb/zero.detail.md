# gitlawb/zero -- full detail

[Back to orientation](zero.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gitlawb/zero/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/20ad3944dceb5124.json](../../../wiki/dossiers/gitlawb/zero/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/20ad3944dceb5124.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The web_fetch tool refuses loopback, private, and special-use addresses by checking the URL, resolving the host, and dialing the validated address to prevent DNS rebinding. -- evidence: [README.md#L280-L282](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L280-L282) (`clm_be3324d5b9714a8e8ac2988c8b8dc6401a06e22005e5c6e9fd3d738342265382`)
- [observation/documented] Zero injects project guidance into the system prompt from the first AGENTS.md, ZERO.md, or .zero/AGENTS.md found per directory from the git root to the cwd, capped at 8 KiB per file and 32 KiB total. -- evidence: [README.md#L338-L342](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L338-L342) (`clm_ed4a89d9f2ffe489479c2ea7ba4637812d6eaca841b5a274cc9232478023fd5e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should run `make fmt`, `make vet`, `make lint-static`, and `make vulncheck` before committing, using repository-managed targets with pinned tool versions rather than globally installed binaries. -- evidence: [README.md#L403-L406](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L403-L406), [README.md#L408-L410](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L408-L410), [README.md#L401-L401](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L401-L401) (`clm_df0ee0062fb01b6d5e391e268332a07f7a0b77642d06f84a219094f0aaa580b4`)
- [observation/documented] Repository development practice: contributors run `go test ./...`, and the internal/agenteval tests validate every suite JSON file, rejecting missing task IDs, empty verification commands, and malformed changed-file expectations. -- evidence: [README.md#L382-L387](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L382-L387), [docs/AGENT_EVALS.md#L237-L239](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L237-L239) (`clm_f937581a41e9eb47c8de8c28b35dfff381421fc8c6943ce9e2ba755a1aa382a9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Zero offers an interactive TUI plus a scriptable headless mode (`zero exec`) supporting text, JSON, and stream-JSON I/O with meaningful exit codes for CI. -- evidence: [README.md#L20-L24](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L20-L24), [README.md#L28-L42](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L28-L42) (`clm_b61168c694f9e71d8e64101868100f7b30014338aa75fcfd2c45932fce325417`)
- [observation/documented] The CLI exposes subcommands including setup, providers, models, doctor, sessions, spec, skills, plugins, hooks, mcp, sandbox, worktrees, verify, usage, cron, and `serve --mcp` to expose Zero tools over MCP stdio. -- evidence: [README.md#L304-L332](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L304-L332) (`clm_af54df982615470ed9e6d69901214f47499068ba70ba88f8143e723ff2d9820b`)
- [observation/documented] The TUI supports slash commands such as /model, /spec, /image, /resume, /rewind, /btw, /loop, /compact, /permissions, /add-dir, and /theme, plus Shift+Tab to cycle permission modes. -- evidence: [README.md#L214-L226](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L214-L226), [README.md#L202-L210](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L202-L210) (`clm_02c62d4f688ecacca51411d6d6db52a725cccb6ca7e481e6ec3685635002e0d6`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are stored on disk locally, searchable, resumable, and forkable, and the README states they are never uploaded as telemetry by Zero. -- evidence: [README.md#L28-L42](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L28-L42), [README.md#L304-L332](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L304-L332) (`clm_e5f097d92e89db263ed3e2bf39d4f6e2f38ee9afe3f946be285d50a102d8df39`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Workspace reads are allowed by default; file writes are limited to the workspace unless extra write roots are granted via --add-dir or /add-dir, and shell, network, destructive, and elevated actions are permission-gated. -- evidence: [README.md#L252-L259](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L252-L259) (`clm_712430ddb125e2a28484c82e3f0433453faf89a92bed2c23707740346881290b`)
- [observation/documented] Sandbox policy and grants can be inspected at runtime with `zero sandbox policy` and `zero sandbox grants list`; Linux source builds can include a native sandbox helper binary. -- evidence: [README.md#L96-L99](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L96-L99), [README.md#L270-L273](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L270-L273) (`clm_bf9422ff6f5187c65d75864d5bb375bb320aa191b8f8f5d42943b9b87f37e918`)

## evaluation (2 claim(s))

- [observation/documented] Zero ships an agent-eval harness (`zero eval`) with validate, run, and bench modes that score agent runs against fixture suites using verification commands, changed-file expectations, context checks, and required trace events. -- evidence: [docs/AGENT_EVALS.md#L114-L117](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L114-L117), [docs/AGENT_EVALS.md#L68-L71](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L68-L71), [docs/AGENT_EVALS.md#L85-L92](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L85-L92), [docs/AGENT_EVALS.md#L43-L47](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L43-L47) (`clm_df20135ae712835550d9c75edf542d45694f3d026f677929c3f55ff9c23d8595`)
- [observation/documented] A task benchmark measures end-to-end headless completion via `zero exec --output-format stream-json`, recording pass rate per model with and without the self-correct loop, using the verification command's exit status as authoritative. -- evidence: [docs/BENCHMARK.md#L3-L6](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/BENCHMARK.md#L3-L6), [docs/BENCHMARK.md#L42-L46](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/BENCHMARK.md#L42-L46), [docs/BENCHMARK.md#L8-L13](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/BENCHMARK.md#L8-L13), [docs/BENCHMARK.md#L38-L40](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/BENCHMARK.md#L38-L40) (`clm_980e57fb73809efdaf988734b88ebc0b9ed6c3628011cd4df756417ddf126f0f`)

## dependencies (2 claim(s))

- [observation/documented] Source builds require Go 1.26.6+; the npm wrapper ships platform builds for Linux and macOS on x64/arm64 and Windows on x64 as an optional npm dependency. -- evidence: [README.md#L53-L61](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L53-L61), [README.md#L79-L79](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L79-L79) (`clm_10ed2f3e26d51de4425a28e2af3c51fd2e10b38add9789743453dfae49d8626d`)
- [observation/documented] Zero supports many providers including OpenAI, Anthropic, Gemini, Groq, OpenRouter, DeepSeek, Mistral, xAI, Qwen, Kimi, Ollama, LM Studio, and any OpenAI- or Anthropic-compatible endpoint. -- evidence: [README.md#L28-L42](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L28-L42) (`clm_828e8c09a9d90a9c1bca579083ea62cd2d9833b9e62d72fceef5c78ff171cde7`)

## limitations (2 claim(s))

- [observation/documented] When HTTP_PROXY/HTTPS_PROXY is set, web_fetch's local address checks can be bypassed because the proxy decides the actual destination; leaving the variables unset keeps the checks enforced end to end. -- evidence: [README.md#L284-L291](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L284-L291) (`clm_891667e23e4716c22321a12e81412174f563cdce620f4a1ab44ad5e82eb84be6`)
- [observation/documented] The eval bench changed-file scoring uses `git status --porcelain` against a baseline, so an agent that commits its own changes defeats the expectedChangedFiles check. -- evidence: [docs/AGENT_EVALS.md#L213-L217](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L213-L217) (`clm_03542652bab2197f1e2d62c324e18afe732a4f8ce64d9835c99b5823382ebc25`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

