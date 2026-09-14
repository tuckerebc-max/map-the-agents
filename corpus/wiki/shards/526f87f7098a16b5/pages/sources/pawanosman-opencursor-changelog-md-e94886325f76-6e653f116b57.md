---
access: public
aliases: []
claim_ids:
- clm_18a92481fcd303acc77449a11fedf537f35e4e4dd2b223dc62ea76b7814d3f74
- clm_8a09a8bd0ed738df9e74ee1516d0cfc4a8cd5626da635d01bc633af9d8a76def
- clm_bfc36574fabb6a845417e597142d0f07c6be8a6cf3ba6020812f19bfd4ec19b0
- clm_ce47e5c2fedfcb09ff4c69ca7391b07f168ee9d1a2b43cef400c6978e78aa6d6
- clm_ef6bc5e03dbaf197aa74ba4e3ec924b5254b884add5de1b693bd6e815e26b825
maturity: draft
page_id: pg_2e8b57deea05519699d66e653f116b57
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_220eded85b3158888bad771f96666f6a
title: PawanOsman/OpenCursor/CHANGELOG.md @ e94886325f76
updated_at: '2026-09-14T02:30:07Z'
---

# PawanOsman/OpenCursor/CHANGELOG.md @ e94886325f76

<!-- rcw:begin owner=source:src_220eded85b3158888bad771f96666f6a block=evidence -->
- The changelog documents per-tool hard timeouts, abort-signal support so Stop cancels mid-work, and configurable per-tool timeout seconds in Settings. [@claim:clm_18a92481fcd303acc77449a11fedf537f35e4e4dd2b223dc62ea76b7814d3f74]
- Context management includes auto-compaction with a verbatim tail, lossless persisted chat history for export, and latest-wins deduplication of older tool results for the same target. [@claim:clm_8a09a8bd0ed738df9e74ee1516d0cfc4a8cd5626da635d01bc633af9d8a76def]
- Project mode lets the agent act as a project lead delegating to a team of subagents (TeamDef presets), with subagents running on isolated history so the parent only receives the final Task result. [@claim:clm_bfc36574fabb6a845417e597142d0f07c6be8a6cf3ba6020812f19bfd4ec19b0]
- Shell commands run in their own child shell and kill child processes on termination, and denied commands are checked per sub-command to prevent chaining-based bypasses. [@claim:clm_ce47e5c2fedfcb09ff4c69ca7391b07f168ee9d1a2b43cef400c6978e78aa6d6]
- The semantic index persists across VS Code restarts, re-indexes incrementally on changed files, and auto-indexes new/modified files via a workspace file watcher; indexing can be fully disabled in settings. [@claim:clm_ef6bc5e03dbaf197aa74ba4e3ec924b5254b884add5de1b693bd6e815e26b825]
<!-- rcw:end owner=source:src_220eded85b3158888bad771f96666f6a block=evidence -->

## Researcher notes

