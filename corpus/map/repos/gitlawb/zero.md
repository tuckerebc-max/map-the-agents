# gitlawb/zero

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c1937dfac72e @ 20ad3944dceb5124

## Summary (orientation draft, not independently verified)

Zero is a Go-based terminal AI coding agent with an interactive TUI and scriptable headless `zero exec` mode, permission/sandbox gating, local on-disk sessions, and a documented offline agent-eval and task-benchmark harness. Development-practice guidance (make targets, go test) is kept separate under workflows. Evidence coverage: 147 of 298 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 23 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The web_fetch tool refuses loopback, private, and special-use addresses by checking the URL, resolving the host, and dialing the validated address to prevent DNS rebinding. -- evidence: [README.md#L280-L282](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L280-L282)
  - [observation/documented] Zero injects project guidance into the system prompt from the first AGENTS.md, ZERO.md, or .zero/AGENTS.md found per directory from the git root to the cwd, capped at 8 KiB per file and 32 KiB total. -- evidence: [README.md#L338-L342](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L338-L342)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should run `make fmt`, `make vet`, `make lint-static`, and `make vulncheck` before committing, using repository-managed targets with pinned tool versions rather than globally installed binaries. -- evidence: [README.md#L403-L406](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L403-L406), [README.md#L408-L410](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L408-L410), [README.md#L401-L401](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L401-L401)
  - [observation/documented] Repository development practice: contributors run `go test ./...`, and the internal/agenteval tests validate every suite JSON file, rejecting missing task IDs, empty verification commands, and malformed changed-file expectations. -- evidence: [README.md#L382-L387](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L382-L387), [docs/AGENT_EVALS.md#L237-L239](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/docs/AGENT_EVALS.md#L237-L239)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Zero offers an interactive TUI plus a scriptable headless mode (`zero exec`) supporting text, JSON, and stream-JSON I/O with meaningful exit codes for CI. -- evidence: [README.md#L20-L24](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L20-L24), [README.md#L28-L42](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L28-L42)
  - [observation/documented] The CLI exposes subcommands including setup, providers, models, doctor, sessions, spec, skills, plugins, hooks, mcp, sandbox, worktrees, verify, usage, cron, and `serve --mcp` to expose Zero tools over MCP stdio. -- evidence: [README.md#L304-L332](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L304-L332)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are stored on disk locally, searchable, resumable, and forkable, and the README states they are never uploaded as telemetry by Zero. -- evidence: [README.md#L28-L42](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L28-L42), [README.md#L304-L332](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L304-L332)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Workspace reads are allowed by default; file writes are limited to the workspace unless extra write roots are granted via --add-dir or /add-dir, and shell, network, destructive, and elevated actions are permission-gated. -- evidence: [README.md#L252-L259](https://github.com/Gitlawb/zero/blob/c1937dfac72e6ad0e5ade6e48e2d9c17d9c3e5d6/README.md#L252-L259)
More evidence: [full detail](zero.detail.md)

Metadata and full claim list: [full detail](zero.detail.md)
Human notes ([notes](zero.notes.md), never overwritten by build)

[Back to map index](../../index.md)
