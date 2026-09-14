# coleam00/mcp-crawl4ai-rag -- full detail

[Back to orientation](mcp-crawl4ai-rag.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coleam00/mcp-crawl4ai-rag/a1c16f675fe0ab1b0026f4ea1103cb205080792e/4333432add921d38.json](../../../wiki/dossiers/coleam00/mcp-crawl4ai-rag/a1c16f675fe0ab1b0026f4ea1103cb205080792e/4333432add921d38.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The knowledge_graphs/ folder includes modules for parsing repos into Neo4j, AST-based script analysis, hallucination validation, report generation with confidence scores, and an interactive CLI query tool. -- evidence: [README.md#L417-L421](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L417-L421) (`clm_98219527e05031f69a1fe35d081a663d3687ef9d6c7b24a75813f22cba4ad013`)
- [observation/documented] The Neo4j schema stores Repository, File, Class, Method, Function, and Attribute nodes linked by CONTAINS, DEFINES, HAS_METHOD, and HAS_ATTRIBUTE relationships. -- evidence: [README.md#L427-L433](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L427-L433), [README.md#L435-L440](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L435-L440) (`clm_56435385a3328741d5cb78d3a970a2256bfee758f29b81e7e601bf1aa2922043`)

## design-choices (3 claim(s))

- [observation/documented] Five RAG strategies are independently toggleable via environment flags defaulting to false: contextual embeddings, hybrid search, agentic RAG, reranking, and knowledge graph. -- evidence: [README.md#L213-L213](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L213-L213), [README.md#L195-L199](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L195-L199) (`clm_04474dc4d3e768411db4d650c29b9fefb8de8023edea40f6525925b707388041`)
- [observation/documented] Hybrid search runs keyword and vector search in parallel and merges results, prioritizing documents appearing in both result sets. -- evidence: [README.md#L223-L223](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L223-L223) (`clm_6c311136013efb4f1bc13c3b833d58cb06f7d1027698a6a3a1521ce29fb768fe`)
- [observation/documented] Agentic RAG extracts code blocks of at least 300 characters with surrounding context, generates summaries, and stores them in a separate vector table for code search. -- evidence: [README.md#L230-L230](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L230-L230) (`clm_e32e2bf364798352d41caaa90267df84088e86b367c6c178b931344e7971a439`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: Database setup requires running the crawled_pages.sql script in the Supabase SQL editor to create tables and functions before starting the server. -- evidence: [README.md#L133-L133](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L133-L133), [README.md#L127-L127](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L127-L127), [README.md#L131-L131](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L131-L131) (`clm_35a43c81d55766956bd69b8001b65a87bf7acc19cfbe848f42388190a3095570`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The server exposes MCP tools crawl_single_page, smart_crawl_url, get_available_sources, and perform_rag_query, with search_code_examples available when USE_AGENTIC_RAG is true. -- evidence: [README.md#L64-L64](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L64-L64), [README.md#L57-L60](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L57-L60) (`clm_e9fd23d7e65b57558def707ef87116e686495ba19334e2e66474f44800abe93f`)
- [observation/documented] With USE_KNOWLEDGE_GRAPH enabled, three additional tools are offered: parse_github_repository, check_ai_script_hallucinations, and query_knowledge_graph supporting commands like repos, classes, methods, and custom Cypher queries. -- evidence: [README.md#L68-L70](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L68-L70) (`clm_384b780e297dd3c4d6f3b454e105a93319db6bc3b8f94bd470c90e9c9c0852c6`)
- [observation/documented] The server supports SSE transport (default port 8051, endpoint /sse) and stdio transport, with client configuration examples for MCP clients including Claude Desktop and Windsurf. -- evidence: [README.md#L358-L377](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L358-L377), [README.md#L356-L356](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L356-L356), [README.md#L184-L186](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L184-L186), [README.md#L324-L333](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L324-L333), [README.md#L335-L347](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L335-L347) (`clm_29fa2d4a1ebb350582d1e5d89cee8eaa84d1b669676c86091c01fbf7edb965db`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Runtime dependencies include Supabase for the vector database, an OpenAI API key for embeddings, and optionally Neo4j for knowledge-graph features; Docker or Python 3.12+ with uv for hosting. -- evidence: [README.md#L74-L78](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L74-L78) (`clm_ea51a4f5a7fcc5dc79bd5292fc855316878705c0aaeb5dfe42ed88ff67dd76d3`)
- [observation/documented] Reranking uses the local cross-encoder model cross-encoder/ms-marco-MiniLM-L-6-v2 on CPU with no additional API cost, adding roughly 100-200ms per query. -- evidence: [README.md#L238-L238](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L238-L238), [README.md#L240-L243](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L240-L243) (`clm_2b6460c501bf6b1a59079e9724c7fec7b0f3f03b3d9ae0c382a373a63bb5f1c8`)

## limitations (1 claim(s))

- [observation/documented] The README states the knowledge graph implementation is not fully compatible with Docker yet and recommends running via uv for hallucination detection. -- evidence: [README.md#L139-L139](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L139-L139), [README.md#L246-L246](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L246-L246) (`clm_01a34663b5764edd89773c08ae01a75c7bbcc3ecb819a9c407fa919c45a1a0bd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

