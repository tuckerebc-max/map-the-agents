---
access: public
aliases: []
claim_ids:
- clm_09ab4cfcdae81b1ed767c2a3e3c2cc7d3a879a94748cda7c9e45ce9f299020f5
- clm_17d251135130b3e5c741a1c668b4f49c9d629b534c35a798b1cb6e707e0e0be9
- clm_e8f9155826918265d0ad81b68611780ed6b6007bf7a3dbb963166ea15183ae55
maturity: draft
page_id: pg_e3d50737eaf25d168f71f71d0dcd3b06
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e013041a81735954904485f869b363ff
title: andrefetch/postal/docs/tools.md @ 240622b0c2dc
updated_at: '2026-09-14T01:33:24Z'
---

# andrefetch/postal/docs/tools.md @ 240622b0c2dc

<!-- rcw:begin owner=source:src_e013041a81735954904485f869b363ff block=evidence -->
- The main agent can delegate to five specialized sub-agents (codebase_investigator, code_reviewer, software_architect, test_writer, debugger), each running its own loop with a narrowed tool set and turn cap; sub-agent runs are never checkpointed. [@claim:clm_09ab4cfcdae81b1ed767c2a3e3c2cc7d3a879a94748cda7c9e45ce9f299020f5]
- Context handling uses two loop-side mechanisms: pruning clears stale tool outputs to reclaim tokens, and compaction summarizes history into a continuation brief when the context window fills, instead of erroring out. [@claim:clm_17d251135130b3e5c741a1c668b4f49c9d629b534c35a798b1cb6e707e0e0be9]
- Built-in tools include file operations (read, write, edit, apply_patch, grep, glob, list_directories), bash, a plan todo-list tool, DuckDuckGo-backed web search, URL fetching, and cross-session key-value memory. [@claim:clm_e8f9155826918265d0ad81b68611780ed6b6007bf7a3dbb963166ea15183ae55]
<!-- rcw:end owner=source:src_e013041a81735954904485f869b363ff block=evidence -->

## Researcher notes

