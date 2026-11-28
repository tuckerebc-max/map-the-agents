# bough (`bough`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: andreylukin
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI, Web; install=curl -fsSL https://raw.githubusercontent.com/andreylukin/bough/main/install.sh | sh (macOS and Linux, x86-64 and arm64); or brew tap andreylukin/bough https://github.com/andreylukin/bough && brew install bough; or go build ./cmd/bough (Go 1.27+)
- Model providers: Anthropic, OpenAI, OpenRouter, or Cerebras (your own API keys)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [andreylukin/bough](../../repos/andreylukin/bough.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): The model acts by writing one JavaScript program per step — patch, bash, spawn, and every MCP tool are ordinary functions inside it — so a patch and its test run can be one step that branches on results in code instead of one tool call per round trip.

(captured site page body (agents/bough.md), not a verified repo-code finding)
bough is the terminal coding agent its author built to replace Claude Code at work, and its difference is architectural: instead of exposing a list of tools and looping once per call, bough exposes one program runner — the model writes a \`\`\`js block that calls tools.view, tools.patch, tools.bash, tools.spawn and any MCP tool as ordinary functions, and what it prints goes back to the model. From the author's own sessions, 52% of programs made more than one tool call and 30% branched or looped on results, work that would otherwise cost a round trip per call. Everything is a plugin — the provider, the loop, the tools, the UI, MCP, hooks and skills are rows in a YAML file that can be swapped or re-mounted mid-session — and sessions are append-only JSONL under ~/.bough/history, so resume, search, and switching models mid-conversation work. A bough session started in a git checkout can write only there; a --project session runs every shell command inside a Linux container (Apple container on macOS, rootless podman on Linux) against git worktrees with per-turn checkpoints and /undo, for work that needs an enforced boundary. The author positions it beside Claude Code, opencode and pi — borrowing their conventions (AGENTS.md, skills, hooks, MCP, subagents) — and it ships a one-person project in daily use with named gaps: no Windows build, no per-turn ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/bough.md)
