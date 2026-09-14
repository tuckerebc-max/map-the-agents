---
access: public
aliases: []
claim_ids:
- clm_0be1cc2ba787de562b79c51def908d2c4f4b1c78f3c0997d0795c4a4be830872
- clm_d5a030ee615a2e8d25aa434d10f704a5fbceca884ad6a6d07cef4f69cece19c6
- clm_e8831cd744a1b75fd08ac7668c8f462edb19b9c0b0de8f53568c6525dd424f50
maturity: draft
page_id: pg_ec204c9a2cdb52db98cb8d37ad7594a7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_236b147557c95192808d5fa4cf92dd32
title: rokoss21/iosm-cli/docs/acp-rpc-mapping.md @ 6cb971ca9c23
updated_at: '2026-09-14T03:12:36Z'
---

# rokoss21/iosm-cli/docs/acp-rpc-mapping.md @ 6cb971ca9c23

<!-- rcw:begin owner=source:src_236b147557c95192808d5fa4cf92dd32 block=evidence -->
- Unsupported ACP methods return JSON-RPC -32601 with reason=capability_not_supported; the ACP adapter is additive, leaving --mode rpc unchanged, and unsupported features fail with capability-level rejections rather than crashes. [@claim:clm_0be1cc2ba787de562b79c51def908d2c4f4b1c78f3c0997d0795c4a4be830872]
- ACP methods map to internal runtime actions: session start/prompt/steer/follow_up/abort/state, builtin slash command dispatch, resumable shell exec sessions with stdin writes, and permission bridge responses supporting scope=once|turn|session. [@claim:clm_d5a030ee615a2e8d25aa434d10f704a5fbceca884ad6a6d07cef4f69cece19c6]
- The product supports an ACP compatibility mode via --mode acp, with a documented acp.handshake returning protocol version and capabilities including streaming, permissionBridge, toolEvents, sessionLifecycle, backCompatRpc, and execSessions. [@claim:clm_e8831cd744a1b75fd08ac7668c8f462edb19b9c0b0de8f53568c6525dd424f50]
<!-- rcw:end owner=source:src_236b147557c95192808d5fa4cf92dd32 block=evidence -->

## Researcher notes

