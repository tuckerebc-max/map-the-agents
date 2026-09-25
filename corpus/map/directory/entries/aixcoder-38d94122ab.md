# aiXcoder (`aixcoder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aiXcoder
- License: Proprietary
- Language: unknown
- Interface: platforms=IDE; install=IDE plugin (VS Code, JetBrains) and CLI; enterprise private deployment on own compute
- Model providers: aiXcoder (aiXapply-4B open model), enterprise-owned models (private deployment)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Enterprise-grade multi-agent collaborative AI dev platform covering the full R&D lifecycle (requirements, task decomposition, codegen, testing, delivery) with large+small model collaboration; CodeAgent Plugin has Agent/Plan/Ask modes, MCP, and Skills; private deployment on domestic (Chinese) chips. Only the small aiXapply-4B model is open-sourced (github.com/aixcoder-plugin/aiXapply-4B); the main product is proprietary.

(captured site page body (agents/aixcoder.md), not a verified repo-code finding)
The platform (Beijing-based, spun out of academic work dating to 2013) covers requirements mining, task decomposition, code generation, testing, and delivery through six agents, with an Enterprise Hub governing models, MCP servers, skills, and prompts centrally. Deployment is enterprise-private by design: models run on the customer's own hardware — including air-gapped appliances for finance, aerospace, energy, and telecom clients — with no public pricing and a POC-driven sales process. Large models handle planning while small models execute high-frequency deterministic steps; aiXapply-4B (open-sourced, 94.4% change-application accuracy) absorbs the merge workload. Production deployments include finance (8M+ generated lines) and aerospace mission-control software.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/aixcoder.md)
