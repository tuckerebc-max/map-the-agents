# code-agent (`code-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: multiplexer
- Provider/maker: potproject
- License: Apache-2.0
- Language: TypeScript, Docker
- Interface: platforms=CLI; install=Configure as a GitHub Actions workflow; add ANTHROPIC_API_KEY / OPENAI_API_KEY to repo secrets; use potproject/code-agent@main in a workflow YAML triggered on issues/issue_comment/pull_request_review_comment
- Model providers: Anthropic (Claude Code), OpenAI (Codex), AWS Bedrock (Claude Code)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [potproject/code-agent](../../repos/potproject/code-agent.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
The action turns GitHub issues into an interface for coding agents: a maintainer comments /claude fix the failing test, and the agent's work arrives as a commit or pull request with its reasoning post
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
