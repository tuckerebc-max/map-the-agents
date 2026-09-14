# OneCLI (`onecli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: onecli
- License: Apache-2.0 (with enterprise features under the OneCLI Enterprise License)
- Language: TypeScript
- Interface: platforms=Autonomous, CLI, Web; install=Self-host via Node/pnpm monorepo with Docker and PostgreSQL, or use the cloud at onecli.sh (free tier: $5 AI credits, 500 calls/month)
- Model providers: configurable (gateway-mediated)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [onecli/onecli](../../repos/onecli/onecli.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Sandboxed per-employee agent platform where credentials never reach the model: a Rust gateway performs MITM HTTPS to inject scoped secrets per request, backed by an AES-256-GCM secret store or on-demand Bitwarden/1Password, with policy enforced at the network level and deterministic human-in-the-loop approvals for sensitive actions. The runner is outbound-only, working on laptops, homelabs, or NAT'd VPCs.

(captured site page body (agents/onecli.md), not a verified repo-code finding)
OneCLI is an open-source, YC-backed agent platform that gives every employee a personal AI agent in a sealed sandbox, originally built as a Rust credential vault for AI agents and repivoted to team-based agent management after demand from users running autonomous agents like Hermes and OpenClaw. Agents chat via a dashboard or per-agent Slack apps and work on real tasks — triaging tickets, reconciling Stripe charges, opening PRs, revoking access — while all outbound traffic is routed through the gateway, which injects credentials on the fly so the model never sees real secrets, blocks forbidden actions, rate-limits runaway agents, and pauses sensitive actions for approval cards. The stack is a Next.js dashboard, API control plane, Rust gateway, sandbox supervisor with a vendor-neutral harness interface, and an outbound-only runner that needs no inbound ports; it is self-hostable or available as a cloud product. Free tier includes $5 in AI credits and 500 calls per month, with paid tiers beyond.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/onecli.md)
