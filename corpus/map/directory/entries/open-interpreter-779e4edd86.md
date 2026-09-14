# Open Interpreter (`open-interpreter`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: openinterpreter
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://www.openinterpreter.com/install | sh (macOS/Linux), irm https://www.openinterpreter.com/install.ps1 | iex (Windows)
- Model providers: Kimi K3, DeepSeek, Z.AI/GLM/ZCode, Qwen, Claude (via claude-code harness)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [openinterpreter/openinterpreter](../../repos/openinterpreter/openinterpreter.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fork of OpenAI's Codex optimized for low-cost models. Features harness emulation (switch between native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent harnesses via /harness), native sandboxing on all platforms, ACP agent mode, shared AGENTS.md and .agents/skills standards, and a QA skill for web/native app testing.

(captured site page body (agents/open-interpreter.md), not a verified repo-code finding)
Cheap and open-weight models underperform in agent harnesses tuned for frontier models, and the gap is often the harness rather than the model. Open Interpreter, a Rust rewrite of OpenAI's Codex with about 68,000 GitHub stars, addresses this by emulating provider-recommended harnesses: /harness switches between native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent, and minimal modes, so a cheap model runs under the prompting and tool-calling conventions it was trained against. It supports MCP, skills, hooks, permissions, and AGENTS.md, remains compatible with the Codex SDK through a one-line binary override, and speaks ACP, while a built-in QA skill drives browsers and native applications for computer-use tasks. Installation is a curl script on macOS/Linux or PowerShell on Windows, and the tool is free with BYOK model access. Developers running low-cost models who want frontier-harness behavior without paying frontier prices are its audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-interpreter.md)
