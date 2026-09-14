# Podiom (`podiom`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Podiom
- License: MIT
- Language: Go
- Interface: platforms=Autonomous, CLI, IDE, Web; install=macOS/Linux: curl -fsSL https://github.com/Podiom/Podiom/releases/latest/download/install.sh | bash; Windows: irm https://github.com/Podiom/Podiom/releases/latest/download/install.ps1 | iex
- Model providers: Claude Code (Anthropic), OpenAI Codex
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [podiom/podiom](../../repos/podiom/podiom.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source, local-first workspace for Claude Code and OpenAI Codex that provides durable context, sessions, projects, tasks, and scheduling for local LLM agents while the native CLIs do the work. Thin orchestration layer with full audit trails and agent identities. Lead agents can delegate work to other agents and turn outcomes into roadmap tasks.

(captured site page body (agents/podiom.md), not a verified repo-code finding)
Podiom targets developers running Claude Code and OpenAI Codex side by side whose sessions, context, and task state live nowhere durable — each CLI restarts from scratch and nothing links the two. The Go daemon provides that missing layer: named agent identities with workspace, model, profile, and permission mode; projects with shared context and roadmap tasks; scheduled recurring runs; and Goals, where a lead agent pursues a long-running outcome, delegates to other agents, and converts outcomes into roadmap tasks with an auditable trail. Sessions keep canonical history and can replay it onto a fresh CLI session after a provider or profile switch, and the layer never replaces the CLIs' own models, tools, or authentication. State lives under ~/.podiom with an embedded web UI, native mobile apps, and a Home Assistant add-on option. Its early adopters are local-first developers running multi-agent workflows entirely on their own machines.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/podiom.md)
