# snowflake-labs/orchestration-framework -- full detail

[Back to orientation](orchestration-framework.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/snowflake-labs/orchestration-framework/9addb6d4b303a0bbbc25da1f26d017e8504131e9/e02abe008bd13886.json](../../../wiki/dossiers/snowflake-labs/orchestration-framework/9addb6d4b303a0bbbc25da1f26d017e8504131e9/e02abe008bd13886.json)

## specifications (1 claim(s))

- [observation/documented] The Agent Gateway is described as an agentic orchestration framework offering native support for Snowflake tools. -- evidence: [README.md#L3-L4](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L3-L4) (`clm_7988f614b6d56876947c527af7c537e7dabcf8d1ffdbbc927b01ed9a237e4feb`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Rather than forcing users to choose between Cortex Search RAG and Cortex Analyst Text2SQL, the gateway routes each request to the appropriate tool. -- evidence: [README.md#L6-L8](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L6-L8) (`clm_37de4c1411acb67cefa0a66299b55fee0b2383dfbba4da1721f77c274c6d91d7`)
- [observation/documented] The architecture is stated to leverage the LLM Compiler design from Berkeley AI Research Lab, citing a 2024 paper on parallel function calling. -- evidence: [README.md#L216-L217](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L216-L217) (`clm_d46995aa72fa0ac1ad62f0e83cfbdc13c5d80c684e3b247f642edeb8a787bbde`)
- [observation/documented] The library is optimized for client-side orchestration; for orchestration managed inside Snowflake, the README recommends the Snowflake Cortex Agent API instead. -- evidence: [README.md#L156-L156](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L156-L156) (`clm_f87c1c3355267fa0e355173bfbb9d9de2fa403ac540cd7f55e22bc87fc555e8b`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The framework supports four tool types: Cortex Search for unstructured data, Cortex Analyst for structured data, Python for custom operations such as third-party API calls, and SQL for custom user-built SQL pipelines. -- evidence: [README.md#L10-L17](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L10-L17) (`clm_512ae7d1a9db19ca531a9bc83a7874c76b591647898c50904ad277d1aac525f5`)
- [observation/documented] Tools are instantiated from classes including CortexSearchTool, CortexAnalystTool, PythonTool, and SQLTool, configured with metadata such as service_name, semantic_model, tool_description, and a Snowpark session. -- evidence: [README.md#L68-L69](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L68-L69), [README.md#L87-L93](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L87-L93), [README.md#L115-L123](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L115-L123), [README.md#L104-L108](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L104-L108), [README.md#L72-L78](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L72-L78) (`clm_60d1aeeb1bf95a4db105f8bd31861c53907cef1fd5987d7b3a1a7b3d4986b201`)
- [observation/documented] An Agent is constructed with a snowflake_connection and a tools list, and is invoked by calling it directly with a natural-language question string. -- evidence: [README.md#L134-L135](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L134-L135), [README.md#L130-L131](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L130-L131), [README.md#L138-L139](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L138-L139) (`clm_58ebf11e4fbd1a97d37e384f31f0be3aa5e0dc16a128f4a8b789624d14b9f5f4`)
- [inference/documented] Multiple tools of the same type, and tools in different Snowflake accounts or schemas via separate Snowpark sessions, appear attachable to a single agent. -- evidence: [README.md#L194-L195](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L194-L195), [README.md#L185-L190](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L185-L190) (`clm_e59012651ea124b7b6a04f836ff0f8d29b7d0be7d6852c9f29b38b46519c56c8`)
- [observation/documented] The gateway logs at INFO level by default to show which tools answer a question, with LOGGING_LEVEL=DEBUG for more detail, and an optional Trulens integration (orchestration-framework[trulens]) provides execution traces via a TruAgent class. -- evidence: [README.md#L199-L201](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L199-L201), [README.md#L205-L211](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L205-L211) (`clm_790fca3cb7d2ecfb533067a1c55f13198e3bf65ebcb9eb8f33d90321c00caa36`)
- [observation/documented] The gateway can run in SPCS and Snowflake notebooks, requiring an external access integration network rule for direct GitHub or PyPI installation. -- evidence: [README.md#L169-L172](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L169-L172), [README.md#L160-L161](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L160-L161), [README.md#L163-L167](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L163-L167) (`clm_fd4cf707c517f3af8bb79dfb735f4fd12b8431989f64510984373e208bb11d31`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A dedicated planner LLM decomposes the user's request into an execution plan, forming a task graph that invokes tool calls asynchronously and in parallel where possible, with Snowflake compute used for plan generation and tool execution. -- evidence: [README.md#L216-L217](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L216-L217) (`clm_6ac89ab9f6d3e38383bcec97331e611a132ecd376c975548764d78d8d12a99cb`)

## tools-permissions (1 claim(s))

- [observation/documented] Authentication is handled by passing an authenticated Snowpark session, created with standard Snowflake connection parameters, to the gateway and its tools. -- evidence: [README.md#L180-L181](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L180-L181) (`clm_2c40dd9364f2f178b782bfddf5f21143e4f8831ab90ee4dd648f0348c912b830`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The package installs via pip as orchestration-framework and is documented for Python 3.10 or 3.11 in a new virtual environment. -- evidence: [README.md#L28-L29](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L28-L29), [README.md#L31-L33](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L31-L33) (`clm_643c1d58cf32bba0fc82d260c095d1521773cb567b17bb9f2024a3817092f9e2`)
- [observation/documented] Agents require the underlying Cortex Search, Cortex Analyst, SQL, or Python tools to be configured by the user before use. -- evidence: [README.md#L43-L44](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L43-L44) (`clm_85f4fda2e5440eb415122e6395464e63805a998efcf0a3a00775e68f89da8014`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

