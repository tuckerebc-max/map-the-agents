# Testai-Agent (`testai-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: khanzzirfan
- License: MIT
- Language: TypeScript
- Interface: install=npm install; npm run bundle; npm test (Node.js 20.x+). Used as a GitHub Action via uses: syntax in workflows.
- Model providers: LLM API key via env (LangGraph-based; provider not documented)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [khanzzirfan/testai-agent](../../repos/khanzzirfan/testai-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): GitHub Action that uses an AI agent to write automated tests on pull requests. Built on the actions/typescript-action template. 153 commits, 1 star.

(captured site page body (agents/testai-agent.md), not a verified repo-code finding)
TestAI-Agent packages an AI agent as a GitHub Action whose job is generating automated tests for pull requests, so review pipelines gain tests written by a model rather than relying on authors to supply coverage. The repository is built on the official actions/typescript-action template, with LangGraph noted in the source as the agent framework, and it publishes a marketplace action named testifyai-agent. Documentation is minimal — the README remains largely template boilerplate, inputs and model configuration are inferred from .env.example, and the repo is tiny (1 star, 153 commits). It runs on Node.js 20+ like any TypeScript action, and the MIT-licensed source is available for inspection. The practical audience is hobbyists and early experimenters wiring agent-generated tests into PR workflows; its immaturity is documented as part of the census record.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/testai-agent.md)
