# failproofai (`failproofai`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: FailproofAI
- License: MIT with Commons Clause
- Language: TypeScript, Rust
- Interface: platforms=IDE; install=npm
- Model providers: Anthropic (Claude Code), OpenAI (Codex), GitHub (Copilot), Cursor, OpenCode, Pi, Hermes, OpenClaw, Factory Droid, Devin CLI, Antigravity CLI, Goose
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [failproofai/failproofai](../../repos/failproofai/failproofai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runtime failure resolution for coding agents with zero latency, running locally. 30 built-in policies activate immediately (blocks pushes to main, force pushes, recursive deletion, API key leaks). Custom policy system with allow/deny/instruct decisions. Local dashboard for session visibility — every tool call logged. Hooks into 12+ agent CLIs (Claude Code, Codex, Cursor, etc.). MIT with Commons Clause — free for ...

(captured site page body (agents/failproofai.md), not a verified repo-code finding)
FailproofAI was built on the observation that agent harnesses ship powerful tools with permissive defaults, and teams adopt them faster than they write guardrails. It instruments harnesses through their hook systems (PreToolUse and equivalents) across a dozen agents including Claude Code, Codex, Cursor, Copilot CLI, OpenCode, and Devin CLI, plus gateways via a Python SDK for custom agents. Policies return allow, deny with a message, or instruct with guidance, so enforcement is a call-level gate rather than a prompt-level hope; every run is recorded and viewable in a local dashboard on port 8020, with an optional hosted observability tier. Custom policies are TypeScript files in .failproofai/policies/, making it straightforward for platform teams to encode their own rules without forking each harness's configuration.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/failproofai.md)
