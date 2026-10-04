# Codex CLI (`codex-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: openai
- License: Apache-2.0
- Language: Rust, TypeScript
- Interface: platforms=CLI; install=curl -fsSL https://chatgpt.com/codex/install.sh | sh (macOS/Linux), npm install -g @openai/codex, brew install --cask codex, or download binaries from GitHub Releases
- Model providers: OpenAI, Amazon Bedrock
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [openai/codex](../../repos/openai/codex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): OpenAI's official coding agent that runs in the terminal with native sandboxing; can also integrate into VS Code, Cursor, and Windsurf. Supports MCP, plugins, hooks, subagents, and multiple execution modes.

(captured site page body (agents/codex-cli.md), not a verified repo-code finding)
Codex CLI is OpenAI's terminal coding agent, distributed as open source under Apache-2.0 with the core written in Rust. It runs locally with sandboxing around command execution and file edits, and offers approval modes from read-only through full autonomy. Authentication uses either a ChatGPT account (Plus, Pro, Business, Edu, or Enterprise) or an OpenAI API key, and the CLI connects to the same Codex ecosystem as the IDE extension and the cloud-based Codex Web at chatgpt.com/codex. The agent supports MCP servers, plugins, hooks, and subagents, with configuration documented at developers.openai.com/codex. It is installed via a curl script, npm (@openai/codex), Homebrew, or GitHub release binaries.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/codex-cli.md)
