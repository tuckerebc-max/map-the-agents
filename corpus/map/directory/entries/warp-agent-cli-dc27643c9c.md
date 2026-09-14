# Warp Agent CLI (`warp-agent-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: warpdotdev
- License: Proprietary
- Language: unknown
- Interface: platforms=CLI; install=curl -fsSL https://app.warp.dev/download/agent-cli | bash (Mac/Linux); PowerShell one-liner on Windows
- Model providers: Warp-provided models, custom model routers via YAML config, bring-your-own API keys and OpenAI-compatible endpoints
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): The Warp Agent shipped as a standalone CLI that is also a native terminal multiplexer: agent sessions run atop managed pty connections, so you can switch directories within a persistent session, run agents over SSH without installing a remote binary, and drive full-screen apps like vim and gdb. The harness delegates across subagents using different models and different harnesses, including ...

(captured site page body (agents/warp-agent-cli.md), not a verified repo-code finding)
The Warp Agent CLI (announced August 4, 2026) takes the multi-model agent built into Warp Terminal and makes it runnable in any terminal — Ghostty, iTerm 2, VS Code, or the built-in Windows and Mac terminals — with no Warp app install required. Because it is built on Warp's terminal infrastructure, each agent session sits on a managed pty connection like tmux, which enables persistent sessions across directory changes, remote execution over SSH, and interaction with full-screen programs; natural shell input means tab completions work and a classifier detects whether you typed a shell command or a prompt. The agent orchestrates subagents and can hand work off to Warp's cloud agents for monitoring and steering from the web, delegating across different models and even different harnesses including Claude Code and Codex. Inference is configurable three ways: a Warp subscription starting at $18/month including inference credits, ad-hoc credits starting at $10, or bring-your-own API keys and endpoints.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/warp-agent-cli.md)
