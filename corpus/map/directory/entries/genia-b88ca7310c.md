# GeniA (`genia`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: genia-dev
- License: Apache-2.0
- Language: Python
- Interface: platforms=IDE, Web; install=pip3 install streamlit genia, then run genia; also available as Docker container
- Model providers: OpenAI, Azure
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [genia-dev/genia](../../repos/genia-dev/genia.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI platform engineering team member that works alongside you in production environments via Slack integration; built on OpenAI function-calling; covers DevOps, SRE, SecOps, FinOps scenarios; 100% open source and expandable with custom tools

(captured site page body (agents/genia.md), not a verified repo-code finding)
GeniA puts an LLM agent into the Slack channel a platform team already uses, so operational work — deployments to Kubernetes or Argo, incident troubleshooting, log summarization, FinOps and SecOps checks — happens by conversation in the channel rather than in a separate console. It is built on OpenAI and Azure function calling, predating the MCP ecosystem, and the tool layer is deliberately open: teams teach it new capabilities through a documented add-new-tool path. It installs with pip and a Streamlit front end or runs containerized against a Slack workspace, configured through a .env template with the team's OpenAI or Azure keys. Activity effectively stopped with its 2023 releases, leaving 409 stars and an MkDocs site as the record of what it did.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/genia.md)
