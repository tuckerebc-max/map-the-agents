# postal (`postal`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: andrefetch
- License: GPL-3.0
- Language: Python
- Interface: platforms=CLI; install=pip install postalcli
- Model providers: OpenRouter (Claude, OpenAI, Deepseek, Kimi, free smaller models)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [andrefetch/postal](../../repos/andrefetch/postal.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Bring-any-model via OpenRouter; six graduated approval policies with dangerous-command rejection; context pruning + history compaction for long sessions; per-turn session checkpointing with /rewind; readable object-oriented Python codebase; modular component-based Rich TUI

(captured site page body (agents/postal.md), not a verified repo-code finding)
Postal targets developers who want a terminal coding agent with fine-grained control over autonomy rather than an all-or-nothing auto mode. Its loop runs plan, read, edit, and bash tools with every mutating action passing one of six approval policies, switched mid-session with /approval, while dangerous commands are rejected outright regardless of policy. Sessions are checkpointed after every turn, so /rewind can roll conversation state back to any point, and long sessions survive through context pruning plus automatic compaction into a continuation brief when the window fills. Five subagents handle investigation, review, architecture, test writing, and debugging, each subject to the same approval gates. It runs on OpenRouter alone, so users pay their own API costs, and it picks up AGENTS.md per project automatically.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/postal.md)
