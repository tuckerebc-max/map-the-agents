# maximilian-winter/llama-cpp-agent -- full detail

[Back to orientation](llama-cpp-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/maximilian-winter/llama-cpp-agent/26848efd4f3511626982f96a96a54905096795b4/1fc6ccd5a852d881.json](../../../wiki/dossiers/maximilian-winter/llama-cpp-agent/26848efd4f3511626982f96a96a54905096795b4/1fc6ccd5a852d881.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Documented API components include the llm_agent module, FunctionCallingAgent, StructuredOutputAgent, output settings, prompt templates, a messages formatter module, and a chat history/message store module. -- evidence: [docs/agents-api-reference.md#L15-L15](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L15-L15), [docs/agents-api-reference.md#L25-L25](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L25-L25), [docs/agents-api-reference.md#L11-L11](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L11-L11), [docs/chat_history-api-reference.md#L7-L7](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/chat_history-api-reference.md#L7-L7), [docs/agents-api-reference.md#L7-L7](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L7-L7), [docs/agents-api-reference.md#L29-L29](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L29-L29), [docs/agents-api-reference.md#L19-L19](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L19-L19) (`clm_736ff14632f01fa69b3721ec17d22e606d588117244a607efef13383b16b2ffa`)

## design-choices (1 claim(s))

- [observation/documented] Guided sampling via grammars and JSON schema generation constrains model output to user-defined structures, so models not fine-tuned for function calling or JSON output can still perform these tasks. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [ReadMe.md#L15-L15](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L15-L15) (`clm_7fc779315adb036e3e7614a3b76acc4dd7d046417269376774e297e68ad58a2f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The framework provides a chat interface, structured output generation, single and parallel function calling, RAG with colbert reranking, and agent chains of Conversational, Sequential, and Mapping types. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [ReadMe.md#L13-L13](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L13-L13) (`clm_edf7ca33fd184b87d4d1acb891149fbfd03d6fcd5d5e3fe15a00414d83837060`)
- [observation/documented] Tools can be defined as Python functions, pydantic models, llama-index tools, or OpenAI tool schemas; LlamaCppFunctionTool.from_openai_tool converts an OpenAI tool schema plus a callable into a tool. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [docs/function-calling-agent.md#L109-L109](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/function-calling-agent.md#L109-L109) (`clm_5c8752a20aebcb66515d13b664ebffc71c25602f5648d9dc36369b88aa7bef1d`)
- [observation/documented] A MessagesFormatterType enum offers predefined prompt formats including MISTRAL, CHATML, VICUNA, LLAMA_2, LLAMA_3, PHI_3, and DeepSeek Coder v2, and custom formatters can be built by instantiating the MessagesFormatter class. -- evidence: [ReadMe.md#L118-L118](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L118-L118), [ReadMe.md#L138-L138](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L138-L138), [ReadMe.md#L120-L134](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L120-L134) (`clm_79f1ae175303448ac080ce8d2923ea98b5f7b6eb1abd7a603774d1860743b427`)
- [observation/documented] FunctionCallingAgent is constructed with a provider, a list of function tools, a send-message-to-user callback, a message formatter type, and an allow_parallel_function_calling flag. -- evidence: [docs/function-calling-agent.md#L112-L117](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/function-calling-agent.md#L112-L117) (`clm_8aab6b6a87225a7b86eba49c7381aede3b034b56deb1a080e274e1a2bb6ede7f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The framework works with multiple providers: llama-cpp-python and its server, the llama.cpp server, and TGI and vllm servers. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [ReadMe.md#L17-L17](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L17-L17) (`clm_3373bac4f62d048b8e682aefe70b6e5812e423ddf4c5733951079ca61171d3ed`)
- [observation/documented] RAG functionality (the RAGColbertReranker class and RAG example) requires the optional ragatouille dependency, installed via the llama-cpp-agent[rag] extra. -- evidence: [ReadMe.md#L89-L89](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L89-L89), [ReadMe.md#L174-L175](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L174-L175) (`clm_0c23ddbf3efa1da8b3519fecfcdb790257d5d5e1c1cbb9cf8c260ddcff804858`)
- [observation/documented] The package is published on PyPI as llama-cpp-agent and installed with pip. -- evidence: [ReadMe.md#L7-L8](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L7-L8), [ReadMe.md#L57-L60](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L57-L60) (`clm_c231e83ca5eabf1fb43d94f3d642b2ac71a8a4a4cce4b9fa0a6a354c75986ea9`)

## limitations (1 claim(s))

- [observation/documented] The README states the project is no longer maintained and directs users to ToolAgents or other Python agentic frameworks instead. -- evidence: [ReadMe.md#L3-L4](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L3-L4) (`clm_41bfb43dba6e4a6aa4dc31a581597fae0f4968c9dd25b806a9b8789ea7d28313`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

