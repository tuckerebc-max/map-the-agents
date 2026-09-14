# Rover (`rover`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Rover
- License: Proprietary
- Language: unknown
- Interface: platforms=Web; install=GitHub App (2-click install); self-hosting available
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Code reliability platform that scans PRs for bugs/security/performance issues in the context of the entire system (not just the diff). Builds a live interactive code graph across repositories; 'Curio' AI agent lets you chat with your codebase to understand and diagnose issues.

(captured site page body (agents/rover.md), not a verified repo-code finding)
Documatic built Rover around the observation that most AI review tools reason over a patch and miss the blast radius: a change that is locally correct can still break a caller two repositories away. The platform constructs a live graph of the organization's services, APIs, and data stores from the repositories it is connected to, then scans each pull request in that context for bugs, security exposure, performance regressions, and reliability risks such as leaks. Findings land as actionable PR comments, and the Curio agent answers system-level questions like why an API is timing out by walking the graph. Onboarding is a two-click GitHub app install, a free tier covers whole teams, and self-hosting is available for regulated environments.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rover.md)
