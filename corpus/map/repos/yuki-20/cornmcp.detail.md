# yuki-20/cornmcp -- full detail

[Back to orientation](cornmcp.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yuki-20/cornmcp/02db5a1f113329a1ed700a6931634ec861bd6d8f/a4098d183a7dad4f.json](../../../wiki/dossiers/yuki-20/cornmcp/02db5a1f113329a1ed700a6931634ec861bd6d8f/a4098d183a7dad4f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The system comprises three services: corn-mcp on :8317, a Hono REST API (corn-api) on :4000 with SQLite, and a Next.js dashboard (corn-web) on :3000. -- evidence: [README.md#L42-L47](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L42-L47), [README.md#L70-L72](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L70-L72), [README.md#L61-L68](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L61-L68), [README.md#L632-L636](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L632-L636) (`clm_45e38a4d0f393aea915982867d1edd57f13573620a014344e60e514e65689eb0`)
- [observation/documented] Tool modules cover memory, knowledge, code intelligence, quality, sessions, analytics, changes, and health, grouped into 18 named corn_* tools. -- evidence: [README.md#L192-L195](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L192-L195), [README.md#L202-L210](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L202-L210), [README.md#L222-L225](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L222-L225), [README.md#L217-L220](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L217-L220), [README.md#L49-L59](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L49-L59), [README.md#L212-L215](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L212-L215), [README.md#L197-L200](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L197-L200), [README.md#L227-L229](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L227-L229) (`clm_83035c0fdba16ccc91cc8c8de54c760354427a7c62c4f1b7df484b384b19e252`)
- [observation/documented] A native AST engine built on the TypeScript Compiler API parses .ts/.tsx/.js/.jsx files, extracting symbols and call/import/extends/implements edges into SQLite tables. -- evidence: [README.md#L364-L369](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L364-L369), [README.md#L457-L457](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L457-L457), [README.md#L298-L303](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L298-L303), [README.md#L292-L296](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L292-L296), [README.md#L353-L360](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L353-L360), [README.md#L469-L487](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L469-L487), [README.md#L461-L465](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L461-L465) (`clm_aff685ce8f4f19acbe359901796eef84b04ee446153b2a3542c291ab033c8e9f`)

## design-choices (2 claim(s))

- [observation/documented] The MCP server is stateless: each request creates a fresh McpServer instance with no server-side session state. -- evidence: [README.md#L174-L178](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L174-L178) (`clm_6bda71cc905cb41164dc9178b6ee17073a090790c022d7331ad41f0b5bfbff6d`)
- [observation/documented] Quality gates enforce that plans score at least 80% before execution and quality reports must reach 80/100, per a five-phase session-to-end workflow. -- evidence: [README.md#L557-L578](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L557-L578), [README.md#L555-L555](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L555-L555), [README.md#L21-L26](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L21-L26) (`clm_3fbca6bea362b50bf6c4ccbc5766289c32fdcb93e32222ee3645689acb81b63e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is an MCP server exposing 18 tools over JSON-RPC via a Streamable HTTP /mcp endpoint, with Bearer-token API-key auth, plus a REST API and dashboard. -- evidence: [README.md#L36-L40](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L36-L40), [README.md#L42-L47](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L42-L47), [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L17-L17](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L17-L17) (`clm_ca5ea900f083951a3e1974f90ad168d0943f256c8b11075777cf6c45edf56387`)
- [observation/documented] Code intelligence tools include corn_code_search, corn_code_read, corn_code_context, corn_code_impact (recursive-CTE blast radius), corn_cypher (Cypher-to-SQL), corn_detect_changes, and corn_list_repos. -- evidence: [README.md#L524-L532](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L524-L532), [README.md#L202-L210](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L202-L210), [README.md#L265-L284](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L265-L284) (`clm_71b2dfd659e4cea00c24dd523412ed317d19e03b1529ce201383534c5d0f1595`)

## memory-state (1 claim(s))

- [observation/documented] Memory and knowledge tools embed content and store vectors in a local SQLite vector store (mem9-vectors.db) for cross-session semantic search. -- evidence: [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L84-L92](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L84-L92), [README.md#L61-L68](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L61-L68), [README.md#L21-L26](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L21-L26) (`clm_213ffda20cbf0bdc27129dc3d62be16d4456a5ef389c588a9f3a9acd1762bd74`)

## orchestration (1 claim(s))

- [observation/documented] Every tool call is logged fire-and-forget to /api/metrics/query-log with tool name, status, latency, and input size, feeding the analytics dashboard; agents can also see each other's changes. -- evidence: [README.md#L42-L47](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L42-L47), [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L536-L542](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L536-L542), [README.md#L163-L164](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L163-L164), [README.md#L21-L26](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L21-L26) (`clm_3598e885cb831f10108432e2d4a88b7d7605d6ba0e4bd1389076433a5872f99f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports measured token-savings data from a 29-call live session (~137 tokens per tool call vs ~1,500 per standard file read) and projected savings of 30-87% by repo size. -- evidence: [README.md#L732-L732](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L732-L732), [README.md#L743-L748](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L743-L748), [README.md#L734-L739](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L734-L739), [README.md#L730-L730](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L730-L730) (`clm_15f8ec13ee5359ea8690e7dfb31ad8dcfac2a6dcfd4af65768b22f72df2d2ff7`)

## dependencies (1 claim(s))

- [observation/documented] Embeddings use Voyage AI (voyage-code-3, 1024 dims) optionally; on rate limits the server rotates fallback models and ultimately falls back to local hash embeddings (256 dims). -- evidence: [README.md#L719-L722](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L719-L722), [README.md#L174-L178](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L174-L178), [README.md#L109-L117](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L109-L117), [README.md#L724-L724](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L724-L724), [README.md#L151-L156](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L151-L156), [README.md#L74-L76](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L74-L76), [README.md#L717-L717](https://github.com/yuki-20/CornMCP/blob/02db5a1f113329a1ed700a6931634ec861bd6d8f/README.md#L717-L717) (`clm_1e37dc74cd1552da872c60ae8a1ece9096b056815b23276d46a4d9c83fdeb6bc`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

