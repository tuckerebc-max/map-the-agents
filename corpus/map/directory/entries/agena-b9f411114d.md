# Agena (`agena`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: aozyildirim
- License: MIT
- Language: Python, TypeScript
- Interface: platforms=Autonomous; install=brew install aozyildirim/tap/agena | npm install -g @agenaai/cli | git clone + ./start.sh (Docker Compose)
- Model providers: OpenAI, Google Gemini, Claude CLI, Codex CLI, Custom
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aozyildirim/agena](../../repos/aozyildirim/agena.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Runs on existing Claude Code/Codex CLI subscriptions locally via host bridge (no API keys or per-token billing); full autonomous loop from production error to task to AI fix to PR to merge to issue resolved; Team Skill Catalog with Qdrant vector retrieval that re-applies past solutions; pixel-art 'Boss Mode' office UI for managing AI agents visually; self-hostable multi-tenant SaaS with ...

(captured site page body (agents/agena.md), not a verified repo-code finding)
Agena automates the path from production incident to merged fix: errors arriving from Sentry, New Relic, Jira, YouTrack, or Azure DevOps become tasks that a CrewAI/LangGraph pipeline of PM, Planner, Developer, Reviewer, and Finalizer agents turns into reviewed pull requests. Its economic hook is the host bridge — agents run on the team's existing Claude Code or Codex CLI subscriptions locally, so there are no API keys or per-token charges, with OpenAI and Gemini available as alternatives. A Team Skill Catalog in Qdrant retrieves how similar problems were solved before, and integrations cover Jira, YouTrack, and GitHub. It ships as brew/npm CLIs or a self-hosted Docker Compose stack with RBAC and Stripe billing, and a visual flow builder adds approval gates. Teams with steady production-error volume are the intended operators.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agena.md)
