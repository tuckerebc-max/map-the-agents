# frankenterm (`frankenterm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Dicklesworthstone
- License: NOASSERTION
- Language: Rust
- Interface: platforms=CLI; install=Run install.sh script in repository root
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [dicklesworthstone/frankenterm](../../repos/dicklesworthstone/frankenterm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal hypervisor for AI agent swarms; provides real-time pane capture, state-machine pattern detection for agent state, and a JSON API for coordinating fleets of coding agents across WezTerm; turns a terminal multiplexer into a coordination layer for AI agent swarms.

(captured site page body (agents/frankenterm.md), not a verified repo-code finding)
Running many CLI coding agents means manually watching terminals for the moments an agent goes idle, asks a question, or gets stuck. Frankenterm treats the terminal itself as the integration surface: it captures WezTerm pane content in real time, runs state-machine pattern detection to classify what each agent is doing, and publishes that state through a JSON API that scripts and other tools can query and act on. This lets operators build their own coordination logic on top of unmodified agents rather than adopting a vendor's orchestration format. It targets developers running agent swarms in WezTerm who want programmatic fleet control without changing how each agent is invoked.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/frankenterm.md)
