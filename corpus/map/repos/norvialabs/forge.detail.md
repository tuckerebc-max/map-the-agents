# norvialabs/forge -- full detail

[Back to orientation](forge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/norvialabs/forge/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/d8ce37fcadf8e938.json](../../../wiki/dossiers/norvialabs/forge/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/d8ce37fcadf8e938.json)

## specifications (2 claim(s))

- [observation/documented] Forge is an open-source terminal coding environment for working with AI agents, combining agent conversations, file explorer, Vim-style editing, shell, diffs, approvals, and multiple durable sessions in one keyboard-driven TUI. -- evidence: [README.md#L13-L16](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L13-L16) (`clm_8f9e074f5905c940945bf1c2385b5fd1eb77dab5fd165bb7fb7c49bf543e6a43`)
- [observation/documented] The project describes itself as alpha software and advises reviewing every approval prompt and using it first in a disposable or backed-up repository. -- evidence: [README.md#L23-L24](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L23-L24) (`clm_e8b1ab54a7767968ef7d016dd5901c93c862096a3aa551c5868fc04edd750dc2`)

## components (1 claim(s))

- [observation/documented] Forge is a Rust workspace whose main crates include forge-cli (entry point), forge-tui (terminal interface), forge-core (agent loop and session lifecycle), forge-model, forge-connect, forge-tools, and forge-durable (SQLite journals). -- evidence: [README.md#L597-L603](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L597-L603), [README.md#L595-L595](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L595-L595) (`clm_44790f6e238d6f684721058537202ab184ad2ca2faae0c54a5402860211a23df`)

## design-choices (2 claim(s))

- [observation/documented] Colours are semantic tokens defined per theme rather than fixed hex values, and the design system names ACCENT_STATUS_MIN_HUE_DISTANCE as its single hardest rule, asserted over built-in themes in tests. -- evidence: [FORGE-DESIGN.md#L208-L208](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/FORGE-DESIGN.md#L208-L208), [FORGE-DESIGN.md#L171-L171](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/FORGE-DESIGN.md#L171-L171) (`clm_066e542d2001fc7243fb5864bd33c099e22e6736f4e36f596d3fe680e8dab508`)
- [observation/documented] Core UX invariants include exactly one effective keyboard owner at a time, colour never being the sole state indicator, approvals and failures outranking routine activity, and refusing to render below an enforced minimum of 80x18. -- evidence: [FORGE-DESIGN.md#L157-L167](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/FORGE-DESIGN.md#L157-L167) (`clm_8f1cbf5530a23deda01537e2cedf676823793c19414529ea1dde1db0fdacd123`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are told to run cargo fmt --check, cargo clippy with -D warnings, and cargo test --workspace before submitting a change, with further guidance in CONTRIBUTING.md. -- evidence: [README.md#L607-L611](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L607-L611), [README.md#L605-L605](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L605-L605), [README.md#L613-L613](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L613-L613) (`clm_329d4d587ab06c1de9527723944f91bdebdb923df166e7c19d052cd93396dcb3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The TUI exposes in-app slash commands such as /connect, /model, /resume, /continue, /fork, /compact, /terminal, /theme, /effort, /thinking, /status, and /quit. -- evidence: [README.md#L173-L192](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L173-L192) (`clm_3a49fbf0a2901f77043dfa1125fb220fa55b3e5dde68153e2d4e45de5c5b33cd`)
- [observation/documented] Documented CLI forms include bare `forge`, `forge --continue`, `forge --resume [<session-id>]`, and `forge --fork <session-id>`; the default workspace is the current directory, overridable via FORGE_WORKSPACE. -- evidence: [README.md#L194-L196](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L194-L196), [README.md#L560-L566](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L560-L566), [README.md#L114-L115](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L114-L115), [README.md#L548-L550](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L548-L550), [README.md#L552-L553](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L552-L553), [README.md#L555-L558](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L555-L558), [README.md#L110-L112](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L110-L112) (`clm_9e3af8244a399c9f3eb7c4ea4dbfed9c3a92356209e70f61777d686269145c48`)
- [observation/documented] A frontend-independent `forge bench` entry point accepts a piped prompt with flags like --workspace, --journal, --model, --route-id, --effort, and --approve-all, emitting one JSON response on stdout and logs on stderr. -- evidence: [README.md#L125-L127](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L125-L127), [README.md#L129-L138](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L129-L138), [README.md#L140-L142](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L140-L142) (`clm_67640a0e890da21b03556ddc5384e06873f35d807db5ddd49ce0d9cd099f667f`)
- [observation/documented] Configuration is layered from defaults, a user config file, a forge.toml in the working directory, and environment variables, with environment variables overriding file configuration; MCP servers are configured in trusted user config or explicitly managed configuration. -- evidence: [README.md#L325-L326](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L325-L326), [README.md#L254-L256](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L254-L256) (`clm_258d1f7c307c6485d625c5e905f073f8ded7623b61fa492ac3a4ed1acefff646`)

## memory-state (1 claim(s))

- [observation/documented] Sessions preserve transcripts, task state, queued follow-ups, and unfinished work in a local SQLite journal so they survive process restarts; each managed session has its own durable state and isolated linked Git worktree. -- evidence: [README.md#L18-L21](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L18-L21), [README.md#L536-L540](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L536-L540), [README.md#L40-L54](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L40-L54) (`clm_a2ade14295af315d95c6976d9acaad90f58486b83c2d96147f32573119c9ee4c`)

## orchestration (1 claim(s))

- [observation/documented] Agent orchestration is enabled by default: the model can spawn child agents via spawn_agent, send_message, followup_task, wait_agent, list_agents, and interrupt_agent; children run in isolated worktrees, inherit parent model/governance/policy, and can be tool-narrowed with tool_allowlist. -- evidence: [README.md#L278-L282](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L278-L282) (`clm_00f42cfcc0b379883aaaeecde4e70528988009e3f419d37b2d9b0dcf0bd2396c`)

## tools-permissions (3 claim(s))

- [observation/documented] Agent shell commands run under an OS sandbox (Seatbelt on macOS, bubblewrap on Linux, WSL2's Linux sandbox on Windows) confined to the workspace, with network egress denied by default and opened only through explicit host rules via a filtering proxy. -- evidence: [README.md#L18-L21](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L18-L21), [README.md#L424-L428](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L424-L428), [README.md#L430-L433](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L430-L433), [README.md#L348-L352](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L348-L352), [README.md#L40-L54](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L40-L54) (`clm_fb4701a399e7d8cd1af279124588feefdbf202127eb9d51b4e6f8a65f6ea989e`)
- [observation/documented] There is no permission-mode setting: shell commands and file writes run unprompted with the sandbox as the boundary, MCP tools still prompt, and a deny pattern re-prompts even for shell; ACL denies are hard blocks. -- evidence: [README.md#L498-L502](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L498-L502) (`clm_36ad4581810a9b3ba367fe9537726bf8263a1b1a873ee7a1830e6ac5b7ed8d6c`)
- [observation/documented] Permission rules come from a personal permissions.toml and a workspace .forge/permissions.toml; the repo-committed file's allow entries are ignored while its deny entries are always honored, so a checked-out repo cannot widen its own blast radius. -- evidence: [README.md#L461-L466](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L461-L466) (`clm_575f64b10a34fc4f795dc20341257980e7b8276348252b4a6c946d9ca189e831`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] On Linux the installer installs the sandbox dependencies bubblewrap and socat if missing (supporting apt, dnf, yum, pacman, zypper, apk); macOS needs nothing extra, and building from source requires Git and Rust 1.97.1 or newer. -- evidence: [README.md#L91-L91](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L91-L91), [README.md#L83-L83](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L83-L83), [README.md#L77-L81](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L77-L81) (`clm_59070727be783aac589a7d99229d4f6816f4a4d4b8ddaeaf9f8019347bd29880`)
- [observation/documented] Forge ships native provider routes for OpenAI, Anthropic, xAI Grok (OAuth), OpenAI Codex subscriptions, OpenCode Go, OpenCode Zen, and local Ollama, configured via API-key environment variables or /connect. -- evidence: [README.md#L167-L169](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L167-L169), [README.md#L148-L154](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L148-L154), [README.md#L164-L165](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L164-L165) (`clm_2bd9adf3c6409ae8bbc9a0427adb94f8964331ed8a290cb59f5fa2717ffc2f3e`)

## limitations (3 claim(s))

- [observation/documented] There is no native Windows build; Forge runs under WSL2 using the Linux sandbox, and the PowerShell installer detects WSL2 and points to the Linux installer. -- evidence: [README.md#L85-L87](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L85-L87) (`clm_8dabe99f628269fcc9df8fd081fbbc9fa831e954d274b63a42a533887f568276`)
- [observation/documented] The README documents a residual Linux sandbox gap: read-only mounts do not stop Unix socket connections, so sockets under /var or /opt remain reachable despite masking of /run, /tmp, and home trees; tracked in issue #392. -- evidence: [README.md#L404-L416](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L404-L416) (`clm_4c0151c114a9c6cff8e06e509deccdc9d39182f24734c4ffb908c25ee3ef9533`)
- [observation/documented] If the OS cannot confine (e.g. bubblewrap missing or unsupported platform), Forge refuses to start, printing the reason on stderr; there is no setting that turns oversight off without an enforcement floor. -- evidence: [README.md#L418-L420](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L418-L420) (`clm_d86aed90dcb22d75feb37762f854c5875bdb35d1aa2c0371bab5e645679b7263`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

