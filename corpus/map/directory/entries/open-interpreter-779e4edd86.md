# Open Interpreter (`open-interpreter`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
Cheap and open-weight models underperform in agent harnesses tuned for frontier models, and the gap is often the harness rather than the model. Open Interpreter, a Rust rewrite of OpenAI's Codex with
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
