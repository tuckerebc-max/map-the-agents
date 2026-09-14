# stablyai/orca

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5e70014da8ee @ c1b7154334419bff

## Summary (orientation draft, not independently verified)

Orca is a MIT-licensed desktop app for orchestrating CLI coding agents in parallel git worktrees, with terminal splits, embedded browser, SSH/remote worktrees, a mobile companion app, and a cloud relay in the repo; AGENTS.md adds contributor workflow rules.

## Source coverage

Source coverage (partial): 3 of 3 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Orca is a desktop application for running CLI coding agents such as Codex, Claude Code, OpenCode, or Pi side-by-side, each in its own worktree and tracked in one place. -- evidence: [README.md#L18-L21](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L18-L21)
- components (4 claim(s)):
  - [observation/documented] The app includes a terminal feature with WebGL rendering, infinite splits, and scrollback that persists across restarts. -- evidence: [README.md#L65-L65](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L65-L65)
  - [observation/documented] Design Mode lets users click a UI element in an embedded Chromium window to inject its HTML, CSS, and a cropped screenshot into an agent prompt. -- evidence: [README.md#L79-L79](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L79-L79)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: contributors verify changes with `pnpm tc` for typecheck, `pnpm test` for tests, and `oxlint`/`pnpm format` for linting and formatting. -- evidence: [AGENTS.md#L46-L48](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L46-L48)
  - [observation/documented] Repository development practice: Electron UI validation must run in the background with `ORCA_BACKGROUND_LAUNCH=1`, never stealing focus, using Playwright CDP screenshots of hidden renderers. -- evidence: [AGENTS.md#L13-L13](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L13-L13), [AGENTS.md#L7-L11](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/AGENTS.md#L7-L11)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships desktop builds for macOS (Apple Silicon and Intel), Windows, and Linux, plus a mobile companion app for iOS and Android. -- evidence: [README.md#L214-L216](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L214-L216), [README.md#L5-L12](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L5-L12), [README.md#L232-L233](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L232-L233)
  - [observation/documented] An Orca CLI exposes commands like `orca worktree create`, `snapshot`, `click`, and `fill`, letting agents script Orca workflows. -- evidence: [README.md#L149-L149](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L149-L149)
- memory-state (1 claim(s)):
  - [observation/documented] A mobile companion app pairs with the desktop host to monitor and steer agents remotely, with finish notifications and follow-ups from the phone. -- evidence: [README.md#L230-L230](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L230-L230), [README.md#L37-L37](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L37-L37)
- orchestration (1 claim(s)):
  - [observation/documented] A single prompt can be fanned out across multiple agents, each in an isolated git worktree, so results can be compared and the winner merged. -- evidence: [README.md#L51-L51](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L51-L51)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The repository includes a cloud relay under `cloud/` that pairs the mobile app with a desktop host, maintained as a separate pnpm workspace. -- evidence: [README.md#L255-L256](https://github.com/stablyai/orca/blob/5e70014da8ee6aa6635fe4f031baa7dbaca17231/README.md#L255-L256)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](orca.detail.md)

Metadata and full claim list: [full detail](orca.detail.md)
Human notes ([notes](orca.notes.md), never overwritten by build)

[Back to map index](../../index.md)
