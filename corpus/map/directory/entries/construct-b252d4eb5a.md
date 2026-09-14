# construct (`construct`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: construct-worlds
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/construct-worlds/construct/main/install.sh | sh (or cargo build --workspace from source)
- Model providers: OpenAI, Anthropic, Google Gemini, xAI Grok, Ollama, ChatGPT (Codex OAuth), Claude (Claude Code CLI)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [construct-worlds/construct](../../repos/construct-worlds/construct.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native agentic development environment (ADE) — 'tmux for agent fleets.' Manages multiple AI coding agent sessions (Codex, Claude Code, OpenCode, Antigravity, Grok, Muse, Prime Agent, smith) from the terminal. Sessions persist in a daemon (survives SSH drops/sleep). Features session branching/forking (Lineage), executable Markdown Playbooks, agent-to-agent orchestration, generative widgets, remote phone/browser control, and an extensible JSON-RPC harness protocol. Single Rust binary.

(captured site page body (agents/construct.md), not a verified repo-code finding)
Agent CLI sessions die when SSH connections drop or laptops sleep, and running several agents in parallel means juggling terminal windows with no shared history. Construct runs a background daemon that owns every agent session - Codex, Claude Code, OpenCode, Antigravity, Grok, and others - persisting state and serving a terminal UI that reattaches with full scrollback after disconnection. Sessions form a lineage tree: users fork a session, even across different harnesses, to try approaches in parallel and merge the results back. Collaborative Markdown playbooks, agent-generated UI widgets, MCP-based agent-to-agent task handoff, and an ACP server round out the environment, while the wrapped agent CLIs remain separately installed and authenticated. Platform engineers juggling multiple agent sessions across local and remote environments are the target users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/construct.md)
