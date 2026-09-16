# Hindsight (`hindsight`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: vectorize-io
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=pip
- Model providers: OpenAI, Anthropic, Google, Groq, Bedrock, VertexAI, DeepSeek, Ollama, LMStudio, LiteLLM, 100+ via LiteLLM, subscription passthrough (openai-codex, claude-code, github-copilot)
- Feature flags (directory-reported):
  - mcp_support: yes (HTTP transport — http://localhost:8888/mcp/{bank_id}/) (yes)
  - plugin_support: yes (60+ integrations; extensibility via tenant, auth, storage extension points) (yes)
  - claude_code_plugin: yes (native integration via npx @vectorize-io/hindsight-coding-agents install claude-code) (yes)
  - subagents: no (no)
  - hooks: yes (webhooks for retain, consolidation, and refresh lifecycle events) (yes)
  - plan_mode: no (no)

Repository map entry: [vectorize-io/hindsight](../../repos/vectorize-io/hindsight.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Hindsight is a memory service that lets AI agents accumulate durable knowledge instead of treating every session as isolated. It stores memories as world facts, experiences, evidence-backed observatio
Sources: [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
