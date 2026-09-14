# dunk (`dunk`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: amix
- License: MIT
- Language: TypeScript/JavaScript (Node.js 18+)
- Interface: platforms=CLI; install=npm i -g dunkdiff (Node.js 18+, Git)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [amix/dunk](../../repos/amix/dunk.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal UI to review git diffs, leave hunk-anchored inline comments (saved to .dunk/comments.json), and let a coding agent read and fix those comments. Human-agent review loop: one human in a terminal reviewing diffs and one coding agent in another terminal fixing flagged issues — comments are hunk-anchored (not line-scoped) and survive small edits via a context hash. No daemon / ...

(captured site page body (agents/dunk.md), not a verified repo-code finding)
Code review between a human and an agent usually happens through PRs, which are slow and lose the working-tree context. dunk puts the review in the terminal: press a on a hunk to leave a comment, and it lands in .dunk/comments.json as a hunk-scoped note that Claude Code or Codex can read, fix, and delete when resolved. With --watch the diff reloads as the agent commits, and drifted anchors surface at the top instead of silently breaking. It stays deliberately thin — no daemon, no MCP, no session broker — treating the JSON file as the whole contract. The workflow targets developers who review agent output locally, one human terminal next to one agent terminal.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/dunk.md)
