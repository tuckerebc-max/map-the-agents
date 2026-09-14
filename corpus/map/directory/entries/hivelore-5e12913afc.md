# Hivelore (`hivelore`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Doucs91
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @hivelore/cli (optional: npm install -g @hivelore/embeddings for local semantic search)
- Model providers: Claude Code, Cursor, VS Code, Cline, Windsurf, Codex, Continue, GitHub Copilot, Cody, Gemini CLI, Zed, Aider, Roo
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [doucs91/hivelore](../../repos/doucs91/hivelore.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Deterministic policy gate for AI coding agents: briefs agents with team-specific repo knowledge before they act, then blocks commits that repeat past mistakes via MCP, Git hooks, and CI. Converts captured team mistakes into deterministic blocking gates (regex, ast-grep structural patterns, or shell/test command sensors) that refuse the commit repeating them - same diff, same verdict, every machine. The command ...

(captured site page body (agents/hivelore.md), not a verified repo-code finding)
hivelore addresses a recurring failure of coding agents: they lack access to the team's accumulated knowledge and therefore repeat mistakes that have already been diagnosed. It maintains markdown memory records — decisions, gotchas, conventions, failed attempts — anchored to code paths with staleness detection, seeded from git revert history, scanner output (Sonar, SARIF, ESLint), and optional stack packs. Before an agent acts, an MCP briefing tool supplies project context and ranked warnings; before code merges, enforcement gates run regex, ast-grep, and command-based sensors to block diffs that recreate documented failures or weaken the sensors themselves, with advisory, balanced, and strict postures. Bridges write native config for roughly thirteen harnesses (CLAUDE.md, .cursorrules, copilot-instructions, and so on), and a GitHub Action ingests PR review feedback as new memories. The project is early with minimal adoption but under steady development.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hivelore.md)
