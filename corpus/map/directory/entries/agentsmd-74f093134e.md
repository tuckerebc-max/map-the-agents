# agents.md (`agentsmd`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: agentsmd
- License: MIT
- Language: TypeScript
- Interface: install=npm (for local Next.js website)
- Model providers: Provider-agnostic (open format for any coding agents)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [agentsmd/agents.md](../../repos/agentsmd/agents.md.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Acts as a 'README for agents' -- a dedicated, predictable file format designed to provide context, environment tips, testing instructions, and PR rules to help guide AI coding agents working within a project.

(captured site page body (agents/agentsmd.md), not a verified repo-code finding)
As coding agents spread, every tool proposed its own instruction file, leaving repositories with fragmented per-tool configuration. AGENTS.md defines a predictable, plain-Markdown convention: a single file where a project documents environment setup, testing commands, and pull-request rules, with no schema or tooling required. The repository hosts both the specification and the agents.md website, and dogfoods the format with its own AGENTS.md. Adoption spread across major tools and thousands of repositories, making it the reference point against which alternatives like AGENT.md position themselves. Its audience is any team whose repositories are worked on by AI coding agents.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentsmd.md)
