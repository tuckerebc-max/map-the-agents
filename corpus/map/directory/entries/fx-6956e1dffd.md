# fx (`fx`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: vercel-labs
- License: Apache-2.0
- Language: Zig
- Interface: platforms=CLI; install=curl -fsSL https://fx.sh/setup.sh | bash
- Model providers: Model-agnostic (local models, gateways, direct provider APIs, or subscriptions)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [vercel-labs/fx](../../repos/vercel-labs/fx.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A coding agent harness written in Zig that behaves like a Unix shell rather than a terminal IDE: a ~6 MB binary with microsecond cold start, a shell-like UI that preserves scroll history, WebAssembly builds with a pluggable network stack, and a deliberately minimal system prompt for token efficiency.

(captured site page body (agents/fx.md), not a verified repo-code finding)
Most agent CLIs are Node or Python applications with heavy startup costs, which limits where they can run. Vercel Labs built fx in Zig as a ~6 MB static binary with near-instant cold start and a small memory footprint, intended to be embedded in sandboxes, CI, and larger systems rather than to replace an editor. The UI follows shell conventions and preserves scrollback, and the core stays small by pushing capability into skills, plugins, and MCP servers while remaining model- and provider-agnostic. Version 0.0.6 is explicitly experimental with frequent breaking changes expected, so adopters are largely tool builders evaluating embeddable agent runtimes.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fx.md)
