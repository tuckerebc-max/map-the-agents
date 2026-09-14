# Ai-Testing-Agent (`ai-testing-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): Open-source AI agent for software testing. Uses an LLM via OpenRouter to automatically generate test plans, generate pytest test code for API endpoints, run tests, and iteratively refine based on natural-language feedback. Single LangChain agent with plan/generate/run/feedback tools. Only 1 commit, last activity ~2023.

(captured site page body (agents/ai-testing-agent.md), not a verified repo-code finding)
The agent generates a textual test plan, converts it into pytest code for REST API endpoints, executes the tests, and accepts free-form feedback to extend or correct them, overwriting generated_tests.py on each cycle. Mechanically, a LangChain chat agent invokes tools that spawn api_tester.py subprocesses; the LLM (via an OpenRouter API key) writes the test file, and pytest runs it against a configurable endpoint, with a bundled FastAPI demo app for local trials. It is a single-commit proof of concept: no license file, leftover copy files, 48 stars, and no activity since December 2024. Developers evaluating API test generation can run it by cloning the repo and setting OPENROUTER_API_KEY.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ai-testing-agent.md)
