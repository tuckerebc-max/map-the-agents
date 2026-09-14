# claudemacs (`claudemacs`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: cpoile
- License: MIT
- Language: Emacs Lisp
- Interface: install=Install via Doom Emacs package!, use-package with :vc (Emacs 30+), vc-use-package, straight.el, or manual clone. Requires Emacs 28.1+ and eat package.
- Model providers: Any CLI-based AI tool (Claude Code, Codex, Gemini, Aider) via configurable tool registry
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [cpoile/claudemacs](../../repos/cpoile/claudemacs.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Emacs package for AI pair programming with Claude Code and other AI coding CLIs using the eat terminal emulator. Deliberately avoids agents, MCP, and IDE integration to let the LLM CLI 'shine in the terminal.' Features multi-tool support via configurable tool registry, multiple concurrent sessions per workspace, broadcast to all sessions, workspace/project-aware sessions, and rich Emacs integration (fix error at ...

(captured site page body (agents/claudemacs.md), not a verified repo-code finding)
Claudemacs takes the position that Claude Code's terminal UI is the product, so instead of re-implementing chat, diffs, and tools in Elisp it embeds the real TUI in an Emacs terminal window and adds only the integration Emacs users miss: project-aware session management, notifications when the agent needs attention, keybindings that map terminal quirks (C-g to Esc), and commands to send the error at point or implement the comment at point. No agent, MCP, or IDE protocol layer is added, by design, to avoid consuming context. Emacs users who want Claude Code without leaving their editor are the audience, and the package is actively maintained.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claudemacs.md)
