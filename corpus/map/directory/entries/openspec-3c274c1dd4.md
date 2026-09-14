# OpenSpec (`openspec`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Fission-AI
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: BYOK (works with 30+ AI assistants)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (community schemas) (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [fission-ai/openspec](../../repos/fission-ai/openspec.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Adds a lightweight spec layer for AI coding assistants to agree on what to build before code is written, using an artifact-guided workflow with plain Markdown; supports 30+ tools and enables cross-repo planning via 'Stores.'

(captured site page body (agents/openspec.md), not a verified repo-code finding)
AI coding assistants routinely build the wrong thing because intent lives in a chat transcript rather than a reviewable artifact. OpenSpec inserts a lightweight spec process: openspec init scaffolds a convention directory, and each change becomes a proposal, spec deltas, design notes, and a task list in plain Markdown that the assistant must follow before writing code. Slash commands (/opsx:explore, /opsx:propose, /opsx:apply, /opsx:archive) adapt to whichever tool is in use — Claude Code, Cursor, GitHub Copilot, Amazon Q, Codex, and 30-plus others — and archived changes remain in the repo as a decision record. Beta 'Stores' let teams share specs across repositories, and anonymous telemetry (command names only) is opt-out. The npm CLI installs globally under MIT and requires Node 20.19+, and the project dogfoods itself with 66k stars. Teams that want lightweight, tool-agnostic specification discipline ahead of agent-driven implementation are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openspec.md)
