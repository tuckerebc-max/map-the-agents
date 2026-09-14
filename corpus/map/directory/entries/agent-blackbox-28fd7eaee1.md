# Agent-Blackbox (`agent-blackbox`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: TaewoooPark
- License: MIT
- Language: TypeScript
- Interface: install=npx @taewooopark/agent-blackbox up --host claude-code (or codex, or all); or git clone + npm install + npm run build:cli
- Model providers: Ollama, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [taewooopark/agent-blackbox](../../repos/taewooopark/agent-blackbox.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first flight recorder and context-efficiency profiler for coding agents that turns every agent run into a live, replayable operational graph reconstructed from observed events (not agent self-summary). Scores runs on 11 context-efficiency metrics with task-tailored scoring, can write fixes back to CLAUDE.md/AGENTS.md, and offers an in-run optimizer cutting ~94-96% of re-read tokens. Host-agnostic (Claude Code, Codex, OpenCode).

(captured site page body (agents/agent-blackbox.md), not a verified repo-code finding)
When a coding agent wastes half its context re-reading files or repeating failed approaches, nothing in the transcript explains the pattern, so Agent-Blackbox records runs externally and reconstructs what actually happened from observed events — files read, edits, commands, subagent delegations. Each run gets scored on eleven context-efficiency metrics plus outcome, and the tool can write a reversible memory block into CLAUDE.md or AGENTS.md so future runs avoid the same waste; an in-run optimizer trims redundant reads by roughly 94–96%. It runs via npx against Claude Code, Codex, or OpenCode sessions, needs no API key, and keeps everything local. Developers tuning agent cost and reliability use it as a profiler rather than a harness.
Sources: [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/agent-blackbox.md)
