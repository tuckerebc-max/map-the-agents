# construct-worlds/construct -- full detail

[Back to orientation](construct.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/construct-worlds/construct/cf75b7398c784566b7003d7f63253be1b88d9186/c959755ce3b13c69.json](../../../wiki/dossiers/construct-worlds/construct/cf75b7398c784566b7003d7f63253be1b88d9186/c959755ce3b13c69.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Construct is a single Rust binary that includes a TUI, control CLI, daemon, ACP stdio server, an internal MCP bridge, and harness adapters. -- evidence: [README.md#L1-L11](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L1-L11), [README.md#L197-L200](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L197-L200) (`clm_58973e8fe85ab373e8755372f95391b1ac06356fb2abea79894a7de474fb6a4a`)
- [observation/documented] The daemon owns sessions, persists state, and exposes the local IPC socket used by clients; lifecycle helpers include daemon start/stop/restart with session-safe stop variants. -- evidence: [README.md#L143-L149](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L143-L149), [README.md#L140-L141](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L140-L141) (`clm_3ffc63cbc0879acdda1390af2392c9e6e1b71bf70bc50be7b539ca1d18fd655e`)
- [observation/documented] Running `construct` auto-starts a background daemon and attaches if none is running; this can be disabled with CONSTRUCT_NO_AUTOSTART=1. -- evidence: [README.md#L104-L106](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L104-L106) (`clm_fc9074d29ede2832838747342a54e50e667e6b6505a9de115bab1a05c57661bd`)

## design-choices (2 claim(s))

- [observation/documented] Sessions live in the daemon rather than the terminal, so SSH drops or laptop sleep do not stop agents, and users can reattach with scrollback intact. -- evidence: [README.md#L25-L32](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L25-L32) (`clm_161bcf4eddb511af5b2f7ff00ae51ed2c69e4692e7f4292ab68abd5b64b771ab`)
- [observation/documented] Lineage lets sessions branch like ideas: a session can be forked for a parallel attempt, including cross-harness forks, and results merged back. -- evidence: [README.md#L25-L32](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L25-L32) (`clm_127af993f42400a88dd4141a77e2e2c5e02f31dad4eed105f7fe14e6e3dcd847`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: all code changes go through a branch, git worktree under .claude/worktrees, and a PR, with no direct pushes to main and no Co-Authored-By: Claude trailers. -- evidence: [AGENTS.md#L5-L5](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L5-L5), [AGENTS.md#L7-L18](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L7-L18) (`clm_99974a2a443b6b6850c621fc6d6f9fb06f9e4d2eaae7bfa6339ae7b264581f50`)
- [observation/documented] Repository development practice: durable design decisions are recorded as focused spec files in specs/ named NNNN-title-kebab-case.md with status, date, area, scope, decision, reason, and consequences sections. -- evidence: [AGENTS.md#L117-L120](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L117-L120), [AGENTS.md#L106-L110](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L106-L110), [AGENTS.md#L104-L104](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L104-L104) (`clm_8a5e62f4808b3113dc67e6a6075c4fa9f7ad9d2deaad9917c09277b780015fd2`)
- [observation/documented] Repository development practice: TUI demo clips are recorded deterministically with vhs against isolated per-recording daemon state directories, then verified with a midpoint frame before attaching to the PR. -- evidence: [AGENTS.md#L88-L90](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L88-L90), [AGENTS.md#L24-L34](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L24-L34), [AGENTS.md#L22-L22](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L22-L22) (`clm_296548d6b664097c80f0efa5d78661e0d361c1ec3a7ccf9f814c56a2429c03af`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The harness adapter protocol uses separate adapter processes speaking JSON-RPC over stdio, so new tools can plug in without changing the daemon. -- evidence: [README.md#L57-L59](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L57-L59) (`clm_4d9c60a321fbb971b5ef835cfab111699ffb331093beebdc2ad24b6dccb01067`)
- [observation/documented] `construct acp` runs an Agent Client Protocol stdio server that auto-starts the daemon if needed and maps ACP session lifecycle calls onto daemon sessions, with --harness/--model/--cwd defaults. -- evidence: [README.md#L176-L177](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L176-L177), [README.md#L183-L185](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L183-L185) (`clm_c8120fae9c74cc2c013fd43d002e3f8705a2e2fa1653f571606615604cd03424`)
- [observation/documented] Every session gets construct's MCP tools, letting any harness spawn subagents, send them input, and read their output for agent-to-agent orchestration. -- evidence: [README.md#L39-L50](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L39-L50) (`clm_017faa0cbaaf43ee23a1d3ec997a9dfb42a1d566b7437d275029ac48a5b64949`)
- [observation/documented] The TUI supports `?` for help and `M-x` for a command palette, and users can create sessions, switch agents, send input, inspect diffs, and interrupt work from it. -- evidence: [README.md#L108-L110](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L108-L110) (`clm_f781504c28d792a98b1db39c555896954a53e7c1415b1f8ae0f0e1642040448f`)
- [observation/documented] `/remote-control` opens a browser-accessible web client with a QR code so users can connect from a phone without service signup or setup. -- evidence: [README.md#L52-L55](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L52-L55) (`clm_1eca237c3520f8342d800282c4ad374bc38ecc2dcb9c110ec69fa8c2f95fcd42`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Construct wraps CLIs already on the machine; users must install and authenticate harnesses such as codex, claude, opencode, agy, grok, muse, and prime-agent, while smith is built in. -- evidence: [README.md#L69-L81](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L69-L81), [README.md#L65-L67](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L65-L67) (`clm_02011da69bbf74c81888bbae3faca43846633aa9a8c78a4f06a1e71fb4cdc6c2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

