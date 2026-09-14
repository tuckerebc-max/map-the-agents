# Agon (`agon`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: AutoResearch-Factory
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, IDE; install=git clone Agon and agon-artifacts side by side; run claude --plugin-dir ../Agon --dangerously-skip-permissions --effort medium --model claude-sonnet-5
- Model providers: Anthropic, DeepSeek
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [autoresearch-factory/agon](../../repos/autoresearch-factory/agon.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Autonomous AI research system built on the 'Prompt Economy' concept. Agents (scientist, coder, auditor, reviewer) plan, implement, audit, and review each other in closed loops with all handoffs via files on disk for recoverability and auditability. Runs unattended for hours. Deployable across 10+ research domains. No human-written experimental code needed.

(captured site page body (agents/agon.md), not a verified repo-code finding)
Running AI research loops unattended for hours usually produces unrecoverable messes, and the engineering effort of orchestrating agents lands on the human. Agon, distributed as a Claude Code plugin, pushes all coordination into disk files: topics, ideas, proposals, and experiments live in a side-by-side agon-artifacts repository, so any run can be inspected, resumed, or forked independently of the plugin code. Slash commands drive role-structured loops — /idea-tick, /proposal-tick, and /experiment-tick, which coordinates scientist, coder, auditor, and reviewer roles per workspace — with prompts, code, and research data versioned independently. Loops run under --dangerously-skip-permissions for genuinely unattended operation, and wrapper scripts let the same plugin run Claude Code backed by DeepSeek or other providers via CLIProxyAPI. It targets researchers automating the topic-to-running-experiment pipeline across domains.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agon.md)
