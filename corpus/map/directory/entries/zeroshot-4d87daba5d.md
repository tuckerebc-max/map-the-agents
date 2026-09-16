# zeroshot (`zeroshot`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
zeroshot rests on a specific claim: the agent that wrote code is structurally unfit to certify it, since shared context produces shared blind spots. The tool is a CLI that orchestrates clusters of age
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
