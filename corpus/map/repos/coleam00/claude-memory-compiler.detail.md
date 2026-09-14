# coleam00/claude-memory-compiler -- full detail

[Back to orientation](claude-memory-compiler.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coleam00/claude-memory-compiler/54eddd709e83d3be244e9c56c9fc3a6cf375d534/5943a91cc5cbb788.json](../../../wiki/dossiers/coleam00/claude-memory-compiler/54eddd709e83d3be244e9c56c9fc3a6cf375d534/5943a91cc5cbb788.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Claude Code hooks (SessionEnd and PreCompact) capture the conversation transcript and spawn a background process using the Claude Agent SDK to extract decisions, lessons, patterns, and gotchas into a daily log. -- evidence: [AGENTS.md#L361-L361](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L361-L361), [README.md#L5-L5](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L5-L5) (`clm_9bd29ac93cfd95b40f97f92463ad2fb3ae8bfd2708344661fc49cbef39b1f8e7`)
- [observation/documented] The system comprises hooks for capture, flush.py for SDK-based extraction, compile.py for building knowledge articles, query.py for index-guided retrieval, and lint.py running seven health checks. -- evidence: [README.md#L30-L34](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L30-L34) (`clm_d00b1b71e808634fe8d50f904944659727f2b56d8487ddabd23f2bfac7780f6d`)

## design-choices (1 claim(s))

- [observation/documented] Retrieval deliberately avoids RAG: no vector database or embeddings, just a markdown index file, on the rationale that at 50-500 articles an LLM reading a structured index outperforms cosine similarity. -- evidence: [README.md#L48-L48](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L48-L48), [README.md#L5-L5](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L5-L5) (`clm_1c26497e22b6c2a1adf5c72fb421130389719576176f439889d7789d0ba6bfef`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] CLI commands include compile.py (with --all, --file, --dry-run flags), query.py with an optional --file-back flag that saves the answer as a qa/ article, and lint.py with --structural-only. -- evidence: [AGENTS.md#L441-L441](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L441-L441), [AGENTS.md#L457-L461](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L457-L461), [AGENTS.md#L435-L439](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L435-L439), [AGENTS.md#L421-L427](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L421-L427), [README.md#L38-L44](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L38-L44) (`clm_3e89ef6519370e91cd18133768ecf48ea613ae356e5b9eec0a38cd060eba138a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] After 6 PM local time (COMPILE_AFTER_HOUR=18), a flush that detects a changed daily log spawns compile.py as a detached background process, giving once-daily automatic compilation without cron. -- evidence: [README.md#L20-L20](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L20-L20), [AGENTS.md#L371-L379](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L371-L379) (`clm_b781dc566a6f4c7c518a18731a6c1a62497c274aa5e0eb70b53772607a3ecb6e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The index-guided retrieval approach is documented to break down at roughly 2,000+ articles (~2M+ tokens) when the index exceeds the context window, at which point hybrid RAG is suggested. -- evidence: [README.md#L48-L48](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/README.md#L48-L48), [AGENTS.md#L518-L518](https://github.com/coleam00/claude-memory-compiler/blob/54eddd709e83d3be244e9c56c9fc3a6cf375d534/AGENTS.md#L518-L518) (`clm_e1ac2e69d6a66b47aaf9bab86db25d9c066cce057e174ecb91a198063f3f56f1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_8e3480b4087b5b0969d9240171eb776cc6a42ba8f7a35f5b7e6b29f22beef498, clm_ddf08fb63d0fd44d03965017ea4e1dfc8addc74711d2add130ee736252994c04

