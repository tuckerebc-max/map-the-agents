# supabitapp/supacode

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 81cba5538f1e @ 66b194affe240b6a

## Summary (orientation draft, not independently verified)

Supacode is a native macOS app for running coding agents in parallel via git worktrees, with persistent zmx-backed sessions, SSH remote repos, a CLI/deeplink interface, and GitHub PR tracking. The evidence is mostly README product documentation plus contributor build/coding guidelines.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Supacode is a native macOS application (macOS 26.0+ required) that acts as a command center for running coding agents in parallel. -- evidence: [README.md#L3-L3](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L3-L3), [README.md#L73-L76](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L73-L76)
- components (5 claim(s)):
  - [observation/documented] Remote SSH repositories are supported in beta: git probes and terminals share one multiplexed SSH connection, and with zmx on the host, remote sessions survive dropped connections and sleep. -- evidence: [README.md#L31-L35](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L31-L35)
  - [observation/documented] The app detects the coding agent per pane (busy, awaiting input, idle) via installed hooks, supporting Claude, Codex, and Copilot locally and over SSH, and drives notifications. -- evidence: [README.md#L45-L47](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L45-L47)
- design-choices (1 claim(s)):
  - [observation/documented] Each task gets its own git worktree and real terminal so agents run in parallel without colliding; worktrees can be created from the sidebar, hotkey, command palette, CLI, or deeplink. -- evidence: [README.md#L5-L7](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L5-L7), [README.md#L17-L21](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L17-L21)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use mise for a pinned toolchain, git submodules, and make targets (doctor, build-ghostty-xcframework, build-app, run-app); on macOS 26.4+ Xcode 26.3 is needed because the pinned Zig 0.15.2 linker cannot link that SDK. -- evidence: [README.md#L94-L98](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L94-L98), [README.md#L80-L86](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L80-L86), [README.md#L102-L108](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L102-L108), [README.md#L73-L76](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L73-L76)
  - [observation/documented] Repository development practice: contributions require opening an issue first, waiting for a `ready` label, then a focused linked PR; a human, never an AI agent, must be the accountable author, and code follows Swift 6/TCA style rules checked by `make check`. -- evidence: [README.md#L120-L124](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L120-L124), [AGENTS.md#L24-L39](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/AGENTS.md#L24-L39), [AGENTS.md#L51-L55](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/AGENTS.md#L51-L55), [README.md#L134-L137](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L134-L137)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A `supacode` CLI manages worktrees, tabs, splits, and repos; sessions export repo, worktree, tab, and surface IDs, and `supacode://` deeplinks mirror CLI actions. -- evidence: [README.md#L51-L54](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L51-L54)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions run inside zmx, a session daemon, rather than as app children, so quitting and relaunching reattaches sessions with scrollback; this is on by default with an optional teardown quit. -- evidence: [README.md#L25-L27](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L25-L27)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](supacode.detail.md)

Metadata and full claim list: [full detail](supacode.detail.md)
Human notes ([notes](supacode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
