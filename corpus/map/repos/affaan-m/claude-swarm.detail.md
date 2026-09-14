# affaan-m/claude-swarm -- full detail

[Back to orientation](claude-swarm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/affaan-m/claude-swarm/9b1c5561157abd2d0d043758b7bfcb0319267d9f/8f87a26bc8a80398.json](../../../wiki/dossiers/affaan-m/claude-swarm/9b1c5561157abd2d0d043758b7bfcb0319267d9f/8f87a26bc8a80398.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The package is organized into modules for CLI, types, decomposer, orchestrator, quality gate, demo, config, session recording, and UI. -- evidence: [README.md#L228-L239](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L228-L239) (`clm_428cf1c18bce7dd40ccaef5f0094ef56af45003d79d6cb7d45362e7790884885`)

## design-choices (1 claim(s))

- [observation/documented] Strategic model selection: Opus 4.6 for planning and quality review, Haiku for worker agents, described as 3x cheaper. -- evidence: [README.md#L189-L189](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L189-L189), [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124), [README.md#L195-L195](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L195-L195) (`clm_31df70f1d523446e0b44e08b0716ccaf03543e3cb8c63525f50e49b6ebad57b4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors install with pip install -e ".[dev]", run tests via pytest tests/ -v, and lint with ruff check src/ tests/. -- evidence: [README.md#L223-L224](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L223-L224), [README.md#L215-L217](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L215-L217), [README.md#L220-L220](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L220-L220) (`clm_9d9de4df74c9c4cd6853eb71e8fcb85ed87b5c325531b50743ef89fda3abcc1a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The main CLI takes a TASK argument with options for working directory, max agents, model, budget, retries, config path, demo, dry-run, quality-gate toggle, and UI disable. -- evidence: [README.md#L132-L143](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L132-L143), [README.md#L130-L130](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L130-L130) (`clm_cdf4f67bf8c76e0a5dbe0d81143ca0e1eebac9c062885a4a18d5f3493f26e87b`)
- [observation/documented] Subcommands let users list past sessions and replay a session's events by ID. -- evidence: [README.md#L146-L148](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L146-L148) (`clm_b4cb47a9ce9f82884b56c495ac42a13d2c7917b315c017b2fb577e3648911e76`)
- [observation/documented] Swarm topologies are defined in swarm.yaml with agent types (description, model, tools, prompt) and from/to connections forming a dependency graph; the tool auto-detects swarm.yaml or .claude/swarm.yaml. -- evidence: [README.md#L154-L159](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L154-L159), [README.md#L176-L183](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L176-L183), [README.md#L161-L167](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L161-L167), [README.md#L185-L185](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L185-L185), [README.md#L169-L174](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L169-L174) (`clm_b8d094e65c38c6d730f2689f83439190d65a9776fc0097c4a18c54410b036a5e`)
- [observation/documented] A --demo mode runs an animated TUI simulation without needing an API key, and --dry-run shows the plan without executing. -- evidence: [README.md#L132-L143](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L132-L143), [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124) (`clm_7bc2a2bac49cc8e0621205b566a72d73feef111218f5feff286d4f40df834246`)

## memory-state (1 claim(s))

- [observation/documented] Every swarm execution is recorded as JSONL events, enabling later replay of what each agent did. -- evidence: [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124), [README.md#L146-L148](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L146-L148) (`clm_ce7fe09b22140c62557102de320d8a9e242b2a0234a2e138c355d5224df9b6de`)

## orchestration (3 claim(s))

- [observation/documented] Execution runs in phases: Opus decomposes the task into a dependency graph, independent subtasks run in parallel waves while dependents wait, then a quality gate reviews combined output. -- evidence: [README.md#L17-L22](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L17-L22), [README.md#L24-L29](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L24-L29) (`clm_aa5dfb3fb81daa3954934883e45ab9d59118657b7e582814cd0418aed5d6f81a`)
- [observation/documented] Pessimistic file locking prevents agents from editing the same file simultaneously, and a hard budget limit cancels remaining tasks when exceeded. -- evidence: [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124) (`clm_8e0f78781e73969584d6ff2df37959a3bb0931e525c2a2479a995a5d9907a9bb`)
- [observation/documented] Failed tasks are automatically retried with configurable attempt limits; the CLI default is 1 retry. -- evidence: [README.md#L132-L143](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L132-L143), [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124) (`clm_3265a409edcf42c3076b3a4181f8ec8046c7e4387da93676aaf246b509582ce3`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Stack: Python 3.11+, anyio for async concurrency, claude-agent-sdk (v0.1.35+), Rich for terminal UI, Click for CLI, Pydantic for validation, and NetworkX for topological sorting. -- evidence: [README.md#L204-L209](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L204-L209) (`clm_35c26913c44811aa30f06564882cf58ad07afbad4e5b96cd22a0a28e8d607d23`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

