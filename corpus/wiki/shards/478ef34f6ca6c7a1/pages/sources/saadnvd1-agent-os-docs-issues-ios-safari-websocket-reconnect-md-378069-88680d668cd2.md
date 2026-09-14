---
access: public
aliases: []
claim_ids:
- clm_6e0492421513a7e2e049044f542b8250b93f81f8d3a9af479c93906b41d08551
- clm_819fcfe871522be64fe354c87ce8b14a762fb5ab39eb0444547aa258e042cd5b
- clm_b5dab3224d5a180145c83dd60b76e1c69a61394b622dcdcde1d9e1f5e9240a33
maturity: draft
page_id: pg_d2ae7c904771547580e988680d668cd2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f6180115fcb65446b088bdc58b7c262d
title: saadnvd1/agent-os/docs/issues/ios-safari-websocket-reconnect.md @ 378069fed637
updated_at: '2026-09-14T02:37:46Z'
---

# saadnvd1/agent-os/docs/issues/ios-safari-websocket-reconnect.md @ 378069fed637

<!-- rcw:begin owner=source:src_f6180115fcb65446b088bdc58b7c262d block=evidence -->
- The terminal stack appears to consist of a React hook wrapping WebSocket management (websocket-connection.ts, useTerminalConnection.ts) and a server.ts that runs the WebSocket server and spawns PTYs, attaching to tmux sessions. [@claim:clm_6e0492421513a7e2e049044f542b8250b93f81f8d3a9af479c93906b41d08551]
- An iOS Safari issue where the terminal stayed stuck reconnecting after backgrounding was fixed (January 14, 2026, commit 12bae2e); Safari silently kills WebSockets and may not fire onclose while readyState still shows OPEN. [@claim:clm_819fcfe871522be64fe354c87ce8b14a762fb5ab39eb0444547aa258e042cd5b]
- The fix saved WebSocket handlers immediately after definition so forceReconnect could attach them to the new socket, avoiding the bug where nulling handlers on the shared old socket object also cleared the live socket's handlers. [@claim:clm_b5dab3224d5a180145c83dd60b76e1c69a61394b622dcdcde1d9e1f5e9240a33]
<!-- rcw:end owner=source:src_f6180115fcb65446b088bdc58b7c262d block=evidence -->

## Researcher notes

