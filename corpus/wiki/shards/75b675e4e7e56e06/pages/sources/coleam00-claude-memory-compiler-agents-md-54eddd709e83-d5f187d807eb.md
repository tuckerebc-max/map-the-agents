---
access: public
aliases: []
claim_ids:
- clm_3e89ef6519370e91cd18133768ecf48ea613ae356e5b9eec0a38cd060eba138a
- clm_9bd29ac93cfd95b40f97f92463ad2fb3ae8bfd2708344661fc49cbef39b1f8e7
- clm_b781dc566a6f4c7c518a18731a6c1a62497c274aa5e0eb70b53772607a3ecb6e
- clm_e1ac2e69d6a66b47aaf9bab86db25d9c066cce057e174ecb91a198063f3f56f1
maturity: draft
page_id: pg_2a310554c58d5e978a37d5f187d807eb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ba7f6c584d5a5e28af7e942aa9e69f3f
title: coleam00/claude-memory-compiler/AGENTS.md @ 54eddd709e83
updated_at: '2026-09-14T05:00:40Z'
---

# coleam00/claude-memory-compiler/AGENTS.md @ 54eddd709e83

<!-- rcw:begin owner=source:src_ba7f6c584d5a5e28af7e942aa9e69f3f block=evidence -->
- CLI commands include compile.py (with --all, --file, --dry-run flags), query.py with an optional --file-back flag that saves the answer as a qa/ article, and lint.py with --structural-only. [@claim:clm_3e89ef6519370e91cd18133768ecf48ea613ae356e5b9eec0a38cd060eba138a]
- Claude Code hooks (SessionEnd and PreCompact) capture the conversation transcript and spawn a background process using the Claude Agent SDK to extract decisions, lessons, patterns, and gotchas into a daily log. [@claim:clm_9bd29ac93cfd95b40f97f92463ad2fb3ae8bfd2708344661fc49cbef39b1f8e7]
- After 6 PM local time (COMPILE_AFTER_HOUR=18), a flush that detects a changed daily log spawns compile.py as a detached background process, giving once-daily automatic compilation without cron. [@claim:clm_b781dc566a6f4c7c518a18731a6c1a62497c274aa5e0eb70b53772607a3ecb6e]
- The index-guided retrieval approach is documented to break down at roughly 2,000+ articles (~2M+ tokens) when the index exceeds the context window, at which point hybrid RAG is suggested. [@claim:clm_e1ac2e69d6a66b47aaf9bab86db25d9c066cce057e174ecb91a198063f3f56f1]
<!-- rcw:end owner=source:src_ba7f6c584d5a5e28af7e942aa9e69f3f block=evidence -->

## Researcher notes

