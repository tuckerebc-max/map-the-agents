# claude_code_sub_agents (`claude-code-sub-agents`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: yzyydev
- License: unknown
- Language: Markdown
- Interface: install=git clone; use via Claude Code custom commands (.claude/commands/)
- Model providers: Anthropic (via Claude Code subagents)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [yzyydev/claude_code_sub_agents](../../repos/yzyydev/claude_code_sub_agents.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Claude Multi-Agent iterative sub-agent orchestration system using Claude Code custom commands. Wave-based agent deployment, parallel task distribution with concept deduplication, and progressive context summarization to achieve infinite-scale task execution within context constraints.

(captured site page body (agents/claude-code-sub-agents.md), not a verified repo-code finding)
The project demonstrates a pattern for pushing Claude Code past single-context limits: work is divided into waves, each wave spawns fresh sub-agents with clean context windows, and the orchestrator keeps only lightweight state while progressive summarization carries conclusions forward. Each sub-agent receives a unique direction to avoid duplicated output, and the system plans graceful conclusions as capacity is approached. The commands ship as markdown files dropped into .claude/commands/, with no code or runtime beyond Claude Code itself. It is a two-commit proof-of-concept used by prompt-engineering practitioners exploring large parallel generation, not a maintained product.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/claude-code-sub-agents.md)
