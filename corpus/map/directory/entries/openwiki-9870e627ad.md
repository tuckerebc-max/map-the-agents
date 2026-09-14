# OpenWiki (`openwiki`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: langchain-ai
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm
- Model providers: OpenAI, OpenAI (ChatGPT login), Anthropic, Gemini (AI Studio), Gemini Enterprise (Vertex AI), AWS Bedrock, GitHub Copilot, OpenRouter, Nebius, Fireworks, Baseten, NVIDIA NIM, OpenAI-compatible (LiteLLM, Ollama, LM Studio)
- Feature flags (directory-reported):
  - mcp_support: yes (custom MCP connector — point at any MCP server and pull tools into a run; transport not specified) (yes)
  - plugin_support: yes (connectors: Notion, Slack, Gmail, X, Web Search, Hacker News, git-repo, LangSmith, Custom MCP) (yes)
  - claude_code_plugin: partial (generates/maintains CLAUDE.md at repo root for coding agent integration) (reported)
  - subagents: partial (uses Deep Agents framework; explicit subagent architecture not detailed) (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [langchain-ai/openwiki](../../repos/langchain-ai/openwiki.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): CLI that uses AI agents to automatically write and maintain a Markdown wiki for your codebase or personal knowledge, keeping it current via CI on every change, with an interactive node-graph visualizer. Outputs portable Open Knowledge Format (OKF) bundles and supports 12+ model providers.

(captured site page body (agents/openwiki.md), not a verified repo-code finding)
Codebase documentation decays faster than any other artifact, and agent-driven development accelerates the rot. OpenWiki, from the LangChain team, generates and maintains a linked Markdown wiki about a repository using a Deep Agents-powered pipeline: an init run plans and writes pages, and update runs diff the codebase against 'Grounded Claims' — statements tied to versioned source evidence — so the system knows precisely which facts went stale and rewrites only those pages. Scheduled CI workflows (GitHub Actions, GitLab, Bitbucket) keep the wiki current on every merge, and an interactive node-graph visualizer browses the result. Roughly nine connectors (Notion, Slack, Gmail, X, web search) extend sources, and integrations let Codex, Claude Code, OpenCode, or Cursor query the wiki as context. Install is npm -g with Node 22+, MIT-licensed, and 13 model providers are supported. Teams whose docs must survive heavy agent-driven churn are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openwiki.md)
