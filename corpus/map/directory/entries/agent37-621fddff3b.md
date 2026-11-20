# Agent 37 (`agent37`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: agent37
- License: Proprietary
- Language: unknown
- Interface: platforms=Autonomous, Web; install=Hosted service — sign up at agent37.com (dashboard); REST API with X-Agent37-Key. No install
- Model providers: Hosts coding-agent harnesses in its sandboxes — templates for Hermes, OpenClaw, Claude Code, Codex, Grok, OpenCode, Pi, or bring your own Docker image; agents bring their own providers, and managed model access or BYOK is metered separately
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): YC-backed sandbox hosting that bills agent compute by the minute at roughly a tenth of typical sandbox providers — prepaid metered vCPU/memory/disk with billing paused on auto-sleep — and runs persistent gVisor-isolated Linux sandboxes or full VMs (Docker-in-Docker, Android emulator) with an open Gateway API exposing an OpenAI Responses-compatible schema across harnesses.

(captured site page body (agents/agent37.md), not a verified repo-code finding)
Agent 37 is a YC F26 company selling cheap compute for agents: persistent Linux sandboxes (gVisor) or full VMs on Hetzner/OVH hardware, each with its own filesystem, quota, authenticated HTTPS URLs, and observability, launched from a dashboard template or the REST API. The pitch is price — the founder cites bursty CPU/RAM packing and non-hyperscaler hosts to charge under 10% of typical sandbox providers, metered per minute from a prepaid balance with compute billing stopped while a sandbox sleeps. Coding-agent harnesses are the first-class workload: one-click templates for Claude Code, Codex, OpenCode, Pi, Grok, Hermes, and OpenClaw, or any custom Docker image; a Gateway API routes model calls across harnesses behind an OpenAI Responses-compatible schema, and cron scheduling runs agents unattended. The company grew out of managed OpenClaw hosting; developers and agent-platform teams who want always-on agent machines without hyperscaler bills are the customers.
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/agent37.md)
