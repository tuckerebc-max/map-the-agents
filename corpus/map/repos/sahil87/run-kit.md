# sahil87/run-kit

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 65653f4d91c5 @ fc34e1f500229b22

## Summary (orientation draft, not independently verified)

Evidence covers the README of run-kit (HexoKit), a tmux-over-browser dashboard with an agent-workspace spawner, plus two engineering findings documents (a review-cycle post-mortem and a head-of-line-blocking spike). Claims below describe the documented product surface and the repository's development findings; no code was inspected.

## Source coverage

Source coverage (partial): 3 of 98 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] HexoKit is described as a remote, phone-first console for tmux: every tmux session and pane appears as a live browser terminal, with state read directly from tmux rather than a database. -- evidence: [README.md#L7-L7](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L7-L7), [README.md#L50-L53](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L50-L53)
- components (3 claim(s)):
  - [observation/documented] The product is two independent halves that compose: `rk riff`, which spawns agent workspaces (git worktree plus tmux window), and `rk serve`, which runs the browser dashboard watching tmux; either can run alone. -- evidence: [README.md#L84-L84](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L84-L84), [README.md#L76-L82](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L76-L82), [README.md#L74-L74](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L74-L74)
  - [observation/documented] Windows running AI agents can report live lifecycle state (active, waiting, idle) via opt-in per-machine setup that installs agent-harness hooks for Claude Code, Codex, Gemini CLI, Copilot CLI, Kimi Code, OpenCode, and Antigravity CLI, stamping a `@rk_pane_agent_state` tmux pane option. -- evidence: [README.md#L133-L133](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L133-L133), [README.md#L143-L143](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L143-L143)
- design-choices (2 claim(s)):
  - [observation/documented] The product is deliberately agent-agnostic: it does not speak any agent's protocol or parse agent output, treating a pane as just a pane so the terminal layer survives agent-tooling churn. -- evidence: [README.md#L9-L9](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L9-L9), [README.md#L50-L53](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L50-L53)
  - [observation/documented] A measured spike concluded the terminal relay mux must use per-stream bounded send queues with a non-FIFO scheduler: a shared FIFO made echo RTT 1.66s under flood at 1 Mbps, while per-stream queues held it to 32ms with no throughput cost. -- evidence: [docs/findings/relay-mux-hol.md#L51-L60](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/relay-mux-hol.md#L51-L60), [docs/findings/relay-mux-hol.md#L27-L33](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/relay-mux-hol.md#L27-L33), [docs/findings/relay-mux-hol.md#L37-L47](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/relay-mux-hol.md#L37-L47)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: a post-mortem documents that a 59-file PR passed all gates (Go, tsc, ~3,590 vitest tests, two Playwright suites, build) yet needed ten review cycles against a budget of three, and recommends splitting changes by risk class and manually exercising new interaction components before ship. -- evidence: [docs/findings/marker-rework-review-cycles.md#L3-L10](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L3-L10), [docs/findings/marker-rework-review-cycles.md#L14-L23](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L14-L23), [docs/findings/marker-rework-review-cycles.md#L130-L145](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L130-L145), [docs/findings/marker-rework-review-cycles.md#L51-L54](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L51-L54)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] `rk riff` supports repeatable `--skill`/`--cmd` flags (one pane each, in argv order), `--layout` (auto, tiled, even-*, main-*), presets in `fab/project/config.yaml`, `-N` parallel spawning with rollback on failure, and `--` passthrough of flags to `wt create`. -- evidence: [README.md#L90-L94](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L90-L94)
More evidence: [full detail](run-kit.detail.md)

Metadata and full claim list: [full detail](run-kit.detail.md)
Human notes ([notes](run-kit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
