# elirantutia/vibeyard -- full detail

[Back to orientation](vibeyard.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/elirantutia/vibeyard/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/4f13da1bc0dfb5da.json](../../../wiki/dossiers/elirantutia/vibeyard/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/4f13da1bc0dfb5da.json)

## specifications (1 claim(s))

- [observation/documented] Vibeyard is described as an IDE built for AI coding agents: it manages multiple agent sessions, runs them in parallel, tracks costs, and supports Claude Code, Codex CLI, and Gemini CLI. -- evidence: [README.md#L56-L56](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L56-L56), [README.md#L16-L19](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L16-L19) (`clm_f59bf33c1a0b43e39e80f2c3e4c8c2b29e16cdd459aa05679156ab5218072901`)

## components (2 claim(s))

- [observation/documented] Documented features include a customizable per-project dashboard with widgets, a kanban task board, P2P session sharing, multi-session management, cost/context tracking, a session inspector, and an AI Readiness Score. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54), [README.md#L37-L37](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L37-L37) (`clm_cd1dd5c2a27ef7b09646ac0d9c961942353f62a4df313b4f8436558e18979cbf`)
- [inference/documented] The changelog suggests the app was renamed from CCIDE to Vibeyard and evolved from macOS-only unsigned builds to signed, cross-platform releases. -- evidence: [CHANGELOG.md#L651-L657](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CHANGELOG.md#L651-L657), [CHANGELOG.md#L752-L752](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CHANGELOG.md#L752-L752), [CHANGELOG.md#L632-L643](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CHANGELOG.md#L632-L643) (`clm_3a6f110babc800a1873c62bb398eafe429af5e0b98ccd4a1f6efbbc4dd8e74d7`)

## design-choices (2 claim(s))

- [observation/documented] Each agent session runs in its own PTY, and multiple Claude profiles are supported with each session backed by an isolated config directory so credentials and history do not mix. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54) (`clm_d803cc054004706a8e3cb6a609255a59179d79534008bea812b1de5a201f00bf`)
- [observation/documented] P2P session sharing uses encrypted WebRTC connections with read-only or read-write modes and PIN-based authentication. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54) (`clm_f6ec59acb66df9fa496c4b57fd76c388928b2954080e0a4ead3cf76b54f80a44`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run tests with npm test, test:watch, or test:coverage using Vitest with v8 coverage, with tests co-located as *.test.ts files. -- evidence: [CLAUDE.md#L30-L30](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L30-L30), [CLAUDE.md#L24-L28](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L24-L28) (`clm_1b3416d9815041ac3c1f862c333225c89855e2419737e0a1faa61c9637b1b5cc`)
- [observation/documented] Repository development practice: building uses npm run build and npm start, requires Node v24 per .nvmrc, has no lint tooling configured, and changes require a rebuild plus app restart since there is no hot reload. -- evidence: [CLAUDE.md#L16-L16](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L16-L16), [CLAUDE.md#L11-L14](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L11-L14), [CLAUDE.md#L18-L18](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L18-L18) (`clm_213686f2791b56c0795bd86a78c2780f9eef15cd9c4bad46220e5768a7ff0c6c`)
- [observation/documented] Repository development practice: building from source clones the repo and runs npm install && npm start, requiring Node v24+. -- evidence: [README.md#L100-L100](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L100-L100), [README.md#L94-L98](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L94-L98) (`clm_2a87da2b694494b4bb676f10f32dfbc40007d82c2161ab3afa47492cab02c109`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes keyboard-driven interfaces, including Cmd+\ to spin up new sessions in swarm mode and Cmd+Shift+I to open the session inspector. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54) (`clm_5fc7125c9ed8a8f2a1ffdfaf93ce4ded35454ecca6a9a32f6c2bdccc42e4f4e2`)
- [observation/documented] Distribution channels documented are macOS .dmg, Linux .deb and AppImage, Windows NSIS installer and portable .exe, and a global npm package that downloads and launches the app on first run. -- evidence: [README.md#L90-L90](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L90-L90), [README.md#L64-L64](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L64-L64), [README.md#L68-L68](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L68-L68), [README.md#L81-L81](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L81-L81), [README.md#L85-L88](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L85-L88) (`clm_44b916a9bcfff319ae139421728796832813139cab7a625a7f862f9d0b390e12`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The app requires at least one supported CLI (Claude Code, OpenAI Codex CLI, or Gemini CLI) to be installed and authenticated. -- evidence: [README.md#L60-L60](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L60-L60) (`clm_c1f5a5e3af4e3d39a34287010605679fd525ac789bc8dca1b69553693e584ca6`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

