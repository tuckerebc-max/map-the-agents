# hanshuaikang/nezha

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8b1068a87cf2 @ c72eaaf9de1ac3a9

## Summary (orientation draft, not independently verified)

Nezha is a cross-platform lightweight IDE built for AI programming, integrating native Claude Code and Codex sessions in a built-in terminal alongside task tracking, Git, and an editor. The project credits Tauri, React, xterm.js, and Material Icon Theme as open-source projects it depends on.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: development uses pnpm commands — dev (Vite on port 1420), build (tsc + Vite), lint (ESLint), test (Vitest), and tauri dev/build for the desktop app. -- evidence: [AGENTS.md#L13-L20](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/AGENTS.md#L13-L20)
  - [observation/documented] Repository development practice: contributions are issue-first — a GitHub issue must be approved by a maintainer before opening a PR, with narrow exceptions like typos and one-to-two-line bug fixes. -- evidence: [AGENTS.md#L303-L306](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/AGENTS.md#L303-L306), [AGENTS.md#L293-L293](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/AGENTS.md#L293-L293)
- skills-patterns (1 claim(s)):
  - [observation/documented] The app supports skill management, letting users centrally manage local skills via symlinks. -- evidence: [README.md#L61-L67](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/README.md#L61-L67)
- interfaces (1 claim(s)):
  - [observation/documented] Nezha is a cross-platform lightweight IDE built for AI programming, integrating native Claude Code and Codex sessions in a built-in terminal alongside task tracking, Git, and an editor. -- evidence: [README.md#L41-L41](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/README.md#L41-L41), [README.md#L50-L50](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/README.md#L50-L50)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project credits Tauri, React, xterm.js, and Material Icon Theme as open-source projects it depends on. -- evidence: [README.md#L121-L124](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/README.md#L121-L124)
- limitations (1 claim(s)):
  - [observation/documented] The macOS installer is unsigned, so first launch triggers a Gatekeeper 'damaged' warning; the documented workaround is removing the quarantine attribute via xattr. -- evidence: [README.md#L54-L54](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/README.md#L54-L54), [README.md#L56-L58](https://github.com/hanshuaikang/nezha/blob/8b1068a87cf2a3a13785d1698291b9e3e6b7c4e9/README.md#L56-L58)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](nezha.detail.md).

Metadata and full claim list: [full detail](nezha.detail.md)
Human notes ([notes](nezha.notes.md), never overwritten by build)

[Back to map index](../../index.md)
