# Aeon (`aeon`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aeonfun
- License: MIT
- Language: JavaScript
- Interface: platforms=Autonomous; install=source
- Model providers: Claude Code, Grok, Codex, Pi, Vibe, Kimi
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aeonfun/aeon](../../repos/aeonfun/aeon.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Autonomous AI agent framework that runs unattended on GitHub Actions — ships features, deploys apps, finds/discloses vulnerabilities, runs research, and writes new skills for itself. Runs on a schedule (cron), remembers across runs, reacts to conditions, and self-heals its own broken skills with no approval loops. A single skill is just a Markdown file (frontmatter + prompt). Fleet model: spawn-instance ...

(captured site page body (agents/aeon.md), not a verified repo-code finding)
Aeon is built for work nobody schedules: vulnerability disclosure rounds, dependency maintenance, research digests, and feature drops that happen on cron instead of when a developer remembers. An installation is a forked repository plus GitHub Actions — Node.js 20+ and the gh CLI are the only prerequisites — with configuration in aeon.yml defining schedules, skill inputs, models, and notification channels. Skills are individual SKILL.md markdown files organized into packs, and the runtime remembers across runs, reacts to conditions, and repairs skills that break, all without approval loops. An MCP server and Claude Code/Codex plugin support let existing agents invoke Aeon skills. Solo maintainers and small teams running unattended repositories are its users.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/aeon.md)
