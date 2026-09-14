# PR-Agent (`pr-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: The-PR-Agent
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: OpenAI, Anthropic, Google Gemini, DeepSeek, Mistral, LiteLLM (Azure OpenAI, AWS Bedrock, Vertex AI, Databricks, OpenRouter, Ollama)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [codium-ai/pr-agent](https://github.com/codium-ai/pr-agent) (source: backing, field: `source_code_url`) now resolves to [the-pr-agent/pr-agent](../../repos/the-pr-agent/pr-agent.md) (github id 662766482, verified [https://github.com/The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)).

## Description

Highlight (site page `what_makes_it_special`): AI-powered PR review agent where each tool uses a single LLM call for low cost (~30s). Platform-agnostic across 5 git providers (GitHub, GitLab, Bitbucket, Azure DevOps, Gitea). JSON-based customizable prompting. Automatically picks up AGENTS.md repo context and SKILL.md agent skills. PR compression strategy handles PRs of any size.

(captured site page body (agents/pr-agent.md), not a verified repo-code finding)
PR-Agent popularized AI pull-request review as a category, and its design remains distinctive: rather than an autonomous multi-step agent, each command makes one targeted LLM call against a compressed view of the PR, keeping responses fast and cheap enough to run on every pull request. Comment commands like /describe, /review, and /improve work identically on GitHub, GitLab, Bitbucket, Azure DevOps, and Gitea, with TOML configuration and JSON-based prompt customization for teams that need to tune behavior. Token-aware PR compression handles large diffs that would otherwise blow context limits, and a broad LiteLLM-based provider list means it runs against OpenAI, Anthropic, DeepSeek, or self-hosted models. Since Qodo donated the project it is community-maintained, with an external maintainer and a pending foundation transfer. Teams adopt it as the low-cost, platform-agnostic baseline for automated PR review, and its open-source core underpins Qodo's commercial offering.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pr-agent.md)
