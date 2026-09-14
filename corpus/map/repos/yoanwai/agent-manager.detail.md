# yoanwai/agent-manager -- full detail

[Back to orientation](agent-manager.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yoanwai/agent-manager/0f40e31fb1cab86e38748f8677cbf58e4029df69/39eac2119f1af8d9.json](../../../wiki/dossiers/yoanwai/agent-manager/0f40e31fb1cab86e38748f8677cbf58e4029df69/39eac2119f1af8d9.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product is a terminal workspace where Claude Code, Codex, OpenCode, Grok, Gemini CLI, Pi, Command Code, and Hermes Agent run side by side, each in its own persistent tmux session. -- evidence: [README.md#L36-L36](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L36-L36) (`clm_d652a84e4fb02101de726a314085753f6b3c2f3856c9550093cfc122f7199d7a`)

## design-choices (2 claim(s))

- [observation/documented] The tool is described as a thin layer over the user's installed CLIs: sessions launch the user's own tool with its login, config, and MCP servers intact. -- evidence: [README.md#L38-L38](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L38-L38) (`clm_848d73a953683d5679c7886f24ddbee1f880a31e45f4752cc3f12cc627b528b6`)
- [observation/documented] DESIGN.md specifies a terminal-native, keyboard-first, information-dense aesthetic: monospace-only type, semantic theme tokens instead of hard-coded colors, and status color always paired with a glyph or label. -- evidence: [DESIGN.md#L59-L59](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L59-L59), [DESIGN.md#L70-L70](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L70-L70), [DESIGN.md#L61-L64](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L61-L64), [DESIGN.md#L55-L55](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L55-L55) (`clm_62085de4d234eeab867452262617fd7f9cabaa0f86ccd118681a61536a98c244`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: tests must run as `env -u TMUX TMUX_TMPDIR=/tmp/amtest go test ./...` because the suite drives a real tmux server and a bare go test could hit the live socket; gofmt and go vet must be clean before finishing. -- evidence: [AGENTS.md#L21-L25](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L21-L25), [AGENTS.md#L34-L34](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L34-L34), [AGENTS.md#L27-L32](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L27-L32) (`clm_e825889515b7b4d46bbba3f986dfce0fd01d2296ad5d01838eba3c9e68362f59`)
- [observation/documented] Repository development practice: releases are cut locally with goreleaser from a clean worktree at the tag, with no release workflow in CI; AUR_KEY is required or the Arch package publish silently skips. -- evidence: [AGENTS.md#L48-L54](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L48-L54), [AGENTS.md#L56-L58](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L56-L58), [AGENTS.md#L45-L46](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L45-L46) (`clm_9c5da556c2d145f176791006c1991c10606765cb95c5a2a80826063e8e001420`)
- [observation/documented] Repository development practice: the codebase layout is main.go dispatching subcommands, internal/ui as a Bubble Tea program, internal/tmux for the dedicated socket, internal/store for SQLite state, and internal/status for classifying pane output. -- evidence: [AGENTS.md#L92-L101](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L92-L101) (`clm_393a89decc217335128a19a8061fcb03c78a04fcd9620f35e34b405bae33eaaa`)
- [observation/documented] Repository development practice: contributors should keep the product a thin wrapper around supported TUIs, avoiding hardcoded models and provider-specific features, and do feature work in an isolated git worktree. -- evidence: [AGENTS.md#L11-L17](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L11-L17), [AGENTS.md#L38-L41](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L38-L41) (`clm_4bb283606bcd897a87dc54c262f3e8ad737dbbb46739f2b0d5983c60f5b0a0e9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (7 claim(s))

- [observation/documented] Sessions show in one list with live status grouped into a foldable project tree; space sends a prompt into a session's pane or spawns a new agent in the selected group. -- evidence: [README.md#L40-L40](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L40-L40) (`clm_d0e1c445473e94ad7dd52287a8d331cb13fc22e1954e2638c03e4e0fec3556d0`)
- [observation/documented] ctrl+r opens a syntax-highlighted full-file diff of an agent's changes; line comments are sent back to the agent's pane as one review prompt when pressing C. -- evidence: [README.md#L40-L40](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L40-L40) (`clm_5479739fc7d94f57e46d707a9e8060d45143601a0c50fab5848071087b4cb7ee`)
- [observation/documented] Pressing f forks a session's conversation into a separate named fork, and v revives a dead session on its own conversation. -- evidence: [README.md#L40-L40](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L40-L40), [README.md#L42-L42](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L42-L42) (`clm_90676f13d7c01fc9ad34b332e004ca6cd2031884ca810c7ced91d94e1ba95bb6`)
- [observation/documented] Agent sessions run on a private tmux server named agentmgr with am_* session names, isolated from the user's own tmux; reachable via tmux -L agentmgr. -- evidence: [README.md#L84-L84](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L84-L84), [README.md#L82-L82](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L82-L82) (`clm_5846a60cef94e6c76f8226bbd4ce3b1e3372bb22730c3f45cd18ffad99b0622e`)
- [observation/documented] Keybindings are configurable via [keybindings.session] and [keybindings.list] tables in config.toml, with esc and ctrl+c kept fixed. -- evidence: [README.md#L82-L82](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L82-L82) (`clm_a129c3e2722c338e58a04205d72d293a5a9ffd7038dcb295461d01c8f3cb16a8`)
- [observation/documented] Sessions can spawn into their own git worktree under <repo>-worktrees/<name> on branch am/<name>, toggled on the new-session form or set as default in Settings. -- evidence: [README.md#L100-L100](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L100-L100) (`clm_41b3ab4699836279ba1617a58cbc12c7dbf7eb7b6082ebb5d5727e98d457026e`)
- [observation/documented] Status detection rules for the eight supported CLIs ship in the binary, so upgrades bring current launch, revive, fork, and status rules. -- evidence: [README.md#L52-L52](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L52-L52) (`clm_53343d20c7fd8c8bfb24b4790d6e52c440df2b136d40e299e16d0617dbd10b88`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] An agent can spawn another agent, send it a message, and wait until it is done; every MCP-capable session carries those tools on launch. -- evidence: [README.md#L44-L44](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L44-L44) (`clm_268e9cd23d33acdcad65fc800712eb26ea2e8cd488347aba211f67efb54e39dc`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The product depends on tmux (3.1+ per the install script) and git; the Homebrew tap installs tmux if missing, and the install script offers to install missing dependencies via the detected package manager. -- evidence: [README.md#L64-L64](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L64-L64), [README.md#L72-L72](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L72-L72) (`clm_cfcdb84c60a65d0822d02b5b5372e54fc3b218a91cb6559915dd26a93772bf6a`)
- [observation/documented] The tool runs on macOS and Linux, and on Windows inside WSL2. -- evidence: [README.md#L56-L56](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L56-L56) (`clm_1b49bc5398d6def9b474b252c6b7aaca31b5c5c8aff7e7740aa2653ce4572abf`)

## limitations (1 claim(s))

- [observation/documented] The README states cost tracking and mouse-driven list navigation are not yet implemented. -- evidence: [README.md#L46-L46](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L46-L46) (`clm_788cfa0229c15a90813cb802336b72edb9b39c8307aa6be60386d561e5e94b08`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

