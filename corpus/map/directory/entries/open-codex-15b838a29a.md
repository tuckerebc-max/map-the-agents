# Open Codex (`open-codex`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: codingmoh
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=brew tap codingmoh/open-codex && brew install open-codex; or pipx install open-codex; or clone + pip install .
- Model providers: local models (e.g. phi-4-mini) and Ollama (llama3, mistral) via localhost:11434; no cloud APIs
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [codingmoh/open-codex](../../repos/codingmoh/open-codex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runs 100% locally with no OpenAI API key, translating natural language into shell commands via small local models or Ollama, and executes nothing without explicit per-command user confirmation.

(captured site page body (agents/open-codex.md), not a verified repo-code finding)
Most terminal coding assistants require cloud API keys, which blocks offline use and raises cost concerns for simple tasks. Open Codex takes the opposite position: a lightweight Python CLI inspired by OpenAI Codex that converts natural-language requests into shell commands using local models or an Ollama backend such as llama3 or mistral on localhost:11434. The interaction is deliberately one-shot — prompt, suggested command, then confirm, copy, or abort — with execution gated behind explicit user approval, so nothing runs without consent. It installs via Homebrew, pipx, or Debian packaging and runs on macOS, Linux, and Windows. The project is early-stage (36 commits, 696 stars), with interactive chat, TUI, function calling, and a plugin system listed as unimplemented future plans. It fits users who want an offline, zero-API-cost natural-language shell helper rather than a full agentic harness.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-codex.md)
