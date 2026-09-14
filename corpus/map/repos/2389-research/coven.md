# 2389-research/coven

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 36edb5c206af @ 6601678b4e805296

## Summary (orientation draft, not independently verified)

Coven is a documented Rust agent-orchestration platform connecting Claude-powered agents to a Go gateway over bidirectional gRPC, with CLI/TUI/HTTP/Matrix frontends, pluggable LLM backends, and modular tool packs. Corrections: the swarm's per-subdirectory spawning mechanism, cargo-install build instructions, and registration-time metadata reporting were removed or re-scoped to what the cited slices actually state. Evidence coverage: 198 of 293 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Coven is described as a Rust-based platform for orchestrating AI agents with tool capabilities, connecting Claude-powered agents to a central gateway. -- evidence: [README.md#L3-L3](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L3-L3), [README.md#L7-L7](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] The project comprises a Rust monorepo (agents, CLI, TUI, packs), a Go gateway server for routing, storage and pack registry, and shared Protobuf definitions (coven-proto). -- evidence: [README.md#L54-L58](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L54-L58)
- design-choices (2 claim(s)):
  - [observation/documented] Agents use pluggable LLM backends behind an async Backend trait returning a stream of events; documented backends include MuxBackend (direct Anthropic API), DirectCliBackend (claude CLI subprocess), and AcpBackend. -- evidence: [docs/architecture.md#L163-L167](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L163-L167), [docs/architecture.md#L147-L147](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L147-L147), [docs/architecture.md#L151-L159](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L151-L159)
  - [observation/documented] Agent responses stream as ordered events: Thinking, Text, ToolUse, ToolResult, Done, and Error. -- evidence: [docs/architecture.md#L201-L208](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L201-L208)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: development uses make targets (check+test+clippy, build, release, test, clippy, fmt), and CLAUDE.md is referenced for detailed development guidelines. -- evidence: [README.md#L176-L182](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L176-L182), [README.md#L190-L190](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L190-L190)
  - [observation/documented] Repository development practice: components are built via make targets (make coven, make coven-agent, make coven-swarm) or installed with cargo install from crate paths; the gateway is built in a separate coven-gateway repository. -- evidence: [README.md#L78-L81](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L78-L81), [docs/cli.md#L12-L12](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/cli.md#L12-L12), [README.md#L87-L88](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L87-L88)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The gateway exposes an HTTP server with SSE events, a gRPC server for agent streams, and a pack service acting as a tool registry, backed by SQLite. -- evidence: [README.md#L16-L50](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/README.md#L16-L50)
  - [observation/documented] The gRPC protocol defines a bidirectional AgentStream service; AgentMessage payloads are RegisterAgent, MessageResponse, and Heartbeat, while ServerMessage payloads are Welcome, SendMessage, and Shutdown. -- evidence: [docs/architecture.md#L178-L185](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L178-L185), [docs/architecture.md#L187-L195](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L187-L195), [docs/architecture.md#L173-L176](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L173-L176)
- memory-state (2 claim(s)):
  - [observation/documented] The gateway stores threads (frontend-to-agent session mappings), messages (conversation history), and bindings (channel-to-agent routing) in SQLite; agents keep a local threads.db cache and session state. -- evidence: [docs/architecture.md#L214-L216](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L214-L216), [docs/architecture.md#L220-L221](https://github.com/2389-research/coven/blob/36edb5c206af9f6bfe92b73a5203da70d71ea614/docs/architecture.md#L220-L221)
More evidence: [full detail](coven.detail.md)

Metadata and full claim list: [full detail](coven.detail.md)
Human notes ([notes](coven.notes.md), never overwritten by build)

[Back to map index](../../index.md)
