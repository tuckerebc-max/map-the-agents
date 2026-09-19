# Agentic Engineering Framework (`agentic-engineering-framework`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: DimitriGeelen
- License: Apache-2.0
- Language: Bash, YAML
- Interface: platforms=CLI, IDE; install=curl install script; brew install DimitriGeelen/agentic-fw/agentic-fw; local clone; GitHub Action; fw init per-project
- Model providers: Claude Code, Cursor, Aider, Devin, Copilot
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [dimitrigeelen/agentic-engineering-framework](../../repos/dimitrigeelen/agentic-engineering-framework.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Governance and continuity harness around AI coding agents. Provides task traceability, structural gates, session continuity, audit trails, blast-radius foresight, value scoring, and cross-agent coordination. It coordinates agents but does not execute them. Enforces 'nothing gets done without a task' as a hard gate (PreToolUse hooks), three-layer persistent memory, Component Fabric for blast-radius impact analysis, Business Value Points (BVP) scoring, a ...

(captured site page body (agents/agentic-engineering-framework.md), not a verified repo-code finding)
AI coding agents fail in predictable ways: they edit without a task, destroy files with force flags, and run out of context mid-change. The framework interposes itself between the agent and the repository using a PreToolUse hook, tiered authority rules (human sovereignty, framework authority, agent initiative), and Markdown task files with YAML frontmatter carrying acceptance criteria and verification commands. A budget gate watches the live transcript and blocks source edits when the context window nears its limit, forcing a commit and handover instead of a truncated change. Memory, component maps, and audit checks (over 260 checks run on every push and on a 30-minute cron) provide continuity and traceability across sessions. It is used by developers running Claude Code who want audit-grade accountability; the framework itself is developed under its own governance, with thousands of self-governed commits.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agentic-engineering-framework.md)
