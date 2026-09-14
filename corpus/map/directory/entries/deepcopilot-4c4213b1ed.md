# DeepCopilot (`deepcopilot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: deep-copilot
- License: MIT
- Language: JavaScript
- Interface: platforms=IDE; install=VS Code Marketplace (search 'Deep Copilot'); from VSIX: code --install-extension deep-copilot-0.41.6.vsix; from source: npm install && npm run build && npm run package
- Model providers: DeepSeek
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [deep-copilot/deepcopilot](../../repos/deep-copilot/deepcopilot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): VS Code extension providing a conversational AI coding assistant powered by the DeepSeek API with an agentic loop, multi-turn tool calling, and streaming output in the sidebar. Features file tools (read/write/str-replace/apply_patch/list/find/grep), shell execution, web search via Tavily, plan & todos panel, revert last turn, post-tool hooks (.deepcopilot/hooks.json), post-edit LSP diagnostics, parallel sessions, MCP client (mcp__\<server\>__\<tool\>), skills system (compatible with ~/.claude/skills, ...

(captured site page body (agents/deepcopilot.md), not a verified repo-code finding)
DeepCopilot puts a DeepSeek-powered coding agent into VS Code's sidebar: a multi-turn tool-calling loop handles file reads/writes, ripgrep-backed code search, shell execution, and optional Tavily web search, with streaming output and context-window management to stay inside long sessions. The extension deliberately avoids npm runtime dependencies, shipping a small bundle built on the VS Code Extension API, which keeps install weight and supply-chain surface minimal. Around the loop it adds plan/todo tracking, a pending-edits panel with diff review and one-click revert, persistent user memory, a skills system, and FIM inline completions. It requires a DeepSeek API key (Tavily optional), is MIT-licensed JavaScript by a solo author, and releases frequently on the VS Code Marketplace.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepcopilot.md)
