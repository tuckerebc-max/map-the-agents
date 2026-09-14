---
access: public
aliases: []
claim_ids:
- clm_0627396f53bb732fab4aa7cb2251eba29ac476cbcc12c43e518279ab4038d148
- clm_500e495548e065dc6510f5fc5d00ec13ee191168b77eb30c5b6e2580e54102c5
- clm_71f1e7e75d47a1ed76d68098a6acdb1a9c5186a9c3d658e97acb7f3f875af6a8
- clm_8b8e10eb1b1dca668dc9d9561f0c793eb70a15b39ed1a435f57dbe0adfa57706
- clm_b60fff4795f6952f6cdf6237a7b7e5638e5acc0ce5f36ad5be13cfcd59ec11fe
- clm_ef8bd9ef9c188d8e2b5829286fe2fef9bf5df1ae50b58225bad927a1ba859ab0
maturity: draft
page_id: pg_261b5ee0aa92586192a7051b14642970
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_95359247afe55783ba192756bd51b5e8
title: KADEAI/Kade/CHANGELOG.md @ 616148222f74
updated_at: '2026-09-14T04:48:39Z'
---

# KADEAI/Kade/CHANGELOG.md @ 616148222f74

<!-- rcw:begin owner=source:src_95359247afe55783ba192756bd51b5e8 block=evidence -->
- Known issues in the changelog include the native-protocol edit tool not live-streaming in the GUI, LobeHub MCP search being broken, and rare cases of dropped streams, tool output leaking into chat, and duplicating edit/write GUI blocks. [@claim:clm_0627396f53bb732fab4aa7cb2251eba29ac476cbcc12c43e518279ab4038d148]
- The changelog notes the Kiro provider currently supports only the Sonnet 4.5 model, working with both Trial and Pro accounts. [@claim:clm_500e495548e065dc6510f5fc5d00ec13ee191168b77eb30c5b6e2580e54102c5]
- Documentation claims each chat remembers its selected AI model across sessions and automatically restores it, allowing multiple models to run concurrently in different chat windows. [@claim:clm_71f1e7e75d47a1ed76d68098a6acdb1a9c5186a9c3d658e97acb7f3f875af6a8]
- The changelog states Markdown, XML, and CLI tool schemas were removed in favor of an overhauled native JSON system and a new 'Aero' schema allowing single-letter tool calls, which conflicts with the README's four-protocol claim. [@claim:clm_8b8e10eb1b1dca668dc9d9561f0c793eb70a15b39ed1a435f57dbe0adfa57706]
- The changelog says task history was moved from VS Code globalState (SQLite) to disk-based JSON storage at globalStorageUri/task_history.json, using an in-memory cache with debounced writes to reduce I/O. [@claim:clm_b60fff4795f6952f6cdf6237a7b7e5638e5acc0ce5f36ad5be13cfcd59ec11fe]
- The changelog records added skills support, including installing and enabling skills and installing skills from skills.sh via a marketplace tab. [@claim:clm_ef8bd9ef9c188d8e2b5829286fe2fef9bf5df1ae50b58225bad927a1ba859ab0]
<!-- rcw:end owner=source:src_95359247afe55783ba192756bd51b5e8 block=evidence -->

## Researcher notes

