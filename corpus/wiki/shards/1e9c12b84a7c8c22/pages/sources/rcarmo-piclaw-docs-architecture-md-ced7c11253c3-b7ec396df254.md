---
access: public
aliases: []
claim_ids:
- clm_36f444dbdfd4e8cd2f1f0464101e4a1c22e9ba4f0d0de1d141d8f82bb7a8d0da
- clm_5c189280901a1fd0cd1d43e4bf18c2b610a9130e95a86cfb5a497d42b1bcfb1c
- clm_5e8378a6bd2fab34103934df4eaec20290c91397d58ce5f2ff3e8d5084ef6247
- clm_7fbcf5485c9cf90aed1ce709d3df7d04140a5f60641155f61f906461704a9d98
- clm_99795eb62a4baa9dfbf7b3ce1daf70030f4001df8cce3935375bb78940928d98
- clm_a384c5b7be6921687456c3a518688d235c6ce453a656fb8687c0ff554dc6627a
- clm_fa3e7d1dde6d50ddf70860dd3b2b54d7d695c2c7625b99fb18ef15c53972b5b7
maturity: draft
page_id: pg_5446193ca04553e98ca5b7ec396df254
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8c786200a2e55ab5ae377ca5c031f59b
title: rcarmo/piclaw/docs/architecture.md @ ced7c11253c3
updated_at: '2026-09-14T02:35:00Z'
---

# rcarmo/piclaw/docs/architecture.md @ ced7c11253c3

<!-- rcw:begin owner=source:src_8c786200a2e55ab5ae377ca5c031f59b block=evidence -->
- Dream/AutoDream memory consolidation runs as out-of-band model turns on a temporary dream: channel and a dedicated dream:<chatJid> queue lane, so long consolidations do not block interactive chat. [@claim:clm_36f444dbdfd4e8cd2f1f0464101e4a1c22e9ba4f0d0de1d141d8f82bb7a8d0da]
- Durable state lives in SQLite (messages, chats, tasks, configs, token usage), session trees, and a workspace holding notes, skills and files. [@claim:clm_5c189280901a1fd0cd1d43e4bf18c2b610a9130e95a86cfb5a497d42b1bcfb1c]
- Per-chat turns use a cursor with inflight and failed markers: transient failures recover automatically, while persistent failures roll the cursor back and hold the chat for explicit retry or skip. [@claim:clm_5e8378a6bd2fab34103934df4eaec20290c91397d58ce5f2ff3e8d5084ef6247]
- The runtime core comprises a router, a lane-aware AgentQueue, an AgentPool of Pi SDK AgentSessions, built-in and packaged extensions, and background workers for IPC, scheduling, and Dream memory consolidation. [@claim:clm_7fbcf5485c9cf90aed1ce709d3df7d04140a5f60641155f61f906461704a9d98]
- Multi-user family mode is experimental: family-shared deployments share one workspace and process without filesystem isolation, isolated-container mode is unavailable, and no family-mode release gate has passed. [@claim:clm_99795eb62a4baa9dfbf7b3ce1daf70030f4001df8cce3935375bb78940928d98]
- Single-user memory uses a compact notes/memory/MEMORY.md startup index (line-capped, under ~25KB) plus typed files for user, feedback, project and reference detail. [@claim:clm_a384c5b7be6921687456c3a518688d235c6ce453a656fb8687c0ff554dc6627a]
- Chat commands include /login for provider setup, /model for model selection, /dream for memory consolidation, /tasks and /scheduled for scheduled tasks, and /theme and /tint for UI theming. [@claim:clm_fa3e7d1dde6d50ddf70860dd3b2b54d7d695c2c7625b99fb18ef15c53972b5b7]
<!-- rcw:end owner=source:src_8c786200a2e55ab5ae377ca5c031f59b block=evidence -->

## Researcher notes

