# hitch (`hitch`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: maxktz
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=npm install -g hitch-cli then run hitch (first-run wizard sets up SKILL.md)
- Model providers: none
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [maxktz/hitch](../../repos/maxktz/hitch.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight CLI tool that lets AI coding agents share, inspect, and control your real, running terminal. A shell proxy (not a tmux-like multiplexer) that lets agents observe and interact with terminals you already have running. Proxies I/O, records context, and exposes agent-friendly commands (hitch/unhitch). Integrates with skills.sh via SKILL.md. Supports macOS and Linux on arm64/x64.

(captured site page body (agents/hitch.md), not a verified repo-code finding)
hitch addresses the gap between a coding agent and the terminal session the developer is actually working in. Running hitch wraps the current shell as a transparent proxy: the human keeps typing normally while the proxy records useful context and exposes commands that let an agent send input, read output, and observe what is happening in the same session. This removes common frictions — an agent can check whether a dev server is already running, read the output of a long-running process, or interact with a running process without the user copy-pasting logs. The agent-facing contract ships as a SKILL.md installed on first run, so any skills-aware agent discovers how to use it without bespoke integration. The tool stays out of the way on the human side: unhitch restores an ordinary shell.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hitch.md)
