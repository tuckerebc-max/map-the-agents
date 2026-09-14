# Autonoma (`autonoma`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Sebasbo
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=pip install autonoma
- Model providers: pluggable llm_interface (any provider)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: no (no)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [sebasbo/autonoma](../../repos/sebasbo/autonoma.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic AI framework that autonomously modifies, analyzes, and tests codebases. Uses a multi-agent system (PlannerAgent, CoderAgent, Tester) to collaboratively generate, refactor, and test code through an iterative process. Features an extensible architecture for custom agents and tasks.

(captured site page body (agents/autonoma.md), not a verified repo-code finding)
Autonoma is a Python framework in which a multi-agent system autonomously modifies, analyzes, and tests codebases through an event-driven loop. A PlannerAgent splits a query into tasks (up to 10 by default), CoderAgent generates or refactors code with AST manipulation and static analysis, and a Tester generates and runs unittest suites, feeding failures back for revision. Agents operate asynchronously with Pydantic-validated data structures, and the LLM interface is pluggable: any provider with a generate(prompt) method works, so backend choice is fully decoupled. Tasks can specify file paths and complexity estimates, and the architecture supports custom agents and task types. The project is an early-stage MIT-licensed Python package installed via pip, best viewed as a reference design for plan-code-test loops rather than a production harness.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/autonoma.md)
