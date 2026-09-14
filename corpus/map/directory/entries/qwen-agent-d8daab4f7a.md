# Qwen-Agent (`qwen-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: QwenLM
- License: Apache-2.0
- Language: Python
- Interface: install=pip
- Model providers: DashScope (Alibaba Cloud), OpenAI-compatible APIs (vLLM, Ollama), Qwen models
- Feature flags (directory-reported):
  - mcp_support: yes (stdio transport) (yes)
  - plugin_support: yes (custom tools via @register_tool, built-in tools, Chrome extension) (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [qwenlm/qwen-agent](../../repos/qwenlm/qwen-agent.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=other, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Framework for building LLM applications leveraging Qwen's instruction following, tool usage, planning, and memory capabilities, featuring MCP support, code interpreter with Docker sandboxing, RAG for 1M-token contexts, and example applications like Browser Assistant — serves as the backend of Qwen Chat.

(captured site page body (agents/qwen-agent.md), not a verified repo-code finding)
Qwen-Agent is Alibaba's framework for building LLM applications that use tools, plan, and remember — the same code that powers Qwen Chat in production. Its building blocks are a base chat model abstraction and composable agents that combine function calling, RAG over million-token documents, a Docker-sandboxed code interpreter, and browser automation through the BrowserQwen Chrome extension. Unlike coding-specific harnesses, it treats code execution as one tool among many: the framework is equally at home building assistants, document QA pipelines, or browser agents, with prompts and tool-call templates tuned for Qwen models though it runs against any OpenAI-compatible endpoint. The Qwen team maintains it actively, and it ships its own DeepPlanning benchmark for evaluating agent planning. Developers building Qwen-powered applications use it as the foundation layer rather than as a terminal coding tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qwen-agent.md)
