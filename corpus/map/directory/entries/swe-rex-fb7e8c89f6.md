# SWE-ReX (`swe-rex`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: SWE-agent
- License: MIT
- Language: Python
- Interface: platforms=Web; install=pip
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [swe-agent/swe-rex](../../repos/swe-agent/swe-rex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runtime interface for sandboxed shell environments allowing AI agents to run any command locally or remotely (Docker, AWS, Modal, etc.) with identical agent code; supports massively parallel agent runs, interactive CLI tools (ipython, gdb), and multiple parallel shell sessions; disentangles agent logic from infrastructure

(captured site page body (agents/swe-rex.md), not a verified repo-code finding)
SWE-ReX came out of the SWE-agent project's observation that infrastructure churn, not model capability, caused most harness failures at scale. It defines a runtime interface between an agent and its shell: a persistent, sandboxed process manager that detects command completion, extracts output and exit codes, supports interactive programs like ipython and gdb, and keeps several shell sessions open per agent. The same agent code runs locally or against Docker containers, AWS Fargate, or Modal sandboxes, with a pluggable backend interface for adding more, which is what lets benchmark sweeps fan out to dozens of instances in parallel. The project is MIT-licensed, installable from PyPI with per-backend extras, and documented at swe-rex.com. Agent-framework builders — including mini-SWE-agent and SWE-smith — embed it rather than reimplementing sandbox plumbing.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swe-rex.md)
