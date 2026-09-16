# oh-my-cli (`oh-my-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: qwen-code-dev-bot
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Autonomous, CLI; install=npm (build + link)
- Model providers: any OpenAI-compatible (OpenAI, DashScope/Qwen, local Ollama, etc.)
- Feature flags (directory-reported):
  - mcp_support: yes (stdio; mcp section in settings; --mcp-contract, --invoke-mcp; contract v1) (yes)
  - plugin_support: yes (provider, MCP, tool, and workflow extensions as governed contracts) (yes)
  - claude_code_plugin: no (no)
  - subagents: partial (leased git worktrees for delegated agents; --create-worktree/--agent-identity) (reported)
  - hooks: partial (project-controlled hooks gated by folder trust) (reported)
  - plan_mode: yes (--plan emits deterministic dependency-ordered plan: understand -\> implement -\> verify -\> review) (yes)

Repository map entry: [qwen-code-dev-bot/oh-my-cli](../../repos/qwen-code-dev-bot/oh-my-cli.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
oh-my-cli is a coding agent CLI built around the premise that safety guarantees must be structural rather than advisory. Approval previews are hardened against Unicode spoofing, untrusted workspaces f
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
