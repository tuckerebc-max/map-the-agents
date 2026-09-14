---
access: public
aliases: []
claim_ids:
- clm_07cfa57fc6c9a1515ef4ed7bb048d6400d32f6afd273fd5629568d660376234e
- clm_3191dcf4143f79c4fb19ea234222695139f58cf52755d67df8f048376c2b19bc
- clm_3e52077b2ff559f444cf17922e622a22f36aeb92e4fad3c7aad1473fd83d4472
- clm_3ec032ee593f0791bdc1b2469a1b5fa0d82c4459385576b8462ec324a22263c5
- clm_4ecd45cf5e980d9619f4da4a10d9a286eb069c826ba5feb85edbf7d2726aa029
- clm_63e23efd773529940518f1fb1ce334167c0f19ea98a08093c016937cdda4a626
- clm_6ef3ce00978788541270b7a15de8d3f87b6d107643f1ed25178f001d2b6e9c23
- clm_73ab4c005b47f9449826fc998b23b84346f099d698f87957cbe10bc2766a1e9d
- clm_80fdc521582a18fe7e7fdd580f8894a842527d41b76ecb654c9c982dcd58771a
- clm_82a9b318f87f6bab08b904e3ceddbf455d44f7628120e764f98a211bcb9096a2
- clm_8e3b75c74fb8d812792a7023149e3e7b5cff8f9663d6aa8bad5c08d4e7ebd56d
- clm_b13ffd944d0f7dc057cb755b8c52656adb56f47168a16b9f93cac31770e969a6
- clm_be4165d8851873e314cff6b0f4875327711e4547bc9e5555bfee0b296c128b57
- clm_f6b6bb1b173887469c6bc272f026fd36266b6eb3c1e241aa55ca6297870462a3
maturity: draft
page_id: pg_2dc800252f91564780728cc8f4c92985
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_962ebf85bc9053058727328062747ed1
title: langroid/langroid/README.md @ 53c01d4e1a9e
updated_at: '2026-09-14T02:12:38Z'
---

# langroid/langroid/README.md @ 53c01d4e1a9e

<!-- rcw:begin owner=source:src_962ebf85bc9053058727328062747ed1 block=evidence -->
- TableChatAgent accepts a dataset (file path, URL, or dataframe) and answers queries by having its LLM generate Pandas code via function-calling, which the agent's handler method executes. [@claim:clm_07cfa57fc6c9a1515ef4ed7bb048d6400d32f6afd273fd5629568d660376234e]
- The multi-agent paradigm is inspired by the Actor model, and the framework does not use LangChain or any other LLM framework, aiming to work with practically any LLM. [@claim:clm_3191dcf4143f79c4fb19ea234222695139f58cf52755d67df8f048376c2b19bc]
- LLM configuration supports OpenAI models, any model behind an OpenAI-compatible API (e.g. "ollama/mistral"), and local models via chat_model strings such as "local/localhost:8000". [@claim:clm_3e52077b2ff559f444cf17922e622a22f36aeb92e4fad3c7aad1473fd83d4472]
- A Claude Code plugin provides two skills: langroid:patterns for generating Langroid multi-agent code using proper design patterns, and langroid:add-pattern for recording newly learned patterns for future reference. [@claim:clm_3ec032ee593f0791bdc1b2469a1b5fa0d82c4459385576b8462ec324a22263c5]
- Supported vector stores include Qdrant cloud, Chroma (local storage, no API key needed), LanceDB, and Milvus; Milvus defaults to local storage at ./milvus.db, and Milvus Lite is unavailable on Windows. [@claim:clm_4ecd45cf5e980d9619f4da4a10d9a286eb069c826ba5feb85edbf7d2726aa029]
- Langroid is a Python framework for building LLM applications where users set up Agents equipped with optional components (LLM, vector-store, tools/functions) that collaborate by exchanging messages. [@claim:clm_63e23efd773529940518f1fb1ce334167c0f19ea98a08093c016937cdda4a626]
- DocChatAgent supports chat with documents by sharding, embedding, storing in a vector DB, and retrieval-augmented answer generation, configured via DocChatAgentConfig with doc_paths and a vecdb setting. [@claim:clm_6ef3ce00978788541270b7a15de8d3f87b6d107643f1ed25178f001d2b6e9c23]
- The README states the prompts and instructions have been tested to work well with GPT-4 (and to some extent GPT-4o); other LLMs may yield inferior results unless prompts or the multi-agent setup are adjusted. [@claim:clm_73ab4c005b47f9449826fc998b23b84346f099d698f87957cbe10bc2766a1e9d]
- Tools are defined by subclassing ToolMessage with a request field naming the handling agent method, a purpose description, and typed arguments; agents enable tools via enable_message, and Pydantic validation errors are sent back to the LLM for self-correction. [@claim:clm_80fdc521582a18fe7e7fdd580f8894a842527d41b76ecb654c9c982dcd58771a]
- The Agent class encapsulates LLM conversation state plus an optional vector-store and tools, acts as a message transformer, and by default provides three responder methods corresponding to LLM, Agent, and User. [@claim:clm_82a9b318f87f6bab08b904e3ceddbf455d44f7628120e764f98a211bcb9096a2]
- LLM API responses can be cached via Redis or Momento (CACHE_TYPE=momento); if Redis settings are absent, Langroid falls back to a pure-Python in-memory cache via Fakeredis. [@claim:clm_8e3b75c74fb8d812792a7023149e3e7b5cff8f9663d6aa8bad5c08d4e7ebd56d]
- Langroid requires Python 3.11+ and is installable from PyPI, with optional extras including hf-embeddings, doc-chat, db, postgres, and all (the latter increasing install size and startup time). [@claim:clm_b13ffd944d0f7dc057cb755b8c52656adb56f47168a16b9f93cac31770e969a6]
- Langroid includes an MCP tool adapter that converts an MCP server's tools into Langroid ToolMessage instances so any LLM agent can leverage MCP servers. [@claim:clm_be4165d8851873e314cff6b0f4875327711e4547bc9e5555bfee0b296c128b57]
- A Task wraps an Agent, manages iteration over the agent's responder methods, and orchestrates multi-agent interaction via hierarchical, recursive task delegation; sub-tasks are treated as additional responders used round-robin after the agent's own responders. [@claim:clm_f6b6bb1b173887469c6bc272f026fd36266b6eb3c1e241aa55ca6297870462a3]
<!-- rcw:end owner=source:src_962ebf85bc9053058727328062747ed1 block=evidence -->

## Researcher notes

