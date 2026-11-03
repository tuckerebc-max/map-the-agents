# RunVSAgent (`runvsagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: wecode-ai
- License: Apache-2.0
- Language: Kotlin, TypeScript
- Interface: platforms=IDE; install=jetbrains
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [wecode-ai/runvsagent](../../repos/wecode-ai/runvsagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Bridges the VSCode ecosystem and JetBrains IDEs, allowing developers to use VSCode-based AI coding agents (Roo Code, Cline, Kilo Code) natively within JetBrains IDEs (IntelliJ IDEA, WebStorm, PyCharm) via an extension host with RPC communication. Maintained by WeCode-AI Team, Weibo Inc.

(captured site page body (agents/runvsagent.md), not a verified repo-code finding)
JetBrains users faced a choice between switching IDEs or losing access to the VS Code agent ecosystem, since Roo Code, Cline, and Kilo Code ship only as VS Code extensions; Weibo's WeCode-AI team built the bridge rather than a competing agent. The Kotlin plugin provides the IDE surface, while the Node Extension Host emulates the VS Code API the extensions call, with the two processes communicating over local sockets. Any supported agent runs with its own UI, MCP servers, and settings intact, which also means the bridge inherits those agents' model providers rather than defining its own. Installation is via the JetBrains Marketplace or a downloaded zip, requiring IDE 2023.1 or newer. It serves JetBrains developers who want a specific VS Code agent without changing editors, and the project is actively maintained with published known issues.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/runvsagent.md)
