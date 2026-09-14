# coderabbit-review-helper (`coderabbit-review-helper`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: obra
- License: MIT
- Language: Python
- Interface: install=Clone repo + pip install --user beautifulsoup4; run ./extract-coderabbit-feedback.py owner/repo/123
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [obra/coderabbit-review-helper](../../repos/obra/coderabbit-review-helper.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Converts CodeRabbit GitHub PR reviews into clean, LLM-friendly text formatted for AI coding agents to automatically apply suggestions; prioritizes AI-actionable items and organizes feedback by file.

(captured site page body (agents/coderabbit-review-helper.md), not a verified repo-code finding)
CodeRabbit posts rich, structured review comments on pull requests, but their format — HTML, nested threads, interleaved nitpicks and substantive findings — is awkward for AI coding agents to consume. This script pulls a PR's CodeRabbit comments through the GitHub CLI, strips HTML, groups feedback by file, and reorders it so AI-actionable prompts come before informational diffs, emitting plain text suitable for piping into Claude, ChatGPT, or another agent. It is a single Python file depending only on beautifulsoup4 and an authenticated gh CLI, with no published package: users clone the repository and run the script directly. The project dates from September 2025 and has seen only light, occasional maintenance since.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coderabbit-review-helper.md)
