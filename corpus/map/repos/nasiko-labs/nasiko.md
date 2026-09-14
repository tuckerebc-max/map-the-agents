# nasiko-labs/nasiko

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ff3d89bf0789 @ 7860197f8ac0b7db

## Summary (orientation draft, not independently verified)

Nasiko is a single-process Rust control plane for deploying, routing, securing, and observing A2A v1.0-speaking agents, with an embedded OCI registry, MCP gateway, LLM router, and Postgres/Redis/S3 backing services. Evidence is mostly README and protocol documentation; no code inspection is available. Evidence coverage: 132 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Nasiko targets the A2A protocol v1.0 exactly, requiring the A2A-Version: 1.0 header on every request, and uses JSON-RPC 2.0 over HTTP(S) as its sole protocol binding with SSE for streaming. -- evidence: [docs/A2A_PROTOCOL.md#L54-L54](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L54-L54), [README.md#L212-L216](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L212-L216), [docs/A2A_PROTOCOL.md#L56-L60](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L56-L60)
- components (2 claim(s)):
  - [observation/documented] The workspace is organized into crates including server (Axum control plane), orchestrator (routing engine), mcp-gateway, llm-router, runtime (Docker via bollard), flow, secrets, oci, observability, agent-proxy, github, types, config, cli, and ui. -- evidence: [README.md#L512-L533](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L512-L533)
  - [observation/documented] Durable state lives in Postgres, Redis, and S3 (RustFS), with optional observability via Tempo, Loki, and the OTel Collector; the Docker-only quick start starts this full stack. -- evidence: [README.md#L131-L134](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L131-L134), [README.md#L244-L245](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L244-L245)
- design-choices (4 claim(s)):
  - [observation/documented] Nasiko runs as a single control-plane process with no separate gateway; every inter-agent call is proxied back through the server, which enforces flow limits, ACLs, and observability at one chokepoint. -- evidence: [README.md#L131-L134](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L131-L134), [docs/A2A_PROTOCOL.md#L46-L46](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L46-L46), [README.md#L101-L103](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L101-L103)
  - [observation/documented] Agents never receive direct public requests and never hold real API keys or tool credentials; they call back into the LLM Router via OPENAI_BASE_URL and the MCP Gateway instead. -- evidence: [README.md#L204-L206](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L204-L206), [README.md#L116-L128](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L116-L128)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use just recipes — just check (cargo check), just clippy with a zero-warnings policy, just test-unit for hermetic unit tests, and just test for unit plus integration tests requiring just infra. -- evidence: [README.md#L420-L425](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L420-L425)
  - [observation/documented] Repository development practice: the developer path (Path B) requires Rust, just, and Docker; just infra starts backing services, just dev runs the server with hot-reload via cargo-watch, and just run runs without hot-reload. -- evidence: [README.md#L410-L410](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L410-L410), [README.md#L403-L403](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L403-L403), [README.md#L398-L399](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L398-L399), [README.md#L415-L416](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L415-L416)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The nasiko CLI provides commands for connect, auth login, new, build/run, push/deploy, upload, ps, logs, lifecycle (stop/start/restart/scale), chat, secrets, mcp, observe, maf, registry, and github. -- evidence: [README.md#L466-L484](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L466-L484)
More evidence: [full detail](nasiko.detail.md)

Metadata and full claim list: [full detail](nasiko.detail.md)
Human notes ([notes](nasiko.notes.md), never overwritten by build)

[Back to map index](../../index.md)
