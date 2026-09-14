# johannesjo/parallel-code -- full detail

[Back to orientation](parallel-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/johannesjo/parallel-code/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/77106abc8209e886.json](../../../wiki/dossiers/johannesjo/parallel-code/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/77106abc8209e886.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The app is an Electron desktop application with a SolidJS frontend and Node.js backend, published for macOS and Linux only. -- evidence: [CLAUDE.md#L3-L3](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/CLAUDE.md#L3-L3), [README.md#L20-L26](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L20-L26) (`clm_283576c4aa8f14915a2a84d12289afef600dc423f21f68aa9b94a2a677f82b7d`)
- [observation/documented] Features include a built-in diff viewer with inline comments, per-task notes and canvas panels, per-task shell terminals, and an AI Arena head-to-head mode. -- evidence: [README.md#L40-L44](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L40-L44), [README.md#L82-L98](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L82-L98) (`clm_72f59418d199e11afc95b9ca72f1a26ebc2309470764767d0ea2cad599b6df73`)

## design-choices (1 claim(s))

- [observation/documented] Docker sandboxing is supported via a project-specific Dockerfile placed at .parallel-code/Dockerfile, in which tasks then run. -- evidence: [README.md#L82-L98](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L82-L98), [PRIVACY.md#L97-L99](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L97-L99) (`clm_f300bb4f3514101b80124c4876dabc1cc6bbf57cbb6bf4929dd17a5db7e43c56`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: build from source with git clone, npm install, and npm run dev, requiring Node.js v18+; npm run typecheck runs TypeScript checking. -- evidence: [README.md#L143-L143](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L143-L143), [README.md#L136-L141](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L136-L141), [CLAUDE.md#L13-L15](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/CLAUDE.md#L13-L15) (`clm_b2e4d1071d043078adbf31239e8fb9ee674b4f2ea750baba45b6af453d12f158`)
- [observation/documented] Repository development practice: conventions require functional SolidJS components, strict TypeScript with no any, and Electron IPC with channel names in a shared enum. -- evidence: [CLAUDE.md#L27-L30](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/CLAUDE.md#L27-L30) (`clm_034596303c3b7bb3458bc22fc035752c046daba4c420c68ec92e64c769afa4ad`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Creating a task makes a git branch from main, sets up a git worktree, symlinks gitignored directories like node_modules, and spawns the AI agent there. -- evidence: [README.md#L72-L75](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L72-L75) (`clm_81afef8ab67605a23ddc57c61dd8162fb3128dfeee2af639e39f30ed6cca16bf`)
- [observation/documented] Completed task branches can be merged back to main from the sidebar. -- evidence: [README.md#L77-L77](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L77-L77) (`clm_b712e829105fa8bd9e8fe7488e392198c07fc5406c14cf43fc03b9a70b34d074`)
- [observation/documented] A Remote Access feature lets users monitor agents from a phone over Wi-Fi or Tailscale, with a QR code and a bearer-token URL. -- evidence: [PRIVACY.md#L78-L82](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L78-L82), [README.md#L48-L55](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L48-L55) (`clm_22f74dcbf6c53684e87c026d3ee5be369afb17982095e825a3530efc059c8f3f`)

## memory-state (1 claim(s))

- [observation/documented] State is stored locally: state.json with a rolling backup, keybindings, themes, arena files, and a .updaterId UUID in per-OS app data directories. -- evidence: [PRIVACY.md#L86-L86](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L86-L86), [PRIVACY.md#L88-L93](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L88-L93) (`clm_42a3e602e587717a2f8aaa307c91c844ba18eebfa2bd91b880961d701cb2dbd8`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] For coordinator sub-tasks, the app injects a system-prompt preamble telling the sub-agent to call the signal_done MCP tool, via .claude/settings.local.json for Claude Code. -- evidence: [PRIVACY.md#L44-L44](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L44-L44), [PRIVACY.md#L97-L99](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L97-L99) (`clm_415590fe5241a12f44dee3661d9681e4d982609227caca07656ee5a808d39353`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The app drives third-party AI coding CLIs the user installs, including Claude Code, Codex CLI, Gemini CLI, Copilot CLI, OpenCode, and Antigravity CLI. -- evidence: [README.md#L120-L120](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L120-L120), [PRIVACY.md#L31-L31](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L31-L31), [PRIVACY.md#L33-L38](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L33-L38) (`clm_53ae285956b82072ca1fe3b506900271a7257e9aa73b65ca5a7dfa5d32f8e013`)
- [observation/documented] Packaged macOS and Linux builds check GitHub Releases for updates via electron-updater, sending a stable per-install x-user-staging-id UUID to GitHub. -- evidence: [PRIVACY.md#L50-L70](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L50-L70) (`clm_5eab302eac6346d2a2bd883541f3f3306c46194eb927da63bdc2d3bdf02f1d22`)

## limitations (1 claim(s))

- [observation/documented] Docker-isolated Antigravity tasks cannot authenticate because the OS keyring is unreachable in the container and agy has no API-key fallback; Antigravity must run natively. -- evidence: [README.md#L127-L127](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L127-L127) (`clm_96f12013c26700ba4c7f918c1b962974666d87a1d880ef8a9f7ebc573f1b99a7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

