# EntwineLLM (`entwinellm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: EmilianoMusso
- License: MIT
- Language: C#, .NET (Visual Studio extension)
- Interface: install=Install the Visual Studio extension; configure in Visual Studio Options (base URL, model, timeout, language); requires a running local LLM (Ollama or LMStudio) with an accessible API endpoint
- Model providers: Ollama, LMStudio (any local LLM with API endpoint); bearer-token auth for reverse proxies (v1.13+)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [emilianomusso/entwinellm](../../repos/emilianomusso/entwinellm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Free Visual Studio extension for code refactoring, unit-test generation, documentation (Markdown/HTML), and code review using only locally-installed LLMs (Ollama/LMStudio) so no data is sent to third-party APIs; strict prompt engineering rejects non-coding requests and enforces Clean Code principles, Allman-style braces, and modular/testable output; iterative follow-up refinement within the same workflow.

(captured site page body (agents/entwinellm.md), not a verified repo-code finding)
EntwineLLM exists for developers whose code cannot leave the machine — regulated environments, air-gapped networks, or simply preference for local inference. The extension sends selected code to an Ollama or LMStudio endpoint (local or Docker-hosted, with bearer-token auth added in v1.13 for proxied setups) and returns refactoring suggestions aligned with Clean Code principles, unit tests covering execution paths, Markdown documentation exportable to HTML, or a code review from a senior-developer perspective. Follow-up prompts allow iterative refinement, and per-command model and timeout settings let users route cheap tasks to smaller local models. It supports C#, Python, and Java, and is a single-maintainer project with modest but continuing releases.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/entwinellm.md)
