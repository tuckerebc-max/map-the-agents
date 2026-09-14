# Grok Build (`grok-build`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: xai-org
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://x.ai/cli/install.sh | bash (macOS/Linux), irm https://x.ai/cli/install.ps1 | iex (Windows), or cargo build from source
- Model providers: xAI/Grok models (implied)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [xai-org/grok-build](../../repos/xai-org/grok-build.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): SpaceXAI's terminal-based AI coding agent running as a full-screen TUI. Understands codebases, edits files, executes shell commands, searches the web, and manages long-running tasks. Can run interactively, headlessly for scripting/CI, or embedded in editors via Agent Client Protocol (ACP). Source synced periodically from the SpaceXAI monorepo.

(captured site page body (agents/grok-build.md), not a verified repo-code finding)
Grok Build is xAI's official coding agent, distributed as the grok binary and maintained as a periodically synced public mirror of the company's internal monorepo. It presents a full-screen, mouse-interactive terminal UI that reads the codebase, edits files, executes shell commands, performs web searches, and manages long-running tasks, with checkpoints and workspace awareness for safety. The same binary runs interactively, headlessly over stdio for scripts and CI, or embedded in editors through the Agent Client Protocol. The user guide documents MCP servers, plugins, hooks, skills, slash commands, and sandboxing, while authentication is by browser login to an xAI account with no third-party provider support. External contributions are not accepted, and the repository records the internal source revision it was built from.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/grok-build.md)
