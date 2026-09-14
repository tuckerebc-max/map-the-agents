# Grinta (`grinta`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: josephsenior
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, CLI, IDE; install=pipx install grinta (optional extras: grinta\[rag\], grinta\[all\])
- Model providers: OpenAI, Anthropic, Google, OpenRouter, Ollama, LM Studio
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [josephsenior/grinta-coding-agent](../../repos/josephsenior/grinta-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first autonomous coding agent (v1.0.0) that plans, edits, runs commands, debugs failures, validates results, and continues until software tasks are finished end-to-end. Local-first: control plane, execution, session history, and checkpoints all stay local. Failure recovery via durable event ledger, checkpoints, and reverts. Demonstrated a 4h 33m autonomous run (16,393 events, 373 tool outcomes) reaching FINISHED with no additional user messages. ...

(captured site page body (agents/grinta.md), not a verified repo-code finding)
Grinta is a local-first coding agent that plans, edits files, runs commands, debugs failures, and validates its work until a task completes. Its control plane, session history, and checkpoints stay on the local machine while inference can point at hosted models (OpenAI, Anthropic, Google, OpenRouter) or local ones (Ollama, LM Studio). The architecture emphasizes surviving long runs: a durable event ledger records every step, checkpoints allow reverts, and completion quality gates reduce premature declarations of success, with recovery paths for provider outages, malformed tool calls, and context-window pressure. It integrates real LSP servers and DAP debuggers rather than inferring program state from text, and offers Chat, Plan, and Agent workflows in a terminal UI. The audience is developers who want autonomous execution without a cloud account, with optional policy gates and secret masking for safety.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/grinta.md)
