---
access: public
aliases: []
claim_ids:
- clm_5366a4a13191dc83de1becc51c4a41ed544186f2a4060b0135f9198aa0c75489
- clm_578356617ec97a0d348c676410cb8e1332b8e53cbd3264af94b5f58fb8855bcc
- clm_65886b7a0b7ca92aaa7c3b9e783ee3791441b0643b4b04c3965a11504b16dc78
- clm_685300f577cc0943a7cea70792fb0bce36a7bc23c841dc22928f742f0200c116
- clm_8c80167e586d2e5227097dd9f204d893934dbbf1852539d1792c743d660e280d
- clm_aa12aa208a1ff22974cc318ae010668b8baf0dd422496c20ded7a076a57e66f6
maturity: draft
page_id: pg_6d5aeaa41f7857d685859de7bffb131c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_33e26a9f01ac56de837846bae379b816
title: aurasgit/public-agent-framwork/README.md @ f3f27582c6a2
updated_at: '2026-09-14T01:59:36Z'
---

# aurasgit/public-agent-framwork/README.md @ f3f27582c6a2

<!-- rcw:begin owner=source:src_33e26a9f01ac56de837846bae379b816 block=evidence -->
- The framework is designed to perform robustly with IBM Granite and Llama 3.x models, with optimization for other LLMs in progress. [@claim:clm_5366a4a13191dc83de1becc51c4a41ed544186f2a4060b0135f9198aa0c75489]
- Agent runs expose an observe method whose callback receives an emitter for streaming per-update events during execution. [@claim:clm_578356617ec97a0d348c676410cb8e1332b8e53cbd3264af94b5f58fb8855bcc]
- The framework is distributed as the npm package Auralia-agent-framework, installable with npm or yarn. [@claim:clm_65886b7a0b7ca92aaa7c3b9e783ee3791441b0643b4b04c3965a11504b16dc78]
- Agents are constructed with an LLM, memory, and tools, and executed via an async run method taking a prompt. [@claim:clm_685300f577cc0943a7cea70792fb0bce36a7bc23c841dc22928f742f0200c116]
- The framework ships modules including agents, llms, template (Mustache-based prompt templating), memory, tools, cache, errors, and adapters for different environments. [@claim:clm_8c80167e586d2e5227097dd9f204d893934dbbf1852539d1792c743d660e280d]
- LLM adapters include OllamaChatLLM, configurable with modelId, generation parameters, and an optional cache. [@claim:clm_aa12aa208a1ff22974cc318ae010668b8baf0dd422496c20ded7a076a57e66f6]
<!-- rcw:end owner=source:src_33e26a9f01ac56de837846bae379b816 block=evidence -->

## Researcher notes

