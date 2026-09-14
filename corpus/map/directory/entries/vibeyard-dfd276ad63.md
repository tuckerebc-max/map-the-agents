# vibeyard (`vibeyard`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: elirantutia
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=binary, npm
- Model providers: Anthropic, OpenAI, Google
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [elirantutia/vibeyard](../../repos/elirantutia/vibeyard.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): IDE built specifically for AI coding agents — multi-session PTY management, kanban task board, P2P live session sharing (WebRTC), swarm mode, cost & context tracking per session, AI Readiness Score, embedded browser with DOM element inspection, multiple Claude profiles with isolated configs.

(captured site page body (agents/vibeyard.md), not a verified repo-code finding)
Running several agent CLIs means juggling terminal tabs with no overview of which session is waiting, what each costs, or whether the repository is ready for agentic work at all. Vibeyard makes sessions the primary object: each project has a kanban board whose cards spawn and resume Claude Code, Codex, or Gemini CLI sessions in dedicated PTYs, completed sessions move their own cards, and a swarm grid lays every live session out for parallel supervision. It tracks cost, token, and context-window usage per session, scores the repo's AI Readiness, embeds a browser whose DOM elements can be inspected and sent to the agent for editing, and separates work/personal Claude accounts into isolated profiles. Independent developers and small teams supervising multiple agent runs use it; it is MIT-licensed Electron/TypeScript with signed installers for all three desktop platforms.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibeyard.md)
