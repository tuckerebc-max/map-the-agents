# XCoding (`xcoding`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: XCodingLab
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=Download from GitHub Releases latest; or pnpm install + pnpm run dev for local dev
- Model providers: OpenAI Codex, Anthropic Claude Code
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [xcodinglab/xcoding](../../repos/xcodinglab/xcoding.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight AI vibe-coding IDE supporting parallel multi-agent collaboration (Codex/Claude Code) and parallel multi-project development with VS Code-like editor, terminal, and preview in one window.

(captured site page body (agents/xcoding.md), not a verified repo-code finding)
XCoding is a lightweight vibe-coding IDE built for running several AI agents and several projects at once: one window hosts a VS Code-like editor, terminal, and app preview alongside agent collaboration from Codex and Claude Code, with projects switchable via Cmd/Ctrl+1-8. AI assistance can be invoked at any point, with changes applied or rolled back in one step, and task-driven workflows manage code changes across the session. The core is deliberately opinionated: no plugin marketplace, with built-ins covering the main path to keep the app light and fast. The codebase is TypeScript (Vite, tsup, Tailwind, pnpm) under MIT, distributed in English and Simplified Chinese. It is very early stage, with 18 commits and no published releases.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/xcoding.md)
