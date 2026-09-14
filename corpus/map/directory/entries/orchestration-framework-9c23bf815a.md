# orchestration-framework (`orchestration-framework`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Snowflake-Labs
- License: Apache-2.0
- Language: Python
- Interface: install=pip install orchestration-framework
- Model providers: Snowflake Cortex
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [snowflake-labs/orchestration-framework](../../repos/snowflake-labs/orchestration-framework.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent orchestration framework (also called 'Agent Gateway') with native Snowflake services support. Routes requests to appropriate tools (Cortex Search for RAG, Cortex Analyst for Text2SQL, Python for custom operations, SQL for custom pipelines) instead of requiring users to choose between them. Uses LLM Compiler architecture from Berkeley AI Research, supports parallel function calling, Trulens tracing, and runs in SPCS/Snowflake Notebooks ...

(captured site page body (agents/orchestration-framework.md), not a verified repo-code finding)
Snowflake shops face a forced choice when serving AI features: Cortex Search for unstructured RAG or Cortex Analyst for Text2SQL, with no client-side layer that combines them in one request. Snowflake Labs' Agent Gateway fills that gap as a pip-installable Python framework built on Snowpark: a planner LLM decomposes a request into an execution graph of tasks with parallel function calling, following Berkeley's LLM Compiler architecture, and routes each step to Cortex Search, Cortex Analyst, Python tools, or custom SQL tools. Multi-step, multi-tool, multi-hop workflows run client-side with an optional TruLens observability extra, and a Quickstart notebook plus Streamlit demo cover onboarding. The FAQ points teams wanting in-Snowflake orchestration to the managed Cortex Agent API instead, positioning this as the client-side alternative. It is Apache-2.0 Python for Snowpark users, with moderate activity (132 commits).
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/orchestration-framework.md)
