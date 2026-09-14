---
access: public
aliases: []
claim_ids:
- clm_27543b930701c920272a3b40b09909e94d0831ca67bb9b24d05503bb88d6a7f6
- clm_77e00c46cd02a6f9d08325b5d0bc0b50619912d6994148731918f78d584db585
- clm_86f277892e2f2221b21f5e995766cdb9f650b7a75d06db8aaee5d39ac928ab52
- clm_9b9395caa51b0c884f89e569ffc219122b021a5f0128953bb7d9258eafb9c376
- clm_ce1fbfb04a9709b6aa96cf5679f538def96df57b59f027a9981ae973bdb03a53
- clm_efd654a61f1bab9ba1b02582a6721c5b905b9d2071e2fbf0ad403f3b6407e6c4
maturity: draft
page_id: pg_972040a5bfbc5464a6b04911495816ad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6395b34e471355a897ba0d61b909fd3d
title: bombap/tiny-agent/src/runtimes/reactRuntime.ts @ 58ecae062ec6
updated_at: '2026-09-14T04:57:58Z'
---

# bombap/tiny-agent/src/runtimes/reactRuntime.ts @ 58ecae062ec6

<!-- rcw:begin owner=source:src_6395b34e471355a897ba0d61b909fd3d block=evidence -->
- The scratchpad is capped at 33 steps (oldest trimmed) and the message buffer at 33 messages with oldest-message eviction. [@claim:clm_27543b930701c920272a3b40b09909e94d0831ca67bb9b24d05503bb88d6a7f6]
- A ReactAgentRuntime class implements IAgentRuntime, holding an LLMEngine, tools, providers, clients, state, and a message buffer. [@claim:clm_77e00c46cd02a6f9d08325b5d0bc0b50619912d6994148731918f78d584db585]
- The runtime provides public methods to add clients, tools and providers, merge state updates, and disconnect all registered clients. [@claim:clm_86f277892e2f2221b21f5e995766cdb9f650b7a75d06db8aaee5d39ac928ab52]
- Each step builds a context from a React template and a system prompt from a personality template, generates text via the LLM engine, and parses a JSON block from the response. [@claim:clm_9b9395caa51b0c884f89e569ffc219122b021a5f0128953bb7d9258eafb9c376]
- Parsed responses append Thought/Action/Observation entries to a scratchpad; actions are matched to tools by name and executed with the action input, with unknown tools logged as an observation. [@claim:clm_ce1fbfb04a9709b6aa96cf5679f538def96df57b59f027a9981ae973bdb03a53]
- The runtime loops calling _step() until state.completed is set; with SAFE_MODE enabled it stops after MAX_STEPS steps (default 20 from the MAX_STEPS env var). [@claim:clm_efd654a61f1bab9ba1b02582a6721c5b905b9d2071e2fbf0ad403f3b6407e6c4]
<!-- rcw:end owner=source:src_6395b34e471355a897ba0d61b909fd3d block=evidence -->

## Researcher notes

