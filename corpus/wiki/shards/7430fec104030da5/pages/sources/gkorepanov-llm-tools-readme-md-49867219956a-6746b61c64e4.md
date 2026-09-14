---
access: public
aliases: []
claim_ids:
- clm_12d19271dfc920f21baf1fe644fa0568ed95a9ca4fe0d10c9f32355bd64ba5dd
- clm_52f50981951a2a209868ecf981b93327b8fb28f862fe92889e546da364cb500c
- clm_56c4f5020f3a450dc46aaa917a17ac19db7b2ab89aa90f83adfa53be4069f5f3
- clm_7407c05f5ff68c89eab7ab378bdebb10b997fdd6e45c5ac6be78e1060c108874
- clm_8169d6398e89f30b308fcd978634d37af491e34e82e1fd1a53cb4c681f6c97fb
- clm_825fed1aba3b0c3157d91b29dfaa6d7d4cf7fe13b5443e6c2eb99d0e61271da7
maturity: draft
page_id: pg_0456d7ac947052d7b6016746b61c64e4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4e39a2f3d65754bfa80fb2724d6b070b
title: gkorepanov/llm-tools/README.md @ 49867219956a
updated_at: '2026-09-14T03:53:44Z'
---

# gkorepanov/llm-tools/README.md @ 49867219956a

<!-- rcw:begin owner=source:src_4e39a2f3d65754bfa80fb2724d6b070b block=evidence -->
- The package includes input/output token accounting with price estimation, message conversion helpers, and UI translation utilities. [@claim:clm_12d19271dfc920f21baf1fe644fa0568ed95a9ca4fe0d10c9f32355bd64ba5dd]
- Model chains are built on LiteLLM, and the README states the package no longer uses LangChain. [@claim:clm_52f50981951a2a209868ecf981b93327b8fb28f862fe92889e546da364cb500c]
- The package is described as a small shared library for Voicebot's streamed LLM calls. [@claim:clm_56c4f5020f3a450dc46aaa917a17ac19db7b2ab89aa90f83adfa53be4069f5f3]
- Production model chains live in the bot's private configuration and are constructed by bot/parsing/generator.py, currently using Google Gemini as primary with OpenAI GPT-5.4 mini as fallback. [@claim:clm_7407c05f5ff68c89eab7ab378bdebb10b997fdd6e45c5ac6be78e1060c108874]
- It supports ordered fallback across configured model providers, plus empty-response and context-window error handling. [@claim:clm_8169d6398e89f30b308fcd978634d37af491e34e82e1fd1a53cb4c681f6c97fb]
- It provides LiteLLM-based async chat streaming with bounded initial-request and mid-stream retries. [@claim:clm_825fed1aba3b0c3157d91b29dfaa6d7d4cf7fe13b5443e6c2eb99d0e61271da7]
<!-- rcw:end owner=source:src_4e39a2f3d65754bfa80fb2724d6b070b block=evidence -->

## Researcher notes

