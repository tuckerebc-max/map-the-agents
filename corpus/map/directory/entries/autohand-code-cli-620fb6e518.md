# Autohand Code CLI (`autohand-code-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: autohandai
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Autonomous, CLI, IDE, Web; install=curl -fsSL https://autohand.ai/install.sh | bash; or brew install autohandai/code/autohand-code; or clone and build with Bun
- Model providers: Autohand AI, OpenRouter, LLMGateway, OpenAI, AWS Bedrock, DeepSeek, Ollama, llama.cpp, MLX, Z.ai
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [autohandai/code-cli](../../repos/autohandai/code-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fast, self-improving terminal-native AI coding agent built with Bun and Ink. Features 40+ built-in tools, Agent Skills system with auto-generation, Code Extensions (declarative manifest-based), multi-agent team collaboration (/squad), iOS app pairing for remote control/monitoring, auto-mode for autonomous task loops, session checkpointing with rewind/review/share, 18 language documentation translations, and cross-platform support.

(captured site page body (agents/autohand-code-cli.md), not a verified repo-code finding)
Autohand Code CLI is a terminal-native AI coding agent for planning, editing, testing, and automating work across a codebase. It runs an interactive REPL with slash commands, @-file mentions, $-skill mentions, and Shift+Tab mode cycling (edit/plan/YOLO/auto), plus a command mode (autohand -p) for CI with --dry-run, stream-json output, and --auto-commit. Auto-mode runs standalone iteration loops with git worktree isolation, cost/runtime caps, and checkpoints, while a skills system auto-generates per-project skills compatible with Codex and Claude formats. Multi-provider support spans OpenRouter, OpenAI, Bedrock, DeepSeek, Z.ai, Ollama, llama.cpp, MLX, and Autohand's own cloud, with MCP, hooks, and declarative extensions. It is Apache-2.0 with a commercial carve-out above $5M ARR, built in TypeScript on Bun, and distributed via curl script, Homebrew, or npm.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/autohand-code-cli.md)
