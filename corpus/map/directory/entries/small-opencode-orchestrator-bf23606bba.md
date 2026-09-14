# small-opencode-orchestrator (`small-opencode-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tempont
- License: MIT
- Language: TypeScript
- Interface: install=Clone to ~/.config/opencode, then npm install
- Model providers: DeepSeek V4 Pro / GLM 5.2 (primary agents), DeepSeek V4 Flash (subagents)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [tempont/small-opencode-orchestrator](../../repos/tempont/small-opencode-orchestrator.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Lightweight OpenCode configuration implementing an orchestrator pattern for AI-assisted software development. Intentionally minimal — not a general-purpose agent platform, but a small, understandable orchestrator pattern with token-conscious delegation (subagents get focused tasks, not full context) and approval-gated planning. Pairs strong models for coordination/primary agents with cheap models for scoped subagent tasks to optimize cost and quality. Subagents: plan-runner, code-executor, test-verifier, ...

(captured site page body (agents/small-opencode-orchestrator.md), not a verified repo-code finding)
The project is a configuration rather than a binary: cloned into ~/.config/opencode, it defines an orchestrator agent that routes work to plan-runner, code-executor, test-verifier, code-reviewer, docs-reviewer, security-reviewer, and other scoped subagents. Plans are written to .opencode/plans and a post-approval plugin routes the session from planning into build mode, keeping subagent prompts focused instead of shipping them the full context. Model routing is explicit and editable in opencode.jsonc, pairing expensive reasoning models with cheap execution models to control cost. It fits OpenCode users who want a readable, hackable multi-agent setup they can audit line by line rather than an agent platform.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/small-opencode-orchestrator.md)
