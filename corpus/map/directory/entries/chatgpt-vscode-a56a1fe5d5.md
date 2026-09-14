# chatgpt-vscode (`chatgpt-vscode`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ai-genie
- License: ISC
- Language: TypeScript
- Interface: platforms=IDE; install=vscode
- Model providers: OpenAI, Azure OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ai-genie/chatgpt-vscode](../../repos/ai-genie/chatgpt-vscode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): VS Code-native ChatGPT integration with conversation history stored on disk, quick-fix for compile-time errors in Problems window, inline diff view of AI suggestions, Azure OpenAI support, git commit message generation, streaming responses with stop capability, export of conversations to Markdown.

(captured site page body (agents/chatgpt-vscode.md), not a verified repo-code finding)
chatgpt-vscode (marketed as Genie) embedded OpenAI's models into Visual Studio Code via the user's own API key, arriving in early 2023 when editor integrations were still novel. Its feature set centered on the chat-and-suggest workflow of that era: sidebar conversations with history persisted to disk and exportable to Markdown, quick-fix prompts wired into the Problems window for compile-time errors, inline diffs of suggested changes, context-menu actions for generating tests or explanations, and automatic git commit message drafting. It supported Azure OpenAI deployments alongside standard OpenAI keys and included conveniences like stopping streamed responses to conserve tokens. The extension accumulated 1,274 stars and a marketplace following, but development effectively stopped after 2024, with the last release in September 2024 and a large backlog of unresolved issues; it has been overtaken by agentic assistants and now functions mainly as a legacy BYOK chat integration.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/chatgpt-vscode.md)
