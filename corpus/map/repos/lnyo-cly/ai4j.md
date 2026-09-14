# lnyo-cly/ai4j

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ba6b79738535 @ 5d55cba7d712ee44

## Summary (orientation draft, not independently verified)

ai4j is a JDK 8+ Java AI agentic SDK (v2.4.2 on Maven Central) with unified model access, tool calling, MCP/A2A/RAG support and a built-in coding agent CLI/TUI/ACP; APIResponse.md documents raw streaming response formats for OpenAI, DeepSeek, and Ollama models. All prior claims were verified against cited slices; one was corrected to reflect that usage arrives in a separate chunk after the finish_reason stop chunk. Evidence coverage: 111 of 306 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 28 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] ai4j is described as a Java AI agentic development kit targeting JDK 8+, unifying model access, tool calling, MCP, A2A, RAG, an agent runtime, and a built-in coding agent CLI/TUI/ACP. -- evidence: [README.md#L6-L6](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L6-L6), [README.md#L1-L2](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L1-L2)
  - [observation/documented] The project is licensed under Apache License 2.0 and links to a GitHub Pages documentation site plus guides for the coding agent CLI and A2A protocol. -- evidence: [README.md#L55-L58](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L55-L58), [README.md#L66-L66](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L66-L66)
- components (1 claim(s)):
  - [observation/documented] Supported platforms listed include OpenAI and compatible APIs, Anthropic, DashScope, Doubao, DeepSeek, Moonshot, Zhipu, Hunyuan, Lingyi, Ollama, MiniMax, Baichuan, and Suno, plus rerank providers, AgentFlow (Dify/Coze/n8n), and vector stores (Pinecone, Qdrant, pgvector, Milvus, Redis). -- evidence: [README.md#L62-L62](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L62-L62)
- design-choices (1 claim(s)):
  - [observation/documented] Switching providers such as DashScope, DeepSeek, or Ollama is presented as changing only the PlatformType and corresponding config object while the rest of the calling code stays unchanged. -- evidence: [README.md#L51-L51](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L51-L51)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The quickstart flow: build an OpenAiConfig with an API key from OPENAI_API_KEY, wrap it in a Configuration, obtain an IChatService from AiService via PlatformType.OPENAI, then send a ChatCompletion built with a model name and user message. -- evidence: [README.md#L19-L44](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L19-L44), [README.md#L17-L17](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L17-L17)
  - [observation/documented] APIResponse.md documents that Ollama's deepseek-r1 streams thinking and answer content together in the content field, with thinking wrapped in <think> tags, unlike qwen3 which places reasoning in a separate thinking field. -- evidence: [APIResponse.md#L28-L29](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L28-L29), [APIResponse.md#L48-L49](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/APIResponse.md#L48-L49)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The library is published as io.github.lnyo-cly:ai4j version 2.4.2, installable via Gradle or Maven dependency declarations. -- evidence: [README.md#L12-L13](https://github.com/LnYo-Cly/ai4j/blob/ba6b7973853560e961bca34f2a94d537929b2082/README.md#L12-L13)
More evidence: [full detail](ai4j.detail.md)

Metadata and full claim list: [full detail](ai4j.detail.md)
Human notes ([notes](ai4j.notes.md), never overwritten by build)

[Back to map index](../../index.md)
