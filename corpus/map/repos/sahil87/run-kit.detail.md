# sahil87/run-kit -- full detail

[Back to orientation](run-kit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sahil87/run-kit/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/fc34e1f500229b22.json](../../../wiki/dossiers/sahil87/run-kit/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/fc34e1f500229b22.json)

## specifications (1 claim(s))

- [observation/documented] HexoKit is described as a remote, phone-first console for tmux: every tmux session and pane appears as a live browser terminal, with state read directly from tmux rather than a database. -- evidence: [README.md#L7-L7](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L7-L7), [README.md#L50-L53](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L50-L53) (`clm_89939e9b1770978a696a137c5f715e67e705c3d996d393bd21f9df4eed58244c`)

## components (3 claim(s))

- [observation/documented] The product is two independent halves that compose: `rk riff`, which spawns agent workspaces (git worktree plus tmux window), and `rk serve`, which runs the browser dashboard watching tmux; either can run alone. -- evidence: [README.md#L84-L84](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L84-L84), [README.md#L76-L82](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L76-L82), [README.md#L74-L74](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L74-L74) (`clm_6840d2f95ef77ee5d009b170de725c71ef657ddf0d8e4f5cf0de9509fb132772`)
- [observation/documented] Windows running AI agents can report live lifecycle state (active, waiting, idle) via opt-in per-machine setup that installs agent-harness hooks for Claude Code, Codex, Gemini CLI, Copilot CLI, Kimi Code, OpenCode, and Antigravity CLI, stamping a `@rk_pane_agent_state` tmux pane option. -- evidence: [README.md#L133-L133](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L133-L133), [README.md#L143-L143](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L143-L143) (`clm_7d8d18004d1edfaec2739f140c2c309c01bf150d25ec034c4e827f0749c26fe8`)
- [observation/documented] The dashboard offers named cross-server boards pinning multiple tmux panes side-by-side (pin state stored in tmux), a GUI tile running the host desktop via a private X display with selectable window managers, and a macOS Electron desktop app installable via `rk desktop install`. -- evidence: [README.md#L153-L153](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L153-L153), [README.md#L174-L177](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L174-L177), [README.md#L172-L172](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L172-L172), [README.md#L157-L157](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L157-L157) (`clm_a906c6c97146cc28eed680c67837bbea1cbcb9e16dd354804baf5f09fed2addd`)

## design-choices (2 claim(s))

- [observation/documented] The product is deliberately agent-agnostic: it does not speak any agent's protocol or parse agent output, treating a pane as just a pane so the terminal layer survives agent-tooling churn. -- evidence: [README.md#L9-L9](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L9-L9), [README.md#L50-L53](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L50-L53) (`clm_38d90823ae2daa928ab01f58c12d659eae1864baa3de4cda9c02dfbd9c2b0abc`)
- [observation/documented] A measured spike concluded the terminal relay mux must use per-stream bounded send queues with a non-FIFO scheduler: a shared FIFO made echo RTT 1.66s under flood at 1 Mbps, while per-stream queues held it to 32ms with no throughput cost. -- evidence: [docs/findings/relay-mux-hol.md#L51-L60](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/relay-mux-hol.md#L51-L60), [docs/findings/relay-mux-hol.md#L27-L33](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/relay-mux-hol.md#L27-L33), [docs/findings/relay-mux-hol.md#L37-L47](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/relay-mux-hol.md#L37-L47) (`clm_27e6c8fc29e55278d28f76e82b75d2911eee62f6bfd4f55e4ecd99c502c99983`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: a post-mortem documents that a 59-file PR passed all gates (Go, tsc, ~3,590 vitest tests, two Playwright suites, build) yet needed ten review cycles against a budget of three, and recommends splitting changes by risk class and manually exercising new interaction components before ship. -- evidence: [docs/findings/marker-rework-review-cycles.md#L3-L10](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L3-L10), [docs/findings/marker-rework-review-cycles.md#L14-L23](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L14-L23), [docs/findings/marker-rework-review-cycles.md#L130-L145](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L130-L145), [docs/findings/marker-rework-review-cycles.md#L51-L54](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/docs/findings/marker-rework-review-cycles.md#L51-L54) (`clm_71f6b4b3cea2831e40c8a96e40dcd8cd9cf4b9b2f176a79a9f491e3aa9ce9643`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] `rk riff` supports repeatable `--skill`/`--cmd` flags (one pane each, in argv order), `--layout` (auto, tiled, even-*, main-*), presets in `fab/project/config.yaml`, `-N` parallel spawning with rollback on failure, and `--` passthrough of flags to `wt create`. -- evidence: [README.md#L90-L94](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L90-L94) (`clm_4306f314d8d92137c12642ee58d7d9a91625b2a285b827bebc7cf50c30591cc2`)
- [observation/documented] `rk serve` is configurable via `RK_HOST` (default 127.0.0.1) and `RK_PORT` (default 3000), and background operation is provided by `rk daemon` subcommands (start, restart, stop, status) running in a dedicated `rk-daemon` tmux server. -- evidence: [README.md#L107-L107](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L107-L107), [README.md#L109-L112](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L109-L112), [README.md#L114-L114](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L114-L114) (`clm_b392578fc4ad67090dee56f8322a523521ecaf277dea7cfc46df953ad758f562`)
- [observation/documented] The CLI includes an MCP server over stdio (`rk mcp`) as an allowlisted proxy over rk verbs, with `rk url --mcp` printing the `/mcp` endpoint, plus commands like `rk notify`, `rk cron`, `rk gui`, and `rk doctor`. -- evidence: [README.md#L203-L229](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L203-L229) (`clm_54efe180b906563606d715a65f05510f7ef6947b0309dff2f1708d7e2cb478eb`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product requires tmux >= 3.4 (checked at runtime via `rk doctor`) and, for `rk riff`, the sibling `wt` tool and a launcher binary (default `claude --dangerously-skip-permissions`) on PATH. -- evidence: [README.md#L101-L101](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L101-L101), [README.md#L19-L19](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L19-L19), [README.md#L235-L239](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L235-L239) (`clm_8ee09b42188338e586eceb7c4671bb3f27b64243e2cc05cf5641448638b9fbb7`)

## limitations (1 claim(s))

- [observation/documented] `rk riff` requires being inside a tmux session (`$TMUX` set) and fails with "not in a tmux session" otherwise; agent state shows `—` until the hook setup runs and fresh agent sessions are started. -- evidence: [README.md#L143-L143](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L143-L143), [README.md#L235-L239](https://github.com/sahil87/run-kit/blob/65653f4d91c5a1b4c6e2f2cd4018aa7b4bfa1328/README.md#L235-L239) (`clm_1e152ffba5bb509b795e092acb487b38650fd2b97ff4f21caef35710d72c21d4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

