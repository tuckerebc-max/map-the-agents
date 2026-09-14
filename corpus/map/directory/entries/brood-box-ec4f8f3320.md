# brood-box (`brood-box`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: stacklok
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI, IDE; install=Download pre-built binary from GitHub Releases, or build from source with task build
- Model providers: Anthropic (Claude Code), OpenAI (Codex), OpenCode, Hermes, Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [stacklok/brood-box](../../repos/stacklok/brood-box.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runs coding agents inside hardware-isolated microVMs (KVM/Hypervisor.framework via libkrun), not just containers; copy-on-write workspace snapshots with interactive per-file diff review; DNS-aware egress firewall; ephemeral per-session SSH keys; zero persistent state.

(captured site page body (agents/brood-box.md), not a verified repo-code finding)
brood-box exists because letting a coding agent run arbitrary commands on a developer machine is a trust problem that containers only partially solve. Stacklok's Go CLI boots a lightweight virtual machine via libkrun (KVM on Linux, Hypervisor.framework on macOS), snapshots the workspace copy-on-write, and launches the chosen agent — Claude Code, Codex, OpenCode, Hermes, or Gemini CLI — inside it over an ephemeral SSH session. An egress firewall restricts network access to LLM providers and package registries by profile, with a locked mode allowing only the LLM endpoint; ToolHive MCP servers are auto-discovered and proxied into the VM. When the agent exits, the tool computes a diff and the user reviews each file before changes are flushed back, with hash re-verification guarding against tampering. Stacklok positions it as experimental infrastructure for teams that want hardware isolation, DNS-aware egress control, and zero persistent state around agents they run daily.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/brood-box.md)
