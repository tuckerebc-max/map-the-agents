# Cline (`cline`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: cline
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm i -g cline (CLI), VS Code Marketplace, JetBrains Marketplace, npm install @cline/sdk (SDK), npm i -g kanban (Kanban)
- Model providers: Anthropic, OpenAI, Google, OpenRouter, Vercel AI Gateway, AWS Bedrock, Azure, GCP Vertex, Cerebras, Groq, Ollama, LM Studio, any OpenAI-compatible API
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [cline/cline](../../repos/cline/cline.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Autonomous coding agent available as SDK, IDE extension, or CLI. Features Plan/Act modes, multi-agent teams with coordinator delegating to specialist agents, kanban-style parallel agent task boards, scheduled agents, messaging integrations (Slack, Telegram, Discord), and headless CI/CD mode.

(captured site page body (agents/cline.md), not a verified repo-code finding)
Cline's design premise is that autonomy must remain inspectable: every edit appears as a diff, every command can require approval, and checkpoints allow undo, which separates it from fire-and-forget agents. Plan/Act separation lets users review strategy before execution, and the same core powers an IDE extension, a headless CLI for pipelines, and an SDK for building custom agents, all reading the same .clinerules. Multi-agent teams coordinate through a coordinator that delegates to specialists with their own tools, and scheduled agents run recurring jobs like dependency checks. Apache-2.0 and model-agnostic across all major providers plus local runtimes, it is one of the most widely adopted open-source agents in this census.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cline.md)
