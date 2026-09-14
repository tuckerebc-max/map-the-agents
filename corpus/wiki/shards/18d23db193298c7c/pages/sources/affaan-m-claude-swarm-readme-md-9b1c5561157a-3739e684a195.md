---
access: public
aliases: []
claim_ids:
- clm_31df70f1d523446e0b44e08b0716ccaf03543e3cb8c63525f50e49b6ebad57b4
- clm_3265a409edcf42c3076b3a4181f8ec8046c7e4387da93676aaf246b509582ce3
- clm_35c26913c44811aa30f06564882cf58ad07afbad4e5b96cd22a0a28e8d607d23
- clm_428cf1c18bce7dd40ccaef5f0094ef56af45003d79d6cb7d45362e7790884885
- clm_7bc2a2bac49cc8e0621205b566a72d73feef111218f5feff286d4f40df834246
- clm_8e0f78781e73969584d6ff2df37959a3bb0931e525c2a2479a995a5d9907a9bb
- clm_9d9de4df74c9c4cd6853eb71e8fcb85ed87b5c325531b50743ef89fda3abcc1a
- clm_aa5dfb3fb81daa3954934883e45ab9d59118657b7e582814cd0418aed5d6f81a
- clm_b4cb47a9ce9f82884b56c495ac42a13d2c7917b315c017b2fb577e3648911e76
- clm_b8d094e65c38c6d730f2689f83439190d65a9776fc0097c4a18c54410b036a5e
- clm_cdf4f67bf8c76e0a5dbe0d81143ca0e1eebac9c062885a4a18d5f3493f26e87b
- clm_ce7fe09b22140c62557102de320d8a9e242b2a0234a2e138c355d5224df9b6de
maturity: draft
page_id: pg_266893fa72f5576d97753739e684a195
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fd6b9564f1af559980d9478c0ed50a60
title: affaan-m/claude-swarm/README.md @ 9b1c5561157a
updated_at: '2026-09-14T01:31:19Z'
---

# affaan-m/claude-swarm/README.md @ 9b1c5561157a

<!-- rcw:begin owner=source:src_fd6b9564f1af559980d9478c0ed50a60 block=evidence -->
- Strategic model selection: Opus 4.6 for planning and quality review, Haiku for worker agents, described as 3x cheaper. [@claim:clm_31df70f1d523446e0b44e08b0716ccaf03543e3cb8c63525f50e49b6ebad57b4]
- Failed tasks are automatically retried with configurable attempt limits; the CLI default is 1 retry. [@claim:clm_3265a409edcf42c3076b3a4181f8ec8046c7e4387da93676aaf246b509582ce3]
- Stack: Python 3.11+, anyio for async concurrency, claude-agent-sdk (v0.1.35+), Rich for terminal UI, Click for CLI, Pydantic for validation, and NetworkX for topological sorting. [@claim:clm_35c26913c44811aa30f06564882cf58ad07afbad4e5b96cd22a0a28e8d607d23]
- The package is organized into modules for CLI, types, decomposer, orchestrator, quality gate, demo, config, session recording, and UI. [@claim:clm_428cf1c18bce7dd40ccaef5f0094ef56af45003d79d6cb7d45362e7790884885]
- A --demo mode runs an animated TUI simulation without needing an API key, and --dry-run shows the plan without executing. [@claim:clm_7bc2a2bac49cc8e0621205b566a72d73feef111218f5feff286d4f40df834246]
- Pessimistic file locking prevents agents from editing the same file simultaneously, and a hard budget limit cancels remaining tasks when exceeded. [@claim:clm_8e0f78781e73969584d6ff2df37959a3bb0931e525c2a2479a995a5d9907a9bb]
- Repository development practice: contributors install with pip install -e ".[dev]", run tests via pytest tests/ -v, and lint with ruff check src/ tests/. [@claim:clm_9d9de4df74c9c4cd6853eb71e8fcb85ed87b5c325531b50743ef89fda3abcc1a]
- Execution runs in phases: Opus decomposes the task into a dependency graph, independent subtasks run in parallel waves while dependents wait, then a quality gate reviews combined output. [@claim:clm_aa5dfb3fb81daa3954934883e45ab9d59118657b7e582814cd0418aed5d6f81a]
- Subcommands let users list past sessions and replay a session's events by ID. [@claim:clm_b4cb47a9ce9f82884b56c495ac42a13d2c7917b315c017b2fb577e3648911e76]
- Swarm topologies are defined in swarm.yaml with agent types (description, model, tools, prompt) and from/to connections forming a dependency graph; the tool auto-detects swarm.yaml or .claude/swarm.yaml. [@claim:clm_b8d094e65c38c6d730f2689f83439190d65a9776fc0097c4a18c54410b036a5e]
- The main CLI takes a TASK argument with options for working directory, max agents, model, budget, retries, config path, demo, dry-run, quality-gate toggle, and UI disable. [@claim:clm_cdf4f67bf8c76e0a5dbe0d81143ca0e1eebac9c062885a4a18d5f3493f26e87b]
- Every swarm execution is recorded as JSONL events, enabling later replay of what each agent did. [@claim:clm_ce7fe09b22140c62557102de320d8a9e242b2a0234a2e138c355d5224df9b6de]
<!-- rcw:end owner=source:src_fd6b9564f1af559980d9478c0ed50a60 block=evidence -->

## Researcher notes

