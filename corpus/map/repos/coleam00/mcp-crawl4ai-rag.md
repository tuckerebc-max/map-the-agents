# coleam00/mcp-crawl4ai-rag

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a1c16f675fe0 @ 4333432add921d38

## Summary (orientation draft, not independently verified)

README-documented MCP server combining Crawl4AI web crawling with Supabase-backed RAG, offering four core tools plus optional agentic-RAG and Neo4j knowledge-graph tools, five toggleable RAG strategy flags, and SSE/stdio transports.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The knowledge_graphs/ folder includes modules for parsing repos into Neo4j, AST-based script analysis, hallucination validation, report generation with confidence scores, and an interactive CLI query tool. -- evidence: [README.md#L417-L421](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L417-L421)
  - [observation/documented] The Neo4j schema stores Repository, File, Class, Method, Function, and Attribute nodes linked by CONTAINS, DEFINES, HAS_METHOD, and HAS_ATTRIBUTE relationships. -- evidence: [README.md#L427-L433](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L427-L433), [README.md#L435-L440](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L435-L440)
- design-choices (3 claim(s)):
  - [observation/documented] Five RAG strategies are independently toggleable via environment flags defaulting to false: contextual embeddings, hybrid search, agentic RAG, reranking, and knowledge graph. -- evidence: [README.md#L213-L213](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L213-L213), [README.md#L195-L199](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L195-L199)
  - [observation/documented] Hybrid search runs keyword and vector search in parallel and merges results, prioritizing documents appearing in both result sets. -- evidence: [README.md#L223-L223](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L223-L223)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: Database setup requires running the crawled_pages.sql script in the Supabase SQL editor to create tables and functions before starting the server. -- evidence: [README.md#L133-L133](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L133-L133), [README.md#L127-L127](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L127-L127), [README.md#L131-L131](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L131-L131)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The server exposes MCP tools crawl_single_page, smart_crawl_url, get_available_sources, and perform_rag_query, with search_code_examples available when USE_AGENTIC_RAG is true. -- evidence: [README.md#L64-L64](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L64-L64), [README.md#L57-L60](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L57-L60)
  - [observation/documented] With USE_KNOWLEDGE_GRAPH enabled, three additional tools are offered: parse_github_repository, check_ai_script_hallucinations, and query_knowledge_graph supporting commands like repos, classes, methods, and custom Cypher queries. -- evidence: [README.md#L68-L70](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L68-L70)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Runtime dependencies include Supabase for the vector database, an OpenAI API key for embeddings, and optionally Neo4j for knowledge-graph features; Docker or Python 3.12+ with uv for hosting. -- evidence: [README.md#L74-L78](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L74-L78)
  - [observation/documented] Reranking uses the local cross-encoder model cross-encoder/ms-marco-MiniLM-L-6-v2 on CPU with no additional API cost, adding roughly 100-200ms per query. -- evidence: [README.md#L238-L238](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L238-L238), [README.md#L240-L243](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L240-L243)
- limitations (1 claim(s)):
  - [observation/documented] The README states the knowledge graph implementation is not fully compatible with Docker yet and recommends running via uv for hallucination detection. -- evidence: [README.md#L139-L139](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L139-L139), [README.md#L246-L246](https://github.com/coleam00/mcp-crawl4ai-rag/blob/a1c16f675fe0ab1b0026f4ea1103cb205080792e/README.md#L246-L246)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](mcp-crawl4ai-rag.detail.md)

Metadata and full claim list: [full detail](mcp-crawl4ai-rag.detail.md)
Human notes ([notes](mcp-crawl4ai-rag.notes.md), never overwritten by build)

[Back to map index](../../index.md)
