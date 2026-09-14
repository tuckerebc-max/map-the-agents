# invincat (`invincat`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: dog-qiuqiu
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=pip install invincat-cli (Python 3.11+); or clone + pip install -e .
- Model providers: OpenAI, Anthropic, Google, DeepSeek, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [dog-qiuqiu/invincat](../../repos/dog-qiuqiu/invincat.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native AI coding assistant with hierarchical memory (user + project scopes, background memory agent), goal mode for long-running objectives, 4 built-in subagents (explorer, worker, researcher, document-worker), skills system (docx/pdf/pptx/xlsx), WeCom bot daemon for remote turns, scheduled tasks in natural language.

(captured site page body (agents/invincat.md), not a verified repo-code finding)
invincat targets developers who want an agent that remembers and persists rather than restarting each session. Memory splits into user and project scopes, with a background agent distilling learnings after non-trivial turns and an optional dedicated memory model. Plan mode produces a read-only, approval-gated checklist before implementation; goal mode keeps the agent driving toward long-running objectives across turns, with state persisted per thread. Four built-in subagents split exploration, implementation, research, and office-document work, and a WeCom bridge lets enterprise-WeChat messages drive sessions remotely. Scheduled tasks accept natural-language timing, and skills handle PDF, DOCX, PPTX, and XLSX work.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/invincat.md)
