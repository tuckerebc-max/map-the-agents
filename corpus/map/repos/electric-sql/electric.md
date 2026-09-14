# electric-sql/electric

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bb397424db0e @ 9b3c832516e6f8b7

## Summary (orientation draft, not independently verified)

Selected evidence records: A plan proposes a desktop app package at packages/agents-desktop that reuses the existing agents-server-ui React app and adds local desktop functionality. The planned desktop v1 would not bundle an Agents server, Postgres, or Electric; it would run the local builtin agents runtime from @electric-ax/agents while connecting to an external Agents server.

## Source coverage

Source coverage (partial): 6 of 120 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] A plan proposes a desktop app package at packages/agents-desktop that reuses the existing agents-server-ui React app and adds local desktop functionality. -- evidence: [AGENTS_DESKTOP_PLAN.md#L5-L6](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L5-L6)
  - [observation/documented] The planned desktop v1 would not bundle an Agents server, Postgres, or Electric; it would run the local builtin agents runtime from @electric-ax/agents while connecting to an external Agents server. -- evidence: [AGENTS_DESKTOP_PLAN.md#L8-L11](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L8-L11), [AGENTS_DESKTOP_PLAN.md#L46-L50](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L46-L50)
- components (1 claim(s)):
  - [observation/documented] The proposed package structure includes Electron main.ts and preload.ts, a Vite config, and tray icon assets, with dependencies on @electric-ax/agents-server-ui, @electric-ax/agents, and electron. -- evidence: [AGENTS_DESKTOP_PLAN.md#L90-L93](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L90-L93), [AGENTS_DESKTOP_PLAN.md#L74-L86](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L74-L86)
- design-choices (3 claim(s)):
  - [observation/documented] The planned desktop app is both a windowed Agents UI and a background runtime indicator/controller, with a macOS menu bar icon and tray/status icons on Windows and Linux. -- evidence: [AGENTS_DESKTOP_PLAN.md#L17-L18](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L17-L18), [AGENTS_DESKTOP_PLAN.md#L20-L21](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L20-L21)
  - [observation/documented] The plan specifies that closing the last window should not stop the local runtime, while explicitly quitting the app should; the tray should indicate runtime states of starting, running, error, or stopped. -- evidence: [AGENTS_DESKTOP_PLAN.md#L161-L164](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L161-L164), [AGENTS_DESKTOP_PLAN.md#L27-L28](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L27-L28)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: authenticated EAS builds will not run on untrusted fork PRs because GitHub does not expose secrets to them; forks get local checks while EAS builds run for same-repo or trusted labeled PRs. -- evidence: [AGENTS_MOBILE_CI_RELEASE_PLAN.md#L41-L44](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_MOBILE_CI_RELEASE_PLAN.md#L41-L44)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A planned preload API extends window.electronAPI with methods such as getServers, saveServers, getDesktopState, setActiveServer, restartRuntime, stopRuntime, and onDesktopStateChanged, exposing a DesktopState with runtimeStatus, runtimeUrl, activeServer, workingDirectory, and error fields. -- evidence: [AGENTS_DESKTOP_PLAN.md#L218-L221](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L218-L221), [AGENTS_DESKTOP_PLAN.md#L235-L242](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L235-L242), [AGENTS_DESKTOP_PLAN.md#L223-L224](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L223-L224), [AGENTS_DESKTOP_PLAN.md#L226-L228](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L226-L228), [AGENTS_DESKTOP_PLAN.md#L213-L216](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L213-L216)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The mobile package @electric-ax/agents-mobile is described as an existing Expo SDK 54 app using Expo Router, React Native, and Expo DOM Components to embed agents-server-ui surfaces. -- evidence: [AGENTS_MOBILE_CI_RELEASE_PLAN.md#L15-L15](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_MOBILE_CI_RELEASE_PLAN.md#L15-L15)
More evidence: [full detail](electric.detail.md)

Metadata and full claim list: [full detail](electric.detail.md)
Human notes ([notes](electric.notes.md), never overwritten by build)

[Back to map index](../../index.md)
