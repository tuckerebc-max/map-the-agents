---
access: public
aliases: []
claim_ids:
- clm_20c179e47db9836b54d2dc79d876bf1609cc2d97865a0bdb461879958c018297
- clm_5a63018ea5d561f99872f9d0ecac565cb1ee7447b76cffaf69283288a55d7e55
- clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46
maturity: draft
page_id: pg_822d73f26242505f99c0d86741df81b4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ab95da9aa3285a89928d35fb87e5a1ff
title: stippi/code-assistant/docs/context-compaction.md @ ba818a46c472
updated_at: '2026-09-14T02:43:45Z'
---

# stippi/code-assistant/docs/context-compaction.md @ ba818a46c472

<!-- rcw:begin owner=source:src_ab95da9aa3285a89928d35fb87e5a1ff block=evidence -->
- No agent-performance benchmark or eval harness appears in the provided slices; the only test-related evidence is unit/integration test coverage for features, which is development practice rather than agent evaluation. [@claim:clm_20c179e47db9836b54d2dc79d876bf1609cc2d97865a0bdb461879958c018297]
- Automatic context compaction was implemented: when prior assistant usage crosses the configured context-window threshold, a summary request is injected and the result is persisted as a user message tagged is_compaction_summary, with a collapsible UI banner. [@claim:clm_5a63018ea5d561f99872f9d0ecac565cb1ee7447b76cffaf69283288a55d7e55]
- The GUI is built on Zed's GPUI framework; the codebase is organized into crates including llm, code_assistant, and web, with the web crate already owning chromiumoxide for browser automation. [@claim:clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46]
<!-- rcw:end owner=source:src_ab95da9aa3285a89928d35fb87e5a1ff block=evidence -->

## Researcher notes

