# scarmonit/antigravity-jules-orchestration

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 49d26f81817c @ 9593a4b4c9beb21b

## Summary (orientation draft, not independently verified)

Documentation-only evidence describes a Node.js MCP server (v2.6.2) bridging AI assistants to the Jules API, with ~65 cataloged MCP tools, HTTP endpoints, slash commands, approval-gated orchestration, and Render deployment. Two prior claims overstated version numbers not present in their cited slices and were revised.

## Source coverage

Source coverage (partial): 6 of 49 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The system is a Node.js-based custom MCP server using Streamable HTTP transport, with Joi schemas for runtime input validation and a stateless architecture for compatibility with multiple MCP clients. -- evidence: [README.md#L25-L42](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L25-L42)
  - [observation/documented] The README catalogs 65 MCP tools across groups including Jules core (7), session management (5), batch processing (7), semantic memory (8), Render integration (12), Ollama LLM (4), and RAG (4). -- evidence: [README.md#L25-L42](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L25-L42)
- design-choices (2 claim(s)):
  - [observation/documented] Safety design includes approval gates requiring a 'Plan Approved' state before code modification, stricter approval for high-risk infra/auth tasks, and all Jules output delivered via pull requests for human review. -- evidence: [docs/reference/ARCHITECTURE.md#L56-L60](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L56-L60)
  - [observation/documented] Performance features include an LRU cache (100 items, 10s default TTL), a circuit breaker tripping after 5 consecutive failures with 60s reset, and retry logic with 3 exponential-backoff retries plus jitter. -- evidence: [README.md#L142-L144](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L142-L144)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run tests with npm test or node --test tests/unit/health.test.js, and health response format changes must update the health-check workflow and unit tests. -- evidence: [docs/api/API_REFERENCE.md#L171-L171](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L171-L171), [README.md#L155-L157](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L155-L157), [docs/api/API_REFERENCE.md#L71-L71](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L71-L71), [docs/api/API_REFERENCE.md#L180-L182](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L180-L182)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The server exposes HTTP endpoints including GET /health, GET /, GET /mcp/tools, POST /mcp/execute, GET /api/sessions/active, and GET /api/sessions/stats. -- evidence: [docs/api/API_REFERENCE.md#L9-L12](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L9-L12), [docs/api/API_REFERENCE.md#L157-L159](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L157-L159), [docs/api/API_REFERENCE.md#L163-L165](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L163-L165), [docs/api/API_REFERENCE.md#L89-L91](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L89-L91), [docs/api/API_REFERENCE.md#L118-L120](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L118-L120), [docs/api/API_REFERENCE.md#L132-L134](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L132-L134)
  - [observation/documented] POST /mcp/execute accepts a JSON body containing a tool name and a params object, and returns a tool-specific response based on the executed tool. -- evidence: [docs/api/API_REFERENCE.md#L149-L149](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L149-L149), [docs/api/API_REFERENCE.md#L138-L145](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L138-L145)
- memory-state (1 claim(s)):
  - [observation/documented] A semantic memory integration provides 8 MCP tools for persistent AI memory, with SSRF protection via a domain whitelist and error message sanitization. -- evidence: [README.md#L58-L60](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L58-L60)
- orchestration (3 claim(s)):
  - [observation/documented] The documented autonomous loop runs: user task initiation, Antigravity planning, Jules session creation via MCP, parallel execution, progress monitoring, approval gates, then merge/test completion. -- evidence: [README.md#L104-L110](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L104-L110)
More evidence: [full detail](antigravity-jules-orchestration.detail.md)

Metadata and full claim list: [full detail](antigravity-jules-orchestration.detail.md)
Human notes ([notes](antigravity-jules-orchestration.notes.md), never overwritten by build)

[Back to map index](../../index.md)
