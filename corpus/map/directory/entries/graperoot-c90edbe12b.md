# GrapeRoot (`graperoot`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: kunal12203
- License: Apache-2.0
- Language: Python, TypeScript
- Interface: install=pip, binary
- Model providers: Claude Code, OpenAI Codex CLI, Cursor, Gemini CLI, OpenCode, GitHub Copilot, OpenClaw, Kilocode, MiMo Code, Antigravity, Kiro CLI, Command Code, MiniMax
- Feature flags (directory-reported):
  - mcp_support: yes (stdio) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [kunal12203/graperoot](../../repos/kunal12203/graperoot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source context engine that builds a semantic graph of the codebase (files, symbols, imports, call chains) and pre-loads relevant code into every prompt before the AI sees it, reducing token waste and exploration turns. Session memory compounds across a session with up to 81% cost reduction. All processing is local — no code leaves your machine. Hard-capped token budget per ...

(captured site page body (agents/graperoot.md), not a verified repo-code finding)
GrapeRoot addresses the token cost of agentic exploration: rather than letting the model discover a codebase through repeated tool calls, it builds a local semantic graph of files, symbols, imports, and call chains, then packs the highest-ranked relevant code into the prompt before each turn. The graph also tracks session memory — files read, edited, or queried — so later turns carry less and less exploratory overhead, and per-turn token budgets are enforced with configurable caps. It integrates with Claude Code, Codex CLI, Cursor, Gemini CLI, OpenCode, GitHub Copilot, and other assistants through launcher commands, plus MCP tools (graph_read, graph_retrieve, graph_neighbors) for direct drill-down. All processing stays local, and the project claims roughly 43% average cost reduction on large codebases with turn counts dropping from 11.7 to 3.5. The launchers are Apache-2.0 open source while the core PyPI engine is proprietary and free to use.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/graperoot.md)
