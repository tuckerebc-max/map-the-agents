# Harness Starter Kit (`harness-starter-kit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: harnessworks
- License: MIT
- Language: Markdown,Python
- Interface: install=Prompt-first (paste adoption prompt into coding agent); optional Python installer (python scripts/apply_harness.py --target . --profile generic --dry-run); or native plugin install for Codex (codex plugin marketplace add) or Claude Code (claude plugin install harness-agent-skills@harnessworks)
- Model providers: agent-agnostic (Claude Code, Codex, Cursor, Copilot)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [harnessworks/harness-starter-kit](../../repos/harnessworks/harness-starter-kit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Prompt-first starter kit that reframes the problem from 'prompt engineering the agent' to 'engineering the repository'; converts recurring agent failures into durable artifacts (instruction, constraint, check, memory record, drift check) for a continuous improvement loop grounded in repository evidence; separates failure types (functional, schema, workflow, boundary, timeout, hidden-access) instead of reducing to pass/fail; ships runtime-native skills for Codex and Claude ...

(captured site page body (agents/harness-starter-kit.md), not a verified repo-code finding)
harness-starter-kit applies the idea that a repository itself can be engineered to make coding agents fail less often. Rather than shipping a tool, it provides a structured kit — instructions, constraints, feedback loops, memory files, evaluation tasks, and governance documents — plus router prompts (/harness doctor, adopt, review, update, refresh) that a developer pastes into their existing agent, or installs as a Claude Code or Codex plugin for convenience. The kit's core loop converts each recurring agent failure into a durable artifact: an instruction, an automated check, a failure record, a memory entry, or a benchmark task, with a taxonomy separating functional, schema, workflow, boundary, timeout, and hidden-access failures. It takes an explicit measurement stance that harness health and agent effectiveness are separate metrics and ships templates for both. Teams adopting it range from solo developers to platform groups standardizing how agents interact with their repos.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/harness-starter-kit.md)
