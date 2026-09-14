# MiniAgent (`miniagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ZhuLinsen
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI; install=git clone; uv sync (or pip install -r requirements.txt; pip install -e .)
- Model providers: DeepSeek, OpenAI, Gemini, Claude, any OpenAI-compatible endpoint
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [zhulinsen/miniagent](../../repos/zhulinsen/miniagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Minimal, transparent CLI agent framework combining Claude Code-style coding with Manus-style OS control; single-file core engine (agent.py, ~1,000 lines) with no hidden abstractions. Achieves extensibility using just 6 code tools + bash; Skill system with built-in roles (coder/researcher/reviewer/tester); MCP client built-in; dual tool-calling modes (text parsing + native Function Calling); minimal dependencies (only 7).

(captured site page body (agents/miniagent.md), not a verified repo-code finding)
MiniAgent is built as an agent textbook: the entire engine — LLM interaction, tool dispatch, context compression — sits in one readable agent.py of about a thousand lines, positioned as an alternative to opaque frameworks like LangChain or pydantic-ai. Its design argument is that a small tool surface composes further than a large one: six code tools plus bash cover coding, while OS tools (browser, apps, clipboard, document creation) extend it toward Manus-style desktop control, and new tools register with a three-line decorator. Tool calling runs in two modes — transparent text parsing for learners and native function calling for reliability — with dangerous commands intercepted for confirmation. Skill objects bundle a prompt with a tool whitelist into reusable roles (coder, researcher, reviewer, tester), and an optional MCP client loads external servers' tools into the same namespace. Learners and tinkerers use it to read and modify a complete agent in one sitting rather than navigate a framework.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/miniagent.md)
