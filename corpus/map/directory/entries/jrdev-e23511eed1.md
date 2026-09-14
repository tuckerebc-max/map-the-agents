# jrdev (`jrdev`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: presstab
- License: MIT
- Language: Python
- Interface: platforms=CLI, IDE; install=pip install jrdev (PyPI), or install from GitHub source
- Model providers: Anthropic, Google, DeepSeek, OpenAI, Mistral
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: False (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [presstab/jrdev](../../repos/presstab/jrdev.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal AI developer assistant with smart project indexing (/init) that scans codebase and infers conventions; uses multiple AI models for different task tiers to balance cost and performance; smart controls for reviewing/editing code diffs; real-time token/cost monitoring with cancel capability; Git integration (PR summaries, code reviews, commit messages).

(captured site page body (agents/jrdev.md), not a verified repo-code finding)
jrdev targets developers who want a terminal agent that spends expensive models only where they pay off. The /init pass builds a project overview and convention profile that grounds later generations. Tasks flow through an intent router that parses natural-language commands and a code agent that picks models per tier — frontier models for planning and review, cheap ones for searches and fixes — with real-time token and cost readouts and a cancel switch. Diffs land in reviewable, editable form before application, and Git helpers cover PR summaries, reviews, and commit messages. It is early-access software, explicitly warning about breaking changes, distributed via pip under MIT.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/jrdev.md)
