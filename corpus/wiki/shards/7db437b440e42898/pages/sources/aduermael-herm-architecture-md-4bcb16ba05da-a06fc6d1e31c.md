---
access: public
aliases: []
claim_ids:
- clm_460bc4a7c85cc5208096c198c47fa9c8b388d8da580cc30c8842d7c8b7ea5b72
- clm_51aa9be651617cb21e2f3882bff59532613a07a06d17d3e04efc7f2631d31630
maturity: draft
page_id: pg_2a54e1966a14570ca7e5a06fc6d1e31c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d65b8c7a2698566bb97fdfe51972a23a
title: aduermael/herm/ARCHITECTURE.md @ 4bcb16ba05da
updated_at: '2026-09-14T01:29:52Z'
---

# aduermael/herm/ARCHITECTURE.md @ 4bcb16ba05da

<!-- rcw:begin owner=source:src_d65b8c7a2698566bb97fdfe51972a23a block=evidence -->
- Configuration merges a global config (~/.herm/config.json, holding API keys, model, exploration, tool config, UI preferences) with a project-level .herm/config.json that can override model and tools. [@claim:clm_460bc4a7c85cc5208096c198c47fa9c8b388d8da580cc30c8842d7c8b7ea5b72]
- The CLI is a terminal TUI with an event loop selecting on stdin, agent events, and async results; agent events include Thinking, ToolCall, Approval, and Done, and sub-agent events continue to be drained after the main agent stops. [@claim:clm_51aa9be651617cb21e2f3882bff59532613a07a06d17d3e04efc7f2631d31630]
<!-- rcw:end owner=source:src_d65b8c7a2698566bb97fdfe51972a23a block=evidence -->

## Researcher notes

