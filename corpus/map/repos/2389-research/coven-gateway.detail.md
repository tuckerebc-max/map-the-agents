# 2389-research/coven-gateway -- full detail

[Back to orientation](coven-gateway.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/coven-gateway/11425046d196d7afc54e39101b48e921b8d48364/2bb9947e45a92f52.json](../../../wiki/dossiers/2389-research/coven-gateway/11425046d196d7afc54e39101b48e921b8d48364/2bb9947e45a92f52.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository layout includes an agent manager with connection registry and channel bindings, a gateway orchestrator with gRPC and HTTP API handlers, a config loader, and a SQLite persistence store. -- evidence: [README.md#L312-L332](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L312-L332) (`clm_1927dcf64aec32ce21111fbc053ca5a52e260bafec228141bd7986c6f4b089d0`)

## design-choices (2 claim(s))

- [observation/documented] Routing uses channel bindings that map frontend channels (e.g., Slack, Matrix) to specific agents for sticky agent assignment. -- evidence: [README.md#L205-L205](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L205-L205), [README.md#L90-L98](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L90-L98) (`clm_2c3b28d9db15231e4826b283f7baad112332ab89ab7b004a04998dfb1429c83a`)
- [observation/documented] SQLite persistence for threads and messages is implemented in pure Go without CGO, and the database path is configurable, including an in-memory option for testing. -- evidence: [README.md#L227-L228](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L227-L228), [README.md#L90-L98](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L90-L98) (`clm_6f4552093dfc4819b70703c4e690cfa18a763faf6a7289354f21332e5e96e1eb`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors build with make (proto plus binaries), run tests via go test ./... (optionally with -race), and can install pre-commit hooks running go fmt, go vet, go test, and go mod tidy. -- evidence: [README.md#L395-L395](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L395-L395), [README.md#L348-L348](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L348-L348), [README.md#L391-L392](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L391-L392), [README.md#L345-L345](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L345-L345), [README.md#L351-L351](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L351-L351) (`clm_60f633ba7bb8669426b272cdd46dc41f97f90ed0949912390425759dfd2055df`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Agents connect over a bidirectional gRPC stream to the AgentStream RPC of the coven.CovenControl service, defaulting to port 50051. -- evidence: [docs/AGENT_PROTOCOL.md#L53-L57](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L53-L57), [docs/AGENT_PROTOCOL.md#L49-L49](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L49-L49), [docs/AGENT_PROTOCOL.md#L47-L47](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L47-L47), [docs/AGENT_PROTOCOL.md#L51-L51](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L51-L51) (`clm_a011f7c81a9e1278e455a6f50311fd3981e913f586e8ebb6e42e8b6d73345da9`)
- [observation/documented] The gateway exposes an HTTP API on port 8080 with endpoints for listing agents, sending messages with SSE streaming responses, health/readiness checks, and channel-binding CRUD. -- evidence: [README.md#L191-L191](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L191-L191), [README.md#L217-L218](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L217-L218), [README.md#L214-L214](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L214-L214), [README.md#L209-L211](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L209-L211), [README.md#L199-L201](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L199-L201), [README.md#L194-L196](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L194-L196) (`clm_11c174646ea441616ad37e2461eef5f12563c89163630b1b52428ff0b7761350`)
- [observation/documented] Agent-to-gateway messages use an AgentMessage wrapper (register, response, heartbeat, injection_ack, execute_pack_tool) and gateway-to-agent messages use a ServerMessage wrapper (welcome, send_message, shutdown, tool_approval, inject_context, cancel_request, pack_tool_result, registration_error). -- evidence: [docs/AGENT_PROTOCOL.md#L223-L236](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L223-L236), [docs/AGENT_PROTOCOL.md#L63-L73](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L63-L73) (`clm_f1e6545c9d253fb6f03e4e8998182479064f125e8eb7ac791e80f06c6f65c845`)
- [observation/documented] On registration the gateway returns a Welcome message containing server and agent IDs, an instance ID, principal UUID, available pack tool definitions, an MCP token and endpoint, and resolved secrets for the agent. -- evidence: [docs/AGENT_PROTOCOL.md#L242-L253](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L242-L253) (`clm_afc8ade0ea6c85b25b4ef3e57dc11a9116bb41e606d958856d16ea0d58867ead`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The protocol includes a tool-approval flow: agents can request human approval for tool use, and the gateway replies with ToolApprovalResponse indicating approve, skip, or approve-all for the request. -- evidence: [docs/AGENT_PROTOCOL.md#L383-L387](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L383-L387), [docs/AGENT_PROTOCOL.md#L303-L309](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L303-L309), [docs/AGENT_PROTOCOL.md#L389-L399](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L389-L399), [docs/AGENT_PROTOCOL.md#L144-L163](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L144-L163) (`clm_4fe335e50ed11a94e8a7fd71b15ac2dba989a475fc560b4b74b26a3ebc499083`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building requires Go 1.22+, the protoc compiler, and proto generation expects the coven-agent repository checked out as a sibling directory; the project is MIT licensed. -- evidence: [README.md#L432-L432](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L432-L432), [README.md#L359-L359](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L359-L359), [README.md#L44-L46](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L44-L46) (`clm_c2ac3148178583ac309ce8e6cbbd29842dd95093d9f926c4897e70afe1877f92`)

## limitations (1 claim(s))

- [observation/documented] The README lists Slack frontend integration, Prometheus metrics, and mTLS agent authentication as planned rather than implemented, indicating these capabilities are not yet shipped in Phase 1. -- evidence: [README.md#L102-L104](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L102-L104) (`clm_bbfae7a8e419e3065d9568805753f398f9d4ea0b5681ec04bc6b6155913143e7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

