# Zoo-Code (`zoo-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Zoo-Code-Org
- License: Apache-2.0
- Language: TypeScript (VS Code extension)
- Interface: platforms=IDE; install=vscode
- Model providers: Claude, GPT, Gemini, Kimi, GLM, Grok, MiniMax, DeepSeek, Qwen, Azure OpenAI, Zoo Gateway, Moonshot, NanoGPT, Friendli, Kenari, OpenCode Go
- Feature flags (directory-reported):
  - mcp_support: yes - per-mode MCP restrictions (yes)
  - plugin_support: yes - VS Code extension marketplace (yes)
  - claude_code_plugin: no - standalone VS Code extension (no)
  - subagents: yes - orchestrator workflows with parent/child task coordination, parallel subtasks (yes)
  - hooks: no (no)
  - plan_mode: yes - Architect Mode (yes)

Repository map entry: [zoo-code-org/zoo-code](../../repos/zoo-code-org/zoo-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Community-driven continuation of Roo Code after the original Roo team moved to Roomote. AI-powered VS Code extension providing a team of AI agents in-editor, with Semble codebase intelligence (on-demand semantic code search), Destructive Command Guard (DCG) for longer autonomous runs, multiple modes (Code, Architect, Ask, Debug, custom), and very broad model provider support.

(captured site page body (agents/zoo-code.md), not a verified repo-code finding)
Zoo Code exists because Roo Code, one of the most widely used open-source AI coding extensions, stopped receiving active maintenance when its core team shifted to a product called Roomote. Rather than let the codebase stagnate, contributors who had worked on Roo forked it and continued development, publishing a Roo-to-Zoo migration guide so existing users could move over with their settings and workflows intact — which is why the repository carries over 7,500 commits of inherited history. The extension retains Roo's mode system: Code mode for edits, Architect mode for planning and spec work before implementation, Ask and Debug modes, and user-defined custom modes that constrain the agent's behavior per context. Because the lineage traces back through Cline, the tooling includes MCP server integration with per-mode restrictions, an orchestrator mode that delegates parent and child tasks across parallel subtasks, and explicit approval gates before consequential actions. The fork's distinctive additions target autonomous operation: a Destructive Command Guard blocks dangerous shell commands during long unattended runs, and Semble adds on-demand semantic code search without a separate indexing pass. Provider coverage is broad — Claude, GPT, Gemini, Kimi, GLM, Grok, MiniMax, DeepSeek, Qwen, and multiple gateways — and the project publishes docs at docs.zoocode.dev under Apache-2.0. Teams ...
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zoo-code.md)
