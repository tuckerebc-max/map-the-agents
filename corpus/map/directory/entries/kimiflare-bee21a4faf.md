# kimiflare (`kimiflare`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: sinameraji
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Web; install=npm install -g kimiflare (or npx kimiflare)
- Model providers: Cloudflare Workers AI (Kimi K2.7/K2.6/K2.5, GLM-5.2, Kimi K3); any OpenAI-compatible endpoint via KIMIFLARE_BASE_URL
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [sinameraji/kimiflare](../../repos/sinameraji/kimiflare.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal coding agent running entirely on your own Cloudflare account via Workers AI; 262k context window, AI Gateway-confirmed cost tracking, local SQLite+embeddings memory, image understanding, OS-aware shell (Windows support), headless SDK + RPC mode; 5 hook events (PreToolUse, PostToolUse, UserPromptSubmit, Stop, PreCompact).

(captured site page body (agents/kimiflare.md), not a verified repo-code finding)
Kimiflare addresses token-cost opacity by running inference on the user's own Cloudflare Workers AI account and routing traffic through Cloudflare AI Gateway, which returns authoritative per-turn costs, cache-hit ratios, and per-feature breakdowns instead of estimates. The agent ships 262k-context models, image understanding, MCP tool extension, LSP integration, local SQLite memory, and veto-capable hooks at five lifecycle points managed through a /hooks catalog. Modes cycle between plan (read-only research), edit (approval per mutation), and auto. Individual developers and small teams use it to keep coding-agent spend inside a Cloudflare bill they already control.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/kimiflare.md)
