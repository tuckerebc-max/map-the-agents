# Gadfly (`gadfly`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Touchpoint-Labs
- License: MIT
- Language: Python 3.11+
- Interface: install=pip install gadfly-ai, then 'gadfly init' in your project, then 'gadfly status'
- Model providers: Anthropic (Claude Code subscription or Anthropic API)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [touchpoint-labs/gadfly](../../repos/touchpoint-labs/gadfly.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): A Socratic supervision layer for AI coding agents. Sits inside Claude Code's live tool-call loop, intercepting every PreToolUse hook before execution. Two independent supervisors (Architect on Opus, Code Reviewer on Sonnet) deliver one of four verdicts (allow/question/surface/block). Self-improving via append-only edit-ledger and idle-time extractor that distills corrections into durable memory. Enforces spec-driven development, catches drift and bugs pre-execution. Zero dependencies. ...

(captured site page body (agents/gadfly.md), not a verified repo-code finding)
Coding agents drift from their specifications and commit subtle bugs mid-task, and post-hoc review catches these too late. Gadfly intercepts Claude Code's PreToolUse hook so each action is judged before execution, with a deterministic filter auto-approving safe commands and two read-only LLM supervisors handling the rest. It enforces spec-driven development through a required spec.md, an optional midwife pass asks clarifying questions before building, and an idle-time extractor distills out-of-band user corrections from an append-only edit ledger into durable rules. The autonomy dial (autonomous, balanced, collaborative) sets how often it interrupts, configuration lives in gadfly.toml, and it runs on an existing Claude Code subscription or the Anthropic API.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gadfly.md)
