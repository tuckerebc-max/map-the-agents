# Code-Interpreter-Api (`code-interpreter-api`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: leezhuuuuu
- License: GPL-3.0
- Language: Python
- Interface: install=git clone; pip install -r requirements.txt; configure config.yaml; docker pull leezhuuu/code_interpreter:latest; python3 center.py
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [leezhuuuuu/code-interpreter-api](../../repos/leezhuuuuu/code-interpreter-api.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Scheduling center plus sandbox using Docker for safe, isolated Python code execution; stores generated image data in PostgreSQL with API access; designed to accelerate AI agent development by providing a reliable remote code-execution API.

(captured site page body (agents/code-interpreter-api.md), not a verified repo-code finding)
The service gives LLM applications a safe code-execution backend without exposing the host: each request runs in an isolated Docker container with configurable memory/CPU limits and timeouts, and generated images persist in PostgreSQL for retrieval through a REST endpoint. The scheduling center manages concurrency with queues and semaphores, and a hosted demo integrates with FastGPT, so agent platforms can add code execution without building sandbox infrastructure. It deliberately contains no LLM, planning, or agent logic - it is the tool, not the agent. Development activity ceased in early 2025.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/code-interpreter-api.md)
