---
access: public
aliases: []
claim_ids:
- clm_23e86219eba8c2312a176b2d827d51aa47682c2d86c4c5a83f833d6315b352c4
- clm_2e58fdd7cd8f7ca8fa3b7c4028e7cc89d5e6dc378a805977fbc3f023f0d7a434
- clm_69a2fb48fcc6f28ed1e72460612cb93359538ead274f469aaae9f85b3d74c247
- clm_b556f44783ffe99aff84681d9ddca704c95bbf31d196f439f919cbfb842ad5a6
- clm_bb5d861deea3ac77d5a3179f276246de61e7edab7e5b9d2847dfe839c05df337
- clm_f861b6ba3624b949629c004a328c0b15080adaf8ba8a917256d93cd462b62637
maturity: draft
page_id: pg_43fd790ab155502594a281453dd6a059
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_06aedf4fc60e5c8387bf02c22a84e954
title: friuns2/codex-mobile/PROJECT_SPEC.md @ fac2291b0e60
updated_at: '2026-09-14T01:49:12Z'
---

# friuns2/codex-mobile/PROJECT_SPEC.md @ fac2291b0e60

<!-- rcw:begin owner=source:src_06aedf4fc60e5c8387bf02c22a84e954 block=evidence -->
- Architecture: a Vue 3 SPA browser client talks over HTTP/WebSocket to a Node.js Express server, which proxies JSON-RPC over newline-delimited stdin/stdout to a single spawned `codex app-server` child process. [@claim:clm_23e86219eba8c2312a176b2d827d51aa47682c2d86c4c5a83f833d6315b352c4]
- Per the project spec, many protocol capabilities are not yet surfaced in the UI, including thread forking/rollback/naming, context compaction, code review, skills management UI, MCP server status, config UI, command execution, git diff view, and token usage display. [@claim:clm_2e58fdd7cd8f7ca8fa3b7c4028e7cc89d5e6dc378a805977fbc3f023f0d7a434]
- The UI surfaces server-initiated approval requests (command approvals, file changes, tool calls) that the user can approve or reject; production password auth uses an HttpOnly cookie and constant-time comparison, with auto-generated passwords written to $CODEX_HOME/codexui-password with 0600 permissions. [@claim:clm_69a2fb48fcc6f28ed1e72460612cb93359538ead274f469aaae9f85b3d74c247]
- The bridge exposes HTTP endpoints including POST /codex-api/rpc (JSON-RPC proxy), server-request respond/pending endpoints, meta discovery endpoints, an SSE events stream, and a WebSocket upgrade at /codex-api/ws. [@claim:clm_b556f44783ffe99aff84681d9ddca704c95bbf31d196f439f919cbfb842ad5a6]
- The stack requires Node.js 18+ and a Codex app-server environment; documented technologies include Vue 3, Vue Router 4, Tailwind CSS 4, Vite 6, Express 5, Commander 13, TypeScript 5, and tsup 8. [@claim:clm_bb5d861deea3ac77d5a3179f276246de61e7edab7e5b9d2847dfe839c05df337]
- The design avoids Pinia/Vuex: all frontend state lives in one composable (`useDesktopState`), and realtime transport prefers WebSocket on /codex-api/ws with SSE fallback while client-to-server RPC uses HTTP POST. [@claim:clm_f861b6ba3624b949629c004a328c0b15080adaf8ba8a917256d93cd462b62637]
<!-- rcw:end owner=source:src_06aedf4fc60e5c8387bf02c22a84e954 block=evidence -->

## Researcher notes

