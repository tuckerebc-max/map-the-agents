---
access: public
aliases: []
claim_ids:
- clm_4fe335e50ed11a94e8a7fd71b15ac2dba989a475fc560b4b74b26a3ebc499083
- clm_a011f7c81a9e1278e455a6f50311fd3981e913f586e8ebb6e42e8b6d73345da9
- clm_afc8ade0ea6c85b25b4ef3e57dc11a9116bb41e606d958856d16ea0d58867ead
- clm_f1e6545c9d253fb6f03e4e8998182479064f125e8eb7ac791e80f06c6f65c845
maturity: draft
page_id: pg_cf8d507942ac57459725ab386be220e1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fc274a5c209e585a890e1d331284d5fb
title: 2389-research/coven-gateway/docs/AGENT_PROTOCOL.md @ 11425046d196
updated_at: '2026-09-14T04:41:43Z'
---

# 2389-research/coven-gateway/docs/AGENT_PROTOCOL.md @ 11425046d196

<!-- rcw:begin owner=source:src_fc274a5c209e585a890e1d331284d5fb block=evidence -->
- The protocol includes a tool-approval flow: agents can request human approval for tool use, and the gateway replies with ToolApprovalResponse indicating approve, skip, or approve-all for the request. [@claim:clm_4fe335e50ed11a94e8a7fd71b15ac2dba989a475fc560b4b74b26a3ebc499083]
- Agents connect over a bidirectional gRPC stream to the AgentStream RPC of the coven.CovenControl service, defaulting to port 50051. [@claim:clm_a011f7c81a9e1278e455a6f50311fd3981e913f586e8ebb6e42e8b6d73345da9]
- On registration the gateway returns a Welcome message containing server and agent IDs, an instance ID, principal UUID, available pack tool definitions, an MCP token and endpoint, and resolved secrets for the agent. [@claim:clm_afc8ade0ea6c85b25b4ef3e57dc11a9116bb41e606d958856d16ea0d58867ead]
- Agent-to-gateway messages use an AgentMessage wrapper (register, response, heartbeat, injection_ack, execute_pack_tool) and gateway-to-agent messages use a ServerMessage wrapper (welcome, send_message, shutdown, tool_approval, inject_context, cancel_request, pack_tool_result, registration_error). [@claim:clm_f1e6545c9d253fb6f03e4e8998182479064f125e8eb7ac791e80f06c6f65c845]
<!-- rcw:end owner=source:src_fc274a5c209e585a890e1d331284d5fb block=evidence -->

## Researcher notes

