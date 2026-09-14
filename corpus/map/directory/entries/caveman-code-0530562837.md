# caveman-code (`caveman-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: JuliusBrussee
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Anthropic, OpenAI, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, DeepSeek, Google Gemini, GitHub Copilot, Claude Pro/Max, ChatGPT Plus/Pro, and more (20+)
- Feature flags (directory-reported):
  - mcp_support: yes — full, Claude Code-compatible superset; transports: stdio, Streamable HTTP, in-process; OAuth 2.1 + PKCE (yes)
  - plugin_support: yes — plugin marketplace via caveman plugin command (yes)
  - claude_code_plugin: no (no)
  - subagents: yes — up to 7 parallel, worktree-isolated subagents; 5 ship by default; triggered via Task tool (yes)
  - hooks: yes — identical to Claude Code hooks; run as observers, never block (yes)
  - plan_mode: yes — /plan toggles read-only mode (model restricted to read/grep/find/ls); /act executes the saved plan (yes)

Repository map entry: [juliusbrussee/caveman-code](../../repos/juliusbrussee/caveman-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 4-layer token compression always on (Caveman Mode, Tool Budgets, Read Dedup, RTK); ~2x fewer tokens than Codex CLI on identical tasks; Claude Code-compatible superset — paste existing settings/commands/skills/agents/.mcp.json configs and they work.

(captured site page body (agents/caveman-code.md), not a verified repo-code finding)
caveman-code is a terminal coding agent forked from Mario Zechner's pi, modified so that every layer of the interaction pipeline compresses tokens: the model's own replies are constrained into terse 'caveman grammar', tool outputs are truncated to per-tool budgets, repeated file reads return deduplicated stubs, and an optional Rust companion binary further compresses bash output. The agent remains fully compatible with the Claude Code ecosystem — settings.json, hooks, commands, skills, subagents, and .mcp.json are read directly — so users can switch agents without reconfiguring their setup. Benchmark results published in the repository report roughly 2x token reduction against Codex CLI on identical tasks. Subagents run worktree-isolated in parallel, and a read-only plan mode gates model actions until an explicit /act. Development has paused as of August 2026; the maintainer recommends the newer caveman wrapper for ongoing use, though caveman-code remains installable via npm and functions as documented.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/caveman-code.md)
