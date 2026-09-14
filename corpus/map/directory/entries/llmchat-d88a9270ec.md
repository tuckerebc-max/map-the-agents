# Llmchat (`llmchat`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: c0sogi
- License: MIT
- Language: Python, Dart
- Interface: platforms=Web; install=docker-compose -f docker-compose-local.yaml up; or python -m main
- Model providers: OpenAI, LlamaCpp, Exllama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [c0sogi/llmchat](../../repos/c0sogi/llmchat.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Full-stack web UI for chatting with LLMs (ChatGPT, LLaMA, etc.) with web browsing (DuckDuckGo), vector embedding (Redis), auto-summarization, WebSocket real-time streaming, PDF upload/embedding, and local LLM support.

(captured site page body (agents/llmchat.md), not a verified repo-code finding)
LLMChat dates from early 2023, when running LLaMA weights locally required stitching together llama.cpp or ExLlama by hand, and it wrapped those backends plus the OpenAI API behind one authenticated web interface. Conversations stream over WebSockets, a browse toggle adds DuckDuckGo search to replies, and PDF or text uploads are embedded into Redis for retrieval-style memory, with automatic summarization keeping long histories within context limits. FastAPI handles the backend while Flutter serves the same UI to browsers and mobile devices. Development stopped in 2024, leaving a representative but unmaintained example of the pre-agent chat-client era.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/llmchat.md)
