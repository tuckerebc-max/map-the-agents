---
access: public
aliases: []
claim_ids:
- clm_061d969f711d921258787d17bb55eb538c4b88be8313511b5763ffa19342240c
- clm_0a17687afa11ca103f509ccfa23f8f74c52e055d89b9416cf9aa916473dfa0f3
- clm_1472a2d327a4a10c7db33eb840a1d53c4a3766deeb6f0b800f00298177e91c4c
- clm_34e17f71863776f344fe195c92924d20db7c4074ff7de6cda326a394b4260df0
- clm_378556347b3f70811a59a010e8818e530e29ea2f988331455d56142c08b1ec51
- clm_72e8b026f5814980f94e0f0da52ee12409a7a6d5b4b572dc6015125b7eaa8bf3
- clm_afe2f329b3968455daab45c63b955a463b7b39f933c1e9106ff9480356c1f9ea
- clm_d90c00299d4d226a53e117ec80780e58c98d17014906f89330a0d13effbbf2f5
maturity: draft
page_id: pg_deccef2493c3549d9f5651d85d2dd02d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_de0cdd2be5075a92859ff71c24a054d7
title: 2389-research/coven/docs/architecture.md @ 36edb5c206af
updated_at: '2026-09-14T01:26:25Z'
---

# 2389-research/coven/docs/architecture.md @ 36edb5c206af

<!-- rcw:begin owner=source:src_de0cdd2be5075a92859ff71c24a054d7 block=evidence -->
- Authorization is documented so agents can access only their own sessions, pack tools carry explicit permission scopes, and admin endpoints require separate authentication. [@claim:clm_061d969f711d921258787d17bb55eb538c4b88be8313511b5763ffa19342240c]
- The gRPC protocol defines a bidirectional AgentStream service; AgentMessage payloads are RegisterAgent, MessageResponse, and Heartbeat, while ServerMessage payloads are Welcome, SendMessage, and Shutdown. [@claim:clm_0a17687afa11ca103f509ccfa23f8f74c52e055d89b9416cf9aa916473dfa0f3]
- coven-swarm provides a supervisor command for multi-workspace orchestration, documented as spawning agents per workspace. [@claim:clm_1472a2d327a4a10c7db33eb840a1d53c4a3766deeb6f0b800f00298177e91c4c]
- The gateway stores threads (frontend-to-agent session mappings), messages (conversation history), and bindings (channel-to-agent routing) in SQLite; agents keep a local threads.db cache and session state. [@claim:clm_34e17f71863776f344fe195c92924d20db7c4074ff7de6cda326a394b4260df0]
- Agents register with the gateway over gRPC, receive a Welcome containing session_id and configuration, then send heartbeats every 30 seconds while the gateway tracks last_seen. [@claim:clm_378556347b3f70811a59a010e8818e530e29ea2f988331455d56142c08b1ec51]
- Crate dependencies are layered: coven-proto, coven-ssh, and coven-swarm-core have no internal deps; coven-agent depends on coven-core, coven-pack, coven-grpc, and coven-proto. [@claim:clm_72e8b026f5814980f94e0f0da52ee12409a7a6d5b4b572dc6015125b7eaa8bf3]
- Agent responses stream as ordered events: Thinking, Text, ToolUse, ToolResult, Done, and Error. [@claim:clm_afe2f329b3968455daab45c63b955a463b7b39f933c1e9106ff9480356c1f9ea]
- Agents use pluggable LLM backends behind an async Backend trait returning a stream of events; documented backends include MuxBackend (direct Anthropic API), DirectCliBackend (claude CLI subprocess), and AcpBackend. [@claim:clm_d90c00299d4d226a53e117ec80780e58c98d17014906f89330a0d13effbbf2f5]
<!-- rcw:end owner=source:src_de0cdd2be5075a92859ff71c24a054d7 block=evidence -->

## Researcher notes

