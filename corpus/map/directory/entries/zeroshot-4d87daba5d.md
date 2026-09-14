# zeroshot (`zeroshot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: the-open-engine
- License: MIT
- Language: TypeScript/Node.js + Rust components
- Interface: platforms=CLI; install=npm
- Model providers: Claude, Codex, bundled Gateway, Gemini, OpenCode, Pi, OMP, Kiro, Copilot
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes - custom workflows as JSON files; provider registry (yes)
  - claude_code_plugin: n/a - Claude is a supported provider; .claude/CLAUDE.md present (reported)
  - subagents: yes - conductor, executor, planner, worker, validators, meta-coordinator, investigator, fixer, tester, completion-detector (yes)
  - hooks: yes - cluster-hooks/ directory (yes)
  - plan_mode: partial - planner agent in full-workflow (reported)

Repository map entry: [the-open-engine/zeroshot](../../repos/the-open-engine/zeroshot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Independent executor-verifier orchestration: 'The agent that wrote the code shouldn't be the one that says it works.' Verifiers don't share the executor's session, must reproduce failures independently, and approve/reject with specific objections. Complexity-based workflow routing (TRIVIAL through CRITICAL with escalating validator counts), git worktree isolation, crash-safe SQLite ledger, and a message-driven multi-agent architecture. 'Layer 01 - Verification' of The Open ...

(captured site page body (agents/zeroshot.md), not a verified repo-code finding)
zeroshot rests on a specific claim: the agent that wrote code is structurally unfit to certify it, since shared context produces shared blind spots. The tool is a CLI that orchestrates clusters of agents over a message bus, with a conductor classifying each task by complexity and type and selecting a matching workflow — a debug workflow, a lone worker, a worker-plus-validator pair, or the full pipeline where critical tasks get a planner, four validators in two stages, and a meta-coordinator. The load-bearing rule is verifier independence: validation agents receive none of the executor's session or reasoning, must reproduce any reported failure from scratch, and can reject with concrete objections, which forces code that survives to have been checked by an agent that never saw the author's rationale. Runs persist every step to a crash-safe SQLite ledger so interrupted runs resume; tasks enter from GitHub, GitLab, Jira, Azure DevOps, or Linear, and completed work ships through git flows gated by quality checks that fail closed. Agents — conductor, planner, worker, validators, fixer, tester, investigator, completion-detector — are wired through JSON workflow templates that teams can rewrite, and cycles between agents are legal with escape logic for rings. ...
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zeroshot.md)
