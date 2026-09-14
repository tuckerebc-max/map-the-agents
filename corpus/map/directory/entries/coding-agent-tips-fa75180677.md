# coding-agent-tips (`coding-agent-tips`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: anipotts
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=bun install --frozen-lockfile (Astro + Starlight site)
- Model providers: None (documentation site; covers Claude Code, Codex, Grok)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [anipotts/coding-agent-tips](../../repos/anipotts/coding-agent-tips.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Evidence-backed guidance publication for coding agents in production software, covering Claude Code and Codex. Enforces a strict evidence standard (hands-on, source-verified, inference, unknown) and publishes task specs, sanitized run records, and artifacts in a field lab. Corrections require primary sources.

(captured site page body (agents/coding-agent-tips.md), not a verified repo-code finding)
Most advice about coding agents is folklore, and practitioners operating agents on production code need to know which claims are tested. coding-agent-tips is a handbook published at agents.anipotts.com that grades every claim against a stated evidence standard, separating what the author verified hands-on from what official sources, analysis, or open questions support. Content is organized by the stakes of the reader's work - students, startup founders, big-tech engineers - rather than by tool, and covers the distinction between steering surface, harness, model, and orchestration, plus repo instructions, permissions, review practices, and operating costs. The repository is an Astro site with accessibility and site tests, and the guidance doubles as a Claude Code plugin so readers can apply the practices directly. It targets developers standardizing how their teams work with agents.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coding-agent-tips.md)
