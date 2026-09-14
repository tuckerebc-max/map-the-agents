# Deep Agents Code (`deep-agents-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: langchain-ai
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=uv add deepagents (Python), curl -LsSf https://langch.in/dcode | bash (CLI)
- Model providers: OpenAI, Anthropic, Google, open-weight models (Baseten, Fireworks), self-hosted (Ollama, vLLM, llama.cpp), any LangChain chat model
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [langchain-ai/deepagents](../../repos/langchain-ai/deepagents.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Batteries-included agent harness built on LangGraph. Provides planning, file system access, context management, sub-agents with isolated context windows, shell access, persistent memory, human-in-the-loop approval, skills, and tool calling. Designed for long-horizon, multi-step work. Also available as deepagents.js (TypeScript).

(captured site page body (agents/deep-agents-code.md), not a verified repo-code finding)
deepagents exists because teams kept rebuilding the same scaffolding around LLM agents: a planning step, file access, context compaction, and task delegation. The library ships those as defaults inspired by Claude Code — a built-in planning tool, pluggable filesystem (local, sandboxed, or remote backends), sub-agents with isolated context windows, shell access, persistent memory, and human-in-the-loop approval gates — while every component remains replaceable for teams with different needs. It runs on any tool-calling LLM through LangGraph's production features (streaming, checkpointing, persistence) and accepts any MCP server as a tool source. Python and JavaScript teams use it as the foundation for custom agents rather than as an end-user product, with LangSmith available for tracing and evaluation.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deep-agents-code.md)
