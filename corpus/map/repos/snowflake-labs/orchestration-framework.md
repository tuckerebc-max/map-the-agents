# snowflake-labs/orchestration-framework

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9addb6d4b303 @ e02abe008bd13886

## Summary (orientation draft, not independently verified)

The README documents the Agent Gateway, a client-side agentic orchestration framework for Snowflake tools that routes requests across Cortex Search, Cortex Analyst, Python, and SQL tools using an LLM Compiler-style planner. Evidence covers tool configuration, agent usage, authentication, logging, and FAQ guidance; no deployment-coverage claims beyond what slices state.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The Agent Gateway is described as an agentic orchestration framework offering native support for Snowflake tools. -- evidence: [README.md#L3-L4](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L3-L4)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Rather than forcing users to choose between Cortex Search RAG and Cortex Analyst Text2SQL, the gateway routes each request to the appropriate tool. -- evidence: [README.md#L6-L8](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L6-L8)
  - [observation/documented] The architecture is stated to leverage the LLM Compiler design from Berkeley AI Research Lab, citing a 2024 paper on parallel function calling. -- evidence: [README.md#L216-L217](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L216-L217)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The framework supports four tool types: Cortex Search for unstructured data, Cortex Analyst for structured data, Python for custom operations such as third-party API calls, and SQL for custom user-built SQL pipelines. -- evidence: [README.md#L10-L17](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L10-L17)
  - [observation/documented] Tools are instantiated from classes including CortexSearchTool, CortexAnalystTool, PythonTool, and SQLTool, configured with metadata such as service_name, semantic_model, tool_description, and a Snowpark session. -- evidence: [README.md#L68-L69](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L68-L69), [README.md#L87-L93](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L87-L93), [README.md#L115-L123](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L115-L123), [README.md#L104-L108](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L104-L108), [README.md#L72-L78](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L72-L78)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A dedicated planner LLM decomposes the user's request into an execution plan, forming a task graph that invokes tool calls asynchronously and in parallel where possible, with Snowflake compute used for plan generation and tool execution. -- evidence: [README.md#L216-L217](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L216-L217)
- tools-permissions (1 claim(s)):
  - [observation/documented] Authentication is handled by passing an authenticated Snowpark session, created with standard Snowflake connection parameters, to the gateway and its tools. -- evidence: [README.md#L180-L181](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L180-L181)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The package installs via pip as orchestration-framework and is documented for Python 3.10 or 3.11 in a new virtual environment. -- evidence: [README.md#L28-L29](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L28-L29), [README.md#L31-L33](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L31-L33)
  - [observation/documented] Agents require the underlying Cortex Search, Cortex Analyst, SQL, or Python tools to be configured by the user before use. -- evidence: [README.md#L43-L44](https://github.com/Snowflake-Labs/orchestration-framework/blob/9addb6d4b303a0bbbc25da1f26d017e8504131e9/README.md#L43-L44)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](orchestration-framework.detail.md)

Metadata and full claim list: [full detail](orchestration-framework.detail.md)
Human notes ([notes](orchestration-framework.notes.md), never overwritten by build)

[Back to map index](../../index.md)
