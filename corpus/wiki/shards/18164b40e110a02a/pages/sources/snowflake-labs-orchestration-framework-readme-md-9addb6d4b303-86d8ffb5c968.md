---
access: public
aliases: []
claim_ids:
- clm_2c40dd9364f2f178b782bfddf5f21143e4f8831ab90ee4dd648f0348c912b830
- clm_37de4c1411acb67cefa0a66299b55fee0b2383dfbba4da1721f77c274c6d91d7
- clm_512ae7d1a9db19ca531a9bc83a7874c76b591647898c50904ad277d1aac525f5
- clm_58ebf11e4fbd1a97d37e384f31f0be3aa5e0dc16a128f4a8b789624d14b9f5f4
- clm_60d1aeeb1bf95a4db105f8bd31861c53907cef1fd5987d7b3a1a7b3d4986b201
- clm_643c1d58cf32bba0fc82d260c095d1521773cb567b17bb9f2024a3817092f9e2
- clm_6ac89ab9f6d3e38383bcec97331e611a132ecd376c975548764d78d8d12a99cb
- clm_790fca3cb7d2ecfb533067a1c55f13198e3bf65ebcb9eb8f33d90321c00caa36
- clm_7988f614b6d56876947c527af7c537e7dabcf8d1ffdbbc927b01ed9a237e4feb
- clm_85f4fda2e5440eb415122e6395464e63805a998efcf0a3a00775e68f89da8014
- clm_d46995aa72fa0ac1ad62f0e83cfbdc13c5d80c684e3b247f642edeb8a787bbde
- clm_e59012651ea124b7b6a04f836ff0f8d29b7d0be7d6852c9f29b38b46519c56c8
- clm_f87c1c3355267fa0e355173bfbb9d9de2fa403ac540cd7f55e22bc87fc555e8b
- clm_fd4cf707c517f3af8bb79dfb735f4fd12b8431989f64510984373e208bb11d31
maturity: draft
page_id: pg_5a0a5240382459e880ca86d8ffb5c968
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c0b2117589155b4da269322fcfcfbcdf
title: Snowflake-Labs/orchestration-framework/README.md @ 9addb6d4b303
updated_at: '2026-09-14T04:22:13Z'
---

# Snowflake-Labs/orchestration-framework/README.md @ 9addb6d4b303

<!-- rcw:begin owner=source:src_c0b2117589155b4da269322fcfcfbcdf block=evidence -->
- Authentication is handled by passing an authenticated Snowpark session, created with standard Snowflake connection parameters, to the gateway and its tools. [@claim:clm_2c40dd9364f2f178b782bfddf5f21143e4f8831ab90ee4dd648f0348c912b830]
- Rather than forcing users to choose between Cortex Search RAG and Cortex Analyst Text2SQL, the gateway routes each request to the appropriate tool. [@claim:clm_37de4c1411acb67cefa0a66299b55fee0b2383dfbba4da1721f77c274c6d91d7]
- The framework supports four tool types: Cortex Search for unstructured data, Cortex Analyst for structured data, Python for custom operations such as third-party API calls, and SQL for custom user-built SQL pipelines. [@claim:clm_512ae7d1a9db19ca531a9bc83a7874c76b591647898c50904ad277d1aac525f5]
- An Agent is constructed with a snowflake_connection and a tools list, and is invoked by calling it directly with a natural-language question string. [@claim:clm_58ebf11e4fbd1a97d37e384f31f0be3aa5e0dc16a128f4a8b789624d14b9f5f4]
- Tools are instantiated from classes including CortexSearchTool, CortexAnalystTool, PythonTool, and SQLTool, configured with metadata such as service_name, semantic_model, tool_description, and a Snowpark session. [@claim:clm_60d1aeeb1bf95a4db105f8bd31861c53907cef1fd5987d7b3a1a7b3d4986b201]
- The package installs via pip as orchestration-framework and is documented for Python 3.10 or 3.11 in a new virtual environment. [@claim:clm_643c1d58cf32bba0fc82d260c095d1521773cb567b17bb9f2024a3817092f9e2]
- A dedicated planner LLM decomposes the user's request into an execution plan, forming a task graph that invokes tool calls asynchronously and in parallel where possible, with Snowflake compute used for plan generation and tool execution. [@claim:clm_6ac89ab9f6d3e38383bcec97331e611a132ecd376c975548764d78d8d12a99cb]
- The gateway logs at INFO level by default to show which tools answer a question, with LOGGING_LEVEL=DEBUG for more detail, and an optional Trulens integration (orchestration-framework[trulens]) provides execution traces via a TruAgent class. [@claim:clm_790fca3cb7d2ecfb533067a1c55f13198e3bf65ebcb9eb8f33d90321c00caa36]
- The Agent Gateway is described as an agentic orchestration framework offering native support for Snowflake tools. [@claim:clm_7988f614b6d56876947c527af7c537e7dabcf8d1ffdbbc927b01ed9a237e4feb]
- Agents require the underlying Cortex Search, Cortex Analyst, SQL, or Python tools to be configured by the user before use. [@claim:clm_85f4fda2e5440eb415122e6395464e63805a998efcf0a3a00775e68f89da8014]
- The architecture is stated to leverage the LLM Compiler design from Berkeley AI Research Lab, citing a 2024 paper on parallel function calling. [@claim:clm_d46995aa72fa0ac1ad62f0e83cfbdc13c5d80c684e3b247f642edeb8a787bbde]
- Multiple tools of the same type, and tools in different Snowflake accounts or schemas via separate Snowpark sessions, appear attachable to a single agent. [@claim:clm_e59012651ea124b7b6a04f836ff0f8d29b7d0be7d6852c9f29b38b46519c56c8]
- The library is optimized for client-side orchestration; for orchestration managed inside Snowflake, the README recommends the Snowflake Cortex Agent API instead. [@claim:clm_f87c1c3355267fa0e355173bfbb9d9de2fa403ac540cd7f55e22bc87fc555e8b]
- The gateway can run in SPCS and Snowflake notebooks, requiring an external access integration network rule for direct GitHub or PyPI installation. [@claim:clm_fd4cf707c517f3af8bb79dfb735f4fd12b8431989f64510984373e208bb11d31]
<!-- rcw:end owner=source:src_c0b2117589155b4da269322fcfcfbcdf block=evidence -->

## Researcher notes

