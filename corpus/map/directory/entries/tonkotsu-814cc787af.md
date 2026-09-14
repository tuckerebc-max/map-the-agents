# Tonkotsu (`tonkotsu`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Tonkotsu
- License: unknown
- Language: unknown
- Interface: unknown
- Model providers: Anthropic (Claude Code, via the user's existing Anthropic plan)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): A GUI that manages parallel Claude Code agents through a structured plan-code-verify document: Tonkotsu drafts a plan for human sign-off, delegates dozens of coding tasks at once across multiple repos with task dependencies, and runs test plans and code review in one place — with no commits until the human approves. Codes in isolated repo clones on the developer's own ...

(captured site page body (agents/tonkotsu.md), not a verified repo-code finding)
Tonkotsu addresses the monitoring burden of running many Claude Code agents at once: unattended terminals stall, merge into each other, and require constant babysitting. Its workflow moves planning into a shareable document — the human approves or edits the plan, then Tonkotsu delegates the resulting tasks to parallel Claude Code sessions across multiple repositories, respecting declared dependencies and running test plans before review. Nothing is committed until the developer approves, and all execution happens in isolated clones on the local machine rather than a hosted environment. Developers managing concurrent features use it to run agent work with intermediate-level-team turnaround; the site is currently returning 503, with the last archived captures in April 2026.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tonkotsu.md)
