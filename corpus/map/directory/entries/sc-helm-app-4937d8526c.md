# Sc-Helm-App (`sc-helm-app`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: amsilf
- License: unknown
- Language: Python
- Interface: unknown
- Model providers: OpenAI (ChatGPT)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [amsilf/sc-helm-app](../../repos/amsilf/sc-helm-app.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Combines Helm deployment with OPA policy verification and AI-assisted auto-remediation: detects policy violations, applies ChatGPT-suggested fixes, creates a new branch, and opens a pull request — automating the full fix workflow.

(captured site page body (agents/sc-helm-app.md), not a verified repo-code finding)
The repository is an educational reference for wiring policy-as-code into AI-assisted remediation rather than a tool anyone installs. Its pieces are minimal: a Hello-World Nginx Helm chart, Rego policies, a shell script that converts violations to JSON, and an Azure pipeline that calls the OpenAI API with them, then pushes the suggested fix as a branch and PR for human review. Prerequisites are Helm 3, OPA, Python 3, and an OpenAI API key, and the README is the only documentation. There is no license file, no releases, and effectively no adoption (zero stars), with the last meaningful activity some time ago. It is best read as a pattern to copy — policy violation to LLM-suggested patch to reviewable PR — not as software to depend on.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sc-helm-app.md)
