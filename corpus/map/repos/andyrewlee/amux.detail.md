# andyrewlee/amux -- full detail

[Back to orientation](amux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/andyrewlee/amux/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/77bb298aa1345b27.json](../../../wiki/dossiers/andyrewlee/amux/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/77bb298aa1345b27.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Two binaries share internal packages: cmd/amux (interactive app) and cmd/amux-harness (headless renderer for deterministic perf and render testing), with internal layers for app, ui, tmux, pty, git, data, and vterm. -- evidence: [ARCHITECTURE.md#L3-L8](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L3-L8), [ARCHITECTURE.md#L30-L47](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L30-L47), [ARCHITECTURE.md#L64-L97](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L64-L97) (`clm_0ef2ad0503639ad8290439eccf3a615bd96755095aea1c23006068110375617c`)

## design-choices (2 claim(s))

- [observation/documented] amux runs git with repository hooks and core.fsmonitor disabled so a checked-out repo cannot execute code merely because amux touched it; AMUX_ALLOW_GIT_HOOKS=1 re-enables hooks, while git-lfs filters are never disabled. -- evidence: [README.md#L68-L68](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L68-L68), [README.md#L156-L165](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L156-L165) (`clm_ad7233bfa6f3332b5da88037ba9092c6a82acb797e9c3b368b6243a44b54e59e`)
- [observation/documented] Both write actions (commit and merge) are available from the UI and each is placed behind an explicit confirmation. -- evidence: [README.md#L63-L63](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L63-L63) (`clm_416af15c0b2a2c51afa8d50b00b8778c507d445b52fbd1482db9c3731221e14d`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run ./scripts/install-hooks.sh to enable pre-commit fmt/lint checks and a pre-push lint-parity gate, and build the pinned golangci-lint via make lint-tools before make devcheck. -- evidence: [README.md#L144-L146](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L144-L146), [README.md#L136-L142](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L136-L142), [README.md#L148-L152](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L148-L152) (`clm_c922d34785fb9357893436180f3de376ba410ea063c6ed000ac3dc7209228fe0`)
- [observation/documented] Repository development practice: AGENTS.md instructs validating changes with make devcheck, using the harness with -dump-frame for headless render verification, and running make verify-loop for input/send/tmux changes to prove end-to-end keystroke delivery. -- evidence: [AGENTS.md#L3-L16](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/AGENTS.md#L3-L16) (`clm_9d32a63b513f4fb1a0e259c3c83652f5b387e7273575008d9457a5f65a52c0f4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] amux is a terminal UI (Bubble Tea v2) for running multiple coding agents in parallel, using a workspace-first model that can import git worktrees. -- evidence: [ARCHITECTURE.md#L3-L8](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L3-L8), [README.md#L31-L31](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L31-L31) (`clm_592fb050a727d5071ae34f4e91f9412fc86a82b9c36e922f7b65adde2bec7f08`)
- [observation/documented] Workspaces are configured via a project-level .amux/workspaces.json defining setup-workspace, run, and archive commands, with environment variables like AMUX_WORKSPACE_NAME and AMUX_PORT exposed to those scripts. -- evidence: [README.md#L87-L96](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L87-L96), [README.md#L115-L122](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L115-L122), [README.md#L85-L85](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L85-L85) (`clm_58f56cbaf277905d8b57b4f1c3216f279d024bfbe49cd69b86cbf58cc31fbe9a`)
- [observation/documented] Commit (key 'c') stages and commits on the workspace's own branch without pushing; merge (key 'M') uses git merge --no-ff in the primary checkout, refusing if the base branch is not checked out there, and lists conflicted files on conflict. -- evidence: [README.md#L65-L66](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L65-L66) (`clm_f9b5aeedf37e09bd917a10126b8bd6f3e7957bb87879dbb0bce5df4b70c19466`)
- [observation/documented] Agent definitions are configured per-user in ~/.amux/config.json, where users can add assistants or override built-ins; workspace metadata and trusted-script approvals live under ~/.amux. -- evidence: [README.md#L126-L126](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L126-L126), [README.md#L128-L128](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L128-L128) (`clm_2b112b20ca0981723b10b5e603b3ded72a761fb8a66a7ff7576eb138982298f2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Project-supplied workspace scripts are gated: amux records an approval of .amux/workspaces.json content before running it, and edits invalidate the approval until re-trusted; user-entered scripts are never gated. -- evidence: [README.md#L124-L124](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L124-L124) (`clm_23f50ed15deba6890b12b61e5c6ada497f2c7092d25be5e1a92792e6ba3c9f24`)

## evaluation (1 claim(s))

- [inference/documented] The amux-harness binary appears to support deterministic perf and render testing of the UI itself (headless frame dumps), suggesting an internal render/perf evaluation path rather than agent-task benchmarking. -- evidence: [AGENTS.md#L3-L16](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/AGENTS.md#L3-L16), [ARCHITECTURE.md#L3-L8](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L3-L8) (`clm_17cc819bca8d21cf6c9d191bbaab9e041a0d2fd832e754877e069354c13d7d63`)

## dependencies (2 claim(s))

- [observation/documented] amux requires tmux (minimum 3.2); each agent runs in its own tmux session for terminal isolation and persistence, and the tool is supported on Linux/macOS only. -- evidence: [README.md#L132-L132](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L132-L132), [README.md#L35-L35](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L35-L35) (`clm_5f7998296dd7ec0f51b6b8768262f8c605089f5147cd30e0a719b0b14977caa4`)
- [observation/documented] internal/ui/compositor imports charmbracelet/ultraviolet directly on the render path; ultraviolet has no semver releases and its pin must stay in lockstep with bubbletea/v2 to avoid rendering breakage. -- evidence: [ARCHITECTURE.md#L51-L58](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/ARCHITECTURE.md#L51-L58) (`clm_ed5316e179b683c0c7a1374fa17d3b85ba7afd4eeb98f04d28844d6f36a7138f`)

## limitations (1 claim(s))

- [observation/documented] Windows is not supported; the tool requires tmux and targets Linux/macOS. -- evidence: [README.md#L132-L132](https://github.com/andyrewlee/amux/blob/f94362f6c25f20aa0476f3d23f80bd17c3fc4e72/README.md#L132-L132) (`clm_e81dad8ddfe30c4d4bae66a54eba4bb095557541d088f16abeced467728bf904`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

