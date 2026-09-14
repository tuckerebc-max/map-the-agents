# Codex Security (`codex-security`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: openai
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: OpenAI, OpenRouter, Fireworks, Amazon Bedrock
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [openai/codex-security](../../repos/openai/codex-security.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-driven end-to-end security workflow CLI/SDK: discovers, validates, and auto-patches vulnerabilities, verifies fixes, and opens GitHub PRs. Deep multi-agent scans with --subagents flag. Interactive finding review, scan comparison by root cause, Linear issue publishing. Containerized bulk scans with AppArmor hardening. Pluggable inference providers. Extensibility via scan prompt files and knowledge bases.

(captured site page body (agents/codex-security.md), not a verified repo-code finding)
Security review rarely keeps pace with code changes, and static scanners produce noise that nobody remediates. Codex Security applies an agent loop to that gap: discovery runs scan a codebase, each candidate finding is validated before reporting, generated patches are verified, and verified fixes become GitHub pull requests for human review. The CLI wraps a TypeScript SDK so teams can embed scans in CI with an API key or authenticate interactively through ChatGPT, with Trusted Access gating for sensitive finding categories. A findings service stores results in SQLite, deduplicates them by embedding similarity, and serves a dashboard. Security teams and maintainers use it to move from scanner output to verified remediation, and Docker Compose configurations support bulk scans across repository sets.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codex-security.md)
