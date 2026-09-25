# antigravity-jules-orchestration (`antigravity-jules-orchestration`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Scarmonit
- License: MIT
- Language: JavaScript
- Interface: platforms=Autonomous; install=git clone, npm install, configure .env, npm run dev
- Model providers: Jules API, Google Antigravity, Ollama
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [scarmonit/antigravity-jules-orchestration](../../repos/scarmonit/antigravity-jules-orchestration.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Autonomous AI orchestration architecture combining Google Antigravity browser automation with the Jules API for hands-free development. 65 MCP tools across Jules Core API, Session Management, Templates, Batch Processing, Analytics, RAG, Semantic Memory, Render Integration, and Suggested Tasks. Browser Subagent for DOM capture, screenshots, and video recording. Semantic memory and batch processing.

(captured site page body (agents/antigravity-jules-orchestration.md), not a verified repo-code finding)
The project exists because Antigravity's browser automation and Jules' autonomous coding sessions don't compose natively: this Node.js MCP server (Streamable HTTP, port 3323) exposes Jules core API, session management, templates, cloning, PR integration, queueing, batch processing, analytics, and Render deployment as tool families that Antigravity can orchestrate. Supporting machinery includes AES-256-GCM encrypted credential storage, LRU caching, circuit breakers with retry/backoff, and GitHub-issue-to-Jules-session automation. It requires Node 18+, a Jules API key, and both Google products installed; deployment targets Docker or Render (live at scarmonit.com). Version 2.6.x added auto-fix and semantic-memory tools; 42 stars and an active changelog mark it as a working personal automation layer rather than a community project.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/antigravity-jules-orchestration.md)
