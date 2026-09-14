---
access: public
aliases: []
claim_ids:
- clm_0c23ddbf3efa1da8b3519fecfcdb790257d5d5e1c1cbb9cf8c260ddcff804858
- clm_3373bac4f62d048b8e682aefe70b6e5812e423ddf4c5733951079ca61171d3ed
- clm_41bfb43dba6e4a6aa4dc31a581597fae0f4968c9dd25b806a9b8789ea7d28313
- clm_5c8752a20aebcb66515d13b664ebffc71c25602f5648d9dc36369b88aa7bef1d
- clm_79f1ae175303448ac080ce8d2923ea98b5f7b6eb1abd7a603774d1860743b427
- clm_7fc779315adb036e3e7614a3b76acc4dd7d046417269376774e297e68ad58a2f
- clm_c231e83ca5eabf1fb43d94f3d642b2ac71a8a4a4cce4b9fa0a6a354c75986ea9
- clm_edf7ca33fd184b87d4d1acb891149fbfd03d6fcd5d5e3fe15a00414d83837060
maturity: draft
page_id: pg_245df937af5f584b8cd3db259056c731
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fb9211f3d5ff5e7b8d9ac2ec76e25ed8
title: Maximilian-Winter/llama-cpp-agent/ReadMe.md @ 26848efd4f35
updated_at: '2026-09-14T02:17:51Z'
---

# Maximilian-Winter/llama-cpp-agent/ReadMe.md @ 26848efd4f35

<!-- rcw:begin owner=source:src_fb9211f3d5ff5e7b8d9ac2ec76e25ed8 block=evidence -->
- RAG functionality (the RAGColbertReranker class and RAG example) requires the optional ragatouille dependency, installed via the llama-cpp-agent[rag] extra. [@claim:clm_0c23ddbf3efa1da8b3519fecfcdb790257d5d5e1c1cbb9cf8c260ddcff804858]
- The framework works with multiple providers: llama-cpp-python and its server, the llama.cpp server, and TGI and vllm servers. [@claim:clm_3373bac4f62d048b8e682aefe70b6e5812e423ddf4c5733951079ca61171d3ed]
- The README states the project is no longer maintained and directs users to ToolAgents or other Python agentic frameworks instead. [@claim:clm_41bfb43dba6e4a6aa4dc31a581597fae0f4968c9dd25b806a9b8789ea7d28313]
- Tools can be defined as Python functions, pydantic models, llama-index tools, or OpenAI tool schemas; LlamaCppFunctionTool.from_openai_tool converts an OpenAI tool schema plus a callable into a tool. [@claim:clm_5c8752a20aebcb66515d13b664ebffc71c25602f5648d9dc36369b88aa7bef1d]
- A MessagesFormatterType enum offers predefined prompt formats including MISTRAL, CHATML, VICUNA, LLAMA_2, LLAMA_3, PHI_3, and DeepSeek Coder v2, and custom formatters can be built by instantiating the MessagesFormatter class. [@claim:clm_79f1ae175303448ac080ce8d2923ea98b5f7b6eb1abd7a603774d1860743b427]
- Guided sampling via grammars and JSON schema generation constrains model output to user-defined structures, so models not fine-tuned for function calling or JSON output can still perform these tasks. [@claim:clm_7fc779315adb036e3e7614a3b76acc4dd7d046417269376774e297e68ad58a2f]
- The package is published on PyPI as llama-cpp-agent and installed with pip. [@claim:clm_c231e83ca5eabf1fb43d94f3d642b2ac71a8a4a4cce4b9fa0a6a354c75986ea9]
- The framework provides a chat interface, structured output generation, single and parallel function calling, RAG with colbert reranking, and agent chains of Conversational, Sequential, and Mapping types. [@claim:clm_edf7ca33fd184b87d4d1acb891149fbfd03d6fcd5d5e3fe15a00414d83837060]
<!-- rcw:end owner=source:src_fb9211f3d5ff5e7b8d9ac2ec76e25ed8 block=evidence -->

## Researcher notes

