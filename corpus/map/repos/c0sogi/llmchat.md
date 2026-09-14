# c0sogi/llmchat

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 01f53de6630e @ c4528827ac059e0d

## Summary (orientation draft, not independently verified)

LLMChat is a documented full-stack LLM chat product: a FastAPI backend with a Flutter frontend, WebSocket chat authenticated by server-registered API keys, OpenAI plus local LlamaCpp/Exllama models, Redis-backed vector embedding and context caching, auto-summarization, and token/JWT access-control middleware. Evidence coverage: 146 of 156 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The project is described as a full-stack implementation with a Python FastAPI API server and a Flutter frontend for chatting with ChatGPT and other LLM models. -- evidence: [readme.md#L3-L6](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L3-L6)
  - [observation/documented] Three LLM model types are supported: OpenAIModel (async chat completions via the OpenAI API), LlamaCppModel (local GGML .bin files), and ExllamaModel (local GPTQ model folders), all defined as LLMModel subclasses in app/models/llms.py. -- evidence: [readme.md#L307-L307](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L307-L307), [readme.md#L33-L41](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L33-L41), [readme.md#L316-L316](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L316-L316), [readme.md#L311-L312](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L311-L312), [readme.md#L294-L294](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L294-L294)
- design-choices (1 claim(s)):
  - [observation/documented] Local LLMs are assumed to work only locally, hitting http://localhost:8002/v1/completions with a once-per-second health check that auto-starts the API server process if it is down; a Semaphore limits local LLM requests to one at a time. -- evidence: [readme.md#L46-L46](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L46-L46), [readme.md#L296-L296](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L296-L296)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Messages starting with '/' are treated as commands dispatched by a ChatCommands class; /embed stores text in a private Redis vector database, /share stores it publicly, and /query retrieves up to three similar results to ground AI answers. -- evidence: [readme.md#L25-L26](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L25-L26), [readme.md#L212-L212](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L212-L212), [readme.md#L242-L242](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L242-L242), [readme.md#L215-L215](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L215-L215)
- interfaces (2 claim(s)):
  - [observation/documented] Chat runs over a WebSocket route /chat/{api_key}; a valid server-registered API key (distinct from the OpenAI key) is checked on connect, and invalid keys or errors close the connection with a message. -- evidence: [readme.md#L155-L155](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L155-L155), [readme.md#L159-L159](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L159-L159), [readme.md#L157-L157](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L157-L157), [readme.md#L151-L151](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L151-L151)
  - [observation/documented] The Flutter web app is served at /chat, the API exposes docs at http://localhost:8000/docs, and running without Docker puts the server on http://localhost:8001. -- evidence: [readme.md#L125-L125](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L125-L125), [readme.md#L115-L115](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L115-L115), [readme.md#L151-L151](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L151-L151)
- memory-state (2 claim(s)):
  - [observation/documented] A CacheManager stores user chat contexts and message histories in Redis, with methods to create, reset, read, append, pop, set, and delete per-role message histories. -- evidence: [readme.md#L336-L344](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L336-L344), [readme.md#L334-L334](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L334-L334)
  - [observation/documented] A MessageManager enforces token limits on message histories via safe add/pop/set methods that update token counts; a ChatLengthException triggers re-limiting via cutoff_message_histories and a resend. -- evidence: [readme.md#L350-L352](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L350-L352), [readme.md#L326-L326](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L326-L326), [readme.md#L348-L348](https://github.com/c0sogi/LLMChat/blob/01f53de6630e7302fc58f103b3fad382d8d270bc/readme.md#L348-L348)
- orchestration (1 claim(s)):
More evidence: [full detail](llmchat.detail.md)

Metadata and full claim list: [full detail](llmchat.detail.md)
Human notes ([notes](llmchat.notes.md), never overwritten by build)

[Back to map index](../../index.md)
