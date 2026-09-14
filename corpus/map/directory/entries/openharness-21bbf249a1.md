# openHarness (`openharness`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: zhijiewong
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @zhijiewang/openharness
- Model providers: Ollama, OpenAI, Anthropic, OpenRouter, llama.cpp, LM Studio
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [zhijiewong/openharness](../../repos/zhijiewong/openharness.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Works with ANY LLM via Ollama local models or cloud APIs (not locked to one provider); ~95% feature parity with Claude Code for CLI use; 44 tools and 80+ slash commands; auto git-commits every edit, reversible via /undo and /rewind; 27 hook event types configurable via .oh/config.yaml; full MCP server support (stdio + HTTP/SSE, OAuth 2.1); 11 specialized sub-agent roles; ...

(captured site page body (agents/openharness.md), not a verified repo-code finding)
Claude Code's terminal workflow is compelling but locks users to Anthropic models and accounts, and local-model users have no equivalent harness. OpenHarness reimplements that surface as a Node CLI called oh: 44 built-in tools, 80-plus slash commands, MCP server support, 27 hook events, permission modes, checkpoints with rewind, sub-agents, and a headless mode for CI/CD with a --max-budget-usd cost cap. Providers include Ollama (auto-detected, no key needed), OpenAI, Anthropic, OpenRouter, llama.cpp/GGUF, and LM Studio, so the same harness runs free on local models or BYOK in the cloud. Distribution covers npm plus official Python and TypeScript SDKs and a VS Code extension, and the repo publishes SWE-bench-Lite evaluations alongside its benchmarks. The project is small (96 stars) but actively developed with 1,502 passing tests. Developers who want the Claude Code interaction model on their own provider mix — especially local models — are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openharness.md)
