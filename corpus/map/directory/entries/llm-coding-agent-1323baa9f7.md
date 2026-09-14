# llm-coding-agent (`llm-coding-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: simonw
- License: Apache-2.0
- Language: Python
- Interface: install=pip install --pre llm-coding-agent (--pre needed while it depends on an LLM alpha release)
- Model providers: Any tool-capable model LLM knows about (OpenAI, Anthropic, etc. via the LLM ecosystem)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [simonw/llm-coding-agent](../../repos/simonw/llm-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM plugin that adds an \`llm code\` command for interactive coding-agent sessions; works with any LLM-supported model (provider-agnostic) and leverages LLM's SQLite logging, conversation resume, and plugin architecture; fine-grained approval workflows (y once, a approve similar for session, --yolo auto-approve, --allow pre-approve patterns); security by confinement - all file access sandboxed to a root directory with path-traversal protection; dual CLI ...

(captured site page body (agents/llm-coding-agent.md), not a verified repo-code finding)
The plugin exists because Willison wanted a minimal, inspectable coding agent on top of the llm CLI's model-agnostic plugin system; the first alpha was itself written by prompting Claude Code through a spec-and-TDD workflow. Read-only tools (numbered read_file, gitignore-aware list_files, ripgrep-backed search) run freely, while write_file, edit_file, and execute_command require approval, with chain_limit bounding tool rounds per run and every session recorded for resume via -c or --cid. File access is confined to the session root, with traversal via .., absolute paths, or symlinks rejected as errors the model can correct. A Python API (CodingAgent, CodingTools) exposes the same loop programmatically, with a pause/resume approval protocol for non-terminal applications.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/llm-coding-agent.md)
