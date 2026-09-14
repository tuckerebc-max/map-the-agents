# nehemiah (`nehemiah`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: boringcomputers
- License: Apache-2.0
- Language: Go, TypeScript
- Interface: platforms=CLI, Web; install=git clone; npm install; run infra/latitude/provision.sh; set apps/web/.env; npm run dev -w web (full runbook at infra/latitude/README.md)
- Model providers: Preinstalled agents: Claude, Codex, Cursor, Pi; MCP integration with any MCP-compatible client
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: unknown (unknown)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [boringcomputers/nehemiah](../../repos/boringcomputers/nehemiah.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): On-demand Linux computers you can hand to an AI via real Firecracker microVMs that boot in milliseconds. Each machine is a full Linux desktop (VNC) or headless shell with coding agents preinstalled, driven by an AI that can browse the screen or write/run code. Real hardware-virtualized isolation (a kernel per machine, not a shared container), memory snapshot restoration in ~3ms, ...

(captured site page body (agents/nehemiah.md), not a verified repo-code finding)
Nehemiah addresses the problem that AI coding agents need isolated, disposable computers with real isolation guarantees rather than shared containers. Machines boot from signed release artifacts provisioned onto enrolled bare-metal hosts, boot in milliseconds from snapshots, and can be forked mid-run or backed by persistent S3 volumes. An agent drives each machine either through computer use over VNC or by writing and running code, with results exposed as live URLs and forwarded ports. Integration happens through an MCP server for desktop clients and an Effect-native TypeScript SDK. Deployment is deliberately not one-command: hosts are enrolled through a signed-artifact runbook on providers such as Latitude.sh, reflecting a self-host with your own keys philosophy.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nehemiah.md)
