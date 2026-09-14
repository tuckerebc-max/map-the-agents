# coleam00/claude-memory-compiler

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 54eddd709e83 @ 5943a91cc5cbb788

## Summary (orientation draft, not independently verified)

Claude Code hooks (SessionEnd and PreCompact) capture the conversation transcript and spawn a background process using the Claude Agent SDK to extract decisions, lessons, patterns, and gotchas into a daily log. The system comprises hooks for capture, flush.py for SDK-based extraction, compile.py for building knowledge articles, query.py for index-guided retrieval, and lint.py running seven health checks.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Claude Code hooks (SessionEnd and PreCompact) capture the conversation transcript and spawn a background process using the Claude Agent SDK to extract decisions, lessons, patterns, and gotchas into a daily log. -- evidence: [AGENTS.md#L361-L361](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L361-L361), [README.md#L5-L5](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L5-L5)
  - [observation/documented] The system comprises hooks for capture, flush.py for SDK-based extraction, compile.py for building knowledge articles, query.py for index-guided retrieval, and lint.py running seven health checks. -- evidence: [README.md#L30-L34](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L30-L34)
- design-choices (1 claim(s)):
  - [observation/documented] Retrieval deliberately avoids RAG: no vector database or embeddings, just a markdown index file, on the rationale that at 50-500 articles an LLM reading a structured index outperforms cosine similarity. -- evidence: [README.md#L48-L48](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L48-L48), [README.md#L5-L5](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L5-L5)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] CLI commands include compile.py (with --all, --file, --dry-run flags), query.py with an optional --file-back flag that saves the answer as a qa/ article, and lint.py with --structural-only. -- evidence: [AGENTS.md#L441-L441](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L441-L441), [AGENTS.md#L457-L461](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L457-L461), [AGENTS.md#L435-L439](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L435-L439), [AGENTS.md#L421-L427](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L421-L427), [README.md#L38-L44](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L38-L44)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] After 6 PM local time (COMPILE_AFTER_HOUR=18), a flush that detects a changed daily log spawns compile.py as a detached background process, giving once-daily automatic compilation without cron. -- evidence: [README.md#L20-L20](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L20-L20), [AGENTS.md#L371-L379](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L371-L379)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] The index-guided retrieval approach is documented to break down at roughly 2,000+ articles (~2M+ tokens) when the index exceeds the context window, at which point hybrid RAG is suggested. -- evidence: [README.md#L48-L48](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L48-L48), [AGENTS.md#L518-L518](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L518-L518)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](claude-memory-compiler.detail.md).

Metadata and full claim list: [full detail](claude-memory-compiler.detail.md)
Human notes ([notes](claude-memory-compiler.notes.md), never overwritten by build)

[Back to map index](../../index.md)
