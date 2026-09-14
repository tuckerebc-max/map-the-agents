# Zencoder (`zencoder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Zencoder
- License: Proprietary
- Language: unknown
- Interface: platforms=IDE; install=Download Zenflow desktop app; VS Code and JetBrains extensions; CLI
- Model providers: Anthropic, Google, OpenAI
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: yes (yes)
  - hooks: unknown (unknown)
  - plan_mode: yes (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): AI coding orchestration platform with multi-model orchestration (Claude Opus for planning, Gemini for building, OpenAI Codex for reviewing), spec-before-build workflow, parallel agent execution across files/repos, cross-agent review, and multi-repo indexing. SOC 2 Type II / ISO 27001/42001. Connects to Jira, GitHub, Slack, and any custom MCP endpoint.

(captured site page body (agents/zencoder.md), not a verified repo-code finding)
Zencoder's design premise is that no single model is best at every phase of software work, so it assigns each phase deliberately: a reasoning model drafts a specification covering architecture, edge cases, and verification criteria; a faster build model implements against that spec; and a third model family reviews the resulting code with tests and linting on every change. The spec is the source of truth that both builder and reviewer check against, and cross-agent review means the reviewer never shares the author's reasoning blind spots. Agents run in parallel in isolated environments and can be redirected mid-run; scheduled automations cover recurring work such as bug triage, dependency updates, and PR review. Context comes from multi-repo indexing with dependency mapping, sized for organizations with many interconnected repositories rather than single-repo projects. The surface area spans a Zenflow desktop app, VS Code and JetBrains extensions, and a CLI for CI pipelines, with agents connecting to Jira, GitHub, Slack, and arbitrary MCP endpoints. Enterprise posture — SOC 2 Type II, ISO 27001/42001, BYOK, on-premise deployment — positions it for organizations with compliance requirements that consumer coding tools do not address.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zencoder.md)
