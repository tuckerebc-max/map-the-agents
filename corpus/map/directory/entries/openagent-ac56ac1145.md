# openagent (`openagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: the-open-agent
- License: Apache-2.0
- Language: Go
- Interface: platforms=Web; install=binary, docker
- Model providers: OpenAI, Azure OpenAI, Anthropic, Google Gemini, DeepSeek, Mistral, Grok, Qwen, Doubao, Moonshot, ChatGLM, Baichuan, Ernie, iFlytek, HuggingFace, Cohere, Amazon Bedrock, OpenRouter, Ollama
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [the-open-agent/openagent](../../repos/the-open-agent/openagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source personal AI assistant shipped as a single binary with no runtime dependencies (runs natively on Linux/macOS/Windows, including native Windows without WSL/Docker). 30+ LLM providers switchable per conversation. Autonomous agent loops with browser-use, shell execution, office automation, and MCP integration (SSE/Stdio/StreamableHTTP). Built-in RAG knowledge base with pluggable embeddings, visual BPMN-style workflow builder with conditional/parallel execution and scheduling, and enterprise features ...

(captured site page body (agents/openagent.md), not a verified repo-code finding)
Personal AI assistants usually demand Python environments, Docker, or per-seat cloud accounts, which puts them out of reach for privacy-conscious individuals and small teams. OpenAgent compiles a Go backend with a React frontend into a single binary that installs via curl or PowerShell script, runs natively on Linux, macOS, and Windows without WSL or Docker, and starts a web UI on port 14000. Its agent loop draws on 30-plus switchable LLM providers (OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Qwen, OpenRouter, Ollama, and more), executes tools through any MCP-compatible server over SSE, stdio, or Streamable HTTP, and adds browser automation, shell execution, office automation, and a RAG knowledge base with pluggable embeddings. Multi-tenancy with OIDC/OAuth2/LDAP/SAML, audit logs, and usage-cost analytics target self-hosted team deployment. It suits users who want a private, single-binary assistant combining coding-agent abilities with office and browser automation.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openagent.md)
