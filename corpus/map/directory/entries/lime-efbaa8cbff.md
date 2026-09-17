# lime (`lime`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: limecloud
- License: GPL-3.0
- Language: TypeScript, Rust, JavaScript (Electron + React + Vite, Rust App Server)
- Interface: platforms=CLI; install=binary - GitHub Releases (.dmg/.exe) or Homebrew (brew install --cask lime)
- Model providers: configurable providers/models/credentials/routing/retries, no vendor lock-in
- Feature flags (directory-reported):
  - mcp_support: yes - tool discovery and external tool integration (yes)
  - plugin_support: yes - Skills system, extensions (e.g., lime-chrome), bundled plugins (openai-bundled) (yes)
  - claude_code_plugin: no - has CLAUDE.md but is its own agent (no)
  - subagents: yes - multi-agent coordination, parallel subtask delegation, shared context (yes)
  - hooks: unknown (unknown)
  - plan_mode: yes - agent proposes plans and boundaries requiring approval before execution (yes)

Repository map entry: [limecloud/lime](../../repos/limecloud/lime.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Lime packages the agentic loop — context, tools, permissions, verification, delivery — into a desktop application rather than a terminal, so users watch plans, approve actions, and inspect diffs and a
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
