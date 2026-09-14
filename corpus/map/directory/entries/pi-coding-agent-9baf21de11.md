# pi-coding-agent (`pi-coding-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: dnouri
- License: GPL-3.0-or-later
- Language: Emacs Lisp
- Interface: install=M-x package-install RET pi-coding-agent RET (from MELPA); or git clone with load-path setup
- Model providers: DeepSeek, OpenAI, Z.AI (via Pi CLI)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry (renamed): original lead [dnouri/pi-coding-agent](https://github.com/dnouri/pi-coding-agent) (source: backing, field: `source_code_url`) now resolves to [dnouri/pilish](../../repos/dnouri/pilish.md) (github id 1125438750, verified [https://github.com/dnouri/pilish](https://github.com/dnouri/pilish)).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Emacs frontend for the Pi coding agent that communicates over RPC for structured messages and tool events (instead of terminal text). Provides a Markdown-rendered chat buffer with tree-sitter highlighting, a separate editable prompt buffer, session management, fork/compact, and Evil integration — letting you use familiar Emacs editing habits for composing prompts.

(captured site page body (agents/pi-coding-agent.md), not a verified repo-code finding)
pi-coding-agent brings pi into Emacs on RPC rather than terminal emulation, so the package receives structured messages and tool events instead of scraping ANSI output — the difference between a real client and a screen-scraping wrapper. The chat buffer renders Markdown with tree-sitter highlighting, a separate prompt buffer keeps drafts editable between turns, and sessions support fork and compact operations from Emacs. Activity-phase hooks fire as sessions move between thinking, replying, running, compacting, and idle states, letting Elisp tint inputs, send notifications, or track busy sessions; Evil integration keeps modal editing intact for Vim users. Distributed on MELPA under GPL-3.0-or-later and tested in CI across Emacs 29 and 30 plus nightly builds, it targets Emacs users who want agentic coding without leaving their editor's conventions.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-coding-agent.md)
