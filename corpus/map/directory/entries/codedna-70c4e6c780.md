# codedna (`codedna`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Larens94
- License: MIT
- Language: Python
- Interface: install=Claude plugin (claude plugin marketplace add Larens94/codedna && claude plugin install codedna@codedna) or pipx install git+https://github.com/Larens94/codedna.git (Python 3.11+)
- Model providers: Anthropic, Google, DeepSeek, Ollama
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [larens94/codedna](../../repos/larens94/codedna.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): In-source communication protocol - AI agents embed architectural context (exports, used_by, related, rules, message) directly in code files. No external memory, retrieval pipeline, or infrastructure needed. Code carries its own context across sessions, models, and multi-agent teams.

(captured site page body (agents/codedna.md), not a verified repo-code finding)
CodeDNA proposes that the durable fix for agent context loss is to store architectural knowledge in the code itself rather than in an external memory system. Source files carry structured headers — exports, used_by reverse-dependency links, related semantic links, hard rules, and agent-to-agent messages that can be promoted to rules — and a Python CLI (codedna init/verify/impact/check/manifest) verifies that annotations stay accurate as code changes, with git hooks gating commits on stale annotations. The spec targets 12 languages, and integrations reach Claude Code (as an installable plugin), Codex, OpenCode, Aider, Cursor, Copilot, Cline, and Windsurf through instruction files. The project reports benchmark results including a 17-percentage-point navigation F1 gain on SWE-bench navigation tasks with DeepSeek and a 1.6x speedup for multi-agent teams, published alongside a Zenodo DOI for independent replication.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codedna.md)
