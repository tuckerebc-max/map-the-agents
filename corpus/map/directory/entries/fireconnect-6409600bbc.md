# FireConnect (`fireconnect`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: fw-ai
- License: Apache-2.0
- Language: JavaScript / Node.js (requires Node.js 18+) and Bash
- Interface: platforms=CLI, IDE; install=curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
- Model providers: Fireworks AI, Azure/Microsoft Foundry, Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [fw-ai/fireconnect](../../repos/fw-ai/fireconnect.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): CLI that configures existing AI coding tools (Claude Code, OpenCode, Codex, Pi, Cursor, VS Code, DeepSeek Harness) to route requests through Fireworks AI by natively rewriting their config files, restoring originals byte-for-byte on disconnect. Installs fireworks-websearch MCP server for Claude Code. Supports subagent model slot mapping. FireRouter feature dynamically routes requests based on complexity/cost.

(captured site page body (agents/fireconnect.md), not a verified repo-code finding)
Fireworks AI built FireConnect to remove the integration tax of pointing coding harnesses at alternative model providers: one command per harness (fireconnect claude, fireconnect codex, and so on) edits the tool's native configuration to route through Fireworks, and fireconnect off restores the original file byte-for-byte. There is deliberately no proxy or wrapper process, which keeps request paths and failure modes identical to the harness's normal operation. Beyond the core harness set (Claude Code, Codex, OpenCode, Pi, Cursor, VS Code Chat, DeepSeek Harness), it supports Azure/Foundry endpoints and FireRouter, a judge-model router for evaluation workflows. Users are Fireworks customers who want frontier-agent UX — Claude Code, Codex, Cursor — running against Fireworks' serverless model endpoints.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fireconnect.md)
