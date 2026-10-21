# Llm_Rag (`llm-rag`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: dongdongunique
- License: MIT
- Language: Python
- Interface: install=pip install -U -r requirements.txt
- Model providers: OpenAI (GPT)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [dongdongunique/llm_rag](../../repos/dongdongunique/llm_rag.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Retrieval-Augmented Generation (RAG) system using FAISS for vector-based retrieval and GPT for generative responses. Gradio-powered UI for document uploading, searching, and CRUD operations on document chunks. Modular design to support other LLMs (e.g., HuggingFace).

(captured site page body (agents/llm-rag.md), not a verified repo-code finding)
Built as homework for an Advanced Database course, LLM_RAG demonstrates the standard RAG pipeline end to end: documents are chunked and embedded into a FAISS index, similarity search retrieves context for GPT, and a Gradio interface handles upload, search, and chunk-level CRUD. Both a CLI entry point and a web interface are provided, and the modular design leaves room for swapping in Hugging Face models alongside the default OpenAI backend. It serves as an educational reference for RAG mechanics rather than production software; the project has seen no meaningful activity since early 2025.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/llm-rag.md)
