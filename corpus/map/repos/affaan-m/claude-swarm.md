# affaan-m/claude-swarm

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9b1c5561157a @ 8f87a26bc8a80398

## Summary (orientation draft, not independently verified)

Claude Swarm is a Python CLI that orchestrates parallel Claude Code agents via the Claude Agent SDK, with Opus-based task decomposition and quality review, Haiku worker agents, file locking, budget enforcement, YAML-configurable topologies, and JSONL session recording/replay. Evidence is README-only; no source code slices are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The package is organized into modules for CLI, types, decomposer, orchestrator, quality gate, demo, config, session recording, and UI. -- evidence: [README.md#L228-L239](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L228-L239)
- design-choices (1 claim(s)):
  - [observation/documented] Strategic model selection: Opus 4.6 for planning and quality review, Haiku for worker agents, described as 3x cheaper. -- evidence: [README.md#L189-L189](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L189-L189), [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124), [README.md#L195-L195](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L195-L195)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors install with pip install -e ".[dev]", run tests via pytest tests/ -v, and lint with ruff check src/ tests/. -- evidence: [README.md#L223-L224](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L223-L224), [README.md#L215-L217](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L215-L217), [README.md#L220-L220](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L220-L220)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The main CLI takes a TASK argument with options for working directory, max agents, model, budget, retries, config path, demo, dry-run, quality-gate toggle, and UI disable. -- evidence: [README.md#L132-L143](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L132-L143), [README.md#L130-L130](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L130-L130)
  - [observation/documented] Subcommands let users list past sessions and replay a session's events by ID. -- evidence: [README.md#L146-L148](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L146-L148)
- memory-state (1 claim(s)):
  - [observation/documented] Every swarm execution is recorded as JSONL events, enabling later replay of what each agent did. -- evidence: [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124), [README.md#L146-L148](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L146-L148)
- orchestration (3 claim(s)):
  - [observation/documented] Execution runs in phases: Opus decomposes the task into a dependency graph, independent subtasks run in parallel waves while dependents wait, then a quality gate reviews combined output. -- evidence: [README.md#L17-L22](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L17-L22), [README.md#L24-L29](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L24-L29)
  - [observation/documented] Pessimistic file locking prevents agents from editing the same file simultaneously, and a hard budget limit cancels remaining tasks when exceeded. -- evidence: [README.md#L111-L124](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L111-L124)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Stack: Python 3.11+, anyio for async concurrency, claude-agent-sdk (v0.1.35+), Rich for terminal UI, Click for CLI, Pydantic for validation, and NetworkX for topological sorting. -- evidence: [README.md#L204-L209](https://github.com/affaan-m/claude-swarm/blob/9b1c5561157abd2d0d043758b7bfcb0319267d9f/README.md#L204-L209)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](claude-swarm.detail.md) for every claim.)

Metadata and full claim list: [full detail](claude-swarm.detail.md)
Human notes ([notes](claude-swarm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
