---
access: public
aliases: []
claim_ids:
- clm_3a35abc0ab3886c491577e5428afa1e059f7c475970138a961f111750923fb56
- clm_410eeadab9a9b048927a2028c47e957cdbbbbf3257edf51cf73ab659ddc5e955
- clm_4d0d33b3d19d15a490dc413142a8253f34c807ea17b37ff3c25c282a85b44c74
- clm_4d0f083011863f5728f4354129479fe11e18c08aaa4aca9fbd4c93a4cf0924bf
- clm_520f54ca532d02a216d8f5b8e6315fafea568ace62a747186ed375a6af5b7e94
- clm_5280e2df4fdd745487c5c948e11ef64520db7c71d29424aa8094cc6601c5065a
- clm_52b2a6d0924693977e4520fce30b98f172bebb599ceb0d5bd0ed15039db38f41
- clm_58c0f27c4120df079fda8b4c48ce40d10dbdcad9802cd44e542f7ce3a55a0d79
- clm_a29750042a02082d9c8efc55eaa24d128ea90fa21bb813c68f30cc30023641ac
- clm_d624435eb0f1d70e5354ad13d8fe8e4ce0eae579dca448c886587106cbb67096
maturity: draft
page_id: pg_305c96871d3b509091d4dd7b516b925a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c04f058aecdf5c55811d7a446755f67f
title: entropy-research/Devon/README.md @ 8f68f1d74671
updated_at: '2026-09-14T01:48:12Z'
---

# entropy-research/Devon/README.md @ 8f68f1d74671

<!-- rcw:begin owner=source:src_c04f058aecdf5c55811d7a446755f67f block=evidence -->
- Running Devon requires node.js/npm, pipx, and at least one API key from Anthropic or OpenAI. [@claim:clm_3a35abc0ab3886c491577e5428afa1e059f7c475970138a961f111750923fb56]
- The agent is documented to only access files and folders in the directory it was started from, and users can correct it mid-action. [@claim:clm_410eeadab9a9b048927a2028c47e957cdbbbbf3257edf51cf73ab659ddc5e955]
- Documented limitations: minimal functionality for non-Python languages, sometimes needing to specify the target file, and immature local mode with significantly degraded performance. [@claim:clm_4d0d33b3d19d15a490dc413142a8253f34c807ea17b37ff3c25c282a85b44c74]
- The TUI offers a --debug mode and a --help flag listing available commands. [@claim:clm_4d0f083011863f5728f4354129479fe11e18c08aaa4aca9fbd4c93a4cf0924bf]
- The product collects basic event-type and failure telemetry, which users can disable by setting DEVON_TELEMETRY_DISABLED=true. [@claim:clm_520f54ca532d02a216d8f5b8e6315fafea568ace62a747186ed375a6af5b7e94]
- The product ships as a backend installed via pipx (devon_agent) with a main UI run through npx devon-ui. [@claim:clm_5280e2df4fdd745487c5c948e11ef64520db7c71d29424aa8094cc6601c5065a]
- The project appears to track agent performance via SWE-bench Lite, citing a past milestone of beating AutoCodeRover and a goal to set SOTA there. [@claim:clm_52b2a6d0924693977e4520fce30b98f172bebb599ceb0d5bd0ed15039db38f41]
- A terminal interface exists, installed globally via npm as devon-tui and launched with the devon-tui command. [@claim:clm_58c0f27c4120df079fda8b4c48ce40d10dbdcad9802cd44e542f7ce3a55a0d79]
- Windows support is not yet available; the README says the team is currently working on it. [@claim:clm_a29750042a02082d9c8efc55eaa24d128ea90fa21bb813c68f30cc30023641ac]
- Supported models include Claude 3.5 Sonnet, GPT4-o, Groq llama3-70b, and Ollama deepseek-coder:6.7b, with Gemini 1.5 Pro planned but unchecked. [@claim:clm_d624435eb0f1d70e5354ad13d8fe8e4ce0eae579dca448c886587106cbb67096]
<!-- rcw:end owner=source:src_c04f058aecdf5c55811d7a446755f67f block=evidence -->

## Researcher notes

