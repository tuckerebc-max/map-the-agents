# c0sogi/llmchat -- full detail

[Back to orientation](llmchat.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/c0sogi/llmchat/01f53de6630e7302fc58f103b3fad382d8d270bc/c4528827ac059e0d.json](../../../wiki/dossiers/c0sogi/llmchat/01f53de6630e7302fc58f103b3fad382d8d270bc/c4528827ac059e0d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The project is described as a full-stack implementation with a Python FastAPI API server and a Flutter frontend for chatting with ChatGPT and other LLM models. -- evidence: [readme.md#L3-L6](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L3-L6) (`clm_b6f94438e21382c20a508ff7395b7350966126e7b6ef876d89dfe46bcb856a5b`)
- [observation/documented] Three LLM model types are supported: OpenAIModel (async chat completions via the OpenAI API), LlamaCppModel (local GGML .bin files), and ExllamaModel (local GPTQ model folders), all defined as LLMModel subclasses in app/models/llms.py. -- evidence: [readme.md#L307-L307](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L307-L307), [readme.md#L33-L41](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L33-L41), [readme.md#L316-L316](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L316-L316), [readme.md#L311-L312](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L311-L312), [readme.md#L294-L294](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L294-L294) (`clm_7e2c2389ea8f9ffd0f89f1abf6ab5515c7d559bd77377bfbab935b9321321606`)

## design-choices (1 claim(s))

- [observation/documented] Local LLMs are assumed to work only locally, hitting http://localhost:8002/v1/completions with a once-per-second health check that auto-starts the API server process if it is down; a Semaphore limits local LLM requests to one at a time. -- evidence: [readme.md#L46-L46](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L46-L46), [readme.md#L296-L296](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L296-L296) (`clm_ab41ed8182a2d5529ae4a2c46998b31a9c4560d0b77092d3bbab08c75f5c45ee`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Messages starting with '/' are treated as commands dispatched by a ChatCommands class; /embed stores text in a private Redis vector database, /share stores it publicly, and /query retrieves up to three similar results to ground AI answers. -- evidence: [readme.md#L25-L26](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L25-L26), [readme.md#L212-L212](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L212-L212), [readme.md#L242-L242](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L242-L242), [readme.md#L215-L215](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L215-L215) (`clm_5905e5047c84f8fdbb91ce12195f2bcc5463c8680d0f763758a289e787e7a3ac`)

## interfaces (2 claim(s))

- [observation/documented] Chat runs over a WebSocket route /chat/{api_key}; a valid server-registered API key (distinct from the OpenAI key) is checked on connect, and invalid keys or errors close the connection with a message. -- evidence: [readme.md#L155-L155](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L155-L155), [readme.md#L159-L159](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L159-L159), [readme.md#L157-L157](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L157-L157), [readme.md#L151-L151](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L151-L151) (`clm_f587b86a4362eb667266c3dc1d4e5f6dee0484abe923f5382fa2a13ebc945f8d`)
- [observation/documented] The Flutter web app is served at /chat, the API exposes docs at http://localhost:8000/docs, and running without Docker puts the server on http://localhost:8001. -- evidence: [readme.md#L125-L125](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L125-L125), [readme.md#L115-L115](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L115-L115), [readme.md#L151-L151](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L151-L151) (`clm_0624c75af59ff8833b2216af316dfc0101989a70f8bc7f78729dc7a86c82db09`)

## memory-state (2 claim(s))

- [observation/documented] A CacheManager stores user chat contexts and message histories in Redis, with methods to create, reset, read, append, pop, set, and delete per-role message histories. -- evidence: [readme.md#L336-L344](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L336-L344), [readme.md#L334-L334](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L334-L334) (`clm_2923994f95fc6e3d6439f2a24dc719d917e28c8c90567750e0dd9bb3ada05955`)
- [observation/documented] A MessageManager enforces token limits on message histories via safe add/pop/set methods that update token counts; a ChatLengthException triggers re-limiting via cutoff_message_histories and a resend. -- evidence: [readme.md#L350-L352](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L350-L352), [readme.md#L326-L326](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L326-L326), [readme.md#L348-L348](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L348-L348) (`clm_732e3044c865bc4b8c7254cfe000542cccfdfc9b22a23a2e5c75e9a2a1a7653b`)

## orchestration (1 claim(s))

- [observation/documented] Auto-summarization: after each user/AI exchange, a summarization task queued in BufferUserChatContext is harvested, and summaries replace original messages in LLM prompts to save tokens, without the user seeing the summarized text. -- evidence: [readme.md#L278-L278](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L278-L278), [readme.md#L276-L276](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L276-L276), [readme.md#L282-L282](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L282-L282), [readme.md#L280-L280](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L280-L280), [readme.md#L284-L284](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L284-L284) (`clm_02ab68b128fab07bb6e03e79b58e5454104490778be612430b6aa3864b369063`)

## tools-permissions (2 claim(s))

- [observation/documented] A 'Browse' toggle enables Duckduckgo web search so the assistant can find relevant web information during chat. -- evidence: [readme.md#L16-L17](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L16-L17), [readme.md#L60-L71](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L60-L71) (`clm_363b9959707c5252a6501aaa536c462305a9a931052c798a1ce2613ab33b8c4f`)
- [observation/documented] Access control uses a token_validator middleware validating API keys and JWT tokens, plus CORS and TrustedHost middlewares; the Validator returns a UserToken on success and errors raise HTTP exceptions. -- evidence: [readme.md#L420-L420](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L420-L420), [readme.md#L386-L386](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L386-L386), [readme.md#L415-L416](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L415-L416), [readme.md#L392-L394](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L392-L394), [readme.md#L408-L409](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L408-L409), [readme.md#L398-L398](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L398-L398) (`clm_ae0e22766efe4020ecad20458168d6cfa367ee061fc195bd80a6ca02127a2963`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack relies on FastAPI, Flutter, Langchain, Redis (aioredis), MySQL via sqlalchemy.asyncio, and Docker/docker-compose for deployment; Exllama and llama.cpp are included as git submodules. -- evidence: [readme.md#L81-L84](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L81-L84), [readme.md#L76-L77](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L76-L77), [readme.md#L60-L71](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L60-L71) (`clm_8d8c0ba3a0fbf0c28ed4da3ae8a18b91745d40e9a808e7bc7bcde7f033f80d66`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

