---
access: public
aliases: []
claim_ids:
- clm_15f8ec13ee5359ea8690e7dfb31ad8dcfac2a6dcfd4af65768b22f72df2d2ff7
- clm_1e37dc74cd1552da872c60ae8a1ece9096b056815b23276d46a4d9c83fdeb6bc
- clm_213ffda20cbf0bdc27129dc3d62be16d4456a5ef389c588a9f3a9acd1762bd74
- clm_3598e885cb831f10108432e2d4a88b7d7605d6ba0e4bd1389076433a5872f99f
- clm_3fbca6bea362b50bf6c4ccbc5766289c32fdcb93e32222ee3645689acb81b63e
- clm_45e38a4d0f393aea915982867d1edd57f13573620a014344e60e514e65689eb0
- clm_6bda71cc905cb41164dc9178b6ee17073a090790c022d7331ad41f0b5bfbff6d
- clm_71b2dfd659e4cea00c24dd523412ed317d19e03b1529ce201383534c5d0f1595
- clm_83035c0fdba16ccc91cc8c8de54c760354427a7c62c4f1b7df484b384b19e252
- clm_aff685ce8f4f19acbe359901796eef84b04ee446153b2a3542c291ab033c8e9f
- clm_ca5ea900f083951a3e1974f90ad168d0943f256c8b11075777cf6c45edf56387
maturity: draft
page_id: pg_de16d7ae08da540eacedec2a0f13fcc3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6e4f6f7ffef15f47967b535dd3841d72
title: yuki-20/CornMCP/README.md @ 02db5a1f1133
updated_at: '2026-09-14T04:32:31Z'
---

# yuki-20/CornMCP/README.md @ 02db5a1f1133

<!-- rcw:begin owner=source:src_6e4f6f7ffef15f47967b535dd3841d72 block=evidence -->
- The README reports measured token-savings data from a 29-call live session (~137 tokens per tool call vs ~1,500 per standard file read) and projected savings of 30-87% by repo size. [@claim:clm_15f8ec13ee5359ea8690e7dfb31ad8dcfac2a6dcfd4af65768b22f72df2d2ff7]
- Embeddings use Voyage AI (voyage-code-3, 1024 dims) optionally; on rate limits the server rotates fallback models and ultimately falls back to local hash embeddings (256 dims). [@claim:clm_1e37dc74cd1552da872c60ae8a1ece9096b056815b23276d46a4d9c83fdeb6bc]
- Memory and knowledge tools embed content and store vectors in a local SQLite vector store (mem9-vectors.db) for cross-session semantic search. [@claim:clm_213ffda20cbf0bdc27129dc3d62be16d4456a5ef389c588a9f3a9acd1762bd74]
- Every tool call is logged fire-and-forget to /api/metrics/query-log with tool name, status, latency, and input size, feeding the analytics dashboard; agents can also see each other's changes. [@claim:clm_3598e885cb831f10108432e2d4a88b7d7605d6ba0e4bd1389076433a5872f99f]
- Quality gates enforce that plans score at least 80% before execution and quality reports must reach 80/100, per a five-phase session-to-end workflow. [@claim:clm_3fbca6bea362b50bf6c4ccbc5766289c32fdcb93e32222ee3645689acb81b63e]
- The system comprises three services: corn-mcp on :8317, a Hono REST API (corn-api) on :4000 with SQLite, and a Next.js dashboard (corn-web) on :3000. [@claim:clm_45e38a4d0f393aea915982867d1edd57f13573620a014344e60e514e65689eb0]
- The MCP server is stateless: each request creates a fresh McpServer instance with no server-side session state. [@claim:clm_6bda71cc905cb41164dc9178b6ee17073a090790c022d7331ad41f0b5bfbff6d]
- Code intelligence tools include corn_code_search, corn_code_read, corn_code_context, corn_code_impact (recursive-CTE blast radius), corn_cypher (Cypher-to-SQL), corn_detect_changes, and corn_list_repos. [@claim:clm_71b2dfd659e4cea00c24dd523412ed317d19e03b1529ce201383534c5d0f1595]
- Tool modules cover memory, knowledge, code intelligence, quality, sessions, analytics, changes, and health, grouped into 18 named corn_* tools. [@claim:clm_83035c0fdba16ccc91cc8c8de54c760354427a7c62c4f1b7df484b384b19e252]
- A native AST engine built on the TypeScript Compiler API parses .ts/.tsx/.js/.jsx files, extracting symbols and call/import/extends/implements edges into SQLite tables. [@claim:clm_aff685ce8f4f19acbe359901796eef84b04ee446153b2a3542c291ab033c8e9f]
- The product is an MCP server exposing 18 tools over JSON-RPC via a Streamable HTTP /mcp endpoint, with Bearer-token API-key auth, plus a REST API and dashboard. [@claim:clm_ca5ea900f083951a3e1974f90ad168d0943f256c8b11075777cf6c45edf56387]
<!-- rcw:end owner=source:src_6e4f6f7ffef15f47967b535dd3841d72 block=evidence -->

## Researcher notes

