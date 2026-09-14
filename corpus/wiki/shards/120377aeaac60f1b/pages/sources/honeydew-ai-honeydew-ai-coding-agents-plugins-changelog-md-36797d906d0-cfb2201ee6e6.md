---
access: public
aliases: []
claim_ids:
- clm_1bc47c994d43ff224e4c0e0b2db88fb2be7b3bc98418608bb6920fe662d92a4b
- clm_2a906f7fa72b7c6c0e561a1ba549193a9d800a50f6484e37a34c037faa77bc4e
maturity: draft
page_id: pg_268185d4a5c1537bbbeccfb2201ee6e6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4accc8e09612593dbd18f43f0c4d405c
title: honeydew-ai/honeydew-ai-coding-agents-plugins/CHANGELOG.md @ 36797d906d0a
updated_at: '2026-09-14T03:57:08Z'
---

# honeydew-ai/honeydew-ai-coding-agents-plugins/CHANGELOG.md @ 36797d906d0a

<!-- rcw:begin owner=source:src_4accc8e09612593dbd18f43f0c4d405c block=evidence -->
- PreToolUse hooks gate Honeydew MCP tool calls: query, exploration, and typed create/update calls are blocked once per session when the matching skill is not loaded, with the block naming the skill to load before the retry proceeds. [@claim:clm_1bc47c994d43ff224e4c0e0b2db88fb2be7b3bc98418608bb6920fe662d92a4b]
- The hook gating is designed to be non-wedging: a block fires at most once per skill so a retry always goes through, and uncertain cases such as a missing skill or unparseable payload let the call proceed. [@claim:clm_2a906f7fa72b7c6c0e561a1ba549193a9d800a50f6484e37a34c037faa77bc4e]
<!-- rcw:end owner=source:src_4accc8e09612593dbd18f43f0c4d405c block=evidence -->

## Researcher notes

