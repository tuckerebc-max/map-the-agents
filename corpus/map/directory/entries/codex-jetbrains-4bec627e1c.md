# Codex-JetBrains (`codex-jetbrains`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Haleclipse
- License: Apache-2.0
- Language: Kotlin, TypeScript
- Interface: platforms=IDE; install=JetBrains Marketplace: search RunVSAgent in Settings -\> Plugins -\> Marketplace; or download .zip from GitHub Releases and Install Plugin from Disk; or build from source with Node.js 18+, JDK 17+
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [haleclipse/codex-jetbrains](../../repos/haleclipse/codex-jetbrains.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Cross-platform JetBrains plugin (RunVSAgent) that runs VSCode-based coding agents and extensions (Roo Code, Cline, Kilo Code) within JetBrains IDEs via a Kotlin plugin and Node.js extension host communicating over RPC; supports all major JetBrains IDEs (2023.1+)

(captured site page body (agents/codex-jetbrains.md), not a verified repo-code finding)
RunVSAgent, of which this repository is a mirror, brings VS Code-only coding agents to JetBrains IDEs. A Kotlin plugin provides the JetBrains-side UI and editor integration, while a Node.js extension host implements the VS Code API surface those extensions expect, with the two communicating over RPC on Unix domain sockets or named pipes. The result is that Roo Code, Cline, and Kilo Code run inside IntelliJ IDEA, WebStorm, PyCharm, GoLand, Rider, and other JetBrains IDEs from 2023.1 onward with their native UIs and agent behavior intact. The tool was developed by the WeCode-AI team at Weibo and is distributed through the JetBrains Marketplace as plugin 28068; the Haleclipse repository mirrors it rather than being the primary distribution.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codex-jetbrains.md)
