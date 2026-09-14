# Mistral Vibe (`mistral-vibe`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: mistralai
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI; install=curl -LsSf https://mistral.ai/vibe/install.sh | bash
- Model providers: Mistral (default); Mistral-compatible domains/deployments
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [mistralai/mistral-vibe](../../repos/mistralai/mistral-vibe.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Mistral's official open-source CLI agent with subagents, hooks (pre_tool/post_tool/post_agent), Skills system following Agent Skills specification, voice mode, git worktree integration, multimodal image support, OpenTelemetry tracing, Agent Client Protocol (ACP) for IDE integration, and programmatic mode with cost/token/turn budgets.

(captured site page body (agents/mistral-vibe.md), not a verified repo-code finding)
Mistral Vibe gives the Mistral ecosystem a first-party terminal agent comparable to Claude Code: the model plans with a todo list, edits and patches files, runs shell commands, and searches with ripgrep under per-profile permission approval, with compaction managing context across long sessions. Delegation runs through a task tool whose subagents work independently — including a read-only explore agent for codebase reconnaissance — and custom subagents are defined as agent-type config files that inherit the parent's hooks. Hooks themselves are shell commands wired at pre_tool, post_tool, and post_agent points, able to deny or fully rewrite tool inputs and outputs. Skills follow the agentskills.io specification, adding tools and user-invocable slash commands from SKILL.md directories, and MCP servers attach over stdio or streamable HTTP with static or OAuth auth. Programmatic mode caps cost, tokens, and turns for scripted CI use, and Agent Client Protocol integration reaches Zed and VS Code. Developers use it interactively in the terminal and teams run it headless in CI against Mistral models.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mistral-vibe.md)
