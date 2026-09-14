# rules (`rules`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: project-codeguard
- License: NOASSERTION
- Language: Python
- Interface: install=Python tooling from source (pyproject/uv); rules distributed to coding agents via per-agent translators and a bundled Claude Code plugin/skills format
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [project-codeguard/rules](../../repos/project-codeguard/rules.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI model-agnostic security framework and ruleset that embeds secure-by-default practices into AI coding workflows; ships core security rules, translators for popular coding agents, and validators. Donated/moved to Coalition for Secure AI (CoSAI) at github.com/cosai-oasis/project-codeguard

(captured site page body (agents/rules.md), not a verified repo-code finding)
AI-generated code tends to reproduce the insecure patterns in its training data, and every agent ecosystem invented its own instruction format, so a security team would have to maintain parallel rule sets. CodeGuard centralizes the rules — secure-by-default practices for generation and review — and translates them into the formats specific agents consume, from Cursor and Copilot conventions to a Claude Code plugin with software-security skills. Validators close the loop by checking that an agent's output satisfies the rules rather than assuming the instructions were followed. The project originated in industry and was donated to CoSAI for vendor-neutral stewardship, so the original repository is now a pointer; adopters should track the cosai-oasis repository. It is aimed at security teams rolling out AI coding tools with consistent guardrails.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rules.md)
