# NVIDIA NeMo Agent Toolkit (`nvidia-nemo-agent-toolkit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: NVIDIA
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI, Library; install=pip install nvidia-nat (PyPI); optional extras e.g. pip install 'nvidia-nat\[langchain\]'
- Model providers: NVIDIA NIMs (build.nvidia.com)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [nvidia/nemo](https://github.com/nvidia/nemo) (source: backing, field: `source_code_url`) now resolves to [nvidia-nemo/speech](../../repos/nvidia-nemo/speech.md) (github id 200722670, verified [https://github.com/NVIDIA-NeMo/Speech](https://github.com/NVIDIA-NeMo/Speech)).

## Description

Highlight (site page `what_makes_it_special`): Open-source library for connecting and optimizing teams of AI agents across any framework. Supports MCP as both client and server (FastMCP), a public Plugin API, distributed agent teams via Agent-to-Agent (A2A) Protocol with authentication, and runtime telemetry hooks. Enterprise-grade instrumentation, observability, and continuous learning.

(captured site page body (agents/nvidia-nemo-agent-toolkit.md), not a verified repo-code finding)
NeMo Agent Toolkit connects teams of AI agents to data sources and tools without requiring replatforming onto NVIDIA's stack, wrapping existing frameworks rather than replacing them. Workflows are declared in a YAML file with pre-built agent types (ReAct, ReWOO, reasoning, router, parallel/sequential executors) and run via the nat CLI. Evaluation and profiling are first-class: workflow-level tracing down to individual tools with token and timing attribution, optimizers, and trajectory formats for evaluation runs. A public plugin API covers custom LLM providers, retrievers, evaluators, memory providers, and telemetry exporters, shareable as packages. The A2A protocol support allows distributed agent teams, and observability integrates with LangSmith, Phoenix, Langfuse, and OpenTelemetry.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nvidia-nemo-agent-toolkit.md)
