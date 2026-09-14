---
access: public
aliases: []
claim_ids:
- clm_01752396b1ccfe249bbc9e001aa04632d3c86a52ea172df1eb3ea7c2202d9afa
- clm_1a33b045de0a3c6c45f517f8e8a18876af843afbab468e9a9d13e6c19b422d92
- clm_1d154453a3d2a065b5dc0be4753f65255c6d6a33ee52d97866fa539f3585ec9a
- clm_329ec64319076f47af34258aabab17cc65ce5a04a2bdbb1cc9c0e4e4ce45f4cc
- clm_3b79ecb91062a6902804265b671ed4ce2c97e3b8c12d7ccdb5a778223fbd0568
- clm_59ad139d782d94cd3b874e3fba55260ff56c6e91c1fd72e53beeabd56b60c1d2
- clm_ca60e5c3ef0f9ab99d3c9ddd1bcdbd0e08ba0cbbb30a558abd75e5c616a63b4b
- clm_e44a617bec0722403cbe152d547777196452afaf70fe83dcbc18690e9695307a
- clm_efa97550933afaf5bfec5c104f0877b5e194dc1d0a340cac5bc022abf6f77e2c
- clm_f00647ef4c22ca30723ccda44426414b23c0cf3d43fabce25784ebb54a7ac68d
- clm_f6229731514c737e08ffbbcf752f196592f9b3cd1ae9bcc77f22d0745878f895
- clm_f9d2aaefbba177aaedea5947a3fa1460cd124a4dc2647bc0af221020e471313b
maturity: draft
page_id: pg_e30de01fd20655f88b4b791080c5662d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e3a381606e05e21b6e75457b9b450f1
title: qodo-ai/open-aware/README.md @ 68976a9dd957
updated_at: '2026-09-14T04:17:12Z'
---

# qodo-ai/open-aware/README.md @ 68976a9dd957

<!-- rcw:begin owner=source:src_7e3a381606e05e21b6e75457b9b450f1 block=evidence -->
- The recommended MCP configuration points clients at the streamable HTTP endpoint https://open-aware.qodo.ai/mcp. [@claim:clm_01752396b1ccfe249bbc9e001aa04632d3c86a52ea172df1eb3ea7c2202d9afa]
- The free service covers only pre-indexed popular open-source libraries listed in indexed_repositories.json, with indexes updated daily; queries against unindexed repositories will not work. [@claim:clm_1a33b045de0a3c6c45f517f8e8a18876af843afbab468e9a9d13e6c19b422d92]
- An alternative connection method uses the mcp-remote npm package via npx as a proxy to the same remote MCP endpoint. [@claim:clm_1d154453a3d2a065b5dc0be4753f65255c6d6a33ee52d97866fa539f3585ec9a]
- deep_research analyzes code structure, patterns and relationships to answer or plan complex queries, accepting an input query, repository list, and session_id for conversation tracking. [@claim:clm_329ec64319076f47af34258aabab17cc65ce5a04a2bdbb1cc9c0e4e4ce45f4cc]
- The MCP server provides three tools: get_context for semantic code search, deep_research for complex codebase analysis, and ask for basic coding questions. [@claim:clm_3b79ecb91062a6902804265b671ed4ce2c97e3b8c12d7ccdb5a778223fbd0568]
- Open Aware exposes its code-intelligence capabilities through the Model Context Protocol, making it usable by any MCP-compatible AI assistant or development environment. [@claim:clm_59ad139d782d94cd3b874e3fba55260ff56c6e91c1fd72e53beeabd56b60c1d2]
- get_context performs semantic search using vector embeddings, supports multi-repository queries, language filtering, and configurable result limits with relevance ranking. [@claim:clm_ca60e5c3ef0f9ab99d3c9ddd1bcdbd0e08ba0cbbb30a558abd75e5c616a63b4b]
- Prompt examples recommend including the target repository name in the prompt to help the agent focus, and show patterns for invoking open-aware, deep-research, or get-context with a repositories list. [@claim:clm_e44a617bec0722403cbe152d547777196452afaf70fe83dcbc18690e9695307a]
- The free Open Aware tier is rate-limited to roughly 10 calls per minute, offers no private-repository access, and does not allow customization of indexing or tools. [@claim:clm_efa97550933afaf5bfec5c104f0877b5e194dc1d0a340cac5bc022abf6f77e2c]
- A separate enterprise product, Qodo Aware, adds private repository indexing, custom indexing schedules, zero data retention, and enterprise security and usage plans. [@claim:clm_f00647ef4c22ca30723ccda44426414b23c0cf3d43fabce25784ebb54a7ac68d]
- The ask tool accepts a query, a repository list, and a session_id, and answers basic coding questions about the selected repositories. [@claim:clm_f6229731514c737e08ffbbcf752f196592f9b3cd1ae9bcc77f22d0745878f895]
- The tool targets code discovery and analysis use cases such as architecture understanding, security analysis, feature planning, and cross-repository comparison, with an explicit disclaimer that outputs are provided as-is and require user review and security testing. [@claim:clm_f9d2aaefbba177aaedea5947a3fa1460cd124a4dc2647bc0af221020e471313b]
<!-- rcw:end owner=source:src_7e3a381606e05e21b6e75457b9b450f1 block=evidence -->

## Researcher notes

