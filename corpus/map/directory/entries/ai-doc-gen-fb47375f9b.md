# ai-doc-gen (`ai-doc-gen`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: divar-ir
- License: MIT
- Language: Python
- Interface: install=Claude Code plugin install, pip (uv sync), docker
- Model providers: any OpenAI-compatible (OpenAI, Anthropic-compatible gateways, OpenRouter, local models)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Claude Code plugin) (yes)
  - claude_code_plugin: yes (/plugin marketplace add divar-ir/ai-doc-gen; /plugin install ai-doc-gen@divar) (yes)
  - subagents: yes (5 specialized analysis agents: code structure, data flow, dependencies, request flow, APIs; coordinated by AnalyzerAgent via worker pool) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [divar-ir/ai-doc-gen](../../repos/divar-ir/ai-doc-gen.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): AI-powered multi-agent system that analyzes codebases and generates documentation (README.md) plus AI assistant configuration files (CLAUDE.md, AGENTS.md, .cursor/rules/). 5 specialized AI agents run in parallel for deep analysis. Dual-purpose as Claude Code plugin (no API keys needed). GitLab cronjob automation discovers active projects and opens MRs with fresh docs. Production-ready with Docker, Helm, OpenTelemetry/Langfuse observability.

(captured site page body (agents/ai-doc-gen.md), not a verified repo-code finding)
Documentation and AI-assistant config files go stale the moment a codebase changes, and most generators produce one-shot summaries with no intermediate evidence. ai-doc-gen runs five specialized analysis agents concurrently over the repository — each producing a document in .ai/docs/ — then feeds them to a DocumenterAgent that writes the README and an AIRulesGeneratorAgent that emits CLAUDE.md, AGENTS.md, and .cursor/rules files from the same analysis. Agents are built on pydantic-ai with YAML/Jinja2 prompts and only file-read/list tools, with worker-pool concurrency tuned by environment variable and observability via logfire/OpenTelemetry and Langfuse. It is distributed both as a Python CLI (Python 3.13, uv) and as a Claude Code plugin installable from a marketplace, and a GitLab cron mode can discover active projects and open merge requests with refreshed docs. Divar uses it internally to keep assistant context files aligned with the actual codebase.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ai-doc-gen.md)
