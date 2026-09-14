# dudufcb1/codebase-index-cli -- full detail

[Back to orientation](codebase-index-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dudufcb1/codebase-index-cli/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/59d30715023ee86a.json](../../../wiki/dossiers/dudufcb1/codebase-index-cli/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/59d30715023ee86a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project is described as modular, with an indexer core, workspace watcher, git commit watcher, commit LLM service, vector store implementations, embedders, and tree-sitter parsing modules. -- evidence: [README.md#L371-L377](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L371-L377) (`clm_c3435ee9a99bf7ad837357dedad0cefc1df12b0a0d45d9e78a4bfba5a5801b99`)

## design-choices (2 claim(s))

- [observation/documented] Different embedders can be configured per vector store, with store-specific variables overriding a global fallback, e.g. a cheaper local model for SQLite and a larger one for Qdrant. -- evidence: [README.md#L106-L106](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L106-L106), [README.md#L123-L124](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L123-L124), [README.md#L127-L129](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L127-L129), [README.md#L108-L111](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L108-L111), [README.md#L117-L120](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L117-L120) (`clm_3143cc4f0ba3faa7e26380645846b8635e6e7246f5f911b34194c583a8aee05c`)
- [observation/documented] The semantic-search command can rerank top vector hits with Voyage AI, configured via environment variables with fallbacks, and the rerank step is skipped automatically if no API key is set. -- evidence: [README.md#L169-L169](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L169-L169), [README.md#L171-L175](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L171-L175), [README.md#L177-L177](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L177-L177) (`clm_ab0aa1a973b0e3bf5d33444190183fc774eb188d5efe2f8286ed55d3f1a7cfbc`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands including -start, -restart, -stats, -full-reset, -index-history <count>, and semantic-search with options like --collection, --limit, and --rerank. -- evidence: [README.md#L135-L140](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L135-L140) (`clm_4dfa063fa687d3fab228f404db2275ab7816f98071486a29bc41a8143f0f0c55`)
- [observation/documented] The vector store is selected by the wrapper command used: codesql for local SQLite-vec and codebase for a remote Qdrant server; codebase-index is a legacy compatibility wrapper. -- evidence: [README.md#L67-L70](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L67-L70), [README.md#L88-L88](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L88-L88) (`clm_e7c72a9d2167f404953f430fe270c292c3f2d1021bd052c7adf6b6db6f970cd8`)
- [observation/documented] A companion MCP server project is referenced that queries indexes created by this CLI, offering code and commit-history search across MCP-compatible IDEs for both storage backends. -- evidence: [README.md#L762-L762](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L762-L762), [README.md#L764-L769](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L764-L769) (`clm_051563f04c911383ea3368da83f190cdf3fd637e9bc39de746e67461e3ed1611`)

## memory-state (1 claim(s))

- [observation/documented] Each workspace keeps state in .codebase/: state.json for collection and indexing status, cache.json for file hashes, and vectors.db for the SQLite-vec store; legacy files are migrated on first run. -- evidence: [README.md#L325-L325](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L325-L325), [README.md#L327-L329](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L327-L329), [README.md#L331-L331](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L331-L331) (`clm_0c6632fea12d0debe85a570aaeee56eab1841268050596f955a63652b0828dac`)

## orchestration (1 claim(s))

- [observation/documented] When git tracking is enabled, the CLI watches the .git directory, detects commits, pulls, merges and branch changes, extracts metadata and diffs, sends context to an LLM, and indexes the analysis alongside code. -- evidence: [README.md#L189-L189](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L189-L189), [README.md#L191-L195](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L191-L195) (`clm_13ddd0fcefebef76fa624191dd5dd0a77f3b909857a46a684b9df7d9ef683c40`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Embedding requires an OpenAI-compatible API (OpenAI, compatible endpoints, or Ollama with explicit dimension); Gemini, Anthropic, and non-OpenAI-compatible APIs are not supported. -- evidence: [README.md#L581-L581](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L581-L581), [README.md#L583-L589](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L583-L589), [README.md#L591-L594](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L591-L594) (`clm_8d7f93e45695b85799308466f96f25c399224490bf8c2a9f0fe583add61eed5c`)
- [observation/documented] Qdrant mode requires a running Qdrant server, e.g. via Docker on port 6333, while SQLite-vec mode needs no external services. -- evidence: [README.md#L98-L102](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L98-L102), [README.md#L91-L95](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L91-L95) (`clm_97bec9def58c1f1e8ff1c7b6d1ec26227d9a101ec8d4acfa23adbb7744323645`)

## limitations (2 claim(s))

- [observation/documented] Git commit tracking works only with Qdrant; the SQLite-vec schema is hardcoded for code chunks and lacks commit metadata fields such as author, branch, and hash. -- evidence: [README.md#L621-L621](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L621-L621), [README.md#L183-L185](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L183-L185) (`clm_0b1a23e4573bb529fd902376a0a2c44ca18c8e4d9c4a0e12b51f6ffd99094a46`)
- [observation/documented] Installation scripts for macOS and Windows are provided but explicitly untested; only Linux is marked as tested, and the author requests PRs from those who verify them. -- evidence: [README.md#L47-L51](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L47-L51), [README.md#L59-L59](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L59-L59), [README.md#L55-L57](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L55-L57) (`clm_d91fa3b0665c5f4d045afc935607e1f7fb27e1784d888143ea463b159711ef78`)

## relevance (1 claim(s))

- [observation/documented] The tool targets AI coding assistants like Claude Code, Cline, and Codex that lack native semantic search, acting as a lightweight semantic context engine with Claude Code hooks and status-line integration. -- evidence: [README.md#L15-L15](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L15-L15), [README.md#L13-L13](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L13-L13), [README.md#L17-L17](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L17-L17), [README.md#L23-L26](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L23-L26) (`clm_fa46a22c393c5d3dd474f9903753938e1812aca57d8289655a91c5b27587f59b`)

