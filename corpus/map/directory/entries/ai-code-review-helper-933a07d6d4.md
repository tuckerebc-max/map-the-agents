# ai-code-review-helper (`ai-code-review-helper`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

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

Highlight (site page `what_makes_it_special`): LLM-based automated code review assistant listening to GitHub/GitLab Webhook events for PR/MR changes; dual-platform GitHub + GitLab support out of the box; two review modes (detailed line-level JSON-driven and general Markdown summary); built-in web admin panel for runtime config management; Redis-powered dedup and persistence with auto-cleanup on PR/MR close/merge; WeChat Work notification integration; async webhook processing. ~90% of code generated ...

(captured site page body (agents/ai-code-review-helper.md), not a verified repo-code finding)
Teams that cannot run IDE-side assistants still want automated review on every pull request. This service registers GitHub/GitLab webhooks, sends changed files to an OpenAI-compatible model, and posts results back: the detailed mode emits per-file JSON converted into line-anchored comments with category, severity, and suggestions, while the general mode posts one Markdown summary per file when structured output is unreliable. Redis handles per-commit deduplication and result storage with a seven-day TTL, and a /admin panel manages tokens, model parameters, and notification targets (WeCom or custom webhooks). Reviews are asynchronous with a summary comment after all files complete, including a friendly note when nothing was found. It deploys as a Docker container, and roughly 90% of its own code was written with Aider and Gemini.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ai-code-review-helper.md)
