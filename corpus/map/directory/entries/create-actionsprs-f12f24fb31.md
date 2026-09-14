# Create-Actionsprs (`create-actionsprs`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: jhutchings1
- License: MIT
- Language: PowerShell
- Interface: install=Clone repo, rename .env-example to .env with GitHub token, run ./Create-ActionsPRs.ps1
- Model providers: none
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [jhutchings1/create-actionsprs](../../repos/jhutchings1/create-actionsprs.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Automates creation of PRs across many repos to install/update GitHub Actions workflows (e.g., CodeQL). Three targeting modes: all repos in an org via API, custom file list of repos, auto-detect CodeQL-eligible repos. NOTE: This is a GitHub Actions automation script, not an AI coding agent harness.

(captured site page body (agents/create-actionsprs.md), not a verified repo-code finding)
Before agents, keeping GitHub Actions workflows consistent across an organization meant repetitive manual PRs. Create-ActionsPRs automates that with a single PowerShell script: authenticate with a GitHub token, choose a targeting mode (every repo in an org via API, an explicit list of repositories, or all repos eligible for CodeQL using a bundled workflow file), and the script opens one pull request per repository installing or updating the workflow. It requires only PowerShell, git, the GitHub CLI, and a token with repo scope, and includes a ready-made CodeQL workflow for the third mode. The last meaningful development dates to 2023 and the repo is dormant, but security teams rolling out CodeQL at scale still fork it. It belongs in the census as 'other': classic automation that predates and contains no AI.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/create-actionsprs.md)
