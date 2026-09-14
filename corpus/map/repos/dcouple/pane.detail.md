# dcouple/pane -- full detail

[Back to orientation](pane.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dcouple/pane/df04c767aa669d953f9624a6f0a66782582522f4/8a95ecdbaaeaa09d.json](../../../wiki/dossiers/dcouple/pane/df04c767aa669d953f9624a6f0a66782582522f4/8a95ecdbaaeaa09d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Pane is organized around two primitives, panes and tabs: each pane maps to one git worktree and contains tabs for agents, diff viewer, file explorer, git tree, logs, and terminals, with state persisting across restarts. -- evidence: [README.md#L238-L238](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L238-L238) (`clm_c7af3eccfc8c92a0ca803a6dfc576558eb6be8513d0d535722e082589c434b7f`)

## design-choices (2 claim(s))

- [observation/documented] Pane is agent-agnostic: any CLI tool that runs in a terminal runs in Pane with no plugins or SDK, and the terminal serves as the integration layer rather than Pane re-implementing agent integrations. -- evidence: [README.md#L96-L96](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L96-L96), [README.md#L244-L244](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L244-L244), [README.md#L240-L240](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L240-L240) (`clm_a4bd14758a7bf54322fb755d5d22ae0651d62e668fa4bc4619d67e0fae377470`)
- [observation/documented] Each pane gets its own worktree, port range, and copy of secrets so parallel agents run in isolated workspaces without conflicts, and worktrees are created and torn down automatically with panes. -- evidence: [README.md#L408-L409](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L408-L409), [README.md#L405-L406](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L405-L406) (`clm_a25befdc414660e979bc5badb908b5291e055ca06ef9729566776cff10add709`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the repo is a pnpm workspace with main (Electron main process), frontend (React+Vite), shared types, and Playwright E2E tests; dev runs via pnpm dev and builds via pnpm build with per-platform build scripts. -- evidence: [AGENTS.md#L4-L8](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/AGENTS.md#L4-L8), [README.md#L430-L435](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L430-L435), [AGENTS.md#L11-L19](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/AGENTS.md#L11-L19) (`clm_8c5bb47af6e7b3492ba78d6c827748b5f1ace846e22c0598fcf8ef88fe6fba7b`)
- [observation/documented] Repository development practice: contributors use TypeScript with 2-space indentation, no explicit any (ESLint error level), kebab-case filenames, and must run pnpm lint and pnpm typecheck before sending PRs. -- evidence: [AGENTS.md#L22-L26](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/AGENTS.md#L22-L26) (`clm_11f482b0bb2b731d4b1a0a97c3e86eaed5d7d898e335a0928da73dc4ef2e9116`)
- [observation/documented] Repository development practice: releases must run from a clean main checkout matching origin/main, and the release script refuses inferred version bumps when package.json and the latest v* tag disagree. -- evidence: [README.md#L446-L446](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L446-L446) (`clm_a9cfd532ae77f0272b925dad463ab1f62399afb56b26edccc0277a3d7b51acfe`)

## skills-patterns (1 claim(s))

- [observation/documented] Pane Chat writes local orchestrator skills in Codex, Claude, and Cursor formats (e.g. .codex/skills/pane-orchestrator/SKILL.md) and caches workflow skills including discussion, plan, implement, implementation-reviewer, prepare-pr, investigate, and commit from a skills repository. -- evidence: [README.md#L209-L209](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L209-L209), [README.md#L203-L207](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L203-L207) (`clm_a99348a78adeda8dc4bbb32f102be40bd82432a5e1455f7e69faab91b5be0803`)

## interfaces (4 claim(s))

- [observation/documented] Pane ships a runpane CLI intended for agent use, including agent-context, repos add/list, and panes create for registering repositories and opening panes with prompts. -- evidence: [README.md#L221-L226](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L221-L226), [README.md#L118-L133](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L118-L133) (`clm_953539ff2cde46054f4272b9d404361d9515c7b05799c48a03b2b88526c5422e`)
- [observation/documented] runpane agent-context is token-efficient by default, printing only command names, arguments, and usage notes, with per-command detail available via --command and --json. -- evidence: [README.md#L228-L228](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L228-L228) (`clm_8aae6934a712130784ef6e59efaaec8bb223fc045c7269a8a962d95372d2ca48`)
- [observation/documented] The app defines keyboard shortcuts for command palette, new/archive pane, pane switching, settings, clipboard snippet pasting, and sidebar toggle. -- evidence: [README.md#L250-L261](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L250-L261) (`clm_5b00801cb771280446c82e5a18deb3a9bd7c87923703fda5ada4a0e422e67d66`)
- [observation/documented] Remote Pane is self-hosted: a host machine runs repos, terminals, git state, and agent credentials, and clients connect using a generated pane-remote:// code from desktop Pane or a browser app. -- evidence: [README.md#L139-L139](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L139-L139), [README.md#L143-L147](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L143-L147) (`clm_05997fc8dbac870a0d4f5d38c3b306c289dd6423d1988406dd14b6a4d0913e5f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running Pane requires Git in PATH and at least one AI coding agent CLI installed, with Claude Code, Codex, Cursor Agent, Aider, and Goose given as examples. -- evidence: [README.md#L324-L330](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L324-L330) (`clm_40aa2b24f48d0b8388e3adb62810f417e023026de607a01a988c0dc6be08855b`)

## limitations (1 claim(s))

- [observation/documented] Per the changelog, Cursor Agent is supported on macOS, Linux, and WSL repositories, while native Windows launches of Cursor remain disabled. -- evidence: [CHANGELOG.md#L8-L8](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/CHANGELOG.md#L8-L8) (`clm_7e3a9c194de0968e74fc32cba81ca4e098ee0d8876d91989a5c441f0b38b071e`)

## relevance (1 claim(s))

- [observation/documented] Pane targets developers on Windows, macOS, and Linux equally, multi-agent users of tools like Claude Code, Codex, Cursor, Aider, and Goose, and keyboard-driven teams needing a consistent workflow layer. -- evidence: [README.md#L363-L367](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L363-L367) (`clm_ca92bf79164ff68fe9762c5a6b1ea6c6e644d63e0fd6c847b5f11478ca68aea1`)

