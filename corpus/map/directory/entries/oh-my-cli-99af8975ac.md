# oh-my-cli (`oh-my-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): Safety-first code-agent CLI: spoof-resistant approval previews (Unicode neutralization), folder-trust boundary (fail-closed), deterministic offline command policy (denies destructive git, credential access, path escape, device overwrite). Durable JSONL sessions with resume/compact/undo-redo. Headless-first JSON event stream for CI. Run summaries, scorecards, spend budgets. Self-developing via evidence-bound autonomous governance queue.

(captured site page body (agents/oh-my-cli.md), not a verified repo-code finding)
oh-my-cli is a coding agent CLI built around the premise that safety guarantees must be structural rather than advisory. Approval previews are hardened against Unicode spoofing, untrusted workspaces fail closed on mutations, and a deterministic command policy denies destructive operations even in yolo mode. Sessions are durable JSONL records that can be resumed, compacted, and undone turn-by-turn with file-level checkpoints. Headless runs emit a versioned JSON event stream with spend budgets, tool-call caps, and signed evidence archives for audit. MCP servers are declared as versioned contracts resolved read-only, and leased git worktrees give each mutating agent an isolated workspace with idempotent lease semantics.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/oh-my-cli.md)
