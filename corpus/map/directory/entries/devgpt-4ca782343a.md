# DevGPT (`devgpt`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: jina-ai
- License: Apache-2.0
- Language: Python
- Interface: platforms=IDE; install=pip
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [jina-ai/dev-gpt](../../repos/jina-ai/dev-gpt.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An automated AI development team (Product Manager, Developer, DevOps) that generates, tests, builds, and deploys microservices from natural language descriptions, iteratively trying multiple implementation strategies and auto-deploying to Jina Cloud with a Streamlit playground.

(captured site page body (agents/devgpt.md), not a verified repo-code finding)
Dev-GPT treats a microservice request as a handoff across a virtual product manager, developer, and DevOps agent: the PM turns a description into a spec, the developer writes and debugs the code against tests, and the DevOps stage produces a Docker image with an optional hosted endpoint. When an implementation fails its checks, the loop retries alternative approaches rather than surfacing errors to the user. Generated services can include web-search capability via Google Custom Search, and a UI mode renders the result as a running app. It was one of the earliest end-to-end 'describe, deploy' demos from 2023; development stopped that same year, and users today would treat it as a reference implementation.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/devgpt.md)
