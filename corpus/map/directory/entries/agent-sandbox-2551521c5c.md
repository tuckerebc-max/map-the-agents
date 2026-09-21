# agent-sandbox (`agent-sandbox`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: mattolson
- License: MIT
- Language: Go
- Interface: install=curl -fsSL https://github.com/mattolson/agent-sandbox/releases/latest/download/install.sh | sh (or download binary from Releases)
- Model providers: Claude Code, Codex, Gemini, OpenCode, Pi, Factory, Copilot, Hermes (runs agents in sandbox)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mattolson/agent-sandbox](../../repos/mattolson/agent-sandbox.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Runs AI coding agents in a locked-down local sandbox with minimal filesystem access, configurable network egress via sidecar proxy (mitmproxy), proxy-side secret injection where the agent container never sees API keys/tokens, iptables firewall preventing direct outbound bypass, hot-reloadable policies, and seamless agent switching with preserved state/credentials.

(captured site page body (agents/agent-sandbox.md), not a verified repo-code finding)
Giving a coding agent your real machine hands it your credentials and your whole filesystem, which is why many teams refuse to run them locally; agent-sandbox wraps agents (Claude Code, Codex, Gemini, OpenCode, Copilot, and others) in a Debian-based container that mounts only the repo directory. A mitmproxy sidecar enforces fine-grained network policy — allowed hosts with scheme, method, path, and query rules, plus repo-scoped git access with proxy-side credential injection — while iptables blocks any outbound traffic that tries to skip the proxy. Agent state persists across runs in volumes, policies hot-reload, and VS Code or JetBrains devcontainers can attach to the sandbox. Security-conscious developers on Apple Silicon (Colima + Docker) running semi-trusted agents are the users.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agent-sandbox.md)
