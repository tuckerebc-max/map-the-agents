---
access: public
aliases: []
claim_ids:
- clm_1c26497e22b6c2a1adf5c72fb421130389719576176f439889d7789d0ba6bfef
- clm_3e89ef6519370e91cd18133768ecf48ea613ae356e5b9eec0a38cd060eba138a
- clm_9bd29ac93cfd95b40f97f92463ad2fb3ae8bfd2708344661fc49cbef39b1f8e7
- clm_b781dc566a6f4c7c518a18731a6c1a62497c274aa5e0eb70b53772607a3ecb6e
- clm_d00b1b71e808634fe8d50f904944659727f2b56d8487ddabd23f2bfac7780f6d
- clm_e1ac2e69d6a66b47aaf9bab86db25d9c066cce057e174ecb91a198063f3f56f1
maturity: draft
page_id: pg_12ccd07aecdd5c3b8a184645b5ab1cfa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_228b40f1f0955159828cecbb9c1c2854
title: coleam00/claude-memory-compiler/README.md @ 54eddd709e83
updated_at: '2026-09-14T05:00:40Z'
---

# coleam00/claude-memory-compiler/README.md @ 54eddd709e83

<!-- rcw:begin owner=source:src_228b40f1f0955159828cecbb9c1c2854 block=evidence -->
- Retrieval deliberately avoids RAG: no vector database or embeddings, just a markdown index file, on the rationale that at 50-500 articles an LLM reading a structured index outperforms cosine similarity. [@claim:clm_1c26497e22b6c2a1adf5c72fb421130389719576176f439889d7789d0ba6bfef]
- CLI commands include compile.py (with --all, --file, --dry-run flags), query.py with an optional --file-back flag that saves the answer as a qa/ article, and lint.py with --structural-only. [@claim:clm_3e89ef6519370e91cd18133768ecf48ea613ae356e5b9eec0a38cd060eba138a]
- Claude Code hooks (SessionEnd and PreCompact) capture the conversation transcript and spawn a background process using the Claude Agent SDK to extract decisions, lessons, patterns, and gotchas into a daily log. [@claim:clm_9bd29ac93cfd95b40f97f92463ad2fb3ae8bfd2708344661fc49cbef39b1f8e7]
- After 6 PM local time (COMPILE_AFTER_HOUR=18), a flush that detects a changed daily log spawns compile.py as a detached background process, giving once-daily automatic compilation without cron. [@claim:clm_b781dc566a6f4c7c518a18731a6c1a62497c274aa5e0eb70b53772607a3ecb6e]
- The system comprises hooks for capture, flush.py for SDK-based extraction, compile.py for building knowledge articles, query.py for index-guided retrieval, and lint.py running seven health checks. [@claim:clm_d00b1b71e808634fe8d50f904944659727f2b56d8487ddabd23f2bfac7780f6d]
- The index-guided retrieval approach is documented to break down at roughly 2,000+ articles (~2M+ tokens) when the index exceeds the context window, at which point hybrid RAG is suggested. [@claim:clm_e1ac2e69d6a66b47aaf9bab86db25d9c066cce057e174ecb91a198063f3f56f1]
<!-- rcw:end owner=source:src_228b40f1f0955159828cecbb9c1c2854 block=evidence -->

## Researcher notes

