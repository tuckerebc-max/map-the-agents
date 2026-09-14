# SWE-Interact (`swe-interact`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: scaleapi
- License: Apache-2.0
- Language: Shell
- Interface: install=git clone Harbor repo, uv tool install ., then set up Modal (uv pip install modal + modal setup)
- Model providers: OpenAI, Anthropic, Google, Kimi
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [scaleapi/swe-interact](../../repos/scaleapi/swe-interact.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Benchmark of 75 tasks evaluating coding agents on realistic multi-turn, user-driven software engineering sessions using a simulated user (GPT-5.5) that interacts with the agent across turns, plus rubric-based grading (Anthropic Opus) — moving beyond single-turn benchmark evaluation toward authentic developer-agent collaboration.

(captured site page body (agents/swe-interact.md), not a verified repo-code finding)
SWE-Interact, from Scale AI, rethinks SWE evaluation around how engineers actually work with agents: long sessions in which requirements shift and the user supplies context. Its 75 tasks run inside the Harbor harness on Modal sandboxes, where a simulated user model converses with the coding agent over many turns, and success is decided by rubric-based grading from a separate judge model rather than by hidden unit tests alone. The design deliberately stresses behaviors single-turn benchmarks miss — clarifying requirements, recovering from changed instructions, and communicating trade-offs. Run configs cover single-turn baselines and multi-turn sessions for agents such as Codex and Claude Code, and the accompanying paper (arXiv 2606.30573) motivates the user-driven framing. Teams benchmarking coding agents for interactive, multi-turn use are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swe-interact.md)
