# vibe-annotations (`vibe-annotations`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: RaphaelRegnier
- License: PolyForm Shield 1.0.0
- Language: JavaScript
- Interface: install=Browser extension (Chrome Web Store) + npx vibe-annotations-server init (global server setup wizard)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [raphaelregnier/vibe-annotations](../../repos/raphaelregnier/vibe-annotations.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Visual feedback/annotation tool for localhost web development; annotate page elements, make design tweaks, and share with AI coding agents or teammates to auto-implement fixes via MCP. Configures Claude Code, Cursor, Windsurf, Codex, OpenClaw, VS Code.

(captured site page body (agents/vibe-annotations.md), not a verified repo-code finding)
Visual feedback in web development usually dies in screenshots: someone marks up a page, and the annotations become tickets or re-typed prompts. Vibe-annotations closes that loop for AI-driven development — the Chrome extension annotates elements directly on localhost pages across multiple pages per session, and a companion server (installed with a single npx command that also configures the coding agent) exposes those annotations over MCP so Claude Code, Cursor, Windsurf, Codex, or VS Code receive structured fix requests instead of screenshots. Annotations can also be copied to the clipboard or shared with teammates through file sharing and watch mode, making the same channel useful for human review. Front-end developers iterating on design with AI agents are the users; the project is under the PolyForm Shield license, actively maintained with CI and community health files.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibe-annotations.md)
