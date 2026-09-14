# qodo-ai/open-aware -- full detail

[Back to orientation](open-aware.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/qodo-ai/open-aware/68976a9dd957f493a602b1063eaca553718c9254/c4920608ae287716.json](../../../wiki/dossiers/qodo-ai/open-aware/68976a9dd957f493a602b1063eaca553718c9254/c4920608ae287716.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The MCP server provides three tools: get_context for semantic code search, deep_research for complex codebase analysis, and ask for basic coding questions. -- evidence: [README.md#L114-L114](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L114-L114), [README.md#L35-L38](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L35-L38) (`clm_3b79ecb91062a6902804265b671ed4ce2c97e3b8c12d7ccdb5a778223fbd0568`)
- [observation/documented] get_context performs semantic search using vector embeddings, supports multi-repository queries, language filtering, and configurable result limits with relevance ranking. -- evidence: [README.md#L125-L129](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L125-L129), [README.md#L123-L123](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L123-L123) (`clm_ca60e5c3ef0f9ab99d3c9ddd1bcdbd0e08ba0cbbb30a558abd75e5c616a63b4b`)
- [observation/documented] deep_research analyzes code structure, patterns and relationships to answer or plan complex queries, accepting an input query, repository list, and session_id for conversation tracking. -- evidence: [README.md#L152-L152](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L152-L152), [README.md#L161-L172](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L161-L172) (`clm_329ec64319076f47af34258aabab17cc65ce5a04a2bdbb1cc9c0e4e4ce45f4cc`)
- [observation/documented] The ask tool accepts a query, a repository list, and a session_id, and answers basic coding questions about the selected repositories. -- evidence: [README.md#L181-L181](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L181-L181), [README.md#L183-L194](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L183-L194) (`clm_f6229731514c737e08ffbbcf752f196592f9b3cd1ae9bcc77f22d0745878f895`)

## design-choices (1 claim(s))

- [observation/documented] A separate enterprise product, Qodo Aware, adds private repository indexing, custom indexing schedules, zero data retention, and enterprise security and usage plans. -- evidence: [README.md#L49-L54](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L49-L54) (`clm_f00647ef4c22ca30723ccda44426414b23c0cf3d43fabce25784ebb54a7ac68d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Prompt examples recommend including the target repository name in the prompt to help the agent focus, and show patterns for invoking open-aware, deep-research, or get-context with a repositories list. -- evidence: [README.md#L210-L214](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L210-L214), [README.md#L223-L227](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L223-L227), [README.md#L202-L207](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L202-L207), [README.md#L217-L221](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L217-L221) (`clm_e44a617bec0722403cbe152d547777196452afaf70fe83dcbc18690e9695307a`)

## interfaces (3 claim(s))

- [observation/documented] Open Aware exposes its code-intelligence capabilities through the Model Context Protocol, making it usable by any MCP-compatible AI assistant or development environment. -- evidence: [README.md#L76-L76](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L76-L76), [README.md#L8-L8](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L8-L8) (`clm_59ad139d782d94cd3b874e3fba55260ff56c6e91c1fd72e53beeabd56b60c1d2`)
- [observation/documented] The recommended MCP configuration points clients at the streamable HTTP endpoint https://open-aware.qodo.ai/mcp. -- evidence: [README.md#L80-L88](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L80-L88) (`clm_01752396b1ccfe249bbc9e001aa04632d3c86a52ea172df1eb3ea7c2202d9afa`)
- [observation/documented] An alternative connection method uses the mcp-remote npm package via npx as a proxy to the same remote MCP endpoint. -- evidence: [README.md#L92-L94](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L92-L94), [README.md#L96-L108](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L96-L108) (`clm_1d154453a3d2a065b5dc0be4753f65255c6d6a33ee52d97866fa539f3585ec9a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The free service covers only pre-indexed popular open-source libraries listed in indexed_repositories.json, with indexes updated daily; queries against unindexed repositories will not work. -- evidence: [README.md#L202-L207](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L202-L207), [README.md#L35-L38](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L35-L38) (`clm_1a33b045de0a3c6c45f517f8e8a18876af843afbab468e9a9d13e6c19b422d92`)

## limitations (1 claim(s))

- [observation/documented] The free Open Aware tier is rate-limited to roughly 10 calls per minute, offers no private-repository access, and does not allow customization of indexing or tools. -- evidence: [README.md#L42-L43](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L42-L43), [README.md#L35-L38](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L35-L38) (`clm_efa97550933afaf5bfec5c104f0877b5e194dc1d0a340cac5bc022abf6f77e2c`)

## relevance (1 claim(s))

- [observation/documented] The tool targets code discovery and analysis use cases such as architecture understanding, security analysis, feature planning, and cross-repository comparison, with an explicit disclaimer that outputs are provided as-is and require user review and security testing. -- evidence: [README.md#L278-L289](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L278-L289), [README.md#L244-L248](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L244-L248), [README.md#L315-L319](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L315-L319), [README.md#L321-L321](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L321-L321) (`clm_f9d2aaefbba177aaedea5947a3fa1460cd124a4dc2647bc0af221020e471313b`)

