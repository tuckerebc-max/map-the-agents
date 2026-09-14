# code-agent (`code-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): Bridges Claude Code and Codex into GitHub workflows via slash commands (/claude, /codex) in issue/PR comments; automatically creates PRs or commits from AI-suggested changes and posts AI output as a comment when no code changes; checks user permissions and masks sensitive information in outputs.

(captured site page body (agents/code-agent.md), not a verified repo-code finding)
The action turns GitHub issues into an interface for coding agents: a maintainer comments /claude fix the failing test, and the agent's work arrives as a commit or pull request with its reasoning posted as a comment, removing the local checkout from the loop entirely. Permission gating prevents unprivileged commenters from triggering runs, and secrets live in repository settings rather than the conversation. It is a thin TypeScript wrapper around the official CLIs in a Docker action, so agent behavior is exactly upstream Claude Code or Codex. Repository maintainers who want asynchronous, issue-driven agent automation rather than interactive sessions are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/code-agent.md)
