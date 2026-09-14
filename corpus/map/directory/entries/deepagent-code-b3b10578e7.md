# deepagent-code (`deepagent-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: deepagent-ltd
- License: AGPL-3.0-or-later (derived from opencode under MIT)
- Language: TypeScript
- Interface: install=curl -fsSL https://deepagent.ltd/install | bash (macOS/Linux); or desktop app; npm package not yet publicly published
- Model providers: OpenAI, Anthropic, DeepSeek, Google, xAI, ZhipuAI/GLM, OpenAI-compatible, Anthropic-compatible (75+ providers via AI SDK + models.dev)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [deepagent-ltd/deepagent-code](../../repos/deepagent-ltd/deepagent-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI coding agent/workspace with durable governed memory (typed, versioned documents with provenance); four-graph unified store (code + knowledge + memory + docs); live steering during running tasks; three collaboration modes (Auto/Loop/Design); Expert Panel for high-risk decisions; LSP-based AI IDE with 38 language servers

(captured site page body (agents/deepagent-code.md), not a verified repo-code finding)
deepagent-code targets work that spans more than one prompt: long-running tasks where the agent must remember decisions, constraints, and past failures across sessions. It builds on opencode and adds a control plane where project memory is stored as typed, versioned documents with provenance rather than prompt text, and where four graph stores (code symbols, knowledge, memory, documents) feed a shared context assembly with admission gates. During execution, users can steer live goals without aborting in-flight work, and subagents run in isolated worktrees under a generation-fenced lifecycle with review sessions; an Expert Panel mode runs bounded adversarial debate between specialist lenses. It is AGPL-3.0 with a separate enterprise distribution, BYO-model-keys across 75+ providers, and targets teams who need auditable, steerable agent behavior over codebases.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepagent-code.md)
