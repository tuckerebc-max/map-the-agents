# intellegix-code-agent-toolkit (`intellegix-code-agent-toolkit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: intellegix
- License: MIT
- Language: Python, Node.js
- Interface: platforms=CLI, Web; install=git clone to ~/.claude, then pip install (Python deps) and npm install (Node deps)
- Model providers: Anthropic (Claude Sonnet/Opus/Haiku), Perplexity (multi-model council: GPT, Claude, Gemini via Perplexity)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [intellegix/intellegix-code-agent-toolkit](../../repos/intellegix/intellegix-code-agent-toolkit.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Automated loop driver with session continuity, budget enforcement, and stagnation detection; multi-agent parallel orchestration via git worktrees; multi-model council automation through Perplexity; portfolio governance with tier-based project management; 31 custom slash commands.

(captured site page body (agents/intellegix-code-agent-toolkit.md), not a verified repo-code finding)
The toolkit treats Claude Code as a runtime and layers operational discipline on top. The loop driver keeps sessions continuous, enforces token budgets, detects stagnation, and scales models to task weight, while the multi-agent orchestrator farms work into isolated git worktrees under a guard hook that keeps the orchestrator from editing code directly. The Perplexity council is the distinctive piece: it drives a logged-in Perplexity session through Playwright to consult GPT, Claude, and Gemini at zero marginal cost, then synthesizes with Opus. Thirty-one commands cover planning, implementation, review, and a seven-tier frontend E2E pipeline. It installs by cloning straight into ~/.claude and assumes the operator accepts --dangerously-skip-permissions for autonomous runs.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/intellegix-code-agent-toolkit.md)
