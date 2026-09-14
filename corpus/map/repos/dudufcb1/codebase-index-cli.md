# dudufcb1/codebase-index-cli

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8056926534bb @ 59d30715023ee86a

## Summary (orientation draft, not independently verified)

README-only evidence for codebase-index-cli, a Node.js/TypeScript CLI that indexes codebases with vector embeddings into SQLite-vec or Qdrant, with optional LLM-analyzed git commit tracking and Claude Code integration. No code or contributor-workflow evidence is present. Evidence coverage: 184 of 313 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project is described as modular, with an indexer core, workspace watcher, git commit watcher, commit LLM service, vector store implementations, embedders, and tree-sitter parsing modules. -- evidence: [README.md#L371-L377](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L371-L377)
- design-choices (2 claim(s)):
  - [observation/documented] Different embedders can be configured per vector store, with store-specific variables overriding a global fallback, e.g. a cheaper local model for SQLite and a larger one for Qdrant. -- evidence: [README.md#L106-L106](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L106-L106), [README.md#L123-L124](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L123-L124), [README.md#L127-L129](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L127-L129), [README.md#L108-L111](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L108-L111), [README.md#L117-L120](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L117-L120)
  - [observation/documented] The semantic-search command can rerank top vector hits with Voyage AI, configured via environment variables with fallbacks, and the rerank step is skipped automatically if no API key is set. -- evidence: [README.md#L169-L169](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L169-L169), [README.md#L171-L175](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L171-L175), [README.md#L177-L177](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L177-L177)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands including -start, -restart, -stats, -full-reset, -index-history <count>, and semantic-search with options like --collection, --limit, and --rerank. -- evidence: [README.md#L135-L140](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L135-L140)
  - [observation/documented] The vector store is selected by the wrapper command used: codesql for local SQLite-vec and codebase for a remote Qdrant server; codebase-index is a legacy compatibility wrapper. -- evidence: [README.md#L67-L70](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L67-L70), [README.md#L88-L88](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L88-L88)
- memory-state (1 claim(s)):
  - [observation/documented] Each workspace keeps state in .codebase/: state.json for collection and indexing status, cache.json for file hashes, and vectors.db for the SQLite-vec store; legacy files are migrated on first run. -- evidence: [README.md#L325-L325](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L325-L325), [README.md#L327-L329](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L327-L329), [README.md#L331-L331](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L331-L331)
- orchestration (1 claim(s)):
  - [observation/documented] When git tracking is enabled, the CLI watches the .git directory, detects commits, pulls, merges and branch changes, extracts metadata and diffs, sends context to an LLM, and indexes the analysis alongside code. -- evidence: [README.md#L189-L189](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L189-L189), [README.md#L191-L195](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L191-L195)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Embedding requires an OpenAI-compatible API (OpenAI, compatible endpoints, or Ollama with explicit dimension); Gemini, Anthropic, and non-OpenAI-compatible APIs are not supported. -- evidence: [README.md#L581-L581](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L581-L581), [README.md#L583-L589](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L583-L589), [README.md#L591-L594](https://github.com/dudufcb1/codebase-index-cli/blob/8056926534bbd6dbaf7f82b861b0eaa19d5d9746/README.md#L591-L594)
More evidence: [full detail](codebase-index-cli.detail.md)

Metadata and full claim list: [full detail](codebase-index-cli.detail.md)
Human notes ([notes](codebase-index-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
