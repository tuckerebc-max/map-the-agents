# CodeFox-CLI (`codefox-cli`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: codefox-lab
- License: MIT
- Language: Python
- Interface: platforms=CLI, Web; install=uv tool install codefox or python3 -m pip install codefox
- Model providers: Ollama, Gemini, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [codefox-lab/codefox-cli](../../repos/codefox-lab/codefox-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Diff-aware AI code review tool that uses relevant codebase context rather than isolated files. CLI-first design suited for terminal and CI/CD workflows. Runs locally with Ollama for privacy or with cloud LLMs. Configurable review focus (security, performance, style) and can suggest fixes, not just flag issues.

(captured site page body (agents/codefox-cli.md), not a verified repo-code finding)
CodeFox-CLI is built for review workflows in the terminal and CI rather than in-editor assistance. For each change it collects the git diff, retrieves related codebase context using fastembed embeddings, and produces prioritized findings with optional fix suggestions. Review focus is configurable — security, performance, style — and inference runs either fully local through Ollama or through cloud providers Gemini and OpenRouter, with fastembed handling embeddings. It integrates as a GitHub Action ('CodeFox AI Review') and with GitLab pipelines, and configuration (providers, models, review rules, prompts) is documented in a GitHub wiki. The project is an MIT-licensed Python package on PyPI, installed via pip or uv.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codefox-cli.md)
