# friuns2/codex-mobile -- full detail

[Back to orientation](codex-mobile.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/friuns2/codex-mobile/fac2291b0e606c869d4760f56c0f49172214cb79/5767fa3cbc572be0.json](../../../wiki/dossiers/friuns2/codex-mobile/fac2291b0e606c869d4760f56c0f49172214cb79/5767fa3cbc572be0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Architecture: a Vue 3 SPA browser client talks over HTTP/WebSocket to a Node.js Express server, which proxies JSON-RPC over newline-delimited stdin/stdout to a single spawned `codex app-server` child process. -- evidence: [PROJECT_SPEC.md#L215-L215](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L215-L215), [PROJECT_SPEC.md#L42-L45](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L42-L45), [README.md#L227-L240](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L227-L240), [PROJECT_SPEC.md#L13-L38](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L13-L38) (`clm_23e86219eba8c2312a176b2d827d51aa47682c2d86c4c5a83f833d6315b352c4`)
- [observation/documented] An optional Telegram bot bridge forwards messages into a mapped Codex thread and returns assistant replies; it requires TELEGRAM_BOT_TOKEN and TELEGRAM_ALLOWED_USER_IDS, rejecting messages from non-allowlisted users, and supports commands like /threads, /newthread, and /history. -- evidence: [README.md#L148-L153](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L148-L153), [README.md#L146-L146](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L146-L146), [README.md#L165-L173](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L165-L173), [README.md#L155-L155](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L155-L155) (`clm_fd9a30cb8d49af8726f749c5ad0b748bc056a8a8446f8c930c3a9092434d37aa`)
- [observation/documented] Projects can be exported as ZIP archives (including Codex chat JSONL history under .codex-project/chats/) and re-imported via the browser; imported chats are rewritten for the destination CODEX_HOME, project path, and selected provider/model so they can resume there. -- evidence: [README.md#L130-L142](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L130-L142) (`clm_b90a2a4aaa97fdba245a3e057ecc7ff8175f55f0987288c3b90ac15b6759a438`)

## design-choices (1 claim(s))

- [observation/documented] The design avoids Pinia/Vuex: all frontend state lives in one composable (`useDesktopState`), and realtime transport prefers WebSocket on /codex-api/ws with SSE fallback while client-to-server RPC uses HTTP POST. -- evidence: [PROJECT_SPEC.md#L256-L256](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L256-L256), [PROJECT_SPEC.md#L42-L45](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L42-L45) (`clm_f861b6ba3624b949629c004a328c0b15080adaf8ba8a917256d93cd462b62637`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md requires checking live git state before merges/rebases, committing after each discrete task, preferring PR-based merges, and inspecting conflicts intentionally rather than using automatic conflict-bias flags. -- evidence: [AGENTS.md#L5-L18](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L5-L18), [AGENTS.md#L22-L24](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L22-L24) (`clm_d64f17b06380857569dd0a31fe7e29f29e780a75ed2975a799d0475fc58754b6`)
- [observation/documented] Repository development practice: every feature/behavior change needs a measurement-grounded performance audit before completion, with profiler helpers (`pnpm run profile:browser`, `profile:thread`) writing reports under output/playwright/. -- evidence: [AGENTS.md#L38-L52](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L38-L52) (`clm_013a3f8279ff373dcb11380aec2e34177fa85e2549f4eb332d01df0a1d9e0d18`)
- [observation/documented] Repository development practice: Qodo/CodeRabbit review comments are advisory; security-hardening suggestions assuming a hostile remote caller should be rejected because the app server is intended for local-user use, not public internet exposure. -- evidence: [AGENTS.md#L28-L34](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L28-L34) (`clm_5b38afd1914c676952be91764ea64851ae7693bea9834474eec087cd811b4f69`)
- [observation/documented] Repository development practice: changes should be tested before completion, manual test docs under tests/<domain>/ updated with setup/actions/expected results, and a CJS smoke test is required for package/runtime/module-loading changes. -- evidence: [AGENTS.md#L56-L61](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L56-L61) (`clm_aa8798664e9e195f27cea640766fa7e619a757dad7fe42235c95e03d0625f5f7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Running `npx codexapp` starts a local web server whose UI is served at http://localhost:18923, accessible from the local machine or LAN. -- evidence: [README.md#L40-L40](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L40-L40), [README.md#L130-L142](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L130-L142), [README.md#L29-L29](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L29-L29), [README.md#L44-L44](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L44-L44) (`clm_44fa1a75a3c7ac7192cd6e1475e7d79ee0f98f13331d09f5e6766e7b6d641a8d`)
- [observation/documented] By default the tool also launches a cloudflared tunnel to the local port and prints the tunnel URL, a terminal QR code, and a password in startup output; `--no-tunnel` disables this. -- evidence: [README.md#L52-L53](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L52-L53), [README.md#L46-L46](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L46-L46), [README.md#L48-L50](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L48-L50) (`clm_15bcf5ee2ada7fcb4c7761c5c3335cce8bb314c473ce7a75fd5845430c6abc95`)
- [observation/documented] CLI flags include `--no-login` to skip forcing `codex login` at startup (for already-authenticated providers/gateways) and `--port` to choose the serving port. -- evidence: [README.md#L99-L102](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L99-L102), [README.md#L55-L55](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L55-L55), [README.md#L57-L59](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L57-L59) (`clm_88f81db7193bd6317b38ebf599a92f6139603fbc650e45bf4cd4115514c1ce3b`)
- [observation/documented] The bridge exposes HTTP endpoints including POST /codex-api/rpc (JSON-RPC proxy), server-request respond/pending endpoints, meta discovery endpoints, an SSE events stream, and a WebSocket upgrade at /codex-api/ws. -- evidence: [PROJECT_SPEC.md#L203-L211](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L203-L211) (`clm_b556f44783ffe99aff84681d9ddca704c95bbf31d196f439f919cbfb842ad5a6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The UI surfaces server-initiated approval requests (command approvals, file changes, tool calls) that the user can approve or reject; production password auth uses an HttpOnly cookie and constant-time comparison, with auto-generated passwords written to $CODEX_HOME/codexui-password with 0600 permissions. -- evidence: [PROJECT_SPEC.md#L332-L335](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L332-L335), [PROJECT_SPEC.md#L328-L328](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L328-L328), [PROJECT_SPEC.md#L115-L133](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L115-L133) (`clm_69a2fb48fcc6f28ed1e72460612cb93359538ead274f469aaae9f85b3d74c247`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack requires Node.js 18+ and a Codex app-server environment; documented technologies include Vue 3, Vue Router 4, Tailwind CSS 4, Vite 6, Express 5, Commander 13, TypeScript 5, and tsup 8. -- evidence: [PROJECT_SPEC.md#L305-L306](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L305-L306), [PROJECT_SPEC.md#L49-L59](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L49-L59), [README.md#L245-L248](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L245-L248) (`clm_bb5d861deea3ac77d5a3179f276246de61e7edab7e5b9d2847dfe839c05df337`)

## limitations (1 claim(s))

- [observation/documented] Per the project spec, many protocol capabilities are not yet surfaced in the UI, including thread forking/rollback/naming, context compaction, code review, skills management UI, MCP server status, config UI, command execution, git diff view, and token usage display. -- evidence: [PROJECT_SPEC.md#L137-L137](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L137-L137), [PROJECT_SPEC.md#L139-L164](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L139-L164) (`clm_2e58fdd7cd8f7ca8fa3b7c4028e7cc89d5e6dc378a805977fbc3f023f0d7a434`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

