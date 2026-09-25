# am-i-vibing (`am-i-vibing`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ascorbic
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=npm install am-i-vibing (library) or npx am-i-vibing (CLI)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [ascorbic/am-i-vibing](../../repos/ascorbic/am-i-vibing.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Library and CLI that detects whether code is being executed by AI coding agents/editors (16+ tools: Aider, Bolt, Claude Code, Codex CLI, Cursor, Gemini CLI, Copilot, Jules, opencode, Pi, Replit, Warp, Windsurf, Zed, etc.) via environment variables and optional process-tree inspection, so tools can adapt output for agentic vs human consumption.

(captured site page body (agents/am-i-vibing.md), not a verified repo-code finding)
Libraries and CLIs increasingly need to know whether their output is being read by a human or fed back into an agent, since error messages, logging verbosity, and formatting differ. am-i-vibing exposes detectAgenticEnvironment() plus quick checks (isAgent, isInteractive, isHybrid) and a CLI (npx am-i-vibing, exit-code based) that classify the current process against 16 known tools via environment variables, with optional process-tree inspection for tools like Octofriend that leave no env traces. Detection returns the tool id, name, and environment type, with documented caveats about false positives. Matt Kane maintains it actively (125 commits, changesets, Renovate) as MIT-licensed TypeScript on npm.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/am-i-vibing.md)
