# langroid/langroid -- full detail

[Back to orientation](langroid.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/langroid/langroid/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/15dd2d992e81e966.json](../../../wiki/dossiers/langroid/langroid/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/15dd2d992e81e966.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] Langroid is a Python framework for building LLM applications where users set up Agents equipped with optional components (LLM, vector-store, tools/functions) that collaborate by exchanging messages. -- evidence: [README.md#L38-L45](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L38-L45) (`clm_63e23efd773529940518f1fb1ce334167c0f19ea98a08093c016937cdda4a626`)
- [observation/documented] The Agent class encapsulates LLM conversation state plus an optional vector-store and tools, acts as a message transformer, and by default provides three responder methods corresponding to LLM, Agent, and User. -- evidence: [README.md#L455-L493](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L455-L493) (`clm_82a9b318f87f6bab08b904e3ceddbf455d44f7628120e764f98a211bcb9096a2`)
- [observation/documented] DocChatAgent supports chat with documents by sharding, embedding, storing in a vector DB, and retrieval-augmented answer generation, configured via DocChatAgentConfig with doc_paths and a vecdb setting. -- evidence: [README.md#L992-L1000](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L992-L1000), [README.md#L981-L986](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L981-L986) (`clm_6ef3ce00978788541270b7a15de8d3f87b6d107643f1ed25178f001d2b6e9c23`)
- [observation/documented] TableChatAgent accepts a dataset (file path, URL, or dataframe) and answers queries by having its LLM generate Pandas code via function-calling, which the agent's handler method executes. -- evidence: [README.md#L1025-L1028](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L1025-L1028) (`clm_07cfa57fc6c9a1515ef4ed7bb048d6400d32f6afd273fd5629568d660376234e`)

## design-choices (1 claim(s))

- [observation/documented] The multi-agent paradigm is inspired by the Actor model, and the framework does not use LangChain or any other LLM framework, aiming to work with practically any LLM. -- evidence: [README.md#L38-L45](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L38-L45), [README.md#L47-L50](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L47-L50) (`clm_3191dcf4143f79c4fb19ea234222695139f58cf52755d67df8f048376c2b19bc`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] A Claude Code plugin provides two skills: langroid:patterns for generating Langroid multi-agent code using proper design patterns, and langroid:add-pattern for recording newly learned patterns for future reference. -- evidence: [README.md#L52-L53](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L52-L53), [README.md#L552-L555](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L552-L555) (`clm_3ec032ee593f0791bdc1b2469a1b5fa0d82c4459385576b8462ec324a22263c5`)

## interfaces (3 claim(s))

- [observation/documented] Tools are defined by subclassing ToolMessage with a request field naming the handling agent method, a purpose description, and typed arguments; agents enable tools via enable_message, and Pydantic validation errors are sent back to the LLM for self-correction. -- evidence: [README.md#L857-L862](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L857-L862), [README.md#L876-L883](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L876-L883), [README.md#L901-L911](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L901-L911) (`clm_80fdc521582a18fe7e7fdd580f8894a842527d41b76ecb654c9c982dcd58771a`)
- [observation/documented] LLM configuration supports OpenAI models, any model behind an OpenAI-compatible API (e.g. "ollama/mistral"), and local models via chat_model strings such as "local/localhost:8000". -- evidence: [README.md#L106-L109](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L106-L109), [README.md#L776-L781](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L776-L781) (`clm_3e52077b2ff559f444cf17922e622a22f36aeb92e4fad3c7aad1473fd83d4472`)
- [observation/documented] Langroid includes an MCP tool adapter that converts an MCP server's tools into Langroid ToolMessage instances so any LLM agent can leverage MCP servers. -- evidence: [README.md#L59-L61](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L59-L61) (`clm_be4165d8851873e314cff6b0f4875327711e4547bc9e5555bfee0b296c128b57`)

## memory-state (1 claim(s))

- [observation/documented] LLM API responses can be cached via Redis or Momento (CACHE_TYPE=momento); if Redis settings are absent, Langroid falls back to a pure-Python in-memory cache via Fakeredis. -- evidence: [README.md#L626-L659](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L626-L659) (`clm_8e3b75c74fb8d812792a7023149e3e7b5cff8f9663d6aa8bad5c08d4e7ebd56d`)

## orchestration (1 claim(s))

- [observation/documented] A Task wraps an Agent, manages iteration over the agent's responder methods, and orchestrates multi-agent interaction via hierarchical, recursive task delegation; sub-tasks are treated as additional responders used round-robin after the agent's own responders. -- evidence: [README.md#L455-L493](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L455-L493) (`clm_f6b6bb1b173887469c6bc272f026fd36266b6eb3c1e241aa55ca6297870462a3`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Langroid requires Python 3.11+ and is installable from PyPI, with optional extras including hf-embeddings, doc-chat, db, postgres, and all (the latter increasing install size and startup time). -- evidence: [README.md#L500-L530](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L500-L530), [README.md#L536-L544](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L536-L544) (`clm_b13ffd944d0f7dc057cb755b8c52656adb56f47168a16b9f93cac31770e969a6`)
- [observation/documented] Supported vector stores include Qdrant cloud, Chroma (local storage, no API key needed), LanceDB, and Milvus; Milvus defaults to local storage at ./milvus.db, and Milvus Lite is unavailable on Windows. -- evidence: [README.md#L626-L659](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L626-L659) (`clm_4ecd45cf5e980d9619f4da4a10d9a286eb069c826ba5feb85edbf7d2726aa029`)

## limitations (1 claim(s))

- [observation/documented] The README states the prompts and instructions have been tested to work well with GPT-4 (and to some extent GPT-4o); other LLMs may yield inferior results unless prompts or the multi-agent setup are adjusted. -- evidence: [README.md#L730-L735](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L730-L735) (`clm_73ab4c005b47f9449826fc998b23b84346f099d698f87957cbe10bc2766a1e9d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

