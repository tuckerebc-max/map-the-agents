# tarunms7/forge-orchestrator -- full detail

[Back to orientation](forge-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tarunms7/forge-orchestrator/0ac78e8eddf570c11f01e5cb500a74ba148a6477/25cc550ed3447ada.json](../../../wiki/dossiers/tarunms7/forge-orchestrator/0ac78e8eddf570c11f01e5cb500a74ba148a6477/25cc550ed3447ada.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Before coding, a Contract Builder generates binding API and type specs naming producer and consumer tasks, so parallel agents agree on interfaces; the reviewer checks compliance. -- evidence: [README.md#L204-L204](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L204-L204), [README.md#L213-L213](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L213-L213), [README.md#L206-L211](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L206-L211) (`clm_97ae59c960fad73e8553fd6ad5da1ca2ad33a268e79fcf8bc48228859f2ccae2`)
- [inference/documented] An implementation plan proposes replacing the Scout→Architect→Detailer→Validator planning pipeline with a single Unified Planner having read-only tool access (Edit/Write disallowed) and a deterministic validator; this appears to be a planned change, not necessarily shipped behavior. -- evidence: [IMPLEMENTATION_PLAN.md#L177-L189](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L177-L189), [IMPLEMENTATION_PLAN.md#L5-L5](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L5-L5), [IMPLEMENTATION_PLAN.md#L17-L29](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L17-L29), [IMPLEMENTATION_PLAN.md#L287-L287](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L287-L287) (`clm_f54e03ba95d74f62fba177a18ebb89438d983cbbe25a4f7eab338e58c11f62fd`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors set up a venv, pip install -e '.[dev,web]', and run python -m pytest forge/ -q; CI runs ruff lint and format plus 2200+ tests on every PR. -- evidence: [README.md#L543-L543](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L543-L543), [README.md#L535-L541](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L535-L541) (`clm_f0b547aba31bdf94027edff00a7c3a70ac5f40424bea70f22c149dcbba9854ef`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a Click-based CLI with 14 commands including forge tui, run, fix, status, stats, logs, lessons, doctor, clean, init, serve, upgrade, and ping. -- evidence: [README.md#L500-L514](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L500-L514), [README.md#L467-L482](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L467-L482) (`clm_8a6ddf7536a6b29973804692e572d8e9f533e8e6906933d52864c0e3a08738d3`)
- [observation/documented] A terminal UI (forge tui) and a web dashboard (forge serve, backend on port 8000 and frontend on 3000) provide live pipeline progress, plan editing, contract viewing, and cost tracking. -- evidence: [README.md#L492-L492](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L492-L492), [README.md#L488-L490](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L488-L490) (`clm_7411f0e60d0310a10281c7c9accd8bc28e294697e7e1ba2e54d304b3e8405b6c`)

## memory-state (2 claim(s))

- [observation/documented] Forge stores lessons learned from failed-then-retried tasks, filters transient errors like 503s, persists lessons across projects, and adapts timeouts after slow failures; lessons are viewable and addable via forge lessons. -- evidence: [README.md#L219-L222](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L219-L222), [README.md#L224-L227](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L224-L227) (`clm_39cb5a8c1ce0d3afe40ff97ba09a46aecfde5eac5131ab4b5fce348945947fc4`)
- [observation/documented] The resolved provider configuration is persisted in pipelines.provider_config at pipeline creation, and restarts, retries, and webhook resumptions reuse that snapshot rather than current settings. -- evidence: [README.md#L403-L403](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L403-L403) (`clm_b6f2650fe72face375d81b566897f355f626f64e6f113cf89fff7ff2cc5a63a2`)

## orchestration (2 claim(s))

- [observation/documented] Pipelines run six stages: pre-flight validation, planning into a task DAG, contract generation, parallel execution in isolated git worktrees, a five-gate review (build, lint, test, LLM review, contracts), then format, rebase, merge, and gh pr create. -- evidence: [README.md#L174-L200](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L174-L200) (`clm_7b24c603b726ce130335b2c3ee33d7dcb555c211c381afce0f104f58663589e6`)
- [observation/documented] A background health monitor detects tasks in progress over 15 minutes without activity, reviews running over 10 minutes, deadlocks, and dependency cascades, surfacing problems during execution. -- evidence: [README.md#L248-L248](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L248-L248), [README.md#L250-L253](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L250-L253), [README.md#L255-L255](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L255-L255) (`clm_7d67f40c3bad1e1cf7e7e9bfdf7f43acae1b30c91bf4f80f549a0af9835e84a0`)

## tools-permissions (1 claim(s))

- [observation/documented] Codex-backed agent executions run in full-access sandbox mode with automatic execution, no per-command approval prompts, live network access and native web search, while a Forge-level safety policy still blocks explicitly denied operations. -- evidence: [README.md#L423-L423](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L423-L423), [README.md#L425-L428](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L425-L428) (`clm_33f32e56edc697a59e9af78ddd8093c84d189188eab0bb424117818a9cd271c4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites are Git 2.20+ and the Claude Code CLI (claude login); the gh CLI is optional for automatic PR creation, and the installer handles Python 3.12 and uv. -- evidence: [README.md#L120-L121](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L120-L121), [README.md#L127-L127](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L127-L127) (`clm_b62033299eb5122380245f1aef5f1906cee40c31b5a3d59e5a4aac80bed9a7d7`)
- [observation/documented] Claude is the default provider; OpenAI routing is opt-in via FORGE_OPENAI_ENABLED, with Codex-backed models using codex login or CODEX_API_KEY and openai:o3 requiring OPENAI_API_KEY. -- evidence: [README.md#L421-L421](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L421-L421), [README.md#L285-L302](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L285-L302), [README.md#L36-L36](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L36-L36) (`clm_0bcf280e948c1f20c08f7ace889c794519d1f7f0ff3d3805d81f69f5309bffbd`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

