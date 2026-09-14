# Charlie Labs (`charlie-labs`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Charlie Labs
- License: Proprietary
- Language: unknown
- Interface: platforms=Autonomous; install=SaaS (install the Charlie GitHub app; define daemons as .md files in-repo)
- Model providers: Proprietary (provider not disclosed)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (multiple daemons per repo, each with its own watch triggers and routines) (yes)
  - hooks: yes (watch triggers on events: PR merged, Linear issue created, cron schedules) (yes)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Charlie: GitHub-native AI engineer for issues-to-PRs

(captured site page body (agents/charlie-labs.md), not a verified repo-code finding)
Charlie Labs builds Charlie, an AI engineer platform organized around 'daemons': persistent agents that watch repositories and proactively perform recurring engineering work without being prompted each time. A daemon is declared in a markdown file in the repository with frontmatter specifying its watch triggers (events like a merged PR or a new Linear issue), scheduled routines, and deny rules that bound what it may do — never merging PRs, never overriding human decisions — alongside markdown policy sections defining its role. This addresses a gap between one-shot AI coding tools and human maintainer attention: dependency upgrades, PR hygiene, issue triage, and changelog upkeep happen continuously without a developer initiating each task. Daemons wake on events (new issues, merges, security advisories) and run scheduled sweeps, opening reviewable PRs and building compounding organizational memory. Engineering teams adopt Charlie by installing its GitHub integration and committing daemon definitions to their repos, with pricing based on shared team token usage.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/charlie-labs.md)
