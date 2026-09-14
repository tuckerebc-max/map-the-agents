# Stakpak (`stakpak`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Stakpak
- License: Apache-2.0
- Language: Rust
- Interface: install=curl -sSL https://stakpak.dev/install.sh | sh
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): AI DevOps agent for infrastructure code

(captured site page body (agents/stakpak.md), not a verified repo-code finding)
Stakpak runs as a single Rust binary installed as a system service on the machines it manages, addressing the gap between hosted PaaS convenience and the lock-in that comes with it. In autopilot mode it performs health checks, renews expiring certificates and secrets, flags deprecated APIs, and hunts idle RDS and EBS resources for cost savings, surfacing only the decisions that need a human. All agent network traffic passes through a Cedar-policy proxy, secrets are substituted with placeholders before reaching the model, and full session audit logs support rollback. A single TUI handles interactive work alongside the background service. The site announced the company is joining Vercel, so teams evaluating it should account for the transition.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/stakpak.md)
