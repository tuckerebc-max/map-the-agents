---
access: public
aliases: []
claim_ids:
- clm_02ab68b128fab07bb6e03e79b58e5454104490778be612430b6aa3864b369063
- clm_0624c75af59ff8833b2216af316dfc0101989a70f8bc7f78729dc7a86c82db09
- clm_2923994f95fc6e3d6439f2a24dc719d917e28c8c90567750e0dd9bb3ada05955
- clm_363b9959707c5252a6501aaa536c462305a9a931052c798a1ce2613ab33b8c4f
- clm_5905e5047c84f8fdbb91ce12195f2bcc5463c8680d0f763758a289e787e7a3ac
- clm_732e3044c865bc4b8c7254cfe000542cccfdfc9b22a23a2e5c75e9a2a1a7653b
- clm_7e2c2389ea8f9ffd0f89f1abf6ab5515c7d559bd77377bfbab935b9321321606
- clm_8d8c0ba3a0fbf0c28ed4da3ae8a18b91745d40e9a808e7bc7bcde7f033f80d66
- clm_ab41ed8182a2d5529ae4a2c46998b31a9c4560d0b77092d3bbab08c75f5c45ee
- clm_ae0e22766efe4020ecad20458168d6cfa367ee061fc195bd80a6ca02127a2963
- clm_b6f94438e21382c20a508ff7395b7350966126e7b6ef876d89dfe46bcb856a5b
- clm_f587b86a4362eb667266c3dc1d4e5f6dee0484abe923f5382fa2a13ebc945f8d
maturity: draft
page_id: pg_380c632c4bdc5755b9d009ea06c353eb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3b8897c7544e5491ba203ba894e6f210
title: c0sogi/LLMChat/readme.md @ 01f53de6630e
updated_at: '2026-09-14T03:39:54Z'
---

# c0sogi/LLMChat/readme.md @ 01f53de6630e

<!-- rcw:begin owner=source:src_3b8897c7544e5491ba203ba894e6f210 block=evidence -->
- Auto-summarization: after each user/AI exchange, a summarization task queued in BufferUserChatContext is harvested, and summaries replace original messages in LLM prompts to save tokens, without the user seeing the summarized text. [@claim:clm_02ab68b128fab07bb6e03e79b58e5454104490778be612430b6aa3864b369063]
- The Flutter web app is served at /chat, the API exposes docs at http://localhost:8000/docs, and running without Docker puts the server on http://localhost:8001. [@claim:clm_0624c75af59ff8833b2216af316dfc0101989a70f8bc7f78729dc7a86c82db09]
- A CacheManager stores user chat contexts and message histories in Redis, with methods to create, reset, read, append, pop, set, and delete per-role message histories. [@claim:clm_2923994f95fc6e3d6439f2a24dc719d917e28c8c90567750e0dd9bb3ada05955]
- A 'Browse' toggle enables Duckduckgo web search so the assistant can find relevant web information during chat. [@claim:clm_363b9959707c5252a6501aaa536c462305a9a931052c798a1ce2613ab33b8c4f]
- Messages starting with '/' are treated as commands dispatched by a ChatCommands class; /embed stores text in a private Redis vector database, /share stores it publicly, and /query retrieves up to three similar results to ground AI answers. [@claim:clm_5905e5047c84f8fdbb91ce12195f2bcc5463c8680d0f763758a289e787e7a3ac]
- A MessageManager enforces token limits on message histories via safe add/pop/set methods that update token counts; a ChatLengthException triggers re-limiting via cutoff_message_histories and a resend. [@claim:clm_732e3044c865bc4b8c7254cfe000542cccfdfc9b22a23a2e5c75e9a2a1a7653b]
- Three LLM model types are supported: OpenAIModel (async chat completions via the OpenAI API), LlamaCppModel (local GGML .bin files), and ExllamaModel (local GPTQ model folders), all defined as LLMModel subclasses in app/models/llms.py. [@claim:clm_7e2c2389ea8f9ffd0f89f1abf6ab5515c7d559bd77377bfbab935b9321321606]
- The stack relies on FastAPI, Flutter, Langchain, Redis (aioredis), MySQL via sqlalchemy.asyncio, and Docker/docker-compose for deployment; Exllama and llama.cpp are included as git submodules. [@claim:clm_8d8c0ba3a0fbf0c28ed4da3ae8a18b91745d40e9a808e7bc7bcde7f033f80d66]
- Local LLMs are assumed to work only locally, hitting http://localhost:8002/v1/completions with a once-per-second health check that auto-starts the API server process if it is down; a Semaphore limits local LLM requests to one at a time. [@claim:clm_ab41ed8182a2d5529ae4a2c46998b31a9c4560d0b77092d3bbab08c75f5c45ee]
- Access control uses a token_validator middleware validating API keys and JWT tokens, plus CORS and TrustedHost middlewares; the Validator returns a UserToken on success and errors raise HTTP exceptions. [@claim:clm_ae0e22766efe4020ecad20458168d6cfa367ee061fc195bd80a6ca02127a2963]
- The project is described as a full-stack implementation with a Python FastAPI API server and a Flutter frontend for chatting with ChatGPT and other LLM models. [@claim:clm_b6f94438e21382c20a508ff7395b7350966126e7b6ef876d89dfe46bcb856a5b]
- Chat runs over a WebSocket route /chat/{api_key}; a valid server-registered API key (distinct from the OpenAI key) is checked on connect, and invalid keys or errors close the connection with a message. [@claim:clm_f587b86a4362eb667266c3dc1d4e5f6dee0484abe923f5382fa2a13ebc945f8d]
<!-- rcw:end owner=source:src_3b8897c7544e5491ba203ba894e6f210 block=evidence -->

## Researcher notes

