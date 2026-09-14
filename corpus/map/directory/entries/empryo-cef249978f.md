# Empryo (`empryo`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: proxysoul
- License: NOASSERTION
- Language: TypeScript
- Interface: install=binary
- Model providers: Anthropic, OpenAI, Google, Groq, DeepSeek, Bedrock, Ollama, LM Studio, OpenAI-compatible endpoints, LLM Gateway (22 providers total)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [proxysoul/empryo](../../repos/proxysoul/empryo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI coding agent that builds a live dependency graph (genome) of the repo using tree-sitter, then edits code through AST symbol-level operations rather than find-and-replace strings. 65+ atomic AST operations with rollback across 30+ languages, blast-radius analysis before edits, 5.7x fewer input tokens than competitors, time machine (git checkpoint per prompt), and free structural context compaction (no LLM call). Three ...

(captured site page body (agents/empryo.md), not a verified repo-code finding)
Empryo (successor to SoulForge) was built around the observation that string-level find-and-replace edits are the dominant failure mode of LLM coding agents. On launch it parses the repository with tree-sitter into a live graph of symbols, imports, and call sites, ranked by PageRank and git co-change frequency to estimate blast radius, and graph queries run locally at zero token cost. Edits are batches of atomic symbol-level operations with all-or-nothing rollback and a typecheck gate, and a multi-agent layer routes ten roles (brain, spark, explore, verify, and others) across 22 model providers so cheap models scout while strong models write. It ships as CLI, TUI, desktop app, and headless CLI on macOS, Linux, and Windows, with any MCP server and 576+ LSP servers attachable.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/empryo.md)
