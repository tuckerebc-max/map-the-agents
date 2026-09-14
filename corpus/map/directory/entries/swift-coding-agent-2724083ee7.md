# swift-coding-agent (`swift-coding-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ivan-magda
- License: MIT
- Language: Swift
- Interface: install=git clone, cp .env.example .env (set ANTHROPIC_API_KEY and MODEL_ID), swift build, swift run agent
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [ivan-magda/swift-coding-agent](../../repos/ivan-magda/swift-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Swift reimplementation of a Claude Code-style coding agent CLI built stage-by-stage to explore coding-agent architecture. Philosophy: coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers. The agent loop is fixed and minimal (~15 lines); each roadmap stage isolates one mechanism (subagents, context compaction, task DAGs, background tasks). Built with ...

(captured site page body (agents/swift-coding-agent.md), not a verified repo-code finding)
The project's premise is that the way to understand coding agents is to build one, so Ivan Magda rebuilt a Claude Code-style CLI in Swift as a staged series published on ivanmagda.dev. The code keeps the agent loop fixed — send messages, execute tool calls when the model requests them, repeat — and adds capability in isolated stages: file tools with path safety, todo tracking with reminder injection, recursive subagents with fresh context, markdown skill files, three-layer context compaction, a file-based task DAG, and actor-based background tasks under Swift 6.2 strict concurrency. It talks directly to Anthropic's Messages API over SSE rather than using an SDK, runs on macOS and Linux, and deliberately omits conveniences a production tool would need. The audience is engineers studying agent architecture, particularly those who want a compiled-language reference implementation.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swift-coding-agent.md)
