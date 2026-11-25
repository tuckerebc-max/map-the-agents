# Atlarix (`atlarix`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Atlarix
- License: Proprietary
- Language: unknown
- Interface: platforms=CLI, Desktop, IDE; install=curl -fsSL https://atlarix.dev/install | sh, brew install amariahak/atlarix/atlarix, or npm install -g atlarix; desktop app download from atlarix.dev; editor extension on the Visual Studio Marketplace and Open VSX; Chrome extension on the Chrome Web Store
- Model providers: Any model (managed, own key, or fully local)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

Discrepancy between directory sources (not overwritten):

- interface: published=, backing=(('Web',), 'Download signed/notarized Electron builds for macOS, Linux, Windows from website; release artifacts at github.com/AmariahAK/atlarix-releases'), page=(('CLI', 'Desktop', 'IDE'), 'curl -fsSL https://atlarix.dev/install | sh, brew install amariahak/atlarix/atlarix, or npm install -g atlarix; desktop app download from atlarix.dev; editor extension on the Visual Studio Marketplace and Open VSX; Chrome extension on the Chrome Web Store')

## Description

Highlight (site page `what_makes_it_special`): Private AI workstation (desktop app, CLI, and editor extensions) that plans, writes, and verifies code with every edit requiring approval and code staying on your machine; real terminal and test running; drives your own Chrome through the free Atlarix extension; a cloud agent runs in your repository's own GitHub Actions and opens pull requests; integrates GitHub, Slack, Jira, Linear, Notion. ...

(captured site page body (agents/atlarix.md), not a verified repo-code finding)
Atlarix is a private AI workstation built by NorahLabs for teams that need AI coding without code leaving the machine. The agent plans, writes, and verifies code on-device, every edit requires approval through a diff view, and the agent runs tests on its own work, refusing to call a task done while tests fail. Independent tasks go to sub-agents that report back while the session continues, and the free Atlarix extension for Chrome plus persistent terminals support web-bound and CLI-bound work. GitHub, Slack, Jira, Linear, and Notion integrations plus scheduled triggers (fix builds on push, weekly dependency reviews) put the agent into existing workflows, and a read-only Atlarix Reviewer GitHub App posts PR findings and is included with Pro. Models run managed, via user API keys, or fully local, and the app ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [backing feed @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/_data/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/atlarix.md)
