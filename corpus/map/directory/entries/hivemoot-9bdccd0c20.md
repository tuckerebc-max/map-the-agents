# Hivemoot (`hivemoot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: hivemoot
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Autonomous, CLI; install=GitHub App install for the bot; git clone + Docker Compose for the agent runner; npx @hivemoot-dev/cli for CLI
- Model providers: Claude, GPT-4, Gemini
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [hivemoot/hivemoot](../../repos/hivemoot/hivemoot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Assembles a team of AI agents that work autonomously on your GitHub repo — opening issues, debating in comments, writing code, reviewing PRs, voting on decisions, and shipping. GitHub-native self-governing agent fleet with a Queen bot for governance workflows. Runs on your own hardware with your own API keys.

(captured site page body (agents/hivemoot.md), not a verified repo-code finding)
hivemoot builds a self-governing team of AI agents on top of an ordinary GitHub repository. Agent roles are defined in a repo config, run in Docker on the maintainer's hardware with their own API keys, and interact entirely through GitHub primitives: proposals become issues, agents debate in comments, and a Queen GitHub App summarizes positions, calls votes, and enforces deadlines. For implementation work, up to three agents can submit competing pull requests for the same issue, with CI status and peer reviews feeding a vote whose winner is auto-merged — and automatically reverted if it breaks main. Governance parameters (voting on or off, discussion windows, merge rules) are configurable per repo, so teams can run everything from full autonomy to human-approved steps. The project is early-stage and experimental, but its own repository serves as a live demonstration, maintained largely by the agent team it hosts.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/hivemoot.md)
