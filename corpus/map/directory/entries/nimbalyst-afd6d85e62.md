# Nimbalyst (`nimbalyst`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: nimbalyst
- License: MIT
- Language: TypeScript (Electron) + Swift (iOS)
- Interface: platforms=Desktop; install=binary - GitHub Releases (.dmg/.exe/.AppImage)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes - Extension System with pluggable editors (Astro, visual git log, mindmap, slides, 3D object editor) via EditorHost contract (yes)
  - claude_code_plugin: n/a - Claude Code is a first-class supported agent; .claude/ and CLAUDE.md present (reported)
  - subagents: no (no)
  - hooks: no - .githooks present but not a documented feature (no)
  - plan_mode: no (no)

Repository map entry: [nimbalyst/nimbalyst](../../repos/nimbalyst/nimbalyst.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source local visual workspace and session/task manager for coding agents (Codex, Claude Code, OpenCode, Copilot). Visual WYSIWYG collaboration: see agent changes as red/green diffs, approve/edit/annotate directly in markdown, mockups, Mermaid, Excalidraw, CSV, data models, Monaco. Parallel session management (Kanban board, search/resume, link files to sessions) plus task tracking both humans and agents can edit. Mobile companion iOS app. Extension system ...

(captured site page body (agents/nimbalyst.md), not a verified repo-code finding)
Nimbalyst gives developers a visual surface for working with coding agents instead of reading terminal transcripts. Parallel sessions run in isolated git worktrees managed from a kanban board, and agent changes land as inspectable diffs that a human steps through before anything is committed. Task tracking, git staging, AI-drafted commits, and an embedded Ghostty terminal live alongside the editors, and an MCP client renders tool results as visual widgets. Everything is plain files in the user's git repository with no proprietary store, and iOS/Android companions surface which agents need attention. The project is MIT-licensed Electron/TypeScript with an open collaboration wire protocol.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nimbalyst.md)
