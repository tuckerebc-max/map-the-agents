# OpenCode_UI (`opencode-ui`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: LaiZhou
- License: MIT
- Language: Kotlin (JetBrains plugin, Gradle)
- Interface: platforms=IDE; install=JetBrains Marketplace: Settings -\> Plugins -\> Marketplace -\> Search 'OpenCode' -\> Install. Requires OpenCode CLI: npm install -g opencode-ai
- Model providers: inherited from the OpenCode server (none configured by the plugin)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [laizhou/opencode_ui](../../repos/laizhou/opencode_ui.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): JetBrains IDE plugin integrating OpenCode AI coding agent. Native diff viewer with chronological navigation, smart file path links in terminal, automatic session persistence, and seamless context sharing from editor/project view directly to AI terminal.

(captured site page body (agents/opencode-ui.md), not a verified repo-code finding)
OpenCode runs in a terminal, which leaves JetBrains users copying file paths by hand and reviewing agent changes in raw git diffs. This Kotlin plugin bridges the gap: Quick Launch attaches to a running OpenCode server (with optional password) or spawns a local terminal via Cmd+Esc, and Add to Terminal sends the current file or selection as context with Opt+Cmd+K. Diff review uses the IDE's native viewer with accept/reject actions that stage through git add, agent output renders file paths as clickable links, and sessions auto-resume with notifications when tasks complete. It installs from the JetBrains Marketplace, requires the opencode-ai CLI alongside, and works across IntelliJ IDEA, WebStorm, and PyCharm on 2025.2+. Its README candidly notes it lacks diagnostic sharing compared to Claude Code's plugin, since OpenCode relies on built-in LSP. JetBrains users who adopted OpenCode and want it embedded in their IDE are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencode-ui.md)
