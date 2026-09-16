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
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
