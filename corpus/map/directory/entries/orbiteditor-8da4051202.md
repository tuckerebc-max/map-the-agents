# orbiteditor (`orbiteditor`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ashish200729
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Desktop, IDE; install=curl -fsSL https://raw.githubusercontent.com/ashish200729/orbiteditor/main/install.sh | bash, or download .dmg from Releases
- Model providers: OpenAI, Anthropic, Google, local (BYOK)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: yes (yes)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [ashish200729/orbiteditor](../../repos/ashish200729/orbiteditor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI code editor (Cursor alternative) forked from Void Editor/VS Code; BYOK with any provider, local model support, subagents, plan mode, MCP integration, checkpoints and change visualization, no data retention.

(captured site page body (agents/orbiteditor.md), not a verified repo-code finding)
Closed AI editors retain code and prompts on vendor servers, which is a non-starter for some teams. Orbit Editor continues the Void Editor's approach — a VS Code fork that sends messages straight to the chosen provider with no data retention — and layers an agent system on top: subagents with tool policies, a documented plan mode, MCP integration for external tools, Skills for reusable workflows, and checkpoints with change visualization. Providers are BYOK across OpenAI, Anthropic, Google, and local models. It ships as a macOS beta (Apple Silicon and Intel) via a signed install script or DMG, with Windows and Linux marked as coming soon, and its VS Code base keeps the standard extensions directory. The codebase guide and plan-mode/subagent docs in-repo serve as documentation alongside a Discord community. It is a single-maintainer beta project (58 stars, 229 commits), so maturity is unproven, but it is one of the few fully open editor forks still actively carrying the agent stack forward.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/orbiteditor.md)
