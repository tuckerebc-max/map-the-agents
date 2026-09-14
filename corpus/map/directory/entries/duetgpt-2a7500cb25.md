# DuetGPT (`duetgpt`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: kristoferlund
- License: MIT
- Language: TypeScript
- Interface: platforms=Autonomous; install=npm install -g duet-gpt
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [kristoferlund/duet-gpt](../../repos/kristoferlund/duet-gpt.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Semi-autonomous conversational CLI coding assistant using OpenAI function calling (no LangChain); AI proposes commands, developer approves, then auto-execution; can also serve as a general bash helper.

(captured site page body (agents/duetgpt.md), not a verified repo-code finding)
DuetGPT is a deliberately minimal take on the AI pair programmer: a conversation where the model's proposed shell commands and file edits are shown for approval and then executed verbatim, with no LangChain layer and no guardrails beyond the developer's own judgment. It ships as one npm package, asks for an OpenAI key on first run, and works equally well as a general bash helper — writing scripts, grepping trees, drafting PR descriptions from commit logs. The warning in its own README about the absence of guardrails is the design statement: approval is the only safety mechanism. It found its audience among developers experimenting with GPT-4 function calling in 2023; the repo has not been updated since June 2023.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/duetgpt.md)
