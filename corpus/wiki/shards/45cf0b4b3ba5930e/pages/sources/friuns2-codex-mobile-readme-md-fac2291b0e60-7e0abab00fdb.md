---
access: public
aliases: []
claim_ids:
- clm_15bcf5ee2ada7fcb4c7761c5c3335cce8bb314c473ce7a75fd5845430c6abc95
- clm_23e86219eba8c2312a176b2d827d51aa47682c2d86c4c5a83f833d6315b352c4
- clm_44fa1a75a3c7ac7192cd6e1475e7d79ee0f98f13331d09f5e6766e7b6d641a8d
- clm_88f81db7193bd6317b38ebf599a92f6139603fbc650e45bf4cd4115514c1ce3b
- clm_b90a2a4aaa97fdba245a3e057ecc7ff8175f55f0987288c3b90ac15b6759a438
- clm_bb5d861deea3ac77d5a3179f276246de61e7edab7e5b9d2847dfe839c05df337
- clm_fd9a30cb8d49af8726f749c5ad0b748bc056a8a8446f8c930c3a9092434d37aa
maturity: draft
page_id: pg_c3820b4da9a75103b6407e0abab00fdb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_61d26aebd01657dfbebda6623900512a
title: friuns2/codex-mobile/README.md @ fac2291b0e60
updated_at: '2026-09-14T01:49:12Z'
---

# friuns2/codex-mobile/README.md @ fac2291b0e60

<!-- rcw:begin owner=source:src_61d26aebd01657dfbebda6623900512a block=evidence -->
- By default the tool also launches a cloudflared tunnel to the local port and prints the tunnel URL, a terminal QR code, and a password in startup output; `--no-tunnel` disables this. [@claim:clm_15bcf5ee2ada7fcb4c7761c5c3335cce8bb314c473ce7a75fd5845430c6abc95]
- Architecture: a Vue 3 SPA browser client talks over HTTP/WebSocket to a Node.js Express server, which proxies JSON-RPC over newline-delimited stdin/stdout to a single spawned `codex app-server` child process. [@claim:clm_23e86219eba8c2312a176b2d827d51aa47682c2d86c4c5a83f833d6315b352c4]
- Running `npx codexapp` starts a local web server whose UI is served at http://localhost:18923, accessible from the local machine or LAN. [@claim:clm_44fa1a75a3c7ac7192cd6e1475e7d79ee0f98f13331d09f5e6766e7b6d641a8d]
- CLI flags include `--no-login` to skip forcing `codex login` at startup (for already-authenticated providers/gateways) and `--port` to choose the serving port. [@claim:clm_88f81db7193bd6317b38ebf599a92f6139603fbc650e45bf4cd4115514c1ce3b]
- Projects can be exported as ZIP archives (including Codex chat JSONL history under .codex-project/chats/) and re-imported via the browser; imported chats are rewritten for the destination CODEX_HOME, project path, and selected provider/model so they can resume there. [@claim:clm_b90a2a4aaa97fdba245a3e057ecc7ff8175f55f0987288c3b90ac15b6759a438]
- The stack requires Node.js 18+ and a Codex app-server environment; documented technologies include Vue 3, Vue Router 4, Tailwind CSS 4, Vite 6, Express 5, Commander 13, TypeScript 5, and tsup 8. [@claim:clm_bb5d861deea3ac77d5a3179f276246de61e7edab7e5b9d2847dfe839c05df337]
- An optional Telegram bot bridge forwards messages into a mapped Codex thread and returns assistant replies; it requires TELEGRAM_BOT_TOKEN and TELEGRAM_ALLOWED_USER_IDS, rejecting messages from non-allowlisted users, and supports commands like /threads, /newthread, and /history. [@claim:clm_fd9a30cb8d49af8726f749c5ad0b748bc056a8a8446f8c930c3a9092434d37aa]
<!-- rcw:end owner=source:src_61d26aebd01657dfbebda6623900512a block=evidence -->

## Researcher notes

