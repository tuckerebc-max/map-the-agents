# fy0/codekanban -- full detail

[Back to orientation](codekanban.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fy0/codekanban/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/6bf09518330b3b17.json](../../../wiki/dossiers/fy0/codekanban/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/6bf09518330b3b17.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The project is a Go backend paired with a Vue 3.5 / TypeScript 5.8 frontend, per README badges. -- evidence: [README.md#L11-L14](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L11-L14) (`clm_b0d860cda64beb82ce512eb3bd80b778826e85cbb126392ccf27975688b20d38`)
- [observation/documented] The build produces a single-file executable: frontend artifacts from ui/dist are copied to static/ and embedded into the Go binary. -- evidence: [README.md#L135-L137](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L135-L137) (`clm_665a2b565d04a6d93e64ef6234871db8d20d9e5102ad264db40ece396019bf9c`)

## design-choices (1 claim(s))

- [observation/documented] Worktree management uses a hybrid Git engine: go-git for fast in-process reads (status, diff, line stats) and system Git preferred for commits and mutations to preserve hooks, signing, filters, and user config; read and write engines are independently selectable in Settings. -- evidence: [README.md#L43-L46](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L43-L46) (`clm_c0f1365948313364066c9a61f92f5107f80ab83c1ac25edd46cd4006483d048b`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to run `go test ./...` (optionally with -race), regenerate SQLC before committing schema changes, and run `go vet ./...` during review. -- evidence: [AGENTS.md#L7-L11](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/AGENTS.md#L7-L11) (`clm_1e1a5bc784f709a9ed934f338d4090c82bb872ea5422b5eb70351da3d1452c69`)
- [observation/documented] Repository development practice: contributors must format with gofmt, group imports with goimports, use PascalCase/camelCase naming, and write structured zap log fields instead of printf-style strings. -- evidence: [AGENTS.md#L14-L14](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/AGENTS.md#L14-L14) (`clm_da32ec4f2d002431a13b0b82b6ce1e135c8be3acb40d80f535b496bc705f8626`)
- [observation/documented] Repository development practice: commits use imperative mood with issue references in the footer; PRs should describe changes, note config.yaml toggles, and include screenshots or cURL snippets when API responses change. -- evidence: [AGENTS.md#L20-L20](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/AGENTS.md#L20-L20) (`clm_0b402342f6cec69795671d5e66648fb4eba73d9ef73a80a974820f30503a9fc0`)

## skills-patterns (1 claim(s))

- [observation/documented] The repo ships an installable Codex skill bundle built around a single public CLI, codekanban-cli, with the skill source at packages/codekanban-cli/skills/codekanban-cli. -- evidence: [README.md#L54-L55](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L54-L55), [README.md#L59-L61](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L59-L61) (`clm_7844959ef0b0822bf31286dad73f4a5f5243c610f4d080a09044bb52136daa2d`)

## interfaces (4 claim(s))

- [observation/documented] The product is runnable via `npx codekanban` or a global npm install of the codekanban package. -- evidence: [README.md#L22-L23](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L22-L23), [README.md#L25-L27](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L25-L27) (`clm_cde2fbb4711673355804bcd857f14126a7e873fb5cbd5fb82a658cb78aa45000`)
- [observation/documented] The backend exposes an OpenAPI docs page at /docs and a health check at /api/v1/health in development. -- evidence: [README.md#L102-L108](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L102-L108) (`clm_ae9f27385b83bf8aaea0c185150f8da4623c9d17dc23accdc068e9586a38eaba`)
- [observation/documented] The backend binary accepts flags: -m/--migrate to force database migration, -i/--install to install as a system service, and --uninstall. -- evidence: [README.md#L110-L113](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L110-L113) (`clm_d0566ae51692f2a1218ec2fbbcf7e9b059f7894bc8fb9b23f204121dd9ea85da`)
- [observation/documented] codekanban-cli defaults to service URL http://127.0.0.1:3007, supports --base-url overrides, saves auth tokens via `auth save-token --password-stdin`, and stores session.json under %APPDATA% or XDG config paths. -- evidence: [README.md#L65-L68](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L65-L68) (`clm_f7d11faa42b6be413f538e4b2bab18401eb534542b9615e753d8e7cee18f1758`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Development requires Node.js v20.19.0+ or v22.12.0+, Go 1.25+, and pnpm 9.15.9. -- evidence: [README.md#L76-L78](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L76-L78) (`clm_149a190fb794a5c7020cc99802cb63b967a43cc97ccd95cd8bbe6becb0fe0dc2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

