# Repo-To-Text (`repo-to-text`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: kirill-markin
- License: MIT
- Language: Python
- Interface: install=pip install repo-to-text (or via Docker: docker compose build)
- Model providers: none (offline converter; makes no LLM API calls)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [kirill-markin/repo-to-text](../../repos/kirill-markin/repo-to-text.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Generates an XML-formatted text representation of an entire repository (directory tree + file contents) and copies it to the clipboard, optimized for pasting codebases into LLMs for development and debugging.

(captured site page body (agents/repo-to-text.md), not a verified repo-code finding)
Repo-To-Text exists because pasting a codebase into a chat window loses the structure models need: it walks the repository, emits the directory tree plus file contents wrapped in XML tags, and copies the result to the clipboard or stdout. Selection follows gitignore semantics extended with its own settings file, so generated artifacts and vendored code can be excluded without touching the real .gitignore. A maximum word count per file splits oversized outputs deterministically. Python developers working with chat-based LLMs use it to hand a whole project to a model in one paste, and its Docker packaging lets CI jobs produce the same snapshot reproducibly. It deliberately contains no agent logic — conversion happens once, locally, before any model sees the text.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/repo-to-text.md)
