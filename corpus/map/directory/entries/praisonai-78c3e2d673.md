# PraisonAI (`praisonai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: MervinPraison
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, Web; install=pip
- Model providers: OpenAI, Anthropic, Gemini, DeepSeek, Azure, Ollama, Groq, Mistral, Cohere, OpenRouter, Perplexity, Fireworks, AWS Bedrock, xAI Grok, Vertex AI, HuggingFace, Together AI, Databricks, Replicate, Cloudflare, AI21, SageMaker, Moonshot, vLLM (100+ LLMs across 24+ providers)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [mervinpraison/praisonai](../../repos/mervinpraison/praisonai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI agent framework for autonomous, self-improving multi-agent systems. Unique five-layer agent stack (Prompt -\> Context -\> Harness -\> Loop -\> Graph) plus a Managed Agents outer layer for cloud sandboxes (Docker, E2B, Modal, Daytona, Fly.io). MCP support via stdio, HTTP, WebSocket, and SSE transports. Doom-loop detection, context compaction, model routing for cost optimization. No-code YAML workflows, visual flow builder, bot ...

(captured site page body (agents/praisonai.md), not a verified repo-code finding)
PraisonAI is a Python-first multi-agent framework for building autonomous systems that research, plan, code, and execute, with a CLI and SDK surface rather than a fixed product shape. Its signature is the five-layer stack — prompt, context, harness, loop, graph — which gives developers a debugging vocabulary: when an agent misbehaves, the layer tells you where to look, whether that is a missing guardrail, a runaway loop, or a routing decision. The harness layer carries tools, MCP servers, approval gates, hooks, and sandboxing, while the graph layer composes agents through sequential flows, parallel fan-out, loops, and handoffs with doom-loop detection enabled by default. A Managed Agents layer can run any agent or tool set on Docker, E2B, Modal, or Daytona sandboxes, and orchestration extends to external coding CLIs like Claude Code and Codex. Teams use it to build production agent workflows with 100+ LLMs across 24 providers, YAML no-code configurations, and a visual flow builder.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/praisonai.md)
