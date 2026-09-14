# ospec (`ospec`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: clawplays
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm install -g @clawplays/ospec-cli
- Model providers: agent-agnostic (Claude Code, Codex/GPT, Gemini, OpenCode, MCP-based agents)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: yes (yes)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [clawplays/ospec](../../repos/clawplays/ospec.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Spec-driven development (SDD) + 'Loop Engineering' — a verifiable plan -\> act -\> verify goal loop that persists proposals, designs, plans, tasks, reviews, and verification evidence as repo files instead of chat history, enabling any AI agent to resume work mid-stream across different harnesses (Claude Code, Codex/GPT, Gemini, OpenCode). Native subagent dispatch, hooks, and skills system.

(captured site page body (agents/ospec.md), not a verified repo-code finding)
Long agentic tasks fail in chat history: context scrolls away, decisions lose their rationale, and a fresh session cannot resume mid-change. OSpec moves the workflow into the repository — ospec init creates a .ospec/ protocol shell, and changes persist proposals, designs, plans, tasks, reviews, and verification evidence as files any agent can read and extend. A verifiable plan-act-verify goal loop governs execution: token-bounded ticks dispatch tasks to subagents through per-harness adapters, heartbeats track liveness, reviewer gates hold work until checks pass, and ospec verify plus finalize validate and archive the change. It ships as an npm CLI with a SKILL.md-based skill bundle for Claude Code, a hook bundle that hard-blocks subagent dispatch during pending decisions, and equivalents for Codex, Gemini, and OpenCode. Install is npm -g @clawplays/ospec-cli under Node 18+. Teams running multi-hour agent workflows that must survive session boundaries are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ospec.md)
