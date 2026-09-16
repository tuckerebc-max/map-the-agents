# ai-code-review-helper (`ai-code-review-helper`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: Usagi-org
- License: Apache-2.0
- Language: Python
- Interface: platforms=Web; install=docker run -d -p 8088:8088 dingyufei/ai-code-review-helper:latest | pip install -r requirements.txt + python -m api.ai_code_review_helper
- Model providers: OpenAI-compatible (configurable OPENAI_API_BASE_URL, default gpt-4o)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [usagi-org/ai-code-review-helper](../../repos/usagi-org/ai-code-review-helper.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Teams that cannot run IDE-side assistants still want automated review on every pull request. This service registers GitHub/GitLab webhooks, sends changed files to an OpenAI-compatible model, and posts
Sources: [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
