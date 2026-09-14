# lnyo-cly/ai4j -- full detail

[Back to orientation](ai4j.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lnyo-cly/ai4j/ba6b7973853560e961bca34f2a94d537929b2082/5d55cba7d712ee44.json](../../../wiki/dossiers/lnyo-cly/ai4j/ba6b7973853560e961bca34f2a94d537929b2082/5d55cba7d712ee44.json)

## specifications (2 claim(s))

- [observation/documented] ai4j is described as a Java AI agentic development kit targeting JDK 8+, unifying model access, tool calling, MCP, A2A, RAG, an agent runtime, and a built-in coding agent CLI/TUI/ACP. -- evidence: [README.md#L6-L6](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L6-L6), [README.md#L1-L2](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L1-L2) (`clm_07759a5cd6b185b62c473dc2eb8a5d6ff6cb2daafdf35e419523877dbb8b05e8`)
- [observation/documented] The project is licensed under Apache License 2.0 and links to a GitHub Pages documentation site plus guides for the coding agent CLI and A2A protocol. -- evidence: [README.md#L55-L58](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L55-L58), [README.md#L66-L66](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L66-L66) (`clm_c760938c3b0a83108dcddfa13dc926a4fd65f483edf40fe75c8c0c4487448d11`)

## components (1 claim(s))

- [observation/documented] Supported platforms listed include OpenAI and compatible APIs, Anthropic, DashScope, Doubao, DeepSeek, Moonshot, Zhipu, Hunyuan, Lingyi, Ollama, MiniMax, Baichuan, and Suno, plus rerank providers, AgentFlow (Dify/Coze/n8n), and vector stores (Pinecone, Qdrant, pgvector, Milvus, Redis). -- evidence: [README.md#L62-L62](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L62-L62) (`clm_b85a30327e058ec9ea787a242a7399706ec90e7de41e3215aa47601639beb550`)

## design-choices (1 claim(s))

- [observation/documented] Switching providers such as DashScope, DeepSeek, or Ollama is presented as changing only the PlatformType and corresponding config object while the rest of the calling code stays unchanged. -- evidence: [README.md#L51-L51](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L51-L51) (`clm_35bee78282a7d8ee3daf4ae6bc8a57353fcfe2f9d824ba90f3fb0ee1486f9e26`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The quickstart flow: build an OpenAiConfig with an API key from OPENAI_API_KEY, wrap it in a Configuration, obtain an IChatService from AiService via PlatformType.OPENAI, then send a ChatCompletion built with a model name and user message. -- evidence: [README.md#L19-L44](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L19-L44), [README.md#L17-L17](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L17-L17) (`clm_952fc25793abeafe9773dc4a4b4010bb176208e945ff9c3e517c55da72f0e0e3`)
- [observation/documented] APIResponse.md documents that Ollama's deepseek-r1 streams thinking and answer content together in the content field, with thinking wrapped in <think> tags, unlike qwen3 which places reasoning in a separate thinking field. -- evidence: [APIResponse.md#L28-L29](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L28-L29), [APIResponse.md#L48-L49](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L48-L49) (`clm_599285ba2a501176851a2d026b93ac9a935e92d3c18b9fb5b12a562e24ec09a0`)
- [observation/documented] Documented Ollama qwen3 streaming shows tool_calls arriving complete within a single data chunk, including function name and arguments, requiring no extra concatenation. -- evidence: [APIResponse.md#L52-L61](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L52-L61), [APIResponse.md#L63-L65](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L63-L65) (`clm_060790fa73c3100b806c41c281d3bb198d3bd188552f8eb7c78aeb7c861024b7`)
- [observation/documented] Documented OpenAI streaming responses use SSE 'data:' chunks of chat.completion.chunk objects; the finish_reason stop chunk is followed by a separate chunk with empty choices that carries usage, then a 'data: [DONE]' sentinel. -- evidence: [APIResponse.md#L136-L136](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L136-L136), [APIResponse.md#L134-L134](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L134-L134), [APIResponse.md#L132-L132](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L132-L132) (`clm_ebe75ac29d72bd2d2e16c6354077482d665bd0bf24bd0daa67438f280d30e459`)
- [observation/documented] Documented OpenAI streaming tool calls arrive incrementally: each delta carries a tool_calls fragment with index, id, function name, and argument string split across chunks, finishing with finish_reason 'tool_calls'. -- evidence: [APIResponse.md#L147-L147](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L147-L147), [APIResponse.md#L145-L145](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L145-L145), [APIResponse.md#L181-L181](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L181-L181), [APIResponse.md#L161-L161](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L161-L161) (`clm_ea91459b1cab32bd760589d68b637d652dc0cbf82650cdc5d50138f1edf6d45c`)
- [observation/documented] Documented DeepSeek-R1 streaming separates reasoning into a reasoning_content delta field (with reasoning_tokens counted in usage) before regular content deltas begin. -- evidence: [APIResponse.md#L282-L282](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L282-L282), [APIResponse.md#L257-L258](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L257-L258), [APIResponse.md#L260-L260](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L260-L260), [APIResponse.md#L284-L284](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L284-L284) (`clm_3f44cddc2217087654c456e7aae24a3c4d2aed998e00751b5c57c125b1d35272`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The library is published as io.github.lnyo-cly:ai4j version 2.4.2, installable via Gradle or Maven dependency declarations. -- evidence: [README.md#L12-L13](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L12-L13) (`clm_5d49783e73b207a9c4204d3e5846d40121294cb6f098bb332932a53643da535d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

