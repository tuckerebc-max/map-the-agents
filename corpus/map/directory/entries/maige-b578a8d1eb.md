# Maige (`maige`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: unknown
- License: AGPL-3.0
- Language: TypeScript
- Interface: install=Self-host: bun i + bun run dev (with GitHub App + ngrok); or hosted via GitHub App install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Open-source infrastructure by Rubric Labs for running natural language workflows on your codebase; auto-labels, assigns, comments on, and reviews issues/PRs via a GitHub App. Currently in alpha.

(captured site page body (agents/maige.md), not a verified repo-code finding)
Maige automates the triage and review labor that consumes maintainer time on active repositories: plain-language rules replace webhooks-plus-scripts, so instructions like 'review any PR touching auth for security issues' or 'label new issues by component' become standing agent behavior. Runs execute in a sandbox against codebase embeddings, letting the agent label, assign, comment, review, and propose code changes through the GitHub API. The hosted service costs $30/month after 30 free issues, and the AGPL-licensed source supports self-hosting for teams that want their own deployment. Repositories such as Documenso, Nuxt, Highlight.io, and Cal.com have used it; the product remains in alpha under Rubric Labs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/maige.md)
