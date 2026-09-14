# AutoPR (`autopr`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: irgolic
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=docker
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [irgolic/autopr](../../repos/irgolic/autopr.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First bot to autonomously generate pull requests in response to GitHub issues (triggered via label). Built with Guardrails for structured LLM output. Worked ~20% of the time. Now archived.

(captured site page body (agents/autopr.md), not a verified repo-code finding)
AutoPR, created in early 2023 by irgolic, was among the first bots to autonomously generate pull requests in response to GitHub issues: adding a label containing 'AutoPR' triggered a pipeline that drafted a plan, wrote the code, and opened a pull request, all built on the Guardrails library for structured LLM output. Its author has been candid that it worked about 20% of the time, with known failure modes including incorrect code references and calls to nonexistent functions, and support never extended beyond GitHub. The repository was archived on March 5, 2026 and is preserved read-only as a piece of agent history from the early ChatGPT-era. Its historical value lies in documenting how autonomous PR generation worked before dedicated harnesses matured, and its limitations (duplicated lines, nonexistent function calls) illustrate why later systems added verification layers.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/autopr.md)
