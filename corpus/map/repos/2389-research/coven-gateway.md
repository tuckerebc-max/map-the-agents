# 2389-research/coven-gateway

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 11425046d196 @ 2bb9947e45a92f52

## Summary (orientation draft, not independently verified)

Agents connect over a bidirectional gRPC stream to the AgentStream RPC of the coven.CovenControl service, defaulting to port 50051. The gateway exposes an HTTP API on port 8080 with endpoints for listing agents, sending messages with SSE streaming responses, health/readiness checks, and channel-binding CRUD. Evidence coverage: 170 of 361 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 69 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository layout includes an agent manager with connection registry and channel bindings, a gateway orchestrator with gRPC and HTTP API handlers, a config loader, and a SQLite persistence store. -- evidence: [README.md#L312-L332](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L312-L332)
- design-choices (2 claim(s)):
  - [observation/documented] Routing uses channel bindings that map frontend channels (e.g., Slack, Matrix) to specific agents for sticky agent assignment. -- evidence: [README.md#L205-L205](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L205-L205), [README.md#L90-L98](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L90-L98)
  - [observation/documented] SQLite persistence for threads and messages is implemented in pure Go without CGO, and the database path is configurable, including an in-memory option for testing. -- evidence: [README.md#L227-L228](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L227-L228), [README.md#L90-L98](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L90-L98)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors build with make (proto plus binaries), run tests via go test ./... (optionally with -race), and can install pre-commit hooks running go fmt, go vet, go test, and go mod tidy. -- evidence: [README.md#L395-L395](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L395-L395), [README.md#L348-L348](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L348-L348), [README.md#L391-L392](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L391-L392), [README.md#L345-L345](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L345-L345), [README.md#L351-L351](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L351-L351)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Agents connect over a bidirectional gRPC stream to the AgentStream RPC of the coven.CovenControl service, defaulting to port 50051. -- evidence: [docs/AGENT_PROTOCOL.md#L53-L57](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L53-L57), [docs/AGENT_PROTOCOL.md#L49-L49](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L49-L49), [docs/AGENT_PROTOCOL.md#L47-L47](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L47-L47), [docs/AGENT_PROTOCOL.md#L51-L51](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L51-L51)
  - [observation/documented] The gateway exposes an HTTP API on port 8080 with endpoints for listing agents, sending messages with SSE streaming responses, health/readiness checks, and channel-binding CRUD. -- evidence: [README.md#L191-L191](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L191-L191), [README.md#L217-L218](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L217-L218), [README.md#L214-L214](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L214-L214), [README.md#L209-L211](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L209-L211), [README.md#L199-L201](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L199-L201), [README.md#L194-L196](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L194-L196)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The protocol includes a tool-approval flow: agents can request human approval for tool use, and the gateway replies with ToolApprovalResponse indicating approve, skip, or approve-all for the request. -- evidence: [docs/AGENT_PROTOCOL.md#L383-L387](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L383-L387), [docs/AGENT_PROTOCOL.md#L303-L309](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L303-L309), [docs/AGENT_PROTOCOL.md#L389-L399](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L389-L399), [docs/AGENT_PROTOCOL.md#L144-L163](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/docs/AGENT_PROTOCOL.md#L144-L163)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Building requires Go 1.22+, the protoc compiler, and proto generation expects the coven-agent repository checked out as a sibling directory; the project is MIT licensed. -- evidence: [README.md#L432-L432](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L432-L432), [README.md#L359-L359](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L359-L359), [README.md#L44-L46](https://github.com/2389-research/coven-gateway/blob/11425046d196d7afc54e39101b48e921b8d48364/README.md#L44-L46)
More evidence: [full detail](coven-gateway.detail.md)

Metadata and full claim list: [full detail](coven-gateway.detail.md)
Human notes ([notes](coven-gateway.notes.md), never overwritten by build)

[Back to map index](../../index.md)
