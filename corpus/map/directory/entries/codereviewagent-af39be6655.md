# CodeReviewAgent (`codereviewagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: gitbito
- License: MIT
- Language: Shell
- Interface: platforms=IDE; install=Bito Cloud (no install), self-hosted via CLI/webhooks/GitHub Actions, or IDE plugins (VS Code / JetBrains)
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: False (reported)

Repository map entry: [gitbito/codereviewagent](../../repos/gitbito/codereviewagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Bito's AI Code Review Agent provides automated, context-aware code reviews in Git workflows (PR/MR) and IDEs, identifying bugs, code smells, and security vulnerabilities with fix suggestions. First agent built on Bito's AI Agent framework; powered by Anthropic Claude Sonnet 3.5; deep whole-codebase understanding; integrates static analysis tools (fbinfer, OWASP Dependency-Check) out of the box and 3rd-party tools (Snyk, Sonar); does ...

(captured site page body (agents/codereviewagent.md), not a verified repo-code finding)
Bito's CodeReviewAgent automates the review stage of pull and merge requests across GitHub, GitLab, and Bitbucket, reading the whole codebase rather than the diff alone so findings account for surrounding architecture. It flags bugs, code smells, and security vulnerabilities, proposes line-level fixes, and posts results directly as PR comments; the same review engine runs in VS Code and JetBrains IDEs for pre-commit feedback. The agent incorporates static-analysis tooling — fbinfer and OWASP Dependency-Check out of the box, with Snyk, Sonar, and Dependabot configurable — and estimates review effort per change. Bito offers it as a cloud service with a free signup tier, as a self-hosted deployment via CLI, webhooks, or GitHub Actions, and states that customer code is neither stored nor used for model training.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codereviewagent.md)
