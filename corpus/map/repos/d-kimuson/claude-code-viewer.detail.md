# d-kimuson/claude-code-viewer -- full detail

[Back to orientation](claude-code-viewer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/d-kimuson/claude-code-viewer/9367cf006be9965c954e6cd36526f2195dce67ea/d2e4b2b80b9562f7.json](../../../wiki/dossiers/d-kimuson/claude-code-viewer/9367cf006be9965c954e6cd36526f2195dce67ea/d2e4b2b80b9562f7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The product includes an integrated terminal emulator in a bottom panel, letting users launch Claude Code from the browser without leaving it. -- evidence: [README.md#L31-L31](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L31-L31) (`clm_5a1107dda98ff15127b004cd1344fbbad907ac83e0de2cced33132769a78917c`)
- [observation/documented] It is a PWA supporting Add to Home Screen on mobile with an optimized UI and push notifications when sessions complete. -- evidence: [README.md#L95-L95](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L95-L95) (`clm_8ccf7a6c54579992915405c6872f10fe6159e863d602ff78a992e9fd81ad6d70`)

## design-choices (2 claim(s))

- [observation/documented] The app reads Claude Code conversation logs from ~/.claude/projects/<project>/<session-id>.jsonl JSONL files and automatically discovers new projects and sessions. -- evidence: [README.md#L236-L238](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L236-L238) (`clm_5723cc779483262d08a585035b807ad0de57d3d9783ee789b735cf4a7cc5e573`)
- [observation/documented] Conversation data is preserved through strict Zod schema validation, with a progressive-disclosure UI that reveals details on demand. -- evidence: [README.md#L284-L289](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L284-L289), [README.md#L37-L37](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L37-L37) (`clm_746ef0fe0c9accc687c12d9e413503b3793e5ba8d1732072afdcad8f150a61a5`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must avoid 'as' casting, raw fetch, dev servers, and node built-ins; use Effect-TS and Hono RPC + TanStack Query, follow TDD, and run pnpm gatecheck check and lingui-check before committing. -- evidence: [AGENTS.md#L18-L21](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L18-L21), [AGENTS.md#L11-L14](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L11-L14), [AGENTS.md#L77-L80](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L77-L80), [AGENTS.md#L69-L69](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L69-L69) (`clm_186cb8add44bf060085b77e93c463d5e5ed1332b870f225165f71605fcf3e7d3`)
- [observation/documented] Repository development practice: commit messages follow Conventional Commits, appear in release notes, and 'fix' is reserved for user-facing bugs while internal fixes use 'chore'. -- evidence: [AGENTS.md#L25-L25](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L25-L25), [AGENTS.md#L38-L38](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L38-L38), [AGENTS.md#L31-L36](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/AGENTS.md#L31-L36) (`clm_f359b953a53a103814198fb9b11001caef39b6bb7fd9e521e21bce05deb399c0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI accepts options including --port (default 3000), --hostname, --verbose, --password, --executable, --claude-dir, --api-only, and --base-path. -- evidence: [README.md#L71-L80](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L71-L80) (`clm_2a75a4d27cc4d14393c3120aac57a6589b182dd3a492d09bb3b03271f1a52ff2`)
- [observation/documented] When a password is configured, /api routes require authentication via a ccv-session cookie from /api/auth/login or an Authorization: Bearer header; without a password, API auth is disabled. -- evidence: [README.md#L153-L153](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L153-L153), [README.md#L150-L151](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L150-L151), [README.md#L148-L148](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L148-L148) (`clm_c19be55894d6b155d12bce17b5c562df6ddd5866e7c7fa9a8bf1bb147037ea66`)
- [observation/documented] Configuration can come from command-line options or environment variables such as CCV_PASSWORD and CCV_CC_EXECUTABLE_PATH, with CLI options taking precedence over environment variables. -- evidence: [README.md#L124-L124](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L124-L124), [README.md#L142-L144](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L142-L144) (`clm_34eded67735cdb475367893e9b5d1a3c68ff89c5a4f8849f7e5749a23ccb74f1`)
- [observation/documented] In subscription mode the chat input becomes a copy mode that produces an equivalent claude CLI command, which can be pasted into the built-in terminal to start or resume a session. -- evidence: [README.md#L26-L27](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L26-L27), [README.md#L31-L31](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L31-L31) (`clm_e50e74f6baaf851763a416dd06162a72582f819ff925771c02d6363680b256ac`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Due to Anthropic ToS ambiguity for subscription accounts, chat sending, session resuming, permission approval, and AskUserQuestion are opt-in; read-oriented features work independently of the Agent SDK. -- evidence: [README.md#L15-L20](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L15-L20) (`clm_e07fa3d4ceb04642151a02c248f057b4661abbcc030e20ac4b81dac0d9891b37`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requires Node.js 22.13.0 or later and Claude Code v1.0.125 or later; supported operating systems are macOS and Linux only. -- evidence: [README.md#L43-L45](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L43-L45) (`clm_e4fe6e5ab1edc977fee4541dcee497d40d94170acd03d167f94bab1a4daec14d`)

## limitations (3 claim(s))

- [observation/documented] Windows is not supported as an operating system. -- evidence: [README.md#L43-L45](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L43-L45) (`clm_143129fed5c74c2b08085027c7d259866a219fb5de706fc546ac687d61cb57e5`)
- [observation/documented] The viewer makes no backups of session files, so when Claude Code's default 30-day cleanup deletes .jsonl transcripts those sessions disappear; users can raise cleanupPeriodDays in ~/.claude/settings.json. -- evidence: [README.md#L240-L247](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L240-L247) (`clm_f63fcea83df9c64a7e2afc1fa98e24a7486380e044b5384b17ce2b4d8513fd81`)
- [observation/documented] Authentication is a simple single-password mechanism without multi-user support, role-based access control, or OAuth; more sophisticated access control is left to infrastructure like reverse proxies or VPNs. -- evidence: [README.md#L302-L302](https://github.com/d-kimuson/claude-code-viewer/blob/9367cf006be9965c954e6cd36526f2195dce67ea/README.md#L302-L302) (`clm_8265f2721d7e550113969bba288222b30882bdf6e1c101229720a3e9744bed4a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

