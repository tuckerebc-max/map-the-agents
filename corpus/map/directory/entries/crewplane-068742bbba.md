# Crewplane (`crewplane`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: crewplaneai
- License: Apache-2.0
- Language: Python 3.13+
- Interface: platforms=CLI, IDE; install=uv tool install crewplane (recommended); or python -m pip install crewplane; or npm install -g crewplane. Also supports pipx, Homebrew, and an install script. Crewplane does not install or manage provider CLIs or credentials.
- Model providers: Claude Code, Codex, Gemini, Copilot CLI, any CLI-based tool; built-in mock provider for deterministic testing
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [crewplaneai/crewplane](../../repos/crewplaneai/crewplane.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Provider-neutral control plane for human-designed coding-agent workflows; turns AI agent calls into structured, repeatable DAGs defined in Markdown (versioned, reviewable in PRs, shareable); CLI-first design invokes provider CLIs directly instead of wrapping them in vendor SDKs - if a tool has a command line, Crewplane can orchestrate it; saves every input, output, and decision to disk and resumes from validated ...

(captured site page body (agents/crewplane.md), not a verified repo-code finding)
Crewplane targets teams whose coding-agent usage has outgrown ad-hoc prompting but who do not want a vendor's hosted orchestration layer. Workflows are declared in Markdown as DAGs of stages, agent assignments, prompts, handoffs, and review gates; Crewplane validates them, routes work to CLIs like Claude Code and Codex while leaving each agent's models, tools, and MCP servers under native control, and records per-stage artifacts for resumption and audit. The CLI-first design keeps definitions in git, so process changes go through normal code review. Its audience is engineering teams on Linux, macOS, or WSL who want repeatable, observable agent pipelines without giving up control of the underlying agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/crewplane.md)
