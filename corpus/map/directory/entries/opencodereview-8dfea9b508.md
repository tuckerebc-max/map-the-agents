# OpenCodeReview (`opencodereview`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: alibaba
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI; install=npm
- Model providers: OpenAI, Anthropic, BYOK (custom endpoints)
- Feature flags (directory-reported):
  - mcp_support: yes (transport not documented; MCP server at open-codereview.ai/docs/mcp) (yes)
  - plugin_support: yes (plugins for Claude Code, Codex, Cursor, OpenCode, VSCode extension) (yes)
  - claude_code_plugin: yes (review slash commands plugin) (yes)
  - subagents: yes (smart file bundling, each bundle runs as a sub-agent with isolated context) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [alibaba/open-code-review](../../repos/alibaba/open-code-review.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Hybrid architecture code review tool combining deterministic engineering pipelines with an LLM agent, achieving higher precision than general-purpose agents while using ~1/9 of the tokens. Battle-tested at Alibaba scale, serving tens of thousands of developers.

(captured site page body (agents/opencodereview.md), not a verified repo-code finding)
Running a general-purpose coding agent over every pull request is expensive and imprecise, which is why Alibaba built OpenCodeReview: two years of internal use across tens of thousands of developers shaped a design it calls Deterministic Engineering x Agent Hybrid. Deterministic stages select files, bundle them intelligently (i18n properties grouped, each bundle an isolated sub-agent), match template rules, and position comments precisely; a scenario-tuned LLM agent with a distilled toolset reads full files, searches the codebase, and makes the judgment calls. The ocr CLI reads Git diffs or scans whole trees, and a Delegation Mode lets an existing agent (Claude Code, Codex, Cursor, OpenCode) run the review with its own model — no separate API key. Distribution covers npm, install scripts, release binaries, CI integrations (GitHub Actions, GitLab, Gerrit), a VS Code extension, MCP server, and per-harness plugins. Alibaba publishes AACR-Bench alongside, claiming higher precision at roughly one-ninth the token cost of general-purpose agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencodereview.md)
