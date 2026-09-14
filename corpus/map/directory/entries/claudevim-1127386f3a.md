# claude.vim (`claudevim`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: pasky
- License: MIT
- Language: Vim script
- Interface: install=git clone into Vim/Neovim pack directory
- Model providers: Anthropic, AWS Bedrock
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [pasky/claude.vim](../../repos/pasky/claude.vim.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Deep Claude integration into the Vim/Neovim workflow — chat with full visibility of open buffers, vimdiff code review, tool use (open files, run vim/shell commands, evaluate Python, web search). Acts as a terminal-based replacement for Claude.ai/ChatGPT.

(captured site page body (agents/claudevim.md), not a verified repo-code finding)
claude.vim was an early (2024) demonstration of editor-native agent tool use before IDE integrations matured: rather than code completion, it offers chat where the model sees every open buffer and can act - opening files, running commands, evaluating Python - with each action individually consented. Changes arrive as vimdiff review rather than silent rewrites, and chat history is editable, letting users redact expensive context. About 95% of the plugin's own code was written by Claude through the plugin itself. Development has been intermittent, with the last commit in May 2025 updating defaults to Sonnet 4; it remains MIT-licensed and installable from source.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claudevim.md)
