# openchamber/openchamber -- full detail

[Back to orientation](openchamber.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openchamber/openchamber/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/d00ddc4376c3a35c.json](../../../wiki/dossiers/openchamber/openchamber/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/d00ddc4376c3a35c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (5 claim(s))

- [observation/documented] Session Goals let a user set a finish line; the system checks results after each turn and keeps the agent working until the goal completes, the agent is blocked, or a user-set limit is reached, continuing even after the app is closed. -- evidence: [README.md#L32-L32](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L32-L32) (`clm_1efe4dedd499521a2fe52f75d95d77a9f926a1019bea6668dfe5d0a3258fcea3`)
- [observation/documented] Multi-run assigns the same task to up to five models in separate sessions with optional worktrees, and Fusion can combine the strongest parts of those runs into a new session. -- evidence: [README.md#L36-L36](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L36-L36) (`clm_bcb6b6a111ceb495611b5bbc85b345a9000da0d27ac36f5ea81d02ca5390db1c`)
- [observation/documented] Changes Walkthrough turns a large diff into an AI-guided tour that groups related edits into ordered steps and explains how the pieces fit together. -- evidence: [README.md#L40-L40](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L40-L40) (`clm_ba80ba319ebf84f768efca30c786fef102536c92f64ed39c68f69b5512540b4a`)
- [observation/documented] Remote access pairs devices via a one-time QR code through Private Relay with end-to-end encryption and revocable connections; direct, LAN/VPN, Cloudflare/Ngrok tunnels, and SSH connections are also supported. -- evidence: [README.md#L56-L56](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L56-L56) (`clm_668da093690b69c89271a2987827b9fe77ed62998975deb44cff48ee2ee34a99`)
- [inference/documented] OpenChamber appears to gzip-compress HTTP responses with a 1 KB threshold while excluding SSE streaming routes from compression, per the reverse-proxy guidance. -- evidence: [docs/REVERSE_PROXY.md#L299-L301](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/REVERSE_PROXY.md#L299-L301), [docs/REVERSE_PROXY.md#L309-L309](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/REVERSE_PROXY.md#L309-L309) (`clm_78c3e75eb41584e7ab49659c0d6993be4702580e4bfd6708fd319fe5324c6209`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md mandates loading every matching project skill and nearest DOCUMENTATION.md before editing, treats skill loading as required rather than optional, and requires stopping to resolve conflicts between guidance sources. -- evidence: [AGENTS.md#L13-L17](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L13-L17), [AGENTS.md#L11-L11](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L11-L11), [AGENTS.md#L19-L21](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L19-L21), [AGENTS.md#L82-L87](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L82-L87) (`clm_565f1f6b30a56a95b108c0d90ba45bfa03bc0058668e6c298ba88e5e6ac64f17`)
- [observation/documented] Repository development practice: contributors validate changes with package.json scripts, run 'bun run dead-code' after file/export changes, and run 'bunx oxlint' with a vendored anti-slop plugin on new or substantially rewritten TypeScript files. -- evidence: [AGENTS.md#L133-L140](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L133-L140) (`clm_c442d7274061534187febb62c8bcc2de7ab3f4016a616cb8b9b02a4722b231a8`)
- [observation/documented] Repository development practice: development uses Bun (bun install, bun run dev, electron:build, vscode:package), with dev scripts for web HMR, Electron, and VS Code extension development documented in CONTRIBUTING.md. -- evidence: [CONTRIBUTING.md#L28-L32](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/CONTRIBUTING.md#L28-L32), [CONTRIBUTING.md#L46-L50](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/CONTRIBUTING.md#L46-L50), [CONTRIBUTING.md#L17-L22](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/CONTRIBUTING.md#L17-L22), [CONTRIBUTING.md#L5-L9](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/CONTRIBUTING.md#L5-L9) (`clm_7e3a496d41c6b15da5f9cd4761429c801e355372a08a62a370be88a3661481e7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands such as status, connect-url --qr, tunnel start, startup enable, logs, stop, and update, and binds to localhost by default with --lan and --ui-password options. -- evidence: [README.md#L116-L116](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L116-L116), [README.md#L106-L114](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L106-L114) (`clm_b3b0e08acf4f2370c5aaff4dd5ec63aabc6ce406d45576f6119550c62b144dce`)
- [observation/documented] The server exposes WebSocket routes (/api/event/ws, /api/global/event/ws, /api/terminal/ws) and SSE routes (/api/event, /api/global/event, /api/notifications/stream, /api/openchamber/events) that reverse proxies must pass through unbuffered. -- evidence: [docs/REVERSE_PROXY.md#L13-L23](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/REVERSE_PROXY.md#L13-L23) (`clm_5495ba05242f8dcb8c464cc80b4d168b5c27f2897691973c04c86526136793b9`)
- [observation/documented] Users can define custom themes by dropping a JSON file into ~/.config/openchamber/themes/ and reloading from Settings without restarting the app; themes are validated on load and invalid ones are skipped with a console warning. -- evidence: [docs/CUSTOM_THEMES.md#L14-L14](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/CUSTOM_THEMES.md#L14-L14), [docs/CUSTOM_THEMES.md#L218-L218](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/CUSTOM_THEMES.md#L218-L218), [docs/CUSTOM_THEMES.md#L3-L3](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/CUSTOM_THEMES.md#L3-L3) (`clm_f1068bb5760d38090d2cc4ca98c542567d7ca3b390d60c1be08c6b8d2aff71b7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] OpenChamber uses OpenCode to run coding agents, calling official OpenCode APIs through @opencode-ai/sdk/v2; the CLI/Web and VS Code surfaces use the user's installed OpenCode CLI. -- evidence: [README.md#L139-L139](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L139-L139), [AGENTS.md#L32-L32](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L32-L32), [README.md#L97-L97](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L97-L97) (`clm_6e150bab3f132cd8b409bce5ecfe7c57b5095e48415595db98c8570f40b6aaad`)
- [observation/documented] The CLI for web/PWA requires Node.js 22+; Linux AppImages require FUSE (libfuse.so.2), with an APPIMAGE_EXTRACT_AND_RUN=1 fallback. -- evidence: [README.md#L89-L89](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L89-L89), [README.md#L97-L97](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L97-L97) (`clm_c18926456ba7136304a277cbaa30f8db247666acc9013e6d313f45920eade665`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

