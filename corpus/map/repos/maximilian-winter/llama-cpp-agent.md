# maximilian-winter/llama-cpp-agent

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 26848efd4f35 @ 1fc6ccd5a852d881

## Summary (orientation draft, not independently verified)

Selected evidence records: The README states the project is no longer maintained and directs users to ToolAgents or other Python agentic frameworks instead. The framework provides a chat interface, structured output generation, single and parallel function calling, RAG with colbert reranking, and agent chains of Conversational, Sequential, and Mapping types.

## Source coverage

Source coverage (partial): 6 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Documented API components include the llm_agent module, FunctionCallingAgent, StructuredOutputAgent, output settings, prompt templates, a messages formatter module, and a chat history/message store module. -- evidence: [docs/agents-api-reference.md#L15-L15](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L15-L15), [docs/agents-api-reference.md#L25-L25](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L25-L25), [docs/agents-api-reference.md#L11-L11](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L11-L11), [docs/chat_history-api-reference.md#L7-L7](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/chat_history-api-reference.md#L7-L7), [docs/agents-api-reference.md#L7-L7](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L7-L7), [docs/agents-api-reference.md#L29-L29](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L29-L29), [docs/agents-api-reference.md#L19-L19](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/agents-api-reference.md#L19-L19)
- design-choices (1 claim(s)):
  - [observation/documented] Guided sampling via grammars and JSON schema generation constrains model output to user-defined structures, so models not fine-tuned for function calling or JSON output can still perform these tasks. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [ReadMe.md#L15-L15](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L15-L15)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The framework provides a chat interface, structured output generation, single and parallel function calling, RAG with colbert reranking, and agent chains of Conversational, Sequential, and Mapping types. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [ReadMe.md#L13-L13](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L13-L13)
  - [observation/documented] Tools can be defined as Python functions, pydantic models, llama-index tools, or OpenAI tool schemas; LlamaCppFunctionTool.from_openai_tool converts an OpenAI tool schema plus a callable into a tool. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [docs/function-calling-agent.md#L109-L109](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/docs/function-calling-agent.md#L109-L109)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The framework works with multiple providers: llama-cpp-python and its server, the llama.cpp server, and TGI and vllm servers. -- evidence: [ReadMe.md#L20-L28](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L20-L28), [ReadMe.md#L17-L17](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L17-L17)
  - [observation/documented] RAG functionality (the RAGColbertReranker class and RAG example) requires the optional ragatouille dependency, installed via the llama-cpp-agent[rag] extra. -- evidence: [ReadMe.md#L89-L89](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L89-L89), [ReadMe.md#L174-L175](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L174-L175)
- limitations (1 claim(s)):
  - [observation/documented] The README states the project is no longer maintained and directs users to ToolAgents or other Python agentic frameworks instead. -- evidence: [ReadMe.md#L3-L4](https://github.com/Maximilian-Winter/llama-cpp-agent/blob/26848efd4f3511626982f96a96a54905096795b4/ReadMe.md#L3-L4)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](llama-cpp-agent.detail.md) for every claim.)

Metadata and full claim list: [full detail](llama-cpp-agent.detail.md)
Human notes ([notes](llama-cpp-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
