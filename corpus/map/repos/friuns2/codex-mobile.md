# friuns2/codex-mobile

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fac2291b0e60 @ 5767fa3cbc572be0

## Summary (orientation draft, not independently verified)

The repository ships `codexapp`, an npm-distributed Node.js bridge exposing a Codex app-server-backed web UI (Vue 3 + Express) on localhost:18923, with tunneling, password auth, Telegram bot bridge, and project ZIP export/import. Contributor workflow rules live in AGENTS.md and are reported only under workflows.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Architecture: a Vue 3 SPA browser client talks over HTTP/WebSocket to a Node.js Express server, which proxies JSON-RPC over newline-delimited stdin/stdout to a single spawned `codex app-server` child process. -- evidence: [PROJECT_SPEC.md#L215-L215](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L215-L215), [PROJECT_SPEC.md#L42-L45](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L42-L45), [README.md#L227-L240](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L227-L240), [PROJECT_SPEC.md#L13-L38](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L13-L38)
  - [observation/documented] An optional Telegram bot bridge forwards messages into a mapped Codex thread and returns assistant replies; it requires TELEGRAM_BOT_TOKEN and TELEGRAM_ALLOWED_USER_IDS, rejecting messages from non-allowlisted users, and supports commands like /threads, /newthread, and /history. -- evidence: [README.md#L148-L153](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L148-L153), [README.md#L146-L146](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L146-L146), [README.md#L165-L173](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L165-L173), [README.md#L155-L155](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L155-L155)
- design-choices (1 claim(s)):
  - [observation/documented] The design avoids Pinia/Vuex: all frontend state lives in one composable (`useDesktopState`), and realtime transport prefers WebSocket on /codex-api/ws with SSE fallback while client-to-server RPC uses HTTP POST. -- evidence: [PROJECT_SPEC.md#L256-L256](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L256-L256), [PROJECT_SPEC.md#L42-L45](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L42-L45)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md requires checking live git state before merges/rebases, committing after each discrete task, preferring PR-based merges, and inspecting conflicts intentionally rather than using automatic conflict-bias flags. -- evidence: [AGENTS.md#L5-L18](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L5-L18), [AGENTS.md#L22-L24](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L22-L24)
  - [observation/documented] Repository development practice: every feature/behavior change needs a measurement-grounded performance audit before completion, with profiler helpers (`pnpm run profile:browser`, `profile:thread`) writing reports under output/playwright/. -- evidence: [AGENTS.md#L38-L52](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/AGENTS.md#L38-L52)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Running `npx codexapp` starts a local web server whose UI is served at http://localhost:18923, accessible from the local machine or LAN. -- evidence: [README.md#L40-L40](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L40-L40), [README.md#L130-L142](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L130-L142), [README.md#L29-L29](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L29-L29), [README.md#L44-L44](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L44-L44)
  - [observation/documented] By default the tool also launches a cloudflared tunnel to the local port and prints the tunnel URL, a terminal QR code, and a password in startup output; `--no-tunnel` disables this. -- evidence: [README.md#L52-L53](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L52-L53), [README.md#L46-L46](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L46-L46), [README.md#L48-L50](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/README.md#L48-L50)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The UI surfaces server-initiated approval requests (command approvals, file changes, tool calls) that the user can approve or reject; production password auth uses an HttpOnly cookie and constant-time comparison, with auto-generated passwords written to $CODEX_HOME/codexui-password with 0600 permissions. -- evidence: [PROJECT_SPEC.md#L332-L335](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L332-L335), [PROJECT_SPEC.md#L328-L328](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L328-L328), [PROJECT_SPEC.md#L115-L133](https://github.com/friuns2/codex-mobile/blob/fac2291b0e606c869d4760f56c0f49172214cb79/PROJECT_SPEC.md#L115-L133)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](codex-mobile.detail.md)

Metadata and full claim list: [full detail](codex-mobile.detail.md)
Human notes ([notes](codex-mobile.notes.md), never overwritten by build)

[Back to map index](../../index.md)
