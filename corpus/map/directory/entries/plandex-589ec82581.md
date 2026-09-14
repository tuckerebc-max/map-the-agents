# Plandex (`plandex`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: plandex-ai
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl -sL https://plandex.ai/install.sh | bash
- Model providers: Anthropic, OpenAI, Google, OpenRouter, open source providers
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [plandex-ai/plandex](../../repos/plandex-ai/plandex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 2M token effective context window with tree-sitter project maps (30+ languages); cumulative diff sandbox separating AI changes from project files until ready; full version control for plans with branches; handles very large projects.

(captured site page body (agents/plandex.md), not a verified repo-code finding)
Plandex was built for large, multi-file changes that outgrow chat-window coding: tasks spanning dozens of files where a single bad edit deep in the sequence ruins the result. Its core mechanism is a cumulative diff sandbox — AI changes accumulate separately from project files until explicitly applied, with command execution controlled so missteps are easy to roll back — plus full version control over plans, including branches for trying alternative approaches or comparing models on the same task. A 2M-token effective context window over tree-sitter project maps handles codebases of 20M+ tokens, and autonomy is configurable from full-auto mode (with auto-debugging through Chrome for browser apps) down to step-by-step approval. Plandex Cloud wound down in October 2025, leaving self-hosted/local mode with your own API keys as the supported path, and the MIT-licensed v2 remains maintained for that audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/plandex.md)
