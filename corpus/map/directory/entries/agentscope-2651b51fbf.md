# AgentScope (`agentscope`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: agentscope-ai
- License: Apache-2.0
- Language: Python
- Interface: install=pip (uv pip install agentscope)
- Model providers: OpenAI, Anthropic, Google (Gemini), DashScope, DeepSeek, Moonshot, xAI, Ollama
- Feature flags (directory-reported):
  - mcp_support: yes (MCP servers, GitHub MCP Registry & ClawHub) (yes)
  - plugin_support: yes (Skills, MCP servers, Python Toolkit, Hub system) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (Agent Team leader-worker orchestration) (yes)
  - hooks: yes (composable middleware hooks across the loop) (yes)
  - plan_mode: yes (Task/plan tools) (yes)

Repository map entry (renamed): original lead [modelscope/agentscope](https://github.com/modelscope/agentscope) (source: backing, field: `source_code_url`) now resolves to [agentscope-ai/agentscope](../../repos/agentscope-ai/agentscope.md) (github id 742244656, verified [https://github.com/agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)).

## Description

Highlight (site page `what_makes_it_special`): A model-centric (not framework-centric) agent service designed for increasingly agentic LLMs, shipping a full FastAPI backend + Web UI with multi-tenancy, leader-worker agent teams, 8 sandbox backends, and fine-grained permission control out of the box.

(captured site page body (agents/agentscope.md), not a verified repo-code finding)
Most agent frameworks stop at an SDK and leave serving, sandboxing, and permissions to the application layer. AgentScope 2.0 takes a model-centric stance: because modern LLMs already reason and call tools well, the framework provides composable building blocks (ReAct agent, Toolkit with MCP servers and skills, context middleware, permission and human-in-the-loop controls, memory backends) instead of constraining orchestration. The service layer adds a FastAPI backend with a pre-built Web UI, multi-tenancy, RAG, scheduling, and channels into enterprise chat platforms, so a deployment is production-shaped from the start. Agent Teams let a leader agent spawn and coordinate workers, and isolated execution runs across Local, Docker, Apple Container, Bubblewrap, E2B, OpenSandbox, Daytona, and K8s backends. It targets developers building agent applications on Alibaba's ModelScope stack, with Apache-2.0 code, Python 3.11+ packaging on PyPI, and documentation at docs.agentscope.io.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentscope.md)
