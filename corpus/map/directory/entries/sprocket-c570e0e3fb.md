# Sprocket (`sprocket`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: spikonado
- License: FSL-1.1-ALv2 (Functional Source License, converts to Apache-2.0)
- Language: TypeScript
- Interface: platforms=CLI, Desktop, Web; install=npx @spikonado/sprocket (also Electron desktop installers for Linux, macOS, Windows; state in $HOME/.sprocket)
- Model providers: BYOK (self-hosted setup requires model-provider API keys)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [spikonado/sprocket](../../repos/spikonado/sprocket.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Markets itself as the only AI agent for developing both hardware and software: it retrieves best-in-class context from the web, buys parts and subscriptions from any site on request, creates detailed schematics, generates a BOM, and writes assembly instructions.

(captured site page body (agents/sprocket.md), not a verified repo-code finding)
Sprocket is Spikonado's agent for building complete technology systems — apps, robots, devices, and the glue between them — rather than just code. It retrieves web context for everything it does and can purchase hardware parts or SaaS subscriptions from any website when asked, then produce the concrete artifacts of hardware development: detailed schematics, a bill of materials, and assembly instructions. It runs as a browser-based UI by default (the local app launches a Rust-based server on port 17731), as Electron desktop installers for Linux, macOS, and Windows, or via npx, with state stored locally in $HOME/.sprocket. The repo is public under the Functional Source License, and self-hosted development needs a Convex deployment plus model-provider API keys, so users bear their own model costs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sprocket.md)
