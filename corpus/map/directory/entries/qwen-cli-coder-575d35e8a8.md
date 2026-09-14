# qwen_cli_coder (`qwen-cli-coder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: dinoanderson
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI, Web; install=Build from source: git clone, npm install, npm run build, npm run bundle, node bundle/qwen.js
- Model providers: Qwen models via Alibaba Cloud DashScope
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [dinoanderson/qwen_cli_coder](../../repos/dinoanderson/qwen_cli_coder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Community fork of Google's Gemini CLI modified to work with Qwen models from Alibaba Cloud; CLI AI workflow tool with dynamic MCP server management, multi-agent task coordination (spawn_sub_agent, delegate_task, aggregate_results; up to 5 concurrent agents), media generation (Wan models), and Assistant Mode web interface

(captured site page body (agents/qwen-cli-coder.md), not a verified repo-code finding)
qwen_cli_coder appeared within days of Google open-sourcing Gemini CLI in June 2025, adapting the codebase to run Qwen models through Alibaba Cloud's DashScope API. It preserved Gemini CLI's grounded-documentation and workflow machinery while adding dynamic MCP server management and multi-agent task coordination, including sub-agent spawning and delegation tools for splitting work across parallel agent instances. The fork documented Qwen-specific authentication and model configuration for developers who wanted Alibaba's models in a Gemini-CLI-style workflow. Active development lasted roughly a week in mid-2025; Alibaba's own Qwen Code fork, released the same month with an official team behind it, made the community fork redundant. It stands as an early example of the fork-and-retarget wave that followed Gemini CLI's open-sourcing.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qwen-cli-coder.md)
