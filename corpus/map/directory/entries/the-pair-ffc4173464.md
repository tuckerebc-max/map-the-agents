# the-pair (`the-pair`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: timwuhaotian
- License: Apache-2.0
- Language: TypeScript, Rust
- Interface: platforms=Desktop; install=Download from GitHub Releases (.zip macOS / .exe Windows / .AppImage Linux); or build from source: git clone, npm install, npm run build:mac|win|linux (requires Node.js 22.22+ and Rust)
- Model providers: opencode, Anthropic (Claude Code), OpenAI (Codex), Google (Gemini/Antigravity), Kimi, Ollama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [timwuhaotian/the-pair](../../repos/timwuhaotian/the-pair.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Dual-agent cross-validation desktop app where a read-only Mentor agent plans and reviews everything a separate Executor agent produces, catching AI hallucinations before they reach the codebase. Model-agnostic: mix and match any providers (e.g., Claude as Mentor + Codex as Executor).

(captured site page body (agents/the-pair.md), not a verified repo-code finding)
The Pair addresses a specific failure mode of single-agent coding tools: one model that both writes code and reviews it will often approve its own hallucinations. Its desktop app (Tauri 2, Rust + React) runs two roles on every task — a Mentor agent with read-only access that plans and reviews, and an Executor agent that writes code and runs commands — looping through mentoring, execution, and review cycles until work completes or a flat 20-iteration default triggers a pause for human inspection. Because the roles are CLI-backed, any combination of opencode, Claude Code, Codex, Gemini/Antigravity, Kimi, or local Ollama models can be assigned per role, letting users cross-validate with different model families; quality gates, stall detection, per-agent resource monitoring, and git-diff tracking round out the harness. It is free Apache-2.0 software for macOS, Windows, and Linux, with a pair-code CLI for terminal use, and users pay only their own provider costs. Developers burned by hallucinated single-agent edits are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/the-pair.md)
