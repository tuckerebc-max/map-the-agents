# swival (`swival`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Swival
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=uv tool install --python 3.14 swival; or macOS: brew install swival/tap/swival
- Model providers: LM Studio, llama.cpp, HuggingFace Inference, OpenRouter, Google Gemini, Vertex AI, ChatGPT Plus/Pro (browser auth), AWS Bedrock, Apple Foundation Models, generic OpenAI-compatible (ollama, vLLM), Command
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: n/a (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [swival/swival](../../repos/swival/swival.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): CLI coding agent built for any model, especially small/local models with tight context windows. Pure Python (no framework) with graduated compaction, persistent thinking notes, todo checklists that survive context resets, secret encryption, cross-session BM25 memory, goal-driven loops, timer-based scheduled runs, A2A/ACP server modes, and a built-in security audit pipeline.

(captured site page body (agents/swival.md), not a verified repo-code finding)
Swival exists because most coding-agent CLIs assume frontier models with large context windows, leaving users of small or locally hosted models with tools that degrade quickly. It is a single pure-Python agent loop with a deliberately small tool set (read, write, edit, bash) and no framework dependency, and its engineering centers on context discipline: graduated compaction that summarizes in stages, persistent thinking notes that survive context resets, todo checklists that are re-injected after compaction, and cross-session BM25 memory so resumed work recalls earlier decisions. Connectivity is unusually broad for its size — LM Studio and llama.cpp auto-discovery, OpenRouter, Gemini, Bedrock, Vertex, Apple Foundation Models, browser-authenticated ChatGPT subscriptions, and any OpenAI-compatible server — plus a command provider that shells out to external agents like codex exec. Lifecycle hooks and command middleware support unattended or policy-constrained operation, A2A/ACP server modes let other harnesses call it, and scheduled runs suit automation. It targets developers running local or low-cost models who still want durable, multi-session agent behavior.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swival.md)
