# AgentsMesh (`agentsmesh`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: AgentsMesh
- License: BSL-1.1
- Language: Go
- Interface: platforms=CLI, IDE; install=binary
- Model providers: Anthropic, OpenAI, Google, BYOK, local
- Feature flags (directory-reported):
  - mcp_support: partial (.mcp.json and mcp-e2e tests present in repo; not detailed in README) (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [agentsmesh/agentsmesh](../../repos/agentsmesh/agentsmesh.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI agent workforce platform that runs a hundred self-hosted coding agents across your own machines with workspace isolation (git worktree pods), autopilot self-healing, mesh channels, and a single console (web/desktop/iOS).

(captured site page body (agents/agentsmesh.md), not a verified repo-code finding)
One operator can meaningfully supervise only a couple of coding agents before workspace collisions, stalled runs, and credential management take over. AgentsMesh addresses this with AgentPods — isolated execution environments pairing a PTY terminal with a dedicated git worktree and private credentials — scheduled across self-hosted runner daemons so code never leaves the operator's infrastructure. An autopilot control agent watches each pod, sends the next instruction on idle with iteration caps, and hands control back to a human on request, while mesh channels and tickets bind pods into a collaborating, human-visible topology. The stack splits an orchestration control plane (gRPC/mTLS) from a stateless terminal relay, with a shared Rust core powering web, Electron desktop, and SwiftUI iOS clients. Supported agents include Claude Code, Codex CLI, Gemini CLI, Aider, and OpenCode on a BYOK basis, licensed as BSL-1.1 with production use requiring a commercial license until the 2030 conversion to GPL.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentsmesh.md)
