# Ai-Testing-Agent (`ai-testing-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: furudo-erika
- License: unknown
- Language: Python (FastAPI, LangChain, pytest)
- Interface: install=Clone repo, pip install fastapi uvicorn requests pytest langchain openai, set OPENROUTER_API_KEY env var, run python agent.py
- Model providers: OpenRouter
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [furudo-erika/ai-testing-agent](../../repos/furudo-erika/ai-testing-agent.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
The agent generates a textual test plan, converts it into pytest code for REST API endpoints, executes the tests, and accepts free-form feedback to extend or correct them, overwriting generated_tests.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
