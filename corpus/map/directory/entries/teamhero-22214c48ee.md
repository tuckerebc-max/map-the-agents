# TeamHero (`teamhero`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: sagiyaacoby
- License: MIT
- Language: JavaScript, Node.js
- Interface: platforms=Web; install=Prerequisite: npm install -g @anthropic-ai/claude-code. Then: git clone https://github.com/sagiyaacoby/TeamHero.git my-team; cd my-team; npm install; launch via launch.bat (Windows) or bash launch.sh (Mac/Linux); dashboard opens at http://localhost:3777
- Model providers: Claude CLI (Anthropic)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [sagiyaacoby/teamhero](../../repos/sagiyaacoby/teamhero.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted structured AI agent orchestration platform that manages agents like a real team with project-management discipline: every task goes through plan -\> review -\> execute -\> deliver; persistent short/long-term agent memory across sessions; file-scope declarations prevent agents from overwriting each other's work; knowledge base promotes deliverables into a searchable library; dashboard web UI plus integrated Command Center terminal; optional Skills ...

(captured site page body (agents/teamhero.md), not a verified repo-code finding)
TeamHero is the self-hosted, MIT-licensed core of the Kapow managed-agent platform, built on the premise that parallel coding agents fail without management structure. It runs Claude Code as the execution engine and adds an orchestration layer: an orchestrator agent directs the team via a Command Center terminal, every task must produce a plan that is reviewed before any code executes, and finished deliverables are versioned and promoted into a knowledge base for retrieval by later tasks. Coordination hazards are addressed structurally — agents declare file scopes so two workers cannot overwrite the same file, and per-agent short- and long-term memory persists across sessions — while optional skills add browser automation and GitHub integration. A web dashboard at localhost:3777 exposes the whole operation. Solo developers and small teams already paying for Claude Code who want supervised, structured multi-agent execution rather than ad-hoc parallel sessions are the target users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/teamhero.md)
