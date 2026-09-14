# claw-code-agent (`claw-code-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: HarnessLab
- License: unknown
- Language: Python
- Interface: install=git clone; pip install -e .; set OPENAI_BASE_URL/OPENAI_API_KEY/OPENAI_MODEL env vars; run python3 -m src.main
- Model providers: vLLM, Ollama, LiteLLM Proxy, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [harnesslab/claw-code-agent](../../repos/harnesslab/claw-code-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Full Python reimplementation of Claude Code's npm agent architecture with zero external dependencies (pure stdlib), designed for local open-source models (especially Qwen3-Coder via vLLM). Includes local web GUI and comprehensive runtime subsystems (tasks, plans, MCP, plugins, hooks, LSP, worktrees, workflows, teams, background sessions).

(captured site page body (agents/claw-code-agent.md), not a verified repo-code finding)
The project exists for developers who want Claude Code's workflow on local models and under their own control: the entire agent runtime is standard-library Python, so the loop is auditable without node_modules, and the documented deployment is vLLM serving Qwen3-Coder with tool-call parsing configured server-side. It reimplements CLAUDE.md discovery, slash commands, session persistence, and context compaction, then extends them with MCP support, agent delegation, and cost budgets. Permission tiers default to read-only and escalate explicitly, which suits shared machines and enterprise settings. Researchers studying agent architecture and teams with data-sovereignty constraints are the primary users; the project is in alpha with active monthly feature work.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claw-code-agent.md)
