# electric-sql/electric -- full detail

[Back to orientation](electric.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/electric-sql/electric/bb397424db0e1c153dc356713fd3dfd40315470c/9b3c832516e6f8b7.json](../../../wiki/dossiers/electric-sql/electric/bb397424db0e1c153dc356713fd3dfd40315470c/9b3c832516e6f8b7.json)

## specifications (2 claim(s))

- [observation/documented] A plan proposes a desktop app package at packages/agents-desktop that reuses the existing agents-server-ui React app and adds local desktop functionality. -- evidence: [AGENTS_DESKTOP_PLAN.md#L5-L6](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L5-L6) (`clm_ced2ba0d1b7ac9a5411f13caf20f3de9955a52be0658da7fea85f98e0df1a470`)
- [observation/documented] The planned desktop v1 would not bundle an Agents server, Postgres, or Electric; it would run the local builtin agents runtime from @electric-ax/agents while connecting to an external Agents server. -- evidence: [AGENTS_DESKTOP_PLAN.md#L8-L11](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L8-L11), [AGENTS_DESKTOP_PLAN.md#L46-L50](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L46-L50) (`clm_4296e2a763e85f3aba1fef7e0bc28b46d17424ee44e1277d59e2cb35704b5de6`)

## components (1 claim(s))

- [observation/documented] The proposed package structure includes Electron main.ts and preload.ts, a Vite config, and tray icon assets, with dependencies on @electric-ax/agents-server-ui, @electric-ax/agents, and electron. -- evidence: [AGENTS_DESKTOP_PLAN.md#L90-L93](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L90-L93), [AGENTS_DESKTOP_PLAN.md#L74-L86](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L74-L86) (`clm_6b8542cefdc23e81ff1418141701345d9aaa846fc817f996ddcc9dde4c05260d`)

## design-choices (3 claim(s))

- [observation/documented] The planned desktop app is both a windowed Agents UI and a background runtime indicator/controller, with a macOS menu bar icon and tray/status icons on Windows and Linux. -- evidence: [AGENTS_DESKTOP_PLAN.md#L17-L18](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L17-L18), [AGENTS_DESKTOP_PLAN.md#L20-L21](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L20-L21) (`clm_a44fb2a56ef973a1ca42ddf652a19303b597796a2392663489e648f3d0981fd4`)
- [observation/documented] The plan specifies that closing the last window should not stop the local runtime, while explicitly quitting the app should; the tray should indicate runtime states of starting, running, error, or stopped. -- evidence: [AGENTS_DESKTOP_PLAN.md#L161-L164](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L161-L164), [AGENTS_DESKTOP_PLAN.md#L27-L28](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L27-L28) (`clm_1141b7548e7f9db256ffb86fa792cdd5912354488ad4e62ecb970af808f1c72c`)
- [observation/documented] The plan proposes starting BuiltinAgentsServer with host 127.0.0.1 and port 0 so the OS picks a free port, restarting the runtime when the active Agents server changes, and noting that remote servers cannot reach the local callback URL without a later tunnel/relay design. -- evidence: [AGENTS_DESKTOP_PLAN.md#L154-L155](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L154-L155), [AGENTS_DESKTOP_PLAN.md#L65-L68](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L65-L68), [AGENTS_DESKTOP_PLAN.md#L151-L152](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L151-L152), [AGENTS_DESKTOP_PLAN.md#L141-L146](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L141-L146) (`clm_95a8d26c94dc255601eb1098325ad2677ce1fc81bcc5aace8a3eff7438ba9b89`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: authenticated EAS builds will not run on untrusted fork PRs because GitHub does not expose secrets to them; forks get local checks while EAS builds run for same-repo or trusted labeled PRs. -- evidence: [AGENTS_MOBILE_CI_RELEASE_PLAN.md#L41-L44](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_MOBILE_CI_RELEASE_PLAN.md#L41-L44) (`clm_35d45516006b4b57f93bee8454fe1ceb94d9509b35cb552a83295a9e984e8676`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A planned preload API extends window.electronAPI with methods such as getServers, saveServers, getDesktopState, setActiveServer, restartRuntime, stopRuntime, and onDesktopStateChanged, exposing a DesktopState with runtimeStatus, runtimeUrl, activeServer, workingDirectory, and error fields. -- evidence: [AGENTS_DESKTOP_PLAN.md#L218-L221](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L218-L221), [AGENTS_DESKTOP_PLAN.md#L235-L242](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L235-L242), [AGENTS_DESKTOP_PLAN.md#L223-L224](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L223-L224), [AGENTS_DESKTOP_PLAN.md#L226-L228](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L226-L228), [AGENTS_DESKTOP_PLAN.md#L213-L216](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L213-L216) (`clm_3392f10cd9c30fc485ecf2e49d0b7856743def29b38fdc85d0d2d1d4441cc4a9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The mobile package @electric-ax/agents-mobile is described as an existing Expo SDK 54 app using Expo Router, React Native, and Expo DOM Components to embed agents-server-ui surfaces. -- evidence: [AGENTS_MOBILE_CI_RELEASE_PLAN.md#L15-L15](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_MOBILE_CI_RELEASE_PLAN.md#L15-L15) (`clm_a370a49cb525c91b4b180a5e73aaefa7c1c9d4a682dff74cb60829bec65d3954`)
- [observation/documented] The mobile plan records that react, react-dom, react-native-webview, and TypeScript versions were aligned across the mobile/server-ui/runtime graph so expo-doctor passes 18/18 checks. -- evidence: [AGENTS_MOBILE_CI_RELEASE_PLAN.md#L41-L44](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_MOBILE_CI_RELEASE_PLAN.md#L41-L44), [AGENTS_MOBILE_CI_RELEASE_PLAN.md#L277-L280](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_MOBILE_CI_RELEASE_PLAN.md#L277-L280) (`clm_5f51c880e86028c70ab1910e4e2f97963585cad0bfc4a5b351e12f44ab303fd0`)

## limitations (1 claim(s))

- [observation/documented] The desktop plan explicitly marks remote callback tunnelling, bundling the Agents server, Postgres, Electric, and auto-update/signing polish as out of scope for v1. -- evidence: [AGENTS_DESKTOP_PLAN.md#L46-L50](https://github.com/electric-sql/electric/blob/bb397424db0e1c153dc356713fd3dfd40315470c/AGENTS_DESKTOP_PLAN.md#L46-L50) (`clm_729bbadb3cf070715c7a3d280eba3dca3c2c0894ba072596ecbb13c6a500e971`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

