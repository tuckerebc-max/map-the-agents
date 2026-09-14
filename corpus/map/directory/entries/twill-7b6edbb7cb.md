# Twill (`twill`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Twill
- License: Proprietary
- Language: unknown
- Interface: platforms=Autonomous, Web; install=Web app, desktop app, or scriptable CLI
- Model providers: Anthropic (Claude), OpenAI (GPT) for hard tasks; Qwen, Kimi, GLM open-source models for routine work — user's own keys at provider rates
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): A YC-backed 'software factory' that turns triggers (GitHub PR/issue, Slack, Linear, CLI) into pull requests: each task forks a fully provisioned copy of the company environment — repo, deps, running app, seeded database — where a coding agent (Claude Code, Codex CLI, or OpenCode) executes with proof attached (test results like '142 pass'), supports multi-repo reasoning across frontend/backend/infra, and runs ...

(captured site page body (agents/twill.md), not a verified repo-code finding)
Twill exists because handing real tickets to coding agents requires more than the agent: the environment must be cloned, dependencies installed, the app running, and the database seeded before useful work starts. Each incoming task from GitHub, Slack, Linear, or the CLI forks an isolated, pre-warmed copy of the whole company environment — supporting multi-repo setups so an agent can reason across frontend, backend, workers, and infrastructure in one task — and the selected coding agent works inside it, installing packages, running Docker, seeding data, and running tests. Results come back as pull requests with evidence attached, so review centers on test output rather than diffs alone. Recurring automations (incident triage, cloud resource checks, doc updates, follow-ups) run on schedule against the same machinery. Engineering teams use it via web, desktop, or CLI, paying with their own provider keys; YC-backed, with a free Pro tier for open-source maintainers.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/twill.md)
