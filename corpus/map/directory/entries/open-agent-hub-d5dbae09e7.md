# open-agent-hub (`open-agent-hub`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: guanyang
- License: MIT
- Language: JavaScript
- Interface: platforms=CLI; install=npm
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes — agents directory with Orchestrator, Evaluator, and Optimizer roles with handoff contracts (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [guanyang/open-agent-hub](../../repos/guanyang/open-agent-hub.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Zero-dependency, single-command activation of Skills/Agents/Commands across 8+ AI coding assistants (Claude Code, Cursor, Trae, Gemini CLI, Codex, Antigravity, OpenCode, Kiro) with 83+ modular skills and upstream community sync.

(captured site page body (agents/open-agent-hub.md), not a verified repo-code finding)
open-agent-hub addresses the fragmentation of agent configuration formats across coding assistants by maintaining one library of skills, agent role definitions, and slash commands that activate into any supported tool. The oah CLI symlinks rather than copies, so a single source of truth updates everywhere, and an upstream sync command pulls community skill updates. Agent definitions go beyond static prompts: the hub ships Orchestrator, Evaluator, and Optimizer roles with explicit handoff contracts, encoding an evaluator-optimizer loop. Installation ranges from Vercel's skills CLI for skill-only use to the full oah CLI from a cloned repository. Bilingual documentation serves both English and Chinese-speaking users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-agent-hub.md)
