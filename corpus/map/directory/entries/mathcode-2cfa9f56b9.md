# mathcode (`mathcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: math-ai-org
- License: Apache-2.0
- Language: TypeScript, Python
- Interface: install=binary
- Model providers: OpenAI, Anthropic, Bedrock, Vertex, Foundry, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [math-ai-org/mathcode](../../repos/math-ai-org/mathcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Mathematical coding agent focused on formal theorem proving in Lean. Atomic Lean tools (LeanGoal, LeanCheck, LeanSearch, LeanVerify) for interactive proof construction with strict verification. Persistent Lean feedback backends (in-process Lean REPL, optional Kimina Lean Server). Theorem Library (/theorem-store) and Axiom Library (/axiomatize). Obsidian Theorem Graph for visualizing dependencies. Agentic Lean (free subgoal decomposition, no fixed planner). Three plugin mechanisms: Skills, ...

(captured site page body (agents/mathcode.md), not a verified repo-code finding)
MathCode brings the agentic coding workflow to formal mathematics, where a proof is machine-checkable and verification is unambiguous. The agent inspects goals at explicit source positions, compiles candidate proofs with structured feedback, and treats only LeanVerify's verified flag as completion, with optional in-process REPL and Kimina Lean Server backends feeding the loop. Persistent theorem and axiom libraries store verified results transactionally, an Obsidian graph visualizes theorem dependencies, and three extension mechanisms (project-local skills, auto-discovered Python tools, plugin folders with commands/skills/agents/MCP servers/hooks) let formalization teams add domain tooling. Checksum-verified release binaries ship with a setup script that installs and health-checks Lean and Mathlib; mathematicians and formalization teams are the users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mathcode.md)
