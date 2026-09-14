# andyrewlee/amux

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f94362f6c25f @ 77bb298aa1345b27

## Summary (orientation draft, not independently verified)

amux is a Go/Bubble Tea terminal UI for running multiple coding agents in parallel via tmux sessions and git worktrees, with workspace scripts, confirmation-gated git actions, and documented architecture. Evidence covers product behavior, configuration, and contributor workflows.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Two binaries share internal packages: cmd/amux (interactive app) and cmd/amux-harness (headless renderer for deterministic perf and render testing), with internal layers for app, ui, tmux, pty, git, data, and vterm. -- evidence: [ARCHITECTURE.md#L3-L8](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L3-L8), [ARCHITECTURE.md#L30-L47](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L30-L47), [ARCHITECTURE.md#L64-L97](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L64-L97)
- design-choices (2 claim(s)):
  - [observation/documented] amux runs git with repository hooks and core.fsmonitor disabled so a checked-out repo cannot execute code merely because amux touched it; AMUX_ALLOW_GIT_HOOKS=1 re-enables hooks, while git-lfs filters are never disabled. -- evidence: [README.md#L68-L68](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L68-L68), [README.md#L156-L165](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L156-L165)
  - [observation/documented] Both write actions (commit and merge) are available from the UI and each is placed behind an explicit confirmation. -- evidence: [README.md#L63-L63](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L63-L63)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run ./scripts/install-hooks.sh to enable pre-commit fmt/lint checks and a pre-push lint-parity gate, and build the pinned golangci-lint via make lint-tools before make devcheck. -- evidence: [README.md#L144-L146](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L144-L146), [README.md#L136-L142](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L136-L142), [README.md#L148-L152](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L148-L152)
  - [observation/documented] Repository development practice: AGENTS.md instructs validating changes with make devcheck, using the harness with -dump-frame for headless render verification, and running make verify-loop for input/send/tmux changes to prove end-to-end keystroke delivery. -- evidence: [AGENTS.md#L3-L16](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/AGENTS.md#L3-L16)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] amux is a terminal UI (Bubble Tea v2) for running multiple coding agents in parallel, using a workspace-first model that can import git worktrees. -- evidence: [ARCHITECTURE.md#L3-L8](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L3-L8), [README.md#L31-L31](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L31-L31)
  - [observation/documented] Workspaces are configured via a project-level .amux/workspaces.json defining setup-workspace, run, and archive commands, with environment variables like AMUX_WORKSPACE_NAME and AMUX_PORT exposed to those scripts. -- evidence: [README.md#L87-L96](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L87-L96), [README.md#L115-L122](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L115-L122), [README.md#L85-L85](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L85-L85)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Project-supplied workspace scripts are gated: amux records an approval of .amux/workspaces.json content before running it, and edits invalidate the approval until re-trusted; user-entered scripts are never gated. -- evidence: [README.md#L124-L124](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L124-L124)
- evaluation (1 claim(s)):
  - [inference/documented] The amux-harness binary appears to support deterministic perf and render testing of the UI itself (headless frame dumps), suggesting an internal render/perf evaluation path rather than agent-task benchmarking. -- evidence: [AGENTS.md#L3-L16](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/AGENTS.md#L3-L16), [ARCHITECTURE.md#L3-L8](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L3-L8)
- dependencies (2 claim(s)):
More evidence: [full detail](amux.detail.md)

Metadata and full claim list: [full detail](amux.detail.md)
Human notes ([notes](amux.notes.md), never overwritten by build)

[Back to map index](../../index.md)
