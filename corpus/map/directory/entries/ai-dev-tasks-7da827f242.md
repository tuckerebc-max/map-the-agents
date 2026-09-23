# ai-dev-tasks (`ai-dev-tasks`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: snarktank
- License: Apache-2.0
- Language: Markdown
- Interface: install=git-clone
- Model providers: Any (tool-agnostic Markdown prompts)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [snarktank/ai-dev-tasks](../../repos/snarktank/ai-dev-tasks.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Tool-agnostic structured prompt workflow (PRD -\> granular task list -\> iterative implementation with review checkpoints) that brings discipline to AI-assisted development. Just markdown files usable with any AI coding assistant (Amp, Claude Code, Windsurf, etc.) — no install, framework, or specific tool required.

(captured site page body (agents/ai-dev-tasks.md), not a verified repo-code finding)
AI coding sessions derail when a whole feature is requested at once: scope drifts, and nothing is verifiable incrementally. ai-dev-tasks replaces that with a fixed sequence — generate a PRD from a feature description, derive a granular task/subtask list from it, then implement one task at a time with the assistant pausing for review after each. The mechanism is deliberately nothing but Markdown: you clone the prompt files into the repo and tag them with @ in whichever assistant you use, so the workflow survives tool changes and can be edited like any other project file. Human checkpoints at each task boundary are the enforcement mechanism, not software. It is widely used across Claude Code, Cursor, Windsurf, and Amp users, with 7.8k stars.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/ai-dev-tasks.md)
