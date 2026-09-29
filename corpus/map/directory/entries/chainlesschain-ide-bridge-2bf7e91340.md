# ChainlessChain IDE Bridge (`chainlesschain-ide-bridge`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: chainlesschain
- License: MIT
- Language: unknown
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: BYOK via the cc CLI (model configured in the agent, not the bridge)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (via cc CLI /plan) (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Brings the ChainlessChain cc agent CLI into JetBrains as a side-panel coding agent

(captured site page body (agents/chainlesschain-ide-bridge.md), not a verified repo-code finding)
ChainlessChain IDE Bridge integrates the ChainlessChain cc agent CLI into JetBrains IDEs as a side-panel coding agent, for developers who want the agent's capabilities without leaving IntelliJ-based IDEs. The plugin hosts multiple cc agent processes as conversation tabs with session resume across restarts, feeds editor context automatically (current selection, open tabs, diagnostics), and renders proposed changes as native side-by-side diffs with accept, request-changes, or reject actions across multi-file batches. Slash commands mirror the CLI's own vocabulary — including /plan, /auto, /think, and /cost — and an embedded JCEF view runs the dev server inside the IDE for live preview of generated apps. The plugin requires the chainlesschain CLI installed separately and is free under an MIT license, first published to the JetBrains Marketplace in August 2026 with rapid release cadence (v0.4.103 within weeks) tracking the cc CLI's own frequent updates.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/chainlesschain-ide-bridge.md)
