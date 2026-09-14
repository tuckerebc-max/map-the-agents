# Pi Coding Agent (`pi-coding-agent-vscode`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: pi0
- License: unknown
- Language: unknown
- Interface: platforms=IDE; install=Install from the VS Code Marketplace
- Model providers: whatever the pi CLI supports (multi-provider; requires the @mariozechner/pi-coding-agent CLI)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

Discrepancy between directory sources (not overwritten):

- category: published=, backing=multiplexer, page=other

## Description

Highlight (site page `what_makes_it_special`): VS Code extension for the pi coding agent

(captured site page body (agents/pi-coding-agent-vscode.md), not a verified repo-code finding)
This extension is the pi project's own bridge into VS Code: it runs the pi CLI (a prerequisite, installed globally) in an integrated terminal with full PTY support, then bundles a pi extension that feeds the agent around 25 tools reflecting live editor state. The agent can query active editors, selections, diagnostics, symbols, and definitions, and apply workspace edits synchronized with open buffers, while a footer shows the active file, cursor position, and diagnostic counts inside the TUI. A @pi chat participant brings streamed RPC-backed replies into VS Code Chat, and a package-manager sidebar installs pi extensions, skills, prompts, and themes without leaving the editor. With about 7,800 installs, it serves pi users who want the CLI's autonomy without leaving VS Code, keeping the agent loop itself entirely in pi.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-coding-agent-vscode.md)
