---
access: public
aliases: []
claim_ids:
- clm_07759a5cd6b185b62c473dc2eb8a5d6ff6cb2daafdf35e419523877dbb8b05e8
- clm_35bee78282a7d8ee3daf4ae6bc8a57353fcfe2f9d824ba90f3fb0ee1486f9e26
- clm_5d49783e73b207a9c4204d3e5846d40121294cb6f098bb332932a53643da535d
- clm_952fc25793abeafe9773dc4a4b4010bb176208e945ff9c3e517c55da72f0e0e3
- clm_b85a30327e058ec9ea787a242a7399706ec90e7de41e3215aa47601639beb550
- clm_c760938c3b0a83108dcddfa13dc926a4fd65f483edf40fe75c8c0c4487448d11
maturity: draft
page_id: pg_9c446d626b595726ac73646f11f36f3a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_589b0b9aeaec5845bf3b6d97ff43f395
title: LnYo-Cly/ai4j/README.md @ ba6b79738535
updated_at: '2026-09-14T02:13:49Z'
---

# LnYo-Cly/ai4j/README.md @ ba6b79738535

<!-- rcw:begin owner=source:src_589b0b9aeaec5845bf3b6d97ff43f395 block=evidence -->
- ai4j is described as a Java AI agentic development kit targeting JDK 8+, unifying model access, tool calling, MCP, A2A, RAG, an agent runtime, and a built-in coding agent CLI/TUI/ACP. [@claim:clm_07759a5cd6b185b62c473dc2eb8a5d6ff6cb2daafdf35e419523877dbb8b05e8]
- Switching providers such as DashScope, DeepSeek, or Ollama is presented as changing only the PlatformType and corresponding config object while the rest of the calling code stays unchanged. [@claim:clm_35bee78282a7d8ee3daf4ae6bc8a57353fcfe2f9d824ba90f3fb0ee1486f9e26]
- The library is published as io.github.lnyo-cly:ai4j version 2.4.2, installable via Gradle or Maven dependency declarations. [@claim:clm_5d49783e73b207a9c4204d3e5846d40121294cb6f098bb332932a53643da535d]
- The quickstart flow: build an OpenAiConfig with an API key from OPENAI_API_KEY, wrap it in a Configuration, obtain an IChatService from AiService via PlatformType.OPENAI, then send a ChatCompletion built with a model name and user message. [@claim:clm_952fc25793abeafe9773dc4a4b4010bb176208e945ff9c3e517c55da72f0e0e3]
- Supported platforms listed include OpenAI and compatible APIs, Anthropic, DashScope, Doubao, DeepSeek, Moonshot, Zhipu, Hunyuan, Lingyi, Ollama, MiniMax, Baichuan, and Suno, plus rerank providers, AgentFlow (Dify/Coze/n8n), and vector stores (Pinecone, Qdrant, pgvector, Milvus, Redis). [@claim:clm_b85a30327e058ec9ea787a242a7399706ec90e7de41e3215aa47601639beb550]
- The project is licensed under Apache License 2.0 and links to a GitHub Pages documentation site plus guides for the coding agent CLI and A2A protocol. [@claim:clm_c760938c3b0a83108dcddfa13dc926a4fd65f483edf40fe75c8c0c4487448d11]
<!-- rcw:end owner=source:src_589b0b9aeaec5845bf3b6d97ff43f395 block=evidence -->

## Researcher notes

