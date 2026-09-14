# nimbalyst/nimbalyst -- full detail

[Back to orientation](nimbalyst.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nimbalyst/nimbalyst/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/777ff5f0ac48054d.json](../../../wiki/dossiers/nimbalyst/nimbalyst/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/777ff5f0ac48054d.json)

## specifications (1 claim(s))

- [observation/documented] Nimbalyst is described as an open-source, MIT-licensed visual workspace for building with coding agents such as Codex, Claude Code, and OpenCode, shipped as a desktop app for macOS, Windows, and Linux with an iOS companion app. -- evidence: [README.md#L163-L165](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L163-L165), [README.md#L3-L3](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L3-L3) (`clm_fe72318bffa3df25e245e6cd0345d61b63ef13d9ef81083d1c302e3cc7c5b49b`)

## components (1 claim(s))

- [observation/documented] The repository is a TypeScript/Electron npm-workspaces monorepo with packages for the Electron desktop app, a native SwiftUI iOS app, cross-platform runtime services (AI, sync, Lexical editor), a collab-protocol wire-format package, an extension SDK, and built-in extensions. -- evidence: [CLAUDE.md#L123-L132](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L123-L132), [README.md#L144-L149](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L144-L149), [README.md#L129-L129](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L129-L129) (`clm_25d17b3503f0f70a56d4c6627e8e455ba961183096a27edd4b96b0a7361731a3`)

## design-choices (2 claim(s))

- [observation/documented] Content and status are stored as plain markdown files and workflows as slash commands inside the user's git repo, with no proprietary store, and parallel agent sessions are each isolated in their own git worktree. -- evidence: [README.md#L21-L31](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L21-L31) (`clm_d95058f42c060916e81dce858bdd24eadd56aabbc760929ae5b5fa8602e8be3d`)
- [observation/documented] The app sends anonymous usage analytics to PostHog, states it collects no PII, file contents/paths, API keys, or document/session/chat content, uses a random anonymous install ID, and offers an opt-out in Settings. -- evidence: [README.md#L118-L121](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L118-L121), [README.md#L116-L116](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L116-L116), [README.md#L123-L123](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L123-L123) (`clm_53c7a67690d76c01c06a1994da160317c73ed56295e32cbc8ee35fc2e846556c`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md instructs AI contributors that any runtime-behavior change ships with a unit test and that the pre-push gate (npm run typecheck && npm run test:prepush) must be run locally, with failures recorded to .vitest/last-run.log readable via npm run test:last. -- evidence: [CLAUDE.md#L25-L25](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L25-L25), [CLAUDE.md#L27-L27](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L27-L27) (`clm_2bcdede85999f98704e486b2e01b4b012e209c4775e97bf6cadf86b2677d8a9c`)
- [observation/documented] Repository development practice: parallel work slices must declare disjoint file sets (including CHANGELOG.md and package.json), slices never run the full gate themselves, and CHANGELOG entries are written only when a commit is requested, one bullet per feature with no internal scaffolding. -- evidence: [CLAUDE.md#L13-L13](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L13-L13), [CLAUDE.md#L9-L9](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L9-L9), [CLAUDE.md#L21-L21](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L21-L21) (`clm_f5df0aa09e45f5d96eff0a0af29b76683bb3c80fff5af2b8ff2ee961bc47c5dd`)
- [observation/documented] Repository development practice: API keys must never be read from process.env as a fallback for provider authentication; keys may come only from explicitly configured settings, after a past incident where an env var silently billed a user's personal Anthropic account. -- evidence: [CLAUDE.md#L58-L60](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L58-L60), [CLAUDE.md#L56-L56](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L56-L56), [CLAUDE.md#L54-L54](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L54-L54) (`clm_399fd78d899ec5c4ed40d88a8b8b3c35dc125f17f407dac2d37be4572cee4fcc`)
- [observation/documented] Repository development practice: contributors must not open database files directly from a second process (risking corruption via PID-based or exclusive locking) and should instead use the mcp__nimbalyst-extension-dev__database_query tool. -- evidence: [CLAUDE.md#L78-L80](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L78-L80), [CLAUDE.md#L76-L76](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/CLAUDE.md#L76-L76) (`clm_6625bc64d16e48f8af6e5b54bb1562114f2e3ba70e923db60df8dd0be8c99ad1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Every editor, built-in or custom, goes through the same EditorHost contract, making pluggable editors for arbitrary file types first-class; existing extensions include an Astro website editor, visual git log, mindmap, slides, and a 3D object editor. -- evidence: [README.md#L75-L77](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L75-L77), [README.md#L21-L31](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L21-L31) (`clm_ced6f1915ba54d65581d75d1bd0c5333d53c3c99bba7ccf99a612c6771c8e287`)
- [observation/documented] The app acts as an MCP client that can connect any MCP server and renders tool results as visual widgets rather than raw JSON. -- evidence: [README.md#L21-L31](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L21-L31) (`clm_ead391c3adca1bf46277370b6d0b44511af3fdf2de7ee3913ef7af28e5cbb4aa`)
- [observation/documented] Desktop builds are distributed as macOS .dmg (Apple Silicon and Intel), Windows .exe, Linux .deb, and AppImage, with stated OS requirements such as macOS 12+ and Windows 10+; fresh installs default to the stable release channel with an opt-in alpha channel. -- evidence: [README.md#L91-L97](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L91-L97), [README.md#L112-L112](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L112-L112) (`clm_9ce46fb776e9339fbb0576259ef05fc3efef440dbd82dcc66070411e0a766c92`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Acknowledged building blocks include Electron, Meta's Lexical, React, Monaco Editor, and Excalidraw; the collaboration sync server is a separate Cloudflare Worker project reached at wss://sync.nimbalyst.com via the collab-protocol wire format. -- evidence: [README.md#L163-L165](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L163-L165), [README.md#L181-L186](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L181-L186), [README.md#L151-L151](https://github.com/nimbalyst/nimbalyst/blob/d6e1d008d9ee264a7447f3533fa9f48f158a70b0/README.md#L151-L151) (`clm_bedebd5f20a476ed8e607765efbcc4ffa41a4d6c557954a596018a4ea025cc53`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

