# opencode-swarm (`opencode-swarm`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ZaxbyHub
- License: MIT
- Language: TypeScript
- Interface: install=bunx opencode-swarm install (requires Bun) or npm install -g opencode-swarm && opencode-swarm install
- Model providers: OpenCode Zen, Anthropic, Google, Z.ai, MiniMax, Kimi
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [zaxbyhub/opencode-swarm](../../repos/zaxbyhub/opencode-swarm.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): OpenCode plugin that turns one AI coding session into an architect-led team of 20 specialized agents with a gated pipeline (code never ships without reviewer + test engineer approval), shell write detection, scope enforcement, resumable sessions, built-in security scanning, and context budget guard

(captured site page body (agents/opencode-swarm.md), not a verified repo-code finding)
A single coding agent grades its own homework: it writes the code, decides the work is done, and moves on. opencode-swarm restructures the session into a hub-and-spoke swarm where an architect plans, a coder implements, and dedicated reviewer, test-engineer, critic, security, and documentation agents gate the result through a pipeline that blocks shipping until every required approval lands. State persists in .swarm/ so interrupted sessions resume, shell writes are detected and policed against scope, and SAST plus secrets scanning run before completion; thirteen language profiles tune behavior per stack. Installation is one command (bunx opencode-swarm install) and it works with OpenCode Zen's free model roster without an API key, or with any BYO provider. With 4,300 commits, 6,000+ tests, and an active release cadence, it is one of the heavier OpenCode plugins. Teams that want enforceable multi-agent review discipline on top of OpenCode are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencode-swarm.md)
