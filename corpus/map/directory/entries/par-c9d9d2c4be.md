# par (`par`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: jcz2020
- License: MIT
- Language: OCaml
- Interface: platforms=IDE; install=pip install par-runtime (Python); opam pin add par https://github.com/jcz2020/par.git (OCaml); curl installer script; or build from source (git clone + make install-dev)
- Model providers: OpenAI, Anthropic, Ollama
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [jcz2020/par](../../repos/jcz2020/par.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Modular, type-safe agent runtime for building LLM-powered applications ('LangChain + LangGraph for OCaml'). Written in OCaml 5.4 using Eio structured concurrency (no callback hell, compile-time type safety), usable from both OCaml and Python. Features type-safe shell commands (ADT-based, injection-free), structured concurrency with no orphan fibers, 23 built-in tools, and 9 middleware.

(captured site page body (agents/par.md), not a verified repo-code finding)
PAR positions itself as the agent plumbing layer that OCaml's ecosystem lacked, handling the ReAct loop, tool dispatch, multi-provider LLM calls, persistence, and an event bus so developers write only tools and workflows. Its OCaml 5.4 core uses effects and Eio structured concurrency, eliminating orphan fibers and callback nesting, and compiles shell commands into a type-safe ADT that rules out injection at compile time. Nine built-in middleware cover logging, retry, rate limiting, timeouts, argument and output validation, PII masking, and sanitization at every model and tool boundary, while SQLite persistence and an audit log make runs reproducible. Python bindings on PyPI open the runtime to the larger ecosystem, and a companion project, par-code, builds a CLI coding agent on top. Its audience is OCaml developers and Python teams that want a verified, concurrency-safe agent substrate.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/par.md)
