# yuki-20/cornmcp

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 02db5a1f1133 @ a4098d183a7dad4f

## Summary (orientation draft, not independently verified)

The product is an MCP server exposing 18 tools over JSON-RPC via a Streamable HTTP /mcp endpoint, with Bearer-token API-key auth, plus a REST API and dashboard. The system comprises three services: corn-mcp on :8317, a Hono REST API (corn-api) on :4000 with SQLite, and a Next.js dashboard (corn-web) on :3000.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The system comprises three services: corn-mcp on :8317, a Hono REST API (corn-api) on :4000 with SQLite, and a Next.js dashboard (corn-web) on :3000. -- evidence: [README.md#L42-L47](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L42-L47), [README.md#L70-L72](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L70-L72), [README.md#L61-L68](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L61-L68), [README.md#L632-L636](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L632-L636)
  - [observation/documented] Tool modules cover memory, knowledge, code intelligence, quality, sessions, analytics, changes, and health, grouped into 18 named corn_* tools. -- evidence: [README.md#L192-L195](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L192-L195), [README.md#L202-L210](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L202-L210), [README.md#L222-L225](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L222-L225), [README.md#L217-L220](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L217-L220), [README.md#L49-L59](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L49-L59), [README.md#L212-L215](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L212-L215), [README.md#L197-L200](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L197-L200), [README.md#L227-L229](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L227-L229)
- design-choices (2 claim(s)):
  - [observation/documented] The MCP server is stateless: each request creates a fresh McpServer instance with no server-side session state. -- evidence: [README.md#L174-L178](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L174-L178)
  - [observation/documented] Quality gates enforce that plans score at least 80% before execution and quality reports must reach 80/100, per a five-phase session-to-end workflow. -- evidence: [README.md#L557-L578](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L557-L578), [README.md#L555-L555](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L555-L555), [README.md#L21-L26](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L21-L26)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is an MCP server exposing 18 tools over JSON-RPC via a Streamable HTTP /mcp endpoint, with Bearer-token API-key auth, plus a REST API and dashboard. -- evidence: [README.md#L36-L40](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L36-L40), [README.md#L42-L47](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L42-L47), [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L17-L17](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L17-L17)
  - [observation/documented] Code intelligence tools include corn_code_search, corn_code_read, corn_code_context, corn_code_impact (recursive-CTE blast radius), corn_cypher (Cypher-to-SQL), corn_detect_changes, and corn_list_repos. -- evidence: [README.md#L524-L532](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L524-L532), [README.md#L202-L210](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L202-L210), [README.md#L265-L284](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L265-L284)
- memory-state (1 claim(s)):
  - [observation/documented] Memory and knowledge tools embed content and store vectors in a local SQLite vector store (mem9-vectors.db) for cross-session semantic search. -- evidence: [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L84-L92](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L84-L92), [README.md#L61-L68](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L61-L68), [README.md#L21-L26](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L21-L26)
- orchestration (1 claim(s)):
  - [observation/documented] Every tool call is logged fire-and-forget to /api/metrics/query-log with tool name, status, latency, and input size, feeding the analytics dashboard; agents can also see each other's changes. -- evidence: [README.md#L42-L47](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L42-L47), [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L536-L542](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L536-L542), [README.md#L163-L164](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L163-L164), [README.md#L21-L26](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L21-L26)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports measured token-savings data from a 29-call live session (~137 tokens per tool call vs ~1,500 per standard file read) and projected savings of 30-87% by repo size. -- evidence: [README.md#L732-L732](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L732-L732), [README.md#L743-L748](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L743-L748), [README.md#L734-L739](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L734-L739), [README.md#L730-L730](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L730-L730)
- dependencies (1 claim(s)):
More evidence: [full detail](cornmcp.detail.md)

Metadata and full claim list: [full detail](cornmcp.detail.md)
Human notes ([notes](cornmcp.notes.md), never overwritten by build)

[Back to map index](../../index.md)
