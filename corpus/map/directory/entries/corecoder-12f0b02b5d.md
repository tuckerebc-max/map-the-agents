# CoreCoder (`corecoder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: he-yufeng
- License: MIT
- Language: Python 3.10+
- Interface: install=pip
- Model providers: OpenAI, DeepSeek, Ollama, Kimi, Qwen, 100+ via LiteLLM
- Feature flags (directory-reported):
  - mcp_support: no - explicitly listed as a missing feature to add in a fork (no)
  - plugin_support: no (no)
  - claude_code_plugin: no - standalone reimplementation inspired by Claude Code (no)
  - subagents: yes - agent tool spawns sub-agents with isolated context, one fewer tool, shorter round limit (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [he-yufeng/corecoder](../../repos/he-yufeng/corecoder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 'The nanoGPT of coding agents' - radical minimalism at ~1,081 lines across 8 core files, readable in an afternoon. A genuinely runnable teaching tool (86 tests green) that reads/writes files, runs shell, spawns sub-agents, compacts context in 3 tiers (50%/70%/90% thresholds), and reports token cost. Unique-match search/replace editing anchors on unique snippets instead of line numbers. Sub-agents constrained by tool-withholding ...

(captured site page body (agents/corecoder.md), not a verified repo-code finding)
Production coding agents bury their core loop under tens of thousands of lines, which makes it hard to learn how harnesses actually work. CoreCoder reimplements that core in about 1,100 lines of readable Python: a bounded agent loop with parallel tool execution, eight tools (bash, file read/write/edit with unique-match search-replace, glob, grep, a todo list, and a non-recursive sub-agent spawner), three-tier context compaction, streaming with retry and cost accounting, and session save/resume. It speaks any OpenAI-compatible API out of the box and reaches a hundred-plus providers through an optional LiteLLM backend. Deliberate omissions - no real sandbox, no MCP, no fallback model chain - are documented as fork entry points rather than defects. Students and harness authors read the source (aided by an eight-part bilingual essay series) and fork it as a starting point.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/corecoder.md)
