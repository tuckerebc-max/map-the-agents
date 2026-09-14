# codevibes (`codevibes`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: danish296
- License: MIT
- Language: TypeScript
- Interface: install=git clone + npm install (requires Node.js v18+, DeepSeek API key)
- Model providers: DeepSeek
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [danish296/codevibes](../../repos/danish296/codevibes.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Free, open-source AI code review alternative to CodeRabbit. Uses DeepSeek AI for security vulnerability detection, bug/performance analysis, and code quality review. Priority-based three-tier scanning system (P1 security → P2 core logic → P3 quality). Provides a quantifiable 0-100 Vibe Score. Real-time streaming analysis via SSE. Stores analysis history locally in SQLite.

(captured site page body (agents/codevibes.md), not a verified repo-code finding)
CodeVibes provides AI code review for developers who cannot justify a paid review service: a web dashboard where a GitHub repository URL yields security findings, bug and performance issues, and quality observations, condensed into a 0-100 score. Analysis runs on DeepSeek models (deepseek-chat or deepseek-reasoner) with a user-supplied free API key, organized as a priority pipeline — security first, then core-logic defects, then style and quality — with results streaming in real time over server-sent events. The application is a TypeScript monorepo: a React 18 and Vite frontend, an Express backend storing analysis history in SQLite via Better-SQLite3, and Octokit for GitHub access. It is a beta-stage single-author project with a dozen commits, self-described as an affordable CodeRabbit alternative.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codevibes.md)
