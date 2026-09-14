# sondera-coding-agent-hooks (`sondera-coding-agent-hooks`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: sondera-ai
- License: MIT
- Language: Rust
- Interface: install=Download prebuilt archive from GitHub Releases
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [sondera-ai/sondera-coding-agent-hooks](../../repos/sondera-ai/sondera-coding-agent-hooks.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Reference monitor for AI coding agents; Rust hook binaries and Cedar policies intercept every shell command, file operation, and web request to block exfiltration, destructive behaviors, and enforce information flow control. Hook adapters for Claude Code, Cursor, Copilot, Gemini CLI, Antigravity, Codex, Hermes, OpenCode, OpenHands, VS Code.

(captured site page body (agents/sondera-coding-agent-hooks.md), not a verified repo-code finding)
The project addresses a concrete gap: coding agents execute shell commands, file writes, and web requests with limited enforcement, and most guardrails are advisory. Sondera's adapters for Claude Code, Cursor, Copilot, Gemini CLI, Codex, OpenCode, OpenHands, and others normalize agent events and forward them over local gRPC; the service evaluates Cedar policies and YARA signatures deterministically, with optional LLM classifiers for data sensitivity, and can block, escalate to an approval UI, steer via context injection, redact, or terminate. Enforcement fails closed — if the harness is unreachable, hooks deny — and no API key or external service is required. A TUI replays adjudicated trajectories for audit. It was released alongside Unprompted 2026 and Black Hat Arsenal 2026 talks for teams that need policy enforcement, not suggestions, around coding agents.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sondera-coding-agent-hooks.md)
