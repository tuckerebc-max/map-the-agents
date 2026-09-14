# lavra (`lavra`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: roberto-mello
- License: MIT
- Language: JavaScript, TypeScript
- Interface: install=npx @lavralabs/lavra@latest; or git clone + ./install.sh (supports --opencode, --gemini, --cortex flags)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [roberto-mello/lavra](../../repos/roberto-mello/lavra.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Plugin for AI coding agents adding compound engineering workflows and persistent memory; 30 specialized subagents across review/research/design/workflow/docs, structured planning with adversarial review, automatic git-tracked JSONL memory capture, and shipping automation (tests, PRs, secret scanning).

(captured site page body (agents/lavra.md), not a verified repo-code finding)
Compound engineering — where every unit of work passes through design, implementation, review, and ship stages with research in between — is hard to sustain manually across agent sessions. Lavra installs as a plugin into Claude Code (default), OpenCode, Gemini CLI, or Snowflake Cortex Code and provides pipeline commands (/lavra-design, /lavra-work, /lavra-qa, /lavra-ship) plus a persistent memory store recalled at each session start. Its 30 subagents run at lower model tiers for research and review work, cutting cost substantially relative to running everything on a frontier model. Task tracking delegates to the Beads CLI, and knowledge accumulates in .lavra/memory/knowledge.jsonl, git-tracked with the repo.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/lavra.md)
