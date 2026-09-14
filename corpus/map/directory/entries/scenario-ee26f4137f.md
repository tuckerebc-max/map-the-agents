# scenario (`scenario`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: langwatch
- License: Apache-2.0
- Language: Python, TypeScript
- Interface: install=pip
- Model providers: OpenAI, LiteLLM, Vercel AI SDK, ElevenLabs, Gemini
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [langwatch/scenario](../../repos/langwatch/scenario.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Simulation-based agent testing framework that tests real agent behavior by simulating users in different scenarios; first-class voice agent support, built-in red teaming with crescendo escalation, cross-language (Python/TypeScript).

(captured site page body (agents/scenario.md), not a verified repo-code finding)
Agent failures are conversational and stateful — a chatbot that handles turn three wrong, a voice agent that crumbles under background noise — which example-based unit tests miss; Scenario addresses that by simulating users and judging real transcripts. The SDK exposes a script DSL where engineers hardcode or generate messages, assert on tool calls and state, and mix in external evals, with a debug mode that steps through conversations in slow motion. It integrates with pytest and vitest for CI, caches runs for repeatability, and works framework-agnostic against any agent exposing a single call method. Python, TypeScript, and Go SDKs ship under Apache-2.0, with LangWatch visualization optional. It is used by teams building conversational and voice agents who need regression confidence beyond static benchmarks.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/scenario.md)
