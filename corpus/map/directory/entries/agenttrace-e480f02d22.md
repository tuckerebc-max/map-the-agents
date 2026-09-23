# agenttrace (`agenttrace`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: luoyuctl
- License: MIT
- Language: Rust
- Interface: platforms=CLI, IDE; install=brew install luoyuctl/tap/agenttrace; or npm install -g @zack78/agenttrace; or winget install --id Luoyuctl.AgentTrace; or cargo install --git https://github.com/luoyuctl/agenttrace agenttrace
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [luoyuctl/agenttrace](../../repos/luoyuctl/agenttrace.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first terminal TUI and report generator for AI coding-agent session history; reads logs from Claude Code, Codex CLI, Gemini CLI, Qwen Code, Cline, Aider, Cursor, and more; provides cost, token, and time analysis with baseline comparison; MCP governance inspection; all processing local

(captured site page body (agents/agenttrace.md), not a verified repo-code finding)
After a week of agent work, developers have no easy answer to basic questions: what did the runs cost, which sessions hung, why was that task slow. AgentTrace parses local logs from Claude Code, Codex CLI, Gemini CLI, Qwen Code, Cline, Aider, Cursor exports, OpenCode, OpenClaw, Kimi CLI, and generic JSONL traces, then produces spend breakdowns by agent and model, slow-task diagnosis (retry loops, hanging sessions, context pressure), and governance reports with Git delivery correlation. Reports export as JSON, Markdown, or self-contained HTML and can be compared against a local baseline to catch regressions. Reports label their own data completeness as Detailed, Aggregate, or Limited rather than overstating coverage. It is distributed as a Rust binary via brew, npm, winget, and cargo.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agenttrace.md)
