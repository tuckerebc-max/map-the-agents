# lime (`lime`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): Open-source full-stack desktop AI agent combining coding, file operations, terminal commands, tool calls, research, content creation, and multi-agent collaboration in one workspace. Desktop GUI agent with Thread/Turn/Item projections for traceable task chains. Full-stack multimodal (text, code, images, audio, video, PDFs, structured data). Multi-agent coordination delegates research/implementation/testing/documentation to different agents with shared context. Skills system encodes repeatable procedures as reusable execution ...

(captured site page body (agents/lime.md), not a verified repo-code finding)
Lime packages the agentic loop — context, tools, permissions, verification, delivery — into a desktop application rather than a terminal, so users watch plans, approve actions, and inspect diffs and artifacts in a visual workspace. Tasks are structured as Thread/Turn/Item projections that can be paused, reviewed, restored, and continued, and multi-agent collaboration splits research, implementation, testing, and documentation across agents sharing one context. A Rust app server handles the backend, and a Skills system encodes repeatable procedures as units callable through MCP. It is provider-agnostic with local-by-default data, targets developers and technical users who want a GUI over an agentic loop, and runs on macOS and Windows (Linux builds paused).
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/lime.md)
