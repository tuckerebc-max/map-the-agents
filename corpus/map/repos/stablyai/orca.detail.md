# stablyai/orca -- full detail

[Back to orientation](orca.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stablyai/orca/5e70014da8ee6aa6635fe4f031baa7dbaca17231/c1b7154334419bff.json](../../../wiki/dossiers/stablyai/orca/5e70014da8ee6aa6635fe4f031baa7dbaca17231/c1b7154334419bff.json)

## specifications (1 claim(s))

- [observation/documented] Orca is a desktop application for running CLI coding agents such as Codex, Claude Code, OpenCode, or Pi side-by-side, each in its own worktree and tracked in one place. -- evidence: [README.md#L18-L21](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L18-L21) (`clm_bb20dfae8e7cad11ae02d98cddf96e0600431d182f9192082f25bb9424cc7e37`)

## components (4 claim(s))

- [observation/documented] The app includes a terminal feature with WebGL rendering, infinite splits, and scrollback that persists across restarts. -- evidence: [README.md#L65-L65](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L65-L65) (`clm_ac2ef3e6c578df5114edf5d7de47b429eb7c3ad17f9c572c1dcc46a51a487777`)
- [observation/documented] Design Mode lets users click a UI element in an embedded Chromium window to inject its HTML, CSS, and a cropped screenshot into an agent prompt. -- evidence: [README.md#L79-L79](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L79-L79) (`clm_bc2947b9664d981457989bf1ff3ea52d0fe606b29afd91a0e0a6b3640df27b57`)
- [observation/documented] The product supports running agents on remote machines over SSH with file editing, git, terminals, auto-reconnect, and port forwarding. -- evidence: [README.md#L107-L107](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L107-L107) (`clm_bfe8027576c7bf2257c2c76969a76c4e534a25b82d40730c1b115d2af16ec101`)
- [observation/documented] Users can browse PRs, issues, and project boards in-app, open worktrees from tasks, and comment on diff lines to send feedback back to the agent. -- evidence: [README.md#L93-L93](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L93-L93), [README.md#L121-L121](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L121-L121) (`clm_cdb8346deacf9660035b85392158964049c1a61365b179702725e2acfacd32ff`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: contributors verify changes with `pnpm tc` for typecheck, `pnpm test` for tests, and `oxlint`/`pnpm format` for linting and formatting. -- evidence: [AGENTS.md#L46-L48](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L46-L48) (`clm_dd495ee73575222164a5465aa69fb5d62f5cbc00444ef1bb2ec538a6b1c62b82`)
- [observation/documented] Repository development practice: Electron UI validation must run in the background with `ORCA_BACKGROUND_LAUNCH=1`, never stealing focus, using Playwright CDP screenshots of hidden renderers. -- evidence: [AGENTS.md#L13-L13](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L13-L13), [AGENTS.md#L7-L11](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L7-L11) (`clm_ac0c2ba60dfafe95f8372893349d29d0a6e090be07db5d2227fa0f09048577e4`)
- [observation/documented] Repository development practice: UI work must follow docs/STYLEGUIDE.md and use design tokens from main.css and shadcn primitives rather than inventing new values. -- evidence: [AGENTS.md#L3-L3](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L3-L3) (`clm_ca9c5340e6ecf263a0e20d5af8ce199e01b53448d272ddc5c24161d3a657ff12`)
- [observation/documented] Repository development practice: platform-dependent behavior must stay behind runtime checks, and Windows child processes must go through the shared runProcess/spawnProcess helpers instead of child_process directly. -- evidence: [AGENTS.md#L60-L69](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L60-L69), [AGENTS.md#L58-L58](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L58-L58) (`clm_357df3b7ab4931c8a2305858f58799e08c2338ae484e71c57b43bf92be6d27db`)
- [observation/documented] Repository development practice: Git 2.25 is treated as the core-workflow compatibility baseline, with capability caching scoped per executing host (native, WSL, SSH, or relay). -- evidence: [AGENTS.md#L97-L97](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L97-L97), [AGENTS.md#L101-L105](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L101-L105) (`clm_57b460e4b5b660c40632f715be93c0532145751a6642d555a7b00da8370c08a6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product ships desktop builds for macOS (Apple Silicon and Intel), Windows, and Linux, plus a mobile companion app for iOS and Android. -- evidence: [README.md#L214-L216](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L214-L216), [README.md#L5-L12](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L5-L12), [README.md#L232-L233](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L232-L233) (`clm_202925405175482401d26c14910da83c83b5d9d6921152fe462526c188aad900`)
- [observation/documented] An Orca CLI exposes commands like `orca worktree create`, `snapshot`, `click`, and `fill`, letting agents script Orca workflows. -- evidence: [README.md#L149-L149](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L149-L149) (`clm_63241f563ba2077441309619b30f724808f5dbcef9ce1c10d85a1747fc1b88a2`)

## memory-state (1 claim(s))

- [observation/documented] A mobile companion app pairs with the desktop host to monitor and steer agents remotely, with finish notifications and follow-ups from the phone. -- evidence: [README.md#L230-L230](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L230-L230), [README.md#L37-L37](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L37-L37) (`clm_c65beb4d2aa3a8a57c0e159fe83a9dee3ab5fbb506ff34838e793e44804c4709`)

## orchestration (1 claim(s))

- [observation/documented] A single prompt can be fanned out across multiple agents, each in an isolated git worktree, so results can be compared and the winner merged. -- evidence: [README.md#L51-L51](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L51-L51) (`clm_37cde1738016188a58e90000d89ed709edc933d541f2f655489b75a1c5e5d684`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The repository includes a cloud relay under `cloud/` that pairs the mobile app with a desktop host, maintained as a separate pnpm workspace. -- evidence: [README.md#L255-L256](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L255-L256) (`clm_9e76aed561c8db06169722ad9987bd090486ca18b9e7d6711967d0d2fcab9af4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

