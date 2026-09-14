# vibe-replay (`vibe-replay`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tuo-lei
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=CLI: npx vibe-replay; Plugin: /plugin marketplace add tuo-lei/vibe-replay; Agent Skills: npx skills add tuo-lei/vibe-replay --skill replay -g; Manual: curl SKILL.md into ~/.claude/skills/replay/
- Model providers: Supported session providers: Claude Code, Claude Desktop, Claude Cowork, Codex, Cursor, OpenCode, Hermes, Pi
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [tuo-lei/vibe-replay](../../repos/tuo-lei/vibe-replay.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Turns AI coding sessions into shareable, interactive self-contained HTML replays — animating every prompt, thought, tool call, and code diff. One command, zero config, offline-ready. Secret redaction built in. Live mode streams a running Claude Code or Codex session in real time. Deep analytics: token burn, cost over time, context window usage, cache hit rates, tool call distribution. Claude Code ...

(captured site page body (agents/vibe-replay.md), not a verified repo-code finding)
AI coding sessions disappear when the terminal closes: reviewers see only the final diff, and the prompts, dead ends, and tool calls that produced it are lost. Vibe-replay converts session logs from Claude Code, Codex, Cursor, OpenCode, and other harnesses into one self-contained HTML file that animates the whole run — prompts, model thinking, tool calls, and code diffs — without proxies or wrappers since it reads session logs afterward; secret redaction runs before export, and Live mode streams a session in progress. A companion dashboard indexes past sessions with token, cost, and context-window analytics and filters by repo, tool, or MCP server. Developers use it to review their own agent runs, attach reproducible evidence to pull requests and issue reports, and audit what an autonomous session actually did; a Claude Code plugin inserts replay links directly into pull requests.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibe-replay.md)
